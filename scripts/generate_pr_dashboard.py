#!/usr/bin/env python3
"""Astroknot / Open Source Field Notes: self-contained, live GitHub SVG artwork.
No pip dependencies, third-party image hosts, external fonts, or fake counters.
"""
import collections
import datetime as dt
import json
import math
import os
from pathlib import Path
import re
import urllib.parse
import urllib.request
from html import escape

USER = os.environ.get("GH_USERNAME", "astroknot-sheep")
TOKEN = os.environ.get("GH_TOKEN", "")
DIR = Path("assets")
DIR.mkdir(exist_ok=True)

INK = "#080D14"
PANEL = "#101824"
LINE = "#293246"
PAPER = "#F0F3EC"
MUTED = "#8D9AAB"
LIME = "#D5FC70"
LAV = "#A89BFF"
CORAL = "#FFB09D"
BLUE = "#85BFF9"
FONTS = "Inter,Segoe UI,Arial,sans-serif"
MONO = "SFMono-Regular,Consolas,DejaVu Sans Mono,monospace"

def query(q):
    items = []
    for page in range(1, 11):
        qs = urllib.parse.urlencode({"q": q, "per_page": 100, "page": page})
        headers = {"User-Agent": "astroknot-profile-svg", "Accept": "application/vnd.github+json"}
        if TOKEN:
            headers["Authorization"] = "Bearer " + TOKEN
        req = urllib.request.Request("https://api.github.com/search/issues?" + qs, headers=headers)
        with urllib.request.urlopen(req, timeout=35) as response:
            data = json.load(response)
        batch = data.get("items", [])
        items.extend(batch)
        if len(batch) < 100:
            break
    return items

def e(s):
    return escape(str(s), quote=True)

def text(x, y, s, size=16, color=PAPER, weight=400, family=FONTS, extra=""):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" font-size="{size}" font-weight="{weight}" {extra}>{e(s)}</text>'

def rect(x, y, w, h, color, rx=0, extra=""):
    return f'<rect x="{x}" y="{y}" width="{max(0,w)}" height="{max(0,h)}" rx="{rx}" fill="{color}" {extra}/>'

def line(x1,y1,x2,y2,color=LINE,width=1,extra=""):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" {extra}/>'

def circle(x,y,r,fill="none",stroke="none",sw=1,extra=""):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'

def group(s, transform):
    return f'<g transform="{transform}">{s}</g>'

def base(w,h,body,title):
    defs = """<defs>
      <linearGradient id="heroGlow" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stop-color="#202038"/><stop offset=".55" stop-color="#111d29"/><stop offset="1" stop-color="#080d14"/>
      </linearGradient>
      <linearGradient id="lineGrad" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0" stop-color="#A89BFF"/><stop offset="1" stop-color="#D5FC70"/>
      </linearGradient>
      <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color="#A89BFF" stop-opacity=".28"/>
        <stop offset="1" stop-color="#A89BFF" stop-opacity="0"/>
      </linearGradient>
      <radialGradient id="orbGlow"><stop offset="0" stop-color="#A89BFF" stop-opacity=".2"/>
        <stop offset="1" stop-color="#A89BFF" stop-opacity="0"/></radialGradient>
      <pattern id="microGrid" width="32" height="32" patternUnits="userSpaceOnUse">
        <path d="M32 0H0V32" fill="none" stroke="#202838" stroke-width=".55"/>
      </pattern>
      </defs>"""
    header = f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{e(title)}"><title>{e(title)}</title>'
    return header + defs + rect(0,0,w,h,INK,16) + body + '</svg>\n'

def save(filename,w,h,body,title):
    (DIR / filename).write_text(base(w,h,body,title), encoding="utf-8")

def eyebrow(index, label, w=1000):
    s = text(50,43,f"{index} / {label.upper()}",12,LIME,600,MONO)
    s += text(w-50,43,"ASTROKNOT—SHEEP / OSS ARCHIVE",11,MUTED,400,MONO,'text-anchor="end"')
    return s + line(50,59,w-50,59)

