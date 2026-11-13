#!/usr/bin/env python3
"""Print-inspired GitHub profile graphics using verified public PR data.
Python standard library only. Figures are generated in-repo, with no external widgets.
"""
import collections
import datetime as dt
import json
import os
from html import escape
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

USER = os.getenv("GH_USERNAME", "astroknot-sheep")
TOKEN = os.getenv("GH_TOKEN", "")
OUTPUT = Path("assets")
OUTPUT.mkdir(exist_ok=True)

# A restrained print palette: uncoated paper, ink, one signal colour.
PAPER = "#F7F4EE"
INK = "#1E2425"
QUIET = "#677174"
HAIR = "#D8D5CD"
ACCENT = "#C44A31"
FAINT = "#E9E3D9"
SOFT_RED = "#F2D7CE"
SANS = "Arial,Helvetica,sans-serif"
SERIF = "Georgia,Times New Roman,serif"
MONO = "Consolas,Liberation Mono,monospace"

def fetch(search):
    results = []
    for page in range(1, 11):
        url = "https://api.github.com/search/issues?" + urlencode({"q": search, "per_page": 100, "page": page})
        headers = {"Accept": "application/vnd.github+json", "User-Agent": "astroknot-profile"}
        if TOKEN:
            headers["Authorization"] = "Bearer " + TOKEN
        with urlopen(Request(url, headers=headers), timeout=40) as response:
            payload = json.load(response)
        batch = payload.get("items", [])
        results.extend(batch)
        if len(batch) < 100:
            break
    return results

def t(x,y,content,size=16,color=INK,weight=400,font=SANS,other=""):
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" fill="{color}" {other}>{escape(str(content))}</text>'

def r(x,y,w,h,color,rad=0):
    return f'<rect x="{x}" y="{y}" width="{max(0,w)}" height="{max(0,h)}" rx="{rad}" fill="{color}"/>'

def l(x1,y1,x2,y2,color=HAIR,width=1):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"/>'

def svg(name,width,height,contents,alt):
    xml = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-label="{escape(alt,quote=True)}"><title>{escape(alt)}</title>'
    xml += r(0,0,width,height,PAPER,3) + contents + "</svg>\n"
    (OUTPUT / name).write_text(xml, encoding="utf-8")

def label(x,y,value,colour=QUIET):
    return t(x,y,value,13,colour,700,MONO, 'letter-spacing=".6"')

def poster(upstream,merged,repo_count):
    w,h=1100,385
    s=l(40,40,1060,40,INK,2)
    s+=t(42,27,"DHRIMAN DEKA",16,INK,700,MONO,'letter-spacing="1.2"')
    s+=t(1058,27,"GITHUB / ASTROKNOT-SHEEP",13,QUIET,600,MONO,'text-anchor="end"')
    s+=t(38,193,"dhriman.",142,INK,400,SERIF,'font-style="italic" letter-spacing="-8"')
    s+=r(43,215,328,10,ACCENT)
    s+=t(43,260,"engineer by practice, curious by default.",19,INK,400,SANS)
    s+=t(43,286,"economics → machine learning → open source",16,QUIET,400,SANS)
    s+=l(40,314,1060,314,INK,2)
    # An index, not a stack of rounded cards.
    stats=[(44,str(upstream),"UPSTREAM PRs"),(416,str(merged),"MERGED"),(788,str(repo_count),"PROJECTS TOUCHED")]
    for i,(x,value,name) in enumerate(stats):
        s+=t(x,362,value,42,ACCENT if i==1 else INK,700,SANS,'letter-spacing="-1.5"')
        s+=t(x+80,356,name,14,QUIET,700,MONO)
    s+=l(390,327,390,374);s+=l(765,327,765,374)
    svg("profile-poster.svg",w,h,s,"Dhriman Deka, ML engineer and open-source contributor. Live upstream PR totals.")

def overview(prs,merged_urls,now):
    opened=collections.Counter(p["created_at"][:7] for p in prs)
    landed=collections.Counter(p["closed_at"][:7] for p in prs if p["html_url"] in merged_urls and p.get("closed_at"))
    months=[]
    for delta in range(11,-1,-1):
        absolute=now.year*12+now.month-1-delta
        yr,mo=divmod(absolute,12)
        months.append(f"{yr:04d}-{mo+1:02d}")
    peak=max(1,*[max(opened[m],landed[m]) for m in months])
    w,h=1100,350
    s=label(42,36,"01 / UPSTREAM PULL REQUESTS") + t(1058,36,"LAST 12 MONTHS",13,QUIET,600,MONO,'text-anchor="end"')
    s+=l(42,50,1058,50,INK,1.5)
    s+=t(42,95,"Opened and merged, month by month",27,INK,400,SERIF)
    s+=r(744,74,13,13,INK)+t(765,86,"opened",14,QUIET)
    s+=r(872,74,13,13,ACCENT)+t(893,86,"merged",14,QUIET)
    left=56;right=1055;chart_top=132;chart_bottom=277
    for i in range(5):
        y=chart_bottom-i*(chart_bottom-chart_top)/4
        s+=l(left,y,right,y,HAIR)
        s+=t(45,y-6,round(peak*i/4),12,QUIET,400,MONO,'text-anchor="end"')
    full=right-left;slot=full/12
    for i,month in enumerate(months):
        x=left+i*slot+slot*.13
        bar_width=slot*.27
        op=opened[month];mg=landed[month]
        h1=op/peak*(chart_bottom-chart_top)
        h2=mg/peak*(chart_bottom-chart_top)
        s+=r(round(x,1),round(chart_bottom-h1,1),round(bar_width,1),round(h1,1),INK,1)
        s+=r(round(x+bar_width+5,1),round(chart_bottom-h2,1),round(bar_width,1),round(h2,1),ACCENT,1)
        s+=t(round(left+i*slot+slot*.44,1),308,month[5:],14,QUIET,500,MONO,'text-anchor="middle"')
    s+=l(42,325,1058,325)
    s+=t(42,342,"Counts are based on PR creation dates and merge dates, respectively.",12,QUIET)
    svg("pr-months.svg",w,h,s,"Upstream pull requests opened and merged per month over the last year")

