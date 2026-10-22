"""Genera la página de entrega de una versión (artifact) con la estructura fija de Adrián.

Uso: python3 scripts/entrega_artifact.py <division>-<version>
Lee  outputs/<v>/correos.md   (correos del redactor, ya revisados)
     outputs/<v>/entrega.json (cabecera, objetivos, datos anteriores, A/B, pendiente, riesgos
                               y nombres cortos de las novedades para el filtro)
Usa  knowledge/plantilla-entrega.html
Escribe outputs/<v>/entrega.html
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

LINK_KEYS = ("CTA principal", "Enlace secundario", "Enlace en la línea", "Vídeo")


def asunto_label(key):
    if "formato resultado" in key:
        return "Resultado"
    if "formato notas" in key:
        return "Notas"
    m = re.match(r"Asunto ([A-Z])\b", key)
    return m.group(1) if m else "Asunto"


def parse_correos(text):
    correos, cur, mode = [], None, None
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("### #"):
            parts = [p.strip() for p in line[4:].split(" · ")]
            cur = {"n": parts[0].lstrip("#"), "tipo": parts[1] if len(parts) > 1 else "",
                   "novedad": parts[2] if len(parts) > 2 else "", "angulo": " · ".join(parts[3:]),
                   "asuntos": [], "cuerpo": [], "enlaces": [], "sugerencias": []}
            correos.append(cur)
            mode = None
            continue
        if cur is None or line == "---":
            continue
        if mode == "cuerpo":
            if line.startswith("Firma:"):
                cur["firma"] = line.split(":", 1)[1].strip()
                mode = None
            elif line:
                cur["cuerpo"].append(line.strip())
            continue
        if line.startswith("Cuerpo:"):
            mode = "cuerpo"
            continue
        m = re.match(r"^([^:]{2,90}):\s?(.*)$", line)
        if not m:
            continue
        key, val = m.group(1).strip(), m.group(2).strip()
        if key == "Fecha de envío":
            cur["fecha"] = val.replace(" ", "T", 1) if "T" not in val else val
            cur["fecha"] = cur["fecha"].replace("T", " ")
        elif key == "Nombre en HubSpot":
            cur["hubspot"] = val
        elif key.startswith("Asunto"):
            if not val.startswith("("):
                cur["asuntos"].append([asunto_label(key), val])
        elif key == "Preheader":
            cur["preheader"] = val
        elif key == "Titular":
            cur["titular"] = val
        elif key == "Audiencia":
            cur["audiencia"] = val
        elif key == "Hipótesis que prueba":
            cur["hipotesis"] = val
        elif key == "Sugerencia":
            cur["sugerencias"].append(val)
        elif key == "Cross-selling":
            txt, _, url = val.partition(" → ")
            cur["crosssell"] = txt.strip()
            p = re.search(r"crosssell-([a-z]+)", url)
            names = {"vnotify": "vNotify", "vextract": "vExtract", "vinculador": "Vinculador"}
            cur["crosssell_producto"] = names.get(p.group(1), p.group(1)) if p else ""
            cur["enlaces"].append([f"Cross-selling ({cur['crosssell_producto']})", url.strip()])
        elif key.startswith(LINK_KEYS):
            cur["enlaces"].append([key, val])
    return correos


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    v = sys.argv[1]
    out = ROOT / "outputs" / v
    ctx = json.loads((out / "entrega.json").read_text(encoding="utf-8"))
    correos = parse_correos((out / "correos.md").read_text(encoding="utf-8"))
    for c in correos:
        c["fecha"] = c["fecha"][:10] + " " + c["fecha"][11:16]
        c["novedad"] = next((x["nombre"] for x in ctx.get("novedades", [])
                             if re.search(x["si"], c["novedad"], re.I)), c["novedad"])
        c["ab"] = ctx.get("ab_por_correo", {}).get(c["n"], "")
        c["objetivo"] = next((o["objetivo"] for o in ctx["objetivo_por_correo"]
                              if re.search(o["si"], f"{c['tipo']} {c['novedad']}", re.I)), "")
    ctx["correos"] = correos
    tpl = (ROOT / "knowledge" / "plantilla-entrega.html").read_text(encoding="utf-8")
    html = tpl.replace("__TITLE__", f"{ctx['division']} {ctx['version']}").replace(
        "/*__DATA__*/null", json.dumps(ctx, ensure_ascii=False).replace("</", "<\\/"))
    (out / "entrega.html").write_text(html, encoding="utf-8")
    print(f"{out / 'entrega.html'}: {len(correos)} correos")


if __name__ == "__main__":
    main()