def hero(n,merged,open_n,rate,stamp):
    w,h=1000,410
    s=rect(0,0,w,h,"url(#heroGlow)",16) + rect(0,0,w,h,"url(#microGrid)",16, 'opacity=".33"')
    s+=circle(805,176,180,"url(#orbGlow)")
    s+=text(52,48,"ASTROKNOT / SHEEP",14,LIME,700,MONO, 'letter-spacing="2"')
    s+=text(951,48,"ISSUE 001   •   THE INTERNET",12,MUTED,400,MONO,'text-anchor="end"')
    s+=line(52,66,948,66,"#435064")
    s+=text(49,152,"found a bug.",67,PAPER,700,FONTS,'letter-spacing="-3"')
    s+=text(48,226,"sent a patch.",70,LAV,700,FONTS,'letter-spacing="-3"')
    s+=text(53,264,"sometimes a fix. sometimes a long review thread.",15,MUTED,400,MONO)
    # Render a geometric sheep head as an orbiting constellation, no emoji font dependency.
    cx,cy=808,190
    for r in [84,118,149]:
        s+=circle(cx,cy,r,"none","#566279",1,'stroke-dasharray="3 10" opacity=".65"')
    s+=f'<ellipse cx="{cx}" cy="{cy}" rx="176" ry="69" fill="none" stroke="{LAV}" stroke-width="1.2" transform="rotate(-28 {cx} {cy})" opacity=".85"/>'
    for x,y,r,c in [(681,145,4,LIME),(919,122,3,PAPER),(862,330,4,LAV),(965,218,3,LIME),(728,246,2,PAPER)]:
        s+=circle(x,y,r,c)
    # Distinctive minimal line-drawn sheep: looping wool, face, ears, eyes.
    cloud="M763 168 C738 145 756 116 785 128 C797 106 833 109 843 133 C872 121 889 143 880 165 C898 183 885 211 861 214 C852 236 819 245 804 225 C780 238 756 220 756 202 C739 192 742 179 763 168Z"
    s+=f'<path d="{cloud}" fill="#172131" stroke="{PAPER}" stroke-width="2.5" stroke-linejoin="round"/>'
    s+=f'<path d="M789 181 Q808 167 830 180 L832 217 Q814 237 791 215 Z" fill="#253044" stroke="{PAPER}" stroke-width="2"/>'
    s+=f'<path d="M789 187 L766 177 Q766 199 789 200 M832 187 L857 176 Q857 199 832 200" fill="#253044" stroke="{PAPER}" stroke-width="2"/>'
    s+=circle(802,198,3,LIME)+circle(820,198,3,LIME)
    s+=f'<path d="M807 212 Q813 217 818 212" fill="none" stroke="{PAPER}" stroke-width="2" stroke-linecap="round"/>'
    s+=text(810,354,"NODE 01: curious sheep",11,MUTED,400,MONO,'text-anchor="middle"')
    s+=line(52,295,948,295,"#435064")
    for i,(value,label,col) in enumerate([(f"{n:02}","UPSTREAM PRs",PAPER),(f"{merged:02}","MERGED UPSTREAM",LIME),(f"{open_n:02}","OPEN PRs",LAV),(f"{rate:.0%}","MERGE RATIO",CORAL)]):
        x=54+i*229
        s+=text(x,342,value,37,col,700,MONO)+text(x,367,label,10,MUTED,600,MONO,'letter-spacing=".7"')
        if i<3:s+=line(x+209,313,x+209,372,"#435064")
    s+=text(949,397,f"LIVE DATA · {stamp}",10,MUTED,400,MONO,'text-anchor="end"')
    save("field-hero.svg",w,h,s,"Astroknot Open Source Field Notes: real pull request totals")

def smooth_path(points):
    if not points:return ""
    result=f"M {points[0][0]:.2f} {points[0][1]:.2f}"
    for a,b in zip(points,points[1:]):
        midpoint=(b[0]-a[0])/2
        result+=f" C {a[0]+midpoint:.2f} {a[1]:.2f}, {b[0]-midpoint:.2f} {b[1]:.2f}, {b[0]:.2f} {b[1]:.2f}"
    return result

