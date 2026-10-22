#!/usr/bin/env python3
"""Convierte los borradores narrativos (outputs/<division>-<version>/narrativo-*.md) en un HTML por correo con knowledge/plantilla-email.html.
Uso: python3 scripts/maquetar.py outputs/<division>-<version> knowledge/plantilla-email.html outputs/<division>-<version>/html
"""
import re,sys,html,os,glob
src_dir,tpl_path,out=sys.argv[1],sys.argv[2],sys.argv[3]
os.makedirs(out,exist_ok=True)
TPL=open(tpl_path).read()
E=lambda s:html.escape(s,quote=False)
def hero(title):
    t=title.lower()
    if 'invitacion' in t: return 'webinar'
    for k,ks in [('grabacion',['grabacion']),('lanzamiento',['lanzamiento']),('webinar',['recordatorio','· dia','sala']),('cargofive',['cargofive']),('bi',[' bi ','bi integrado','n1']),('digitalizacion',['digitaliz']),('asistente',['asistente']),('divisas',['divisas','xe']),('verifactu',['verifactu']),('vconta',['vconta','vencim'])]:
        if any(x in t for x in ks): return k
    return 'webinar'
def hl(s,kw):
    if not kw: return s
    i=s.lower().find(kw.lower())
    if i<0: return s
    return s[:i]+'<span class="vt-hl" style="background-color:#FDE7A6;padding:0 2px;">'+s[i:i+len(kw)]+'</span>'+s[i+len(kw):]
def paras(lines,kw,used):
    blocks=[];cur=[]
    for l in lines+['']:
        if l.strip()=='' :
            if cur: blocks.append(cur); cur=[]
        else: cur.append(l.strip())
    outp=[]
    for b in blocks:
        if all(x.startswith('- ') for x in b):
            outp.append('<ul style="margin:0;padding-left:20px;">'+''.join(f'<li style="margin:0 0 6px;">{E(x[2:])}</li>' for x in b)+'</ul>')
        else:
            txt='<br>'.join(E(x) if not x.startswith('- ') else '· '+E(x[2:]) for x in b)
            if not used[0]:
                n=hl(txt,kw); used[0]= n!=txt; txt=n
            outp.append(txt)
    return '<br><br>'.join(outp)
def field(blk,name):
    m=re.search(r'^'+re.escape(name)+r':\s*(.*)$',blk,re.M); return m.group(1).strip() if m else ''
def url_of(blk):
    m=re.search(r'^CTA principal:.*?→\s*(\S+)',blk,re.M)
    if m: return m.group(1)
    m=re.search(r'Variante A →\s*(\S+)',blk); return m.group(1) if m else '#'
idx=[]
for f in sorted(glob.glob(src_dir+'/narrativo-*.md')):
    t=open(f).read()
    for blk in re.split(r'\n(?=### #)',t)[1:]:
        blk=blk.split('\n---')[0]
        title=blk.split('\n')[0][4:]
        num=re.match(r'#(\d+)',title).group(1); tipo=title.split('·')[1].strip().lower()
        kw=field(blk,'Palabra clave (resaltado)').strip('«»')
        body=re.search(r'^Cuerpo:\s*\n(.*?)(?=^CTA principal:)',blk,re.S|re.M).group(1)
        lines=body.split('\n')
        bi=next((i for i,l in enumerate(lines) if l.startswith('[Botón:')),None)
        cta=re.match(r'\[Botón:\s*(.*?)\]',lines[bi]).group(1) if bi is not None else 'Ver más'
        pre=lines[:bi] if bi is not None else lines
        post=lines[bi+1:] if bi is not None else []
        micro=''; rest=[]
        for l in post:
            if l.startswith('Microtexto:'): micro=l.split(':',1)[1].strip()
            else: rest.append(l)
        # signature & PD & crosssell
        sig_i=next((i for i,l in enumerate(rest) if l.strip().startswith('Emma González')),None)
        pd=''; after=[]
        if sig_i is not None:
            j=sig_i
            if j>0 and rest[j-1].strip().lower().startswith('un saludo'): j-=1
            if j>0 and rest[j-1].strip().lower().startswith('nos vemos'): j-=1
            after=rest[sig_i+2:]; rest=rest[:j]
        for l in after:
            if l.startswith('P. D.'): pd=re.sub(r'\s*\[[^\]]*→[^\]]*\]\s*$','',l.split(':',1)[1] if ':' in l[:6] else l[5:]).strip()
        used=[False]
        v={'ASUNTO':field(blk,'Asunto A'),'PREHEADER':field(blk,'Preheader'),'TITULAR':hl(E(field(blk,'Titular')),kw),
           'PARRAFO_1':paras(pre,kw,used),'TEXTO_CTA':E(cta),'MICROTEXTO_CTA':E(micro),
           'PARRAFO_2':paras(rest,kw,used),'PARRAFO_CIERRE':'','FIRMA_NOMBRE':'Emma González','FIRMA_CARGO':'Marketing en Visual Trans',
           'PD_TEXTO':E(pd),'PD_ENLACE':E(cta),'URL_CTA_UTM':url_of(blk),'URL_WEB_UTM':url_of(blk),'URL_LOGO':'logo.png',
           'URL_IMAGEN':f'hero-{hero(title)}.png','ALT_IMAGEN':E(field(blk,'Titular'))}
        t2=TPL
        for k,x in v.items(): t2=t2.replace('{{'+k+'}}',x)
        drop=['VIDEO','CROSSSELL']+([] if pd else ['PD'])
        for b in drop: t2=re.sub(r'<!-- BLOQUE:%s.*?<!-- /BLOQUE:%s -->'%(b,b),'',t2,flags=re.S)
        if not micro: t2=re.sub(r'<!-- Microtexto.*?</tr>','',t2,flags=re.S)
        if tipo=='sala': t2=re.sub(r'<!-- Imagen principal.*?</tr>','',t2,flags=re.S)
        t2=re.sub(r'<tr>\s*<td class="vt-pad" style="padding:24px 36px 0;[^>]*>\s*</td>\s*</tr>','',t2)
        name=f'{num}-{tipo}.html'; open(f'{out}/{name}','w').write(t2)
        idx.append((num,tipo,name,v['ASUNTO']))
print(len(idx))
for i in idx: print(*i)
