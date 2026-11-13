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

def fetch_merged_details(prs, merged_urls):
    """Fetch true merged_at timestamps once, for summaries, plots and tables."""
    merged = {}
    for pr in prs:
        if pr["html_url"] not in merged_urls:
            continue
        url = pr["pull_request"]["url"]
        headers = {"User-Agent": "astroknot-profile-svg", "Accept": "application/vnd.github+json"}
        if TOKEN:
            headers["Authorization"] = "Bearer " + TOKEN
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=35) as response:
            details = json.load(response)
        if details.get("merged_at"):
            merged[pr["html_url"]] = details
    return merged

def median(values):
    values = sorted(values)
    n = len(values)
    if not n:
        return 0.0
    return (values[(n-1)//2] + values[n//2]) / 2

def hero(n, merged, open_n, resolved_rate, median_days, stamp):
    # The 2:1 editorial banner from the user's reference, not a cluster of cards.
    w,h=1200,576
    s=rect(0,0,w,h,INK,0)
    s+=text(55,49,"DHRIMAN DEKA / ML ENGINEER",17,LIME,700,MONO,'letter-spacing="1"')
    s+=text(1145,49,"LLM + RETRIEVAL SYSTEMS",16,MUTED,600,MONO,'text-anchor="end" letter-spacing="1"')
    s+=text(52,184,"found a bug.",104,PAPER,750,FONTS,'letter-spacing="-5"')
    s+=text(52,289,"sent a patch.",104,LAV,750,FONTS,'letter-spacing="-5"')
    s+=text(56,346,"i work on the awkward edges of machine learning and retrieval.",22,MUTED,400,FONTS)
    s+=line(56,377,1144,377,"#3D4551",1.5)
    values=[
        (str(merged),"MERGED","UPSTREAM",PAPER),
        (f"{resolved_rate:.0%}","OF RESOLVED","PRs MERGED",LIME),
        (f"{median_days:.1f}d","MEDIAN TIME","TO MERGE",LAV),
        (str(open_n),"OPEN PRs","IN REVIEW",CORAL),
    ]
    for i,(value,lab1,lab2,color) in enumerate(values):
        x=56+i*274
        s+=text(x,447,value,57,color,700,FONTS,'letter-spacing="-2.5"')
        s+=text(x,476,lab1,13,MUTED,600,MONO)
        s+=text(x,497,lab2,13,MUTED,600,MONO)
    s+=line(56,517,1144,517,"#3D4551",1)
    s+=text(56,548,"open to ML systems and retrieval engineering work",16,MUTED,400,FONTS)
    s+=text(1144,548,f"PUBLIC GITHUB DATA · {stamp}",12,MUTED,500,MONO,'text-anchor="end"')
    save("field-hero.svg",w,h,s,"Dhriman Deka: ML engineer, verified upstream merge statistics")

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

def pulse(prs, merge_info, resolved_rate, today):
    """Cumulative upstream merges since September 2026; every increment is a real merge."""
    w,h=1000,392
    s=eyebrow("01","the work")
    s+=text(50,109,"merged upstream, over time.",31,PAPER,700,FONTS,'letter-spacing="-1"')
    s+=text(50,137,"each jump = a PR merged by a maintainer",13,MUTED,400,MONO)
    start=dt.date(2026,9,1)
    events=sorted(dt.date.fromisoformat(v["merged_at"][:10]) for v in merge_info.values()
                  if v.get("merged_at") and dt.date.fromisoformat(v["merged_at"][:10])>=start)
    end=max(today,start+dt.timedelta(days=1))
    left,right,top,bottom=74,921,176,321
    maxval=max(1,len(events))
    for k in range(5):
        y=bottom-k*(bottom-top)/4
        s+=line(left,y,right,y,"#263243",1,'stroke-dasharray="2 7"')
        s+=text(59,y+4,str(round(maxval*k/4)),11,MUTED,400,MONO,'text-anchor="end"')
    span=max(1,(end-start).days)
    def x_for(day): return left+((day-start).days/span)*(right-left)
    def y_for(count):return bottom-(count/maxval)*(bottom-top)
    d=f"M{left} {bottom}"
    count=0
    for day in events:
        xx=x_for(day)
        count+=1
        d+=f" H{xx:.1f} V{y_for(count):.1f}"
        s+=circle(round(xx,1),round(y_for(count),1),4.3,LIME,INK,2)
    d+=f" H{right}"
    area=d+f" V{bottom} H{left} Z"
    s+=f'<path d="{area}" fill="url(#areaGrad)" opacity=".5"/>'
    s+=f'<path d="{d}" stroke="{LIME}" stroke-width="3.4" fill="none" stroke-linejoin="round" stroke-linecap="round"/>'
    # Quarterly markers plus the current month, adapting to elapsed time.
    ticks=[]
    moment=start
    while moment <= end:
        ticks.append(moment)
        month=moment.month+1;year=moment.year
        if month>12:year+=1;month=1
        moment=dt.date(year,month,1)
    ticks.append(end)
    for i,day in enumerate(ticks):
        xx=x_for(day)
        if i==len(ticks)-1 or day.month in (1,3,6,9,11):
            s+=text(round(xx,1),346,day.strftime("%b '%y"),11,MUTED,400,MONO,'text-anchor="middle"')
    s+=text(923,112,str(len(events)),37,LIME,700,MONO,'text-anchor="end"')
    s+=text(923,137,"MERGED SINCE SEP '26",11,MUTED,400,MONO,'text-anchor="end"')
    s+=line(50,371,950,371)
    save("field-pulse.svg",w,h,s,"Cumulative upstream PR merges since September 2026")

def atlas(prs):
    w,h=1000,410
    s=eyebrow("02","where i've sent patches")
    repos=collections.Counter(p["repository_url"].split("/repos/")[-1] for p in prs)
    top=repos.most_common(6)
    total=len(repos)
    maxn=max((n for _,n in top),default=1)
    s+=text(50,110,"the repositories.",31,PAPER,700,FONTS,'letter-spacing="-1"')
    s+=text(50,139,f"top {len(top)} of {total} upstream repositories",13,MUTED,400,MONO)
    cx,cy=252,283
    for radius in [71,120,163]:
        s+=circle(cx,cy,radius,"none","#29364B",1,'stroke-dasharray="4 9"')
    s+=circle(cx,cy,33,"#1B2838",LAV,2)
    s+=text(cx,cy+6,str(total),23,PAPER,700,MONO,'text-anchor="middle"')
    s+=text(cx,cy+23,"REPOS",8,MUTED,500,MONO,'text-anchor="middle"')
    nodes=[(106,265),(174,199),(321,204),(398,285),(329,362),(157,361)]
    for i,(_,n) in enumerate(top):
        x,y=nodes[i]
        c=[LIME,LAV,BLUE,CORAL][i%4]
        s+=line(cx,cy,x,y,"#4C5970",1)
        radius=6+min(12,12*n/maxn)
        s+=circle(x,y,radius,"#182534",c,2)
        s+=circle(x,y,3,c)
    s+=line(499,160,499,369,"#3B495F",1)
    s+=text(530,170,"TOP 6 / 19",11,LIME,600,MONO)
    s+=text(944,170,"PRS",11,MUTED,600,MONO,'text-anchor="end"')
    for i,(repo,n) in enumerate(top):
        y=206+i*30
        shortened=repo if len(repo)<=38 else repo[:35]+"..."
        s+=text(531,y,f"{i+1:02}",11,LAV,600,MONO)
        s+=text(562,y,shortened,13,PAPER,400,FONTS)
        s+=text(944,y,n,13,LIME,700,MONO,'text-anchor="end"')
        s+=line(531,y+8,944,y+8,"#27344B")
    # Correct the legend as repository count changes.
    s=s.replace("TOP 6 / 19",f"TOP {len(top)} OF {total}")
    s+=line(50,393,950,393)
    save("field-atlas.svg",w,h,s,"Six leading upstream repositories among all repositories with authored PRs")

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

def update_readme(prs):
    """Keep the prose intact; list only open upstream PRs in consistent dates."""
    file=Path("README.md")
    if not file.exists():return
    original=file.read_text(encoding="utf-8")
    begin,end="<!-- LIVE_PRS_START -->","<!-- LIVE_PRS_END -->"
    if begin not in original or end not in original:return
    rows=[]
    for pr in [p for p in prs if p["state"]=="open"][:7]:
        url=pr["html_url"]
        repo=pr["repository_url"].split("/repos/")[-1]
        title=pr["title"].replace("|","\\|").replace("[","\\[").replace("]","\\]").replace("\n"," ")
        date=dt.date.fromisoformat(pr["created_at"][:10]).strftime("%d %b %Y")
        rows.append(f"| {date} | [{title}]({url}) | {repo} |")
    table="| Opened | Pull request | Repository |\n|:--|:--|:--|\n"+"\n".join(rows) if rows else "_No PRs currently open._"
    new=original.split(begin,1)[0]+begin+"\n"+table+"\n"+end+original.split(end,1)[1]
    if new!=original:file.write_text(new,encoding="utf-8")

# One-line descriptions grounded in the actual merged fixes.
PR_SUMMARIES={
    "qdrant/qdrant-client": "Set the gRPC text-index tokenizer's default to word.",
    "mlflow/mlflow": "Handle Gemini safety blocks as content-filter events.",
    "deepset-ai/haystack": "Correct line ranges in PythonCodeSplitter secondary splits.",
    "deepset-ai/haystack-core-integrations": "Fix numeric casting in pgvector metadata filters.",
    "docling-project/docling": "Close an open list before a following table in DOCX conversion.",
    "pydantic/logfire": "Avoid reporting early generator closure as an error.",
    "huggingface/sentence-transformers": "Correct a training-arguments import in examples.",
}

def update_merged_history(prs, merge_info):
    """Render merged upstream PRs with exact GitHub timestamps, review times, and context."""
    file=Path("README.md")
    if not file.exists():return
    original=file.read_text(encoding="utf-8")
    begin,end="<!-- MERGED_HISTORY_START -->","<!-- MERGED_HISTORY_END -->"
    if begin not in original or end not in original:return
    entries=[]
    for pr in prs:
        details=merge_info.get(pr["html_url"])
        if not details:continue
        timestamp=dt.datetime.fromisoformat(details["merged_at"].replace("Z","+00:00"))
        created=dt.datetime.fromisoformat(pr["created_at"].replace("Z","+00:00"))
        elapsed=(timestamp-created).total_seconds()/86400
        repo=pr["repository_url"].split("/repos/")[-1]
        title=pr["title"].replace("|","\\|").replace("[","\\[").replace("]","\\]").replace("\n"," ")
        entries.append((timestamp,elapsed,repo,title,pr["html_url"]))
    entries.sort(key=lambda item:item[0],reverse=True)
    rows=[]
    for timestamp,days,repo,title,url in entries:
        human=f"{days:.1f}d" if days>=1 else f"{days*24:.1f}h"
        blurb=PR_SUMMARIES.get(repo, "A bugfix merged by upstream maintainers.")
        rows.append(f"| {timestamp.strftime('%d %b %Y, %H:%M UTC')} | [{title}]({url})<br><sub>{blurb}</sub> | {repo} | {human} |")
    table="| Merged at | Fix | Repository | Time to merge |\n|:--|:--|:--|--:|\n"+"\n".join(rows)
    if not rows:table="_No upstream merges found._"
    new=original.split(begin,1)[0]+begin+"\n"+table+"\n"+end+original.split(end,1)[1]
    if new!=original:file.write_text(new,encoding="utf-8")

def hero_mobile(merged,open_n,resolved_rate,median_days,stamp):
    """A 2-column companion to the desktop SVG for narrow screens."""
    w,h=640,620
    s=rect(0,0,w,h,INK)
    s+=text(34,45,"DHRIMAN DEKA / ML ENGINEER",16,LIME,700,MONO)
    s+=text(34,75,"LLM + RETRIEVAL SYSTEMS",15,MUTED,500,MONO)
    s+=text(31,185,"found a bug.",76,PAPER,750,FONTS,'letter-spacing="-4"')
    s+=text(31,274,"sent a patch.",76,LAV,750,FONTS,'letter-spacing="-4"')
    s+=text(34,316,"fixing the rough edges of ML systems.",19,MUTED,400,FONTS)
    s+=line(34,343,606,343,"#3D4551")
    pairs=[
        (34,409,str(merged),["MERGED","UPSTREAM"],PAPER),
        (330,409,f"{resolved_rate:.0%}",["RESOLVED PRs","MERGED"],LIME),
        (34,515,f"{median_days:.1f}d",["MEDIAN TIME","TO MERGE"],LAV),
        (330,515,str(open_n),["OPEN PRs","IN REVIEW"],CORAL)
    ]
    for x,y,value,labels,color in pairs:
        s+=text(x,y,value,48,color,700,FONTS)
        s+=text(x,y+24,labels[0],13,MUTED,500,MONO)
        s+=text(x,y+41,labels[1],13,MUTED,500,MONO)
    s+=line(34,568,606,568,"#3D4551")
    s+=text(34,594,f"PUBLIC GITHUB DATA · {stamp}",12,MUTED,400,MONO)
    save("field-hero-mobile.svg",w,h,s,"Dhriman Deka: public merged pull requests, resolved rate and median merge time")

def main():
    all_prs=list({p["html_url"]:p for p in query(f"is:pr author:{USER}")}.values())
    def upstream(pr):
        owner=pr["repository_url"].split("/repos/")[-1].split("/")[0]
        return owner.lower()!=USER.lower()
    prs=[p for p in all_prs if upstream(p)]
    prs.sort(key=lambda p:p["created_at"],reverse=True)
    merged_urls={p["html_url"] for p in query(f"is:pr is:merged author:{USER}")}
    merge_info=fetch_merged_details(prs,merged_urls)
    merged_count=len(merge_info)
    open_count=sum(p["state"]=="open" for p in prs)
    resolved_count=len(prs)-open_count
    resolved_rate=merged_count/resolved_count if resolved_count else 0
    times=[]
    for pr in prs:
        d=merge_info.get(pr["html_url"])
        if not d:continue
        merge_time=dt.datetime.fromisoformat(d["merged_at"].replace("Z","+00:00"))
        opened=dt.datetime.fromisoformat(pr["created_at"].replace("Z","+00:00"))
        times.append((merge_time-opened).total_seconds()/86400)
    median_days=median(times)
    today=dt.datetime.now(dt.timezone.utc).date()
    hero(len(prs),merged_count,open_count,resolved_rate,median_days,today.isoformat())
    hero_mobile(merged_count,open_count,resolved_rate,median_days,today.isoformat())
    pulse(prs,merge_info,resolved_rate,today)
    atlas(prs)
    update_readme(prs)
    update_merged_history(prs,merge_info)
    print(f"Upstream PRs: {len(prs)}, merged: {merged_count}, open: {open_count}, resolved merge rate: {resolved_rate:.1%}, median: {median_days:.1f}d")

if __name__=="__main__":
    main()