def months_back(today):
    out=[]
    for j in range(11,-1,-1):
        ordinal=today.year*12+today.month-1-j
        year,month=divmod(ordinal,12)
        out.append(f"{year:04d}-{month+1:02d}")
    return out

def pulse(prs,merged_set,rate,today):
    w,h=1000,425
    s=eyebrow("01","the pulse")
    s+=text(50,111,"the last twelve months.",31,PAPER,700,FONTS,'letter-spacing="-1"')
    s+=text(50,137,"PRs opened vs. PRs merged / last twelve months",13,MUTED,400,MONO)
    s+=text(49,164,"●",13,LAV)+text(67,164,"SUBMITTED",11,MUTED,600,MONO)
    s+=text(182,164,"●",13,LIME)+text(200,164,"LANDED",11,MUTED,600,MONO)
    dates=months_back(today)
    a=collections.Counter(p["created_at"][:7] for p in prs)
    b=collections.Counter(p.get("closed_at","")[:7] for p in prs if p["html_url"] in merged_set and p.get("closed_at"))
    peak=max(1,*[max(a[d],b[d]) for d in dates])
    # Left timeline occupies 650 px; right circular score.
    left,right,top,bottom=55,672,196,351
    for j in range(5):
        y=bottom-j*(bottom-top)/4
        value=round(peak*j/4)
        s+=line(left,y,right,y,"#283247",1,'stroke-dasharray="2 6"')
        s+=text(left-5,y-6,value,10,MUTED,400,MONO)
    pointsA=[];pointsB=[]
    for i,d in enumerate(dates):
        x=left+18+i*(right-left-36)/11
        ya=bottom-a[d]/peak*(bottom-top)
        yb=bottom-b[d]/peak*(bottom-top)
        pointsA.append((x,ya));pointsB.append((x,yb))
        s+=text(x,bottom+25,d[5:],11,MUTED,400,MONO,'text-anchor="middle"')
    pA=smooth_path(pointsA);pB=smooth_path(pointsB)
    s+=f'<path d="{pA} L{pointsA[-1][0]} {bottom} L{pointsA[0][0]} {bottom}Z" fill="url(#areaGrad)"/>'
    s+=f'<path d="{pA}" fill="none" stroke="{LAV}" stroke-width="3.5" stroke-linejoin="round"/>'
    s+=f'<path d="{pB}" fill="none" stroke="{LIME}" stroke-width="3.5" stroke-linejoin="round"/>'
    for x,y in pointsA:s+=circle(round(x,2),round(y,2),3.6,LAV,INK,1.5)
    for x,y in pointsB:s+=circle(round(x,2),round(y,2),3.6,LIME,INK,1.5)
    # Donut gauge with oversized type.
    cx,cy,r=833,269,76
    s+=circle(cx,cy,r,"none","#2C3448",15)
    C=2*math.pi*r
    s+=circle(cx,cy,r,"none",LIME,15,f'stroke-dasharray="{C*rate:.2f} {C:.2f}" stroke-linecap="round" transform="rotate(-90 {cx} {cy})"')
    s+=text(cx,cy+8,f"{rate:.0%}",41,PAPER,700,MONO,'text-anchor="middle"')
    s+=text(cx,cy+31,"MERGED / ALL",10,MUTED,500,MONO,'text-anchor="middle"')
    s+=text(833,382,"PUBLIC UPSTREAM PRs ONLY",10,MUTED,500,MONO,'text-anchor="middle"')
    s+=line(50,402,950,402)
    save("field-pulse.svg",w,h,s,"Twelve months of opened and merged pull requests")

