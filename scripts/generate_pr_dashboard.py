import collections,datetime as dt,json,os,pathlib,urllib.parse,urllib.request
from html import escape
U=os.getenv("GH_USERNAME","astroknot-sheep"); T=os.getenv("GH_TOKEN","")
P=pathlib.Path("assets");P.mkdir(exist_ok=True)
def search(q):
 out=[]
 for pg in range(1,11):
  url="https://api.github.com/search/issues?"+urllib.parse.urlencode({"q":q,"per_page":100,"page":pg})
  req=urllib.request.Request(url,headers={"Accept":"application/vnd.github+json","User-Agent":"pr-dashboard",**({"Authorization":"Bearer "+T} if T else {})})
  with urllib.request.urlopen(req,timeout=30) as f: items=json.load(f)["items"]
  out+=items
  if len(items)<100:break
 return out
def txt(x,y,v,size=14,color="#e6edf3"):
 return f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}">{escape(str(v))}</text>'
def bar(x,y,w,h,c):return f'<rect x="{x}" y="{y}" width="{max(0,w)}" height="{max(0,h)}" rx="3" fill="{c}"/>'
def save(name,w,h,s):
 P.joinpath(name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" rx="12" fill="#0d1117" stroke="#30363d"/>'+s+'</svg>',encoding="utf8")
def main():
 prs=search("is:pr author:"+U);merged={p["html_url"] for p in search("is:pr is:merged author:"+U)}
 prs=list({p["html_url"]:p for p in prs}.values());prs.sort(key=lambda p:p["created_at"],reverse=True)
 n=len(prs);m=sum(p["html_url"] in merged for p in prs);o=sum(p["state"]=="open" for p in prs)
 s=txt(22,31,"open source / pull requests",18)
 for i,(a,b,c) in enumerate([("created",n,"#58a6ff"),("merged",m,"#3fb950"),("open",o,"#58a6ff"),("merge rate",f"{m/n:.0%}" if n else "—","#bc8cff")]):
  x=22+i*190;s+=bar(x,49,173,88,"#161b22")+txt(x+12,74,a,12,"#8b949e")+txt(x+12,119,b,32,c)
 save("pr-overview.svg",798,159,s)
 today=dt.datetime.now(dt.timezone.utc).date()
 opened=collections.Counter(p["created_at"][:7] for p in prs)
 merged_months=collections.Counter(p["closed_at"][:7] for p in prs if p["html_url"] in merged and p.get("closed_at"))
 dates=[]
 for i in range(11,-1,-1):
  y=(today.year*12+today.month-1-i)//12;mo=(today.year*12+today.month-1-i)%12+1;dates.append(f"{y:04}-{mo:02}")
 peak=max([opened[d]+merged_months[d] for d in dates]+[1])
 s=txt(22,30,"pull request activity / last 12 months",18)+txt(22,51,"blue: created     green: merged",12,"#8b949e")
 for i,d in enumerate(dates):
  x=25+i*63; a=round(opened[d]*105/peak);b=round(merged_months[d]*105/peak)
  s+=bar(x,177-a,19,a,"#58a6ff")+bar(x+21,177-b,19,b,"#3fb950")+txt(x,202,d[5:],11,"#8b949e")
 save("pr-activity.svg",798,225,s)
 repos=collections.Counter(p["repository_url"].split("/repos/")[-1] for p in prs)
 top=repos.most_common(8);maximum=max([v for _,v in top]+[1]);s=txt(22,30,"repositories receiving PRs",18)
 for i,(name,v) in enumerate(top):
  y=60+i*36;s+=txt(22,y+12,name[:43],12)+bar(355,y,round(v/maximum*350),16,"#bc8cff")+txt(728,y+13,v,12)
 save("pr-repositories.svg",798,85+36*len(top),s)
 daily=collections.Counter(dt.date.fromisoformat(p["created_at"][:10]) for p in prs)
 start=today-dt.timedelta(days=363);start-=dt.timedelta(days=start.weekday())
 s=txt(22,30,"pull request heatmap / created per day",18)
 colors=["#21262d","#0e4429","#006d32","#26a641","#39d353"]
 for i in range(371):
  day=start+dt.timedelta(days=i)
  if day<=today:s+=bar(24+(i//7)*14,48+(i%7)*14,10,10,colors[min(4,daily[day])])
 s+=txt(22,164,"PR submissions only, not GitHub's general contribution calendar",11,"#8b949e")
 save("pr-heatmap.svg",798,183,s)
 s=txt(22,30,"recent pull requests",18)
 for i,p in enumerate(prs[:8]):
  y=59+i*42;status="merged" if p["html_url"] in merged else p["state"]
  url=escape(p["html_url"],quote=True)
  repo=p["repository_url"].split("/repos/")[-1]
  s+=f'<a href="{url}">'+txt(22,y,repo+"  /  "+status,11,"#3fb950" if status=="merged" else "#58a6ff")+txt(22,y+18,p["title"][:94],13)+'</a>'
 save("pr-recent.svg",798,85+42*min(8,len(prs)),s)
 print("Generated",n,"PRs and",m,"merged")
if __name__=="__main__":main()
