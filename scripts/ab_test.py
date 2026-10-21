#!/usr/bin/env python3
"""Decide un test A/B (campeón frente a retador) con los datos acumulados de uno o varios envíos.

Uso:
  python3 scripts/ab_test.py --a 1450:31 --b 1440:52 [--a 1300:20 --b 1310:35 ...] [--metrica CTR]

Cada --a / --b es «entregados:conversiones» de un envío (clics únicos para CTR, registros para
registros). Se suman todos los envíos del mismo experimento.

Devuelve la tasa de cada variante, la mejora relativa de B sobre A, la probabilidad de que B sea
mejor (modelo Beta-binomial con prior uniforme) y la decisión según las reglas de
knowledge/experimentos.md.
"""
import argparse
import math
import random

MIN_ENTREGADOS = 300      # por variante, acumulado
PROB_GANADOR = 0.95       # B gana (o A gana si P(B>A) <= 0,05)
PROB_TENDENCIA = 0.80     # entre 80% y 95%: tendencia, se sigue probando
MEJORA_MINIMA = 0.10      # por debajo de un 10% relativo no compensa cambiar
MAX_ENVIOS = 4            # sin decisión tras 4 envíos: empate, se cierra
SIMULACIONES = 100_000


def parse(valores):
    entregados = conversiones = 0
    for v in valores:
        e, c = v.split(":")
        entregados += int(e)
        conversiones += int(c)
    return entregados, conversiones


def prob_b_mejor(a, b, n=SIMULACIONES, semilla=26):
    rnd = random.Random(semilla)
    (ea, ca), (eb, cb) = a, b
    gana_b = 0
    for _ in range(n):
        pa = rnd.betavariate(ca + 1, ea - ca + 1)
        pb = rnd.betavariate(cb + 1, eb - cb + 1)
        gana_b += pb > pa
    return gana_b / n


def z_test(a, b):
    (ea, ca), (eb, cb) = a, b
    p = (ca + cb) / (ea + eb)
    se = math.sqrt(p * (1 - p) * (1 / ea + 1 / eb)) if 0 < p < 1 else 0
    if se == 0:
        return 0.0, 1.0
    z = (cb / eb - ca / ea) / se
    p_valor = math.erfc(abs(z) / math.sqrt(2))
    return z, p_valor


def decidir(a, b, envios):
    (ea, ca), (eb, cb) = a, b
    ta, tb = ca / ea, cb / eb
    mejora = (tb - ta) / ta if ta else float("inf")
    prob = prob_b_mejor(a, b)
    if min(ea, eb) < MIN_ENTREGADOS:
        return prob, mejora, "SEGUIR: menos de 300 entregados por variante"
    if prob >= PROB_GANADOR and mejora >= MEJORA_MINIMA:
        return prob, mejora, "GANA B: el retador pasa a campeón"
    if prob <= 1 - PROB_GANADOR and tb and (ta - tb) / tb >= MEJORA_MINIMA:
        return prob, mejora, "GANA A: el campeón se mantiene y el retador se descarta"
    if envios >= MAX_ENVIOS:
        return prob, mejora, "EMPATE: se cierra sin cambio y se prueba otra variable"
    if prob >= PROB_TENDENCIA or prob <= 1 - PROB_TENDENCIA:
        return prob, mejora, "TENDENCIA: se repite el mismo par en el siguiente envío"
    return prob, mejora, "SEGUIR: sin diferencia clara todavía"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--a", action="append", required=True, help="entregados:conversiones del campeón")
    ap.add_argument("--b", action="append", required=True, help="entregados:conversiones del retador")
    ap.add_argument("--metrica", default="CTR")
    args = ap.parse_args()
    if len(args.a) != len(args.b):
        ap.error("hace falta el mismo número de envíos para A y para B")

    a, b = parse(args.a), parse(args.b)
    prob, mejora, decision = decidir(a, b, len(args.a))
    z, p_valor = z_test(a, b)
    print(f"Envíos acumulados: {len(args.a)}")
    print(f"A (campeón): {a[1]}/{a[0]} = {a[1] / a[0]:.2%} {args.metrica}")
    print(f"B (retador): {b[1]}/{b[0]} = {b[1] / b[0]:.2%} {args.metrica}")
    print(f"Mejora relativa de B: {mejora:+.1%}")
    print(f"Probabilidad de que B sea mejor: {prob:.1%}")
    print(f"Contraste z: z = {z:.2f}, p = {p_valor:.3f}")
    print(f"Decisión: {decision}")


if __name__ == "__main__":
    main()