def atlas(prs):
    w,h=1000,410
    s=eyebrow("02","the constellation")
    s+=text(50,111,"where my PRs went.",31,PAPER,700,FONTS,'letter-spacing="-1"')
    s+=text(50,137,"each node = one repo outside my account. size = PRs opened.",13,MUTED,400,MONO)
    repos=collections.Counter(p["repository_url"].split("/repos/")[-1] for p in prs)
    top=repos.most_common(7);maxn=max((n for _,n in top),default=1)
    cx,cy=270,266
    for r in [68,116,158]:
        s+=circle(cx,cy,r,"none","#26354B",1,'stroke-dasharray="4 9"')
    s+=circle(cx,cy,27,"#1D2A38",LIME,2)
    s+=text(cx,cy+6,str(len(repos)),21,PAPER,700,MONO,'text-anchor="middle"')
    s+=text(cx,cy+44,"REPOS",10,MUTED,600,MONO,'text-anchor="middle"')
    # Deterministic node constellation; node size scales with number of PRs.
    nodes=[(112,239),(168,145),(352,159),(422,249),(370,356),(205,378),(95,336)]
    for i,(repo,n) in enumerate(top):
        x,y=nodes[i]
        color=[LAV,LIME,BLUE,CORAL][i%4]
        s+=line(cx,cy,x,y,"#526077",1)
        rr=7+min(15,13*n/maxn)
        s+=circle(x,y,rr,"#1b2736",color,2)
        s+=circle(x,y,3.4,color)
        s+=text(x+rr+7,y-rr-5,str(n),11,color,700,MONO)
    s+=line(513,157,513,371,"#354054")
    s+=text(545,166,"REPOSITORY",11,MUTED,600,MONO,'letter-spacing=".8"')
    s+=text(940,166,"PRS",11,MUTED,600,MONO,'text-anchor="end"')
    for i,(repo,n) in enumerate(top[:6]):
        y=199+i*32
        short=repo if len(repo)<36 else repo[:33]+"..."
        s+=text(545,y,f"{i+1:02}",12,LAV,700,MONO)
        s+=text(579,y,short,13,PAPER,500,FONTS)
        s+=text(938,y,n,13,LIME,700,MONO,'text-anchor="end"')
        s+=line(545,y+9,940,y+9,"#253044")
    if not top:s+=text(545,230,"no public PRs returned by the API",13,MUTED)
    s+=line(50,392,950,392)
    save("field-atlas.svg",w,h,s,"Repository constellation showing distinct repositories and pull requests")

def heatmap(prs,today):
    w,h=1000,245
    s=eyebrow("03","the trail")
    s+=text(50,96,"days i opened a PR.",29,PAPER,700,FONTS,'letter-spacing="-1"')
    counts=collections.Counter(dt.date.fromisoformat(p["created_at"][:10]) for p in prs)
    # 53 columns of seven weekdays; choose a Monday-aligned 371-day grid.
    start=today-dt.timedelta(days=370)
    start-=dt.timedelta(days=start.weekday())
    step=16;xx=64;yy=131
    palette=["#222B39","#494766","#6C68A6","#9E97E9",LIME]
    previous=None
    for week in range(54):
        day=start+dt.timedelta(days=7*week)
        if day>today:break
        month=(day.year,day.month)
        if month!=previous and day.day<8:
            s+=text(xx+week*step,122,day.strftime("%b").upper(),10,MUTED,500,MONO)
        previous=month
        for dow in range(7):
            d=day+dt.timedelta(days=dow)
            if d>today:continue
            c=counts[d]
            color=palette[min(c,4)]
            s+=rect(xx+week*step,yy+dow*13.5,11,11,color,2)
    s+=text(64,236,"MON",9,MUTED,500,MONO)
    s+=text(138,236,"EACH SQUARE = 1 DAY · SHADED BY PRs OPENED",10,MUTED,400,MONO)
    s+=text(831,236,"LESS",10,MUTED,400,MONO)
    for i,c in enumerate(palette):s+=rect(875+i*17,226,11,11,c,2)
    save("field-trail.svg",w,h,s,"Daily pull request creation heatmap, last year")