def repo_sheet(prs):
    counts=collections.Counter(p["repository_url"].split("/repos/")[-1] for p in prs)
    top=counts.most_common(10)
    w=1100;h=128+46*len(top)
    s=label(42,37,"02 / WHERE THE PATCHES WENT")+t(1058,37,"PUBLIC REPOSITORIES",13,QUIET,600,MONO,'text-anchor="end"')
    s+=l(42,50,1058,50,INK,1.5)
    s+=t(42,93,"Projects I've opened PRs in",27,INK,400,SERIF)
    biggest=max((v for _,v in top),default=1)
    for i,(repo,n) in enumerate(top):
        y=134+i*46
        s+=t(42,y,f"{i+1:02}",14,ACCENT,700,MONO)
        s+=t(88,y,repo,16,INK,500,SANS)
        s+=r(630,y-14,365,9,FAINT,1)
        s+=r(630,y-14,365*n/biggest,9,ACCENT,1)
        s+=t(1056,y,str(n).zfill(2),16,INK,700,MONO,'text-anchor="end"')
        s+=l(42,y+14,1058,y+14,HAIR)
    svg("pr-repositories.svg",w,h,s,"Top upstream repositories by authored pull requests")

def calendar(prs,now):
    counts=collections.Counter(dt.date.fromisoformat(p["created_at"][:10]) for p in prs)
    base=now-dt.timedelta(days=363)
    base-=dt.timedelta(days=base.weekday())
    w,h=1100,258
    s=label(42,34,"03 / A YEAR IN PULL REQUESTS")
    s+=l(42,47,1058,47,INK,1.5)
    s+=t(42,87,"Days I submitted PRs",27,INK,400,SERIF)
    x0=62;y0=120
    shades=[FAINT,"#DDAF9F","#CA7D66",ACCENT,"#762F24"]
    last_month=None
    for week in range(53):
        first=base+dt.timedelta(days=7*week)
        if first>now:break
        if first.month!=last_month and first.day<=7:
            s+=t(x0+week*18,113,first.strftime("%b").upper(),11,QUIET,700,MONO)
        last_month=first.month
        for day in range(7):
            d=first+dt.timedelta(days=day)
            if d>now:continue
            num=counts[d]
            s+=r(x0+week*18,y0+day*15,12,12,shades[min(num,4)],1)
    s+=t(43,246,"A square is a day. Shading counts PRs opened, not commits.",13,QUIET)
    s+=t(925,246,"LESS",11,QUIET,600,MONO)
    for i,v in enumerate(shades):s+=r(961+i*19,236,12,12,v,1)
    svg("pr-days.svg",w,h,s,"A one-year calendar showing on which days upstream pull requests were opened")

def populate_readme(prs,merged_urls):
    path=Path("README.md")
    if not path.exists():return
    existing=path.read_text(encoding="utf-8")
    start="<!-- LIVE_PRS_START -->"
    stop="<!-- LIVE_PRS_END -->"
    if start not in existing or stop not in existing:return
    rows=[]
    for p in prs[:7]:
        state="merged" if p["html_url"] in merged_urls else ("open" if p["state"]=="open" else "closed")
        repo=p["repository_url"].split("/repos/")[-1]
        title=p["title"].replace("|", "\\|").replace("[", "\\[").replace("]", "\\]").replace("\n", " ")
        rows.append(f"| {p['created_at'][:10]} | [{title}]({p['html_url']}) | {repo} | {state} |")
    text_rows="| Opened | Pull request | Repo | Status |\n|:--|:--|:--|:--|\n"+"\n".join(rows)
    if not rows:text_rows="_No public upstream PRs found._"
    new=existing.split(start,1)[0]+start+"\n"+text_rows+"\n"+stop+existing.split(stop,1)[1]
    if new!=existing:path.write_text(new,encoding="utf-8")

def main():
    all_prs=list({p["html_url"]:p for p in fetch(f"is:pr author:{USER}")}.values())
    # Exclude repositories owned by this profile. This is an upstream-contribution index,
    # not a count padded with PRs in one's own repositories.
    def foreign(p):
        return p["repository_url"].split("/repos/")[-1].split("/")[0].lower()!=USER.lower()
    prs=[p for p in all_prs if foreign(p)]
    prs.sort(key=lambda p:p["created_at"],reverse=True)
    merged_urls={p["html_url"] for p in fetch(f"is:pr is:merged author:{USER}")}
    m=sum(p["html_url"] in merged_urls for p in prs)
    repos=len(set(p["repository_url"] for p in prs))
    today=dt.datetime.now(dt.timezone.utc).date()
    poster(len(prs),m,repos)
    overview(prs,merged_urls,today)
    repo_sheet(prs)
    calendar(prs,today)
    populate_readme(prs,merged_urls)
    print("Upstream PRs:",len(prs),"merged:",m,"repos:",repos)

if __name__=="__main__":
    main()