def update_readme(prs,merged_urls):
    """Maintain the existing human-written README; only refresh the marked PR table."""
    file = Path("README.md")
    if not file.is_file():
        return
    old = file.read_text(encoding="utf-8")
    begin, end = "<!-- LIVE_PRS_START -->", "<!-- LIVE_PRS_END -->"
    if begin not in old or end not in old:
        return
    rows = []
    for pr in prs[:7]:
        url = pr["html_url"]
        repo = pr["repository_url"].split("/repos/")[-1]
        title = pr["title"].replace("|", "\\|").replace("[", "\\[").replace("]", "\\]").replace("\n", " ")
        status = "merged" if url in merged_urls else ("open" if pr["state"] == "open" else "closed")
        rows.append(f"| {pr['created_at'][:10]} | [{title}]({url}) | {repo} | {status} |")
    content = "| Opened | Pull request | Repo | Status |\n|:--|:--|:--|:--|\n" + "\n".join(rows)
    if not rows:
        content = "_No public upstream PRs found._"
    new = old.split(begin, 1)[0] + begin + "\n" + content + "\n" + end + old.split(end, 1)[1]
    if new != old:
        file.write_text(new, encoding="utf-8")

def update_merged_history(prs, merged_urls):
    """List every upstream merge with its actual GitHub merge timestamp (UTC)."""
    file = Path("README.md")
    if not file.is_file():
        return
    original = file.read_text(encoding="utf-8")
    begin, end = "<!-- MERGED_HISTORY_START -->", "<!-- MERGED_HISTORY_END -->"
    if begin not in original or end not in original:
        return
    entries = []
    for pr in prs:
        if pr["html_url"] not in merged_urls:
            continue
        # Search/issues.closed_at is not a reliable merge timestamp.
        # Fetch the pull request itself for merged_at.
        url = pr["pull_request"]["url"]
        headers = {"User-Agent": "astroknot-profile-svg", "Accept": "application/vnd.github+json"}
        if TOKEN:
            headers["Authorization"] = "Bearer " + TOKEN
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=35) as response:
            details = json.load(response)
        when = details.get("merged_at")
        if not when:
            continue
        repository = pr["repository_url"].split("/repos/")[-1]
        title = pr["title"].replace("|", "\\|").replace("[", "\\[").replace("]", "\\]").replace("\n", " ")
        timestamp = dt.datetime.fromisoformat(when.replace("Z", "+00:00"))
        entries.append((timestamp, repository, title, pr["html_url"], pr["created_at"]))
    entries.sort(reverse=True)
    rows = []
    for timestamp, repository, title, url, created in entries:
        created_time = dt.datetime.fromisoformat(created.replace("Z", "+00:00"))
        duration = timestamp - created_time
        days = duration.total_seconds() / 86400
        elapsed = f"{days:.1f} days" if days >= 1 else f"{duration.total_seconds()/3600:.1f} hours"
        rows.append(f"| {timestamp.strftime('%d %b %Y, %H:%M UTC')} | [{title}]({url}) | {repository} | {elapsed} |")
    table = "| Merged at (UTC) | PR | Repository | Time to merge |\n|:--|:--|:--|--:|\n" + "\n".join(rows)
    if not rows:
        table = "_No upstream merges found._"
    new = original.split(begin, 1)[0] + begin + "\n" + table + "\n" + end + original.split(end, 1)[1]
    if new != original:
        file.write_text(new, encoding="utf-8")

def main():
    all_prs = list({p["html_url"]: p for p in query(f"is:pr author:{USER}")}.values())
    # Exclude PRs in personally owned repositories, so the metrics mean upstream contributions.
    def is_upstream(pr):
        owner = pr["repository_url"].split("/repos/")[-1].split("/")[0]
        return owner.lower() != USER.lower()
    prs = [p for p in all_prs if is_upstream(p)]
    prs.sort(key=lambda p: p["created_at"], reverse=True)
    merged_urls = {p["html_url"] for p in query(f"is:pr is:merged author:{USER}")}
    merged_count = sum(p["html_url"] in merged_urls for p in prs)
    open_count = sum(p["state"] == "open" for p in prs)
    rate = merged_count / len(prs) if prs else 0
    today = dt.datetime.now(dt.timezone.utc).date()
    hero(len(prs), merged_count, open_count, rate, today.isoformat())
    pulse(prs, merged_urls, rate, today)
    atlas(prs)
    heatmap(prs, today)
    update_readme(prs, merged_urls)
    update_merged_history(prs, merged_urls)
    print(f"Rendered field notes: {len(prs)} upstream PRs, {merged_count} merged, {open_count} open.")


if __name__=="__main__":
    main()
