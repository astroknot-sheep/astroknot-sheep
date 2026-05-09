<!-- hey. thanks for stopping by. -->

```aura width=800 height=400
<div style={{display:"flex",flexDirection:"column",width:"100%",height:"100%",background:"#020408",position:"relative",overflow:"hidden",padding:"56px 72px 48px",fontFamily:"-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif"}}>
  <style dangerouslySetInnerHTML={{__html:`
    @keyframes aurora-warm{0%,100%{transform:translate(0,0) scale(1);}33%{transform:translate(40px,-30px) scale(1.08);}66%{transform:translate(-20px,20px) scale(1.05);}}
    @keyframes aurora-cool{0%,100%{transform:translate(0,0) scale(1);}33%{transform:translate(-30px,40px) scale(1.1);}66%{transform:translate(20px,-20px) scale(1.06);}}
    @keyframes aurora-mid{0%,100%{transform:translate(0,0) scale(1);opacity:.35;}50%{transform:translate(15px,-15px) scale(1.12);opacity:.65;}}
    @keyframes sheep-float{0%,100%{transform:rotate(-8deg) translateY(0px);}50%{transform:rotate(8deg) translateY(-14px);}}
    @keyframes handle-pulse{0%,100%{boxShadow:"0 0 12px rgba(255,176,24,0.15),inset 0 1px 0 rgba(255,255,255,0.08)";}50%{boxShadow:"0 0 32px rgba(255,176,24,0.4),inset 0 1px 0 rgba(255,255,255,0.15)";}}
    @keyframes text-glow{0%,100%{filter:drop-shadow(0 0 20px rgba(255,176,24,0.25));}50%{filter:drop-shadow(0 0 45px rgba(255,176,24,0.55));}}
    @keyframes fade-up{from{opacity:0;transform:translateY(20px);}to{opacity:1;transform:translateY(0);}}
    .fade-up{animation:fade-up 0.8s ease both;}
    .d1{animation-delay:0.1s;}.d2{animation-delay:0.25s;}.d3{animation-delay:0.4s;}.d4{animation-delay:0.55s;}
  `}} />

  <div style={{position:"absolute",inset:0,opacity:0.025,backgroundImage:"url('data:image/svg+xml,%3Csvg viewBox=%220 0 200 200%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22noise%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%220.65%22 numOctaves=%223%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23noise)%22/%3E%3C/svg%3E')",pointerEvents:"none"}}></div>

  <div style={{position:"absolute",inset:0,backgroundImage:"linear-gradient(rgba(255,255,255,0.02) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,0.02) 1px,transparent 1px)",backgroundSize:"48px 48px",maskImage:"radial-gradient(ellipse at 30% 50%,black 30%,transparent 80%)",WebkitMaskImage:"radial-gradient(ellipse at 30% 50%,black 30%,transparent 80%)"}}></div>

  <div style={{position:"absolute",top:"-200px",right:"-160px",width:"700px",height:"700px",borderRadius:"50%",background:"radial-gradient(circle,rgba(255,140,40,0.55) 0%,rgba(255,80,0,0.25) 30%,transparent 68%)",filter:"blur(70px)",animation:"aurora-warm 9s ease-in-out infinite"}}></div>
  <div style={{position:"absolute",bottom:"-180px",left:"-120px",width:"520px",height:"520px",borderRadius:"50%",background:"radial-gradient(circle,rgba(80,120,255,0.4) 0%,rgba(60,80,200,0.15) 40%,transparent 75%)",filter:"blur(70px)",animation:"aurora-cool 11s ease-in-out infinite"}}></div>
  <div style={{position:"absolute",top:"10%",left:"25%",width:"450px",height:"450px",borderRadius:"50%",background:"radial-gradient(circle,rgba(255,100,200,0.18) 0%,transparent 70%)",filter:"blur(90px)",animation:"aurora-mid 13s ease-in-out infinite"}}></div>

  <div style={{position:"relative",zIndex:2,display:"flex",flexDirection:"column",height:"100%",justifyContent:"center"}}>
    <div style={{display:"flex",alignItems:"flex-end",gap:"28px",marginBottom:"28px"}} className="fade-up d1">
      <span style={{fontSize:"140px",fontWeight:900,color:"#f0f4fa",letterSpacing:"-9px",lineHeight:0.85,textShadow:"0 0 80px rgba(255,255,255,0.12),0 4px 30px rgba(0,0,0,0.6)"}}>hi.</span>
      <div style={{animation:"sheep-float 3.2s ease-in-out infinite",marginBottom:"18px",filter:"drop-shadow(0 0 24px rgba(255,200,100,0.35))"}}>
        <span style={{fontSize:"80px"}}>🐑</span>
      </div>
    </div>

    <div style={{display:"flex",alignItems:"center",gap:"18px",marginBottom:"32px",position:"relative"}} className="fade-up d2">
      <span style={{fontSize:"22px",color:"#475569",fontWeight:400,letterSpacing:"-0.3px"}}>i'm</span>
      <span style={{fontSize:"56px",fontWeight:900,background:"linear-gradient(135deg,#ffd700 0%,#ff9d00 50%,#ff6b00 100%)",WebkitBackgroundClip:"text",WebkitTextFillColor:"transparent",letterSpacing:"-2.8px",animation:"text-glow 4s ease-in-out infinite"}}>dhriman</span>
      <div style={{display:"flex",alignItems:"center",background:"rgba(255,176,24,0.08)",border:"1px solid rgba(255,176,24,0.4)",borderRadius:"30px",padding:"9px 22px",backdropFilter:"blur(12px)",animation:"handle-pulse 3.5s ease-in-out infinite"}}>
        <span style={{fontSize:"13px",color:"#d4a017",letterSpacing:"0.6px",fontWeight:600}}>@astroknot-sheep</span>
      </div>
    </div>

    <span style={{fontSize:"12px",color:"#334155",letterSpacing:"1.8px",textTransform:"uppercase",fontWeight:500,position:"relative"}} className="fade-up d3">
      building small things · learning in public · the sheep is on purpose
    </span>
  </div>
</div>
```

<div align="center" style="padding: 52px 24px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <div style="max-width: 600px; position: relative;">
    <div style="position: absolute; left: 0; top: 0; bottom: 0; width: 3px; background: linear-gradient(to bottom, rgba(255,176,24,0.7), rgba(255,176,24,0)); border-radius: 3px;"></div>
    <p style="margin: 0; padding-left: 28px; font-size: 18px; color: #94a3b8; line-height: 1.7; font-weight: 400;">
      i don't have a grand mission statement.<br>
      i just like building small things that <em style="color: #e2e8f0; font-style: italic;">might</em> help someone.
    </p>
  </div>
</div>

<div align="center" style="padding: 40px 24px 16px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <h2 style="margin: 0; font-size: 30px; font-weight: 800; color: #e2e8f0; letter-spacing: -0.6px; position: relative; display: inline-block;">
    what i'm fiddling with right now
    <span style="position: absolute; bottom: -10px; left: 0; width: 100%; height: 2px; background: linear-gradient(90deg, transparent, #ff9d00, #3b82f6, #a855f7, transparent); border-radius: 2px;"></span>
  </h2>
</div>

```aura width=800 height=280
<div style={{display:"flex",alignItems:"stretch",width:"100%",height:"100%",background:"#020408",padding:"24px",gap:"20px",position:"relative",overflow:"hidden",fontFamily:"-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif"}}>
  <style dangerouslySetInnerHTML={{__html:`
    @keyframes card-glow-green{0%,100%{box-shadow:0 0 24px rgba(125,211,168,0.06),inset 0 1px 0 rgba(255,255,255,0.04);}50%{box-shadow:0 0 48px rgba(125,211,168,0.2),inset 0 1px 0 rgba(255,255,255,0.1);}}
    @keyframes card-glow-blue{0%,100%{box-shadow:0 0 24px rgba(147,197,253,0.06),inset 0 1px 0 rgba(255,255,255,0.04);}50%{box-shadow:0 0 48px rgba(147,197,253,0.2),inset 0 1px 0 rgba(255,255,255,0.1);}}
    @keyframes card-glow-purple{0%,100%{box-shadow:0 0 24px rgba(196,181,253,0.06),inset 0 1px 0 rgba(255,255,255,0.04);}50%{box-shadow:0 0 48px rgba(196,181,253,0.2),inset 0 1px 0 rgba(255,255,255,0.1);}}
    @keyframes float-card{0%,100%{transform:translateY(0);}50%{transform:translateY(-8px);}}
    .card-green{animation:card-glow-green 4s ease-in-out infinite,float-card 6s ease-in-out infinite;}
    .card-blue{animation:card-glow-blue 4.8s ease-in-out infinite,float-card 6.8s ease-in-out infinite;animation-delay:0s,0.6s;}
    .card-purple{animation:card-glow-purple 5.6s ease-in-out infinite,float-card 7.6s ease-in-out infinite;animation-delay:0s,1.2s;}
  `}} />

  <div style={{position:"absolute",inset:0,background:"radial-gradient(ellipse at 15% 50%,rgba(125,211,168,0.04) 0%,transparent 50%),radial-gradient(ellipse at 85% 50%,rgba(147,197,253,0.04) 0%,transparent 50%),radial-gradient(ellipse at 50% 100%,rgba(196,181,253,0.04) 0%,transparent 50%)"}}></div>

  <div className="card-green" style={{display:"flex",flexDirection:"column",flex:1,background:"linear-gradient(165deg,rgba(125,211,168,0.09) 0%,rgba(125,211,168,0.02) 100%)",borderTop:"1px solid rgba(125,211,168,0.3)",borderRight:"1px solid rgba(125,211,168,0.08)",borderBottom:"1px solid rgba(125,211,168,0.08)",borderLeft:"3px solid #7dd3a8",borderRadius:"4px 18px 18px 4px",padding:"28px",position:"relative",overflow:"hidden"}}>
    <div style={{position:"absolute",top:0,right:0,width:"140px",height:"140px",background:"radial-gradient(circle,rgba(125,211,168,0.15) 0%,transparent 70%)",borderRadius:"50%",transform:"translate(35%,-35%)"}}></div>
    <span style={{fontSize:"34px",marginBottom:"16px",filter:"drop-shadow(0 0 10px rgba(125,211,168,0.5))"}}>📈</span>
    <span style={{fontSize:"15px",fontWeight:800,color:"#7dd3a8",marginBottom:"10px",letterSpacing:"-0.3px"}}>finance_transformer</span>
    <span style={{fontSize:"13px",color:"#5a6a72",lineHeight:1.7,flex:1}}>can transformers read stock charts? pytorch playground adapting attention for financial time-series.</span>
    <div style={{display:"flex",marginTop:"18px",alignSelf:"flex-start",background:"rgba(125,211,168,0.1)",borderRadius:"8px",padding:"6px 12px",border:"1px solid rgba(125,211,168,0.25)",backdropFilter:"blur(10px)"}}>
      <span style={{fontSize:"11px",color:"#5a8a6a",letterSpacing:"0.4px",fontWeight:600}}>python · pytorch</span>
    </div>
  </div>

  <div className="card-blue" style={{display:"flex",flexDirection:"column",flex:1,background:"linear-gradient(165deg,rgba(147,197,253,0.09) 0%,rgba(147,197,253,0.02) 100%)",borderTop:"1px solid rgba(147,197,253,0.3)",borderRight:"1px solid rgba(147,197,253,0.08)",borderBottom:"1px solid rgba(147,197,253,0.08)",borderLeft:"3px solid #93c5fd",borderRadius:"4px 18px 18px 4px",padding:"28px",position:"relative",overflow:"hidden"}}>
    <div style={{position:"absolute",top:0,right:0,width:"140px",height:"140px",background:"radial-gradient(circle,rgba(147,197,253,0.15) 0%,transparent 70%)",borderRadius:"50%",transform:"translate(35%,-35%)"}}></div>
    <span style={{fontSize:"34px",marginBottom:"16px",filter:"drop-shadow(0 0 10px rgba(147,197,253,0.5))"}}>🎲</span>
    <span style={{fontSize:"15px",fontWeight:800,color:"#93c5fd",marginBottom:"10px",letterSpacing:"-0.3px"}}>DQN for Ludo</span>
    <span style={{fontSize:"13px",color:"#5a6a72",lineHeight:1.7,flex:1}}>teaching AI to beat my cousins. double DQN + prioritized replay + mandatory chai breaks.</span>
    <div style={{display:"flex",marginTop:"18px",alignSelf:"flex-start",background:"rgba(147,197,253,0.1)",borderRadius:"8px",padding:"6px 12px",border:"1px solid rgba(147,197,253,0.25)",backdropFilter:"blur(10px)"}}>
      <span style={{fontSize:"11px",color:"#4a6a8a",letterSpacing:"0.4px",fontWeight:600}}>RL · double DQN</span>
    </div>
  </div>

  <div className="card-purple" style={{display:"flex",flexDirection:"column",flex:1,background:"linear-gradient(165deg,rgba(196,181,253,0.09) 0%,rgba(196,181,253,0.02) 100%)",borderTop:"1px solid rgba(196,181,253,0.3)",borderRight:"1px solid rgba(196,181,253,0.08)",borderBottom:"1px solid rgba(196,181,253,0.08)",borderLeft:"3px solid #c4b5fd",borderRadius:"4px 18px 18px 4px",padding:"28px",position:"relative",overflow:"hidden"}}>
    <div style={{position:"absolute",top:0,right:0,width:"140px",height:"140px",background:"radial-gradient(circle,rgba(196,181,253,0.15) 0%,transparent 70%)",borderRadius:"50%",transform:"translate(35%,-35%)"}}></div>
    <span style={{fontSize:"34px",marginBottom:"16px",filter:"drop-shadow(0 0 10px rgba(196,181,253,0.5))"}}>📦</span>
    <span style={{fontSize:"15px",fontWeight:800,color:"#c4b5fd",marginBottom:"10px",letterSpacing:"-0.3px"}}>other experiments</span>
    <span style={{fontSize:"13px",color:"#5a6a72",lineHeight:1.7,flex:1}}>agents · ML projects · sandboxes and some very fresh sprouts 🌱 still finding their feet.</span>
    <div style={{display:"flex",marginTop:"18px",alignSelf:"flex-start",background:"rgba(196,181,253,0.1)",borderRadius:"8px",padding:"6px 12px",border:"1px solid rgba(196,181,253,0.25)",backdropFilter:"blur(10px)"}}>
      <span style={{fontSize:"11px",color:"#6a5890",letterSpacing:"0.4px",fontWeight:600}}>various</span>
    </div>
  </div>
</div>
```

<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; padding: 8px 24px; max-width: 848px; margin: 0 auto;">

  <details open style="margin-bottom: 16px; background: linear-gradient(90deg, rgba(125,211,168,0.06) 0%, transparent 100%); border-left: 3px solid #7dd3a8; border-radius: 0 14px 14px 0; padding: 22px 28px;">
    <summary style="list-style: none; cursor: pointer; font-size: 16px; font-weight: 700; color: #e2e8f0; display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
      <span style="font-size: 20px;">📈</span>
      <span>finance_transformer</span>
      <span style="color: #7dd3a8; font-weight: 500;">— can transformers read stock charts?</span>
    </summary>
    <div style="margin-top: 18px; padding-left: 30px; color: #94a3b8; font-size: 14px; line-height: 1.85;">
      • python + pytorch playground<br>
      • adapting attention for continuous financial time-series<br>
      • spoiler: sometimes it works. mostly it confuses noise for signal. still fun.<br>
      👉 <a href="https://github.com/astroknot-sheep/finance_transformer" style="color: #7dd3a8; text-decoration: none; border-bottom: 1px solid rgba(125,211,168,0.35); font-weight: 500;">see the code</a>
    </div>
  </details>

  <details style="margin-bottom: 16px; background: linear-gradient(90deg, rgba(147,197,253,0.06) 0%, transparent 100%); border-left: 3px solid #93c5fd; border-radius: 0 14px 14px 0; padding: 22px 28px;">
    <summary style="list-style: none; cursor: pointer; font-size: 16px; font-weight: 700; color: #e2e8f0; display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
      <span style="font-size: 20px;">🎲</span>
      <span>DQN for Ludo</span>
      <span style="color: #93c5fd; font-weight: 500;">— teaching AI to play better than my cousins</span>
    </summary>
    <div style="margin-top: 18px; padding-left: 30px; color: #94a3b8; font-size: 14px; line-height: 1.85;">
      • double dqn + prioritized replay + chai breaks<br>
      • math notes included (no jargon without explanation)<br>
      👉 <a href="https://github.com/astroknot-sheep/Reinforcement_Learning_DQN_for_Ludo" style="color: #93c5fd; text-decoration: none; border-bottom: 1px solid rgba(147,197,253,0.35); font-weight: 500;">see the code</a>
    </div>
  </details>

  <details style="margin-bottom: 16px; background: linear-gradient(90deg, rgba(196,181,253,0.06) 0%, transparent 100%); border-left: 3px solid #c4b5fd; border-radius: 0 14px 14px 0; padding: 22px 28px;">
    <summary style="list-style: none; cursor: pointer; font-size: 16px; font-weight: 700; color: #e2e8f0; display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
      <span style="font-size: 20px;">📦</span>
      <span>other experiments</span>
    </summary>
    <div style="margin-top: 18px; padding-left: 30px; color: #94a3b8; font-size: 14px; line-height: 1.85;">
      • <a href="https://github.com/astroknot-sheep/TWS_WriterAgent" style="color: #c4b5fd; text-decoration: none; border-bottom: 1px solid rgba(196,181,253,0.35);">TWS_WriterAgent</a> — playful agent prototyping<br>
      • <a href="https://github.com/astroknot-sheep/ML_project_final" style="color: #c4b5fd; text-decoration: none; border-bottom: 1px solid rgba(196,181,253,0.35);">ML_project_final</a> — completed learning journey<br>
      • <a href="https://github.com/astroknot-sheep/mlproject" style="color: #c4b5fd; text-decoration: none; border-bottom: 1px solid rgba(196,181,253,0.35);">mlproject</a> — early sandbox<br>
      • <a href="https://github.com/astroknot-sheep/data-gravity-portfolio" style="color: #c4b5fd; text-decoration: none; border-bottom: 1px solid rgba(196,181,253,0.35);">data-gravity-portfolio</a> — fresh sprouts 🌱
    </div>
  </details>

</div>

```aura width=800 height=120
<div style={{display:"flex",alignItems:"center",width:"100%",height:"100%",background:"#020408",padding:"0 36px",position:"relative",overflow:"hidden",fontFamily:"-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif"}}>
  <style dangerouslySetInnerHTML={{__html:`
    @keyframes slide-in{from{opacity:0;transform:translateX(-12px);}to{opacity:1;transform:translateX(0);}}
    .pill-anim{animation:slide-in 0.5s ease both;}
    .p0{animation-delay:.05s}.p1{animation-delay:.12s}.p2{animation-delay:.19s}.p3{animation-delay:.26s}.p4{animation-delay:.33s}.p5{animation-delay:.40s}.p6{animation-delay:.47s}
  `}} />

  <div style={{position:"absolute",inset:0,background:"radial-gradient(ellipse at 50% 50%,rgba(255,176,24,0.04) 0%,transparent 70%)"}}></div>

  <div style={{display:"flex",alignItems:"center",marginRight:"32px",paddingRight:"32px",borderRight:"1px solid rgba(255,255,255,0.08)",position:"relative",zIndex:2}}>
    <span style={{fontSize:"12px",color:"#334155",letterSpacing:"1.8px",textTransform:"uppercase",fontWeight:700}}>stack</span>
  </div>

  <div style={{display:"flex",alignItems:"center",gap:"10px",flex:1,position:"relative",zIndex:2}}>
    <div className="pill-anim p0" style={{display:"flex",alignItems:"center",padding:"10px 20px",background:"rgba(255,255,255,0.04)",border:"1px solid rgba(255,255,255,0.1)",borderRadius:"10px",backdropFilter:"blur(10px)"}}>
      <span style={{fontSize:"13px",color:"#94a3b8",letterSpacing:"0.2px",fontWeight:500}}>python</span>
    </div>
    <div className="pill-anim p1" style={{display:"flex",alignItems:"center",padding:"10px 20px",background:"rgba(255,255,255,0.04)",border:"1px solid rgba(255,255,255,0.1)",borderRadius:"10px",backdropFilter:"blur(10px)"}}>
      <span style={{fontSize:"13px",color:"#94a3b8",letterSpacing:"0.2px",fontWeight:500}}>pytorch</span>
    </div>
    <div className="pill-anim p2" style={{display:"flex",alignItems:"center",padding:"10px 20px",background:"rgba(255,255,255,0.04)",border:"1px solid rgba(255,255,255,0.1)",borderRadius:"10px",backdropFilter:"blur(10px)"}}>
      <span style={{fontSize:"13px",color:"#94a3b8",letterSpacing:"0.2px",fontWeight:500}}>typescript</span>
    </div>
    <div className="pill-anim p3" style={{display:"flex",alignItems:"center",padding:"10px 20px",background:"rgba(255,255,255,0.04)",border:"1px solid rgba(255,255,255,0.1)",borderRadius:"10px",backdropFilter:"blur(10px)"}}>
      <span style={{fontSize:"13px",color:"#94a3b8",letterSpacing:"0.2px",fontWeight:500}}>git</span>
    </div>
    <div className="pill-anim p4" style={{display:"flex",alignItems:"center",padding:"10px 20px",background:"rgba(255,255,255,0.04)",border:"1px solid rgba(255,255,255,0.1)",borderRadius:"10px",backdropFilter:"blur(10px)"}}>
      <span style={{fontSize:"13px",color:"#94a3b8",letterSpacing:"0.2px",fontWeight:500}}>jupyter</span>
    </div>
    <div className="pill-anim p5" style={{display:"flex",alignItems:"center",padding:"10px 20px",background:"rgba(255,255,255,0.04)",border:"1px solid rgba(255,255,255,0.1)",borderRadius:"10px",backdropFilter:"blur(10px)"}}>
      <span style={{fontSize:"13px",color:"#94a3b8",letterSpacing:"0.2px",fontWeight:500}}>vs code</span>
    </div>
    <div className="pill-anim p6" style={{display:"flex",alignItems:"center",padding:"10px 20px",background:"rgba(255,176,24,0.12)",border:"1px solid rgba(255,176,24,0.45)",borderRadius:"10px",backdropFilter:"blur(10px)",boxShadow:"0 0 28px rgba(255,176,24,0.18)",position:"relative",overflow:"hidden"}}>
      <div style={{position:"absolute",inset:0,background:"radial-gradient(circle at 50% 0%,rgba(255,200,100,0.25) 0%,transparent 70%)"}}></div>
      <span style={{fontSize:"13px",color:"#fbbf24",letterSpacing:"0.2px",fontWeight:600,position:"relative",zIndex:2}}>chai ☕</span>
    </div>
  </div>
</div>
```

<div align="center" style="padding: 28px 24px 52px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <p style="margin: 0; font-size: 15px; color: #475569; font-style: italic; letter-spacing: 0.3px; line-height: 1.6;">
    i'm not an expert in any of these.<br>
    i just keep showing up.
  </p>
</div>

<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; padding: 48px 24px 32px; max-width: 800px; margin: 0 auto;">
  <h2 style="margin: 0 0 6px 0; font-size: 28px; font-weight: 800; color: #e2e8f0; letter-spacing: -0.6px;">want to interact? here's how.</h2>
  <p style="margin: 0; font-size: 14px; color: #64748b;">(no bots, no dead links)</p>
</div>

<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; padding: 0 24px 56px; max-width: 800px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px;">

  <div style="background: linear-gradient(165deg, rgba(255,176,24,0.07) 0%, rgba(255,176,24,0.01) 100%); border: 1px solid rgba(255,176,24,0.18); border-radius: 18px; padding: 30px; position: relative; overflow: hidden;">
    <div style="position: absolute; top: -24px; right: -24px; width: 90px; height: 90px; background: radial-gradient(circle, rgba(255,176,24,0.18) 0%, transparent 70%); border-radius: 50%;"></div>
    <div style="width: 48px; height: 48px; background: linear-gradient(135deg, rgba(255,176,24,0.2), rgba(255,176,24,0.05)); border-radius: 14px; display: flex; align-items: center; justify-content: center; margin-bottom: 18px; border: 1px solid rgba(255,176,24,0.3);">
      <span style="font-size: 24px;">🎲</span>
    </div>
    <h3 style="margin: 0 0 14px 0; font-size: 17px; font-weight: 700; color: #fbbf24;">quick game</h3>
    <p style="margin: 0; font-size: 13px; color: #94a3b8; line-height: 1.75;">
      guess which repo has a hidden comment that says <code style="background: rgba(255,255,255,0.05); padding: 3px 7px; border-radius: 5px; color: #e2e8f0; font-size: 12px; border: 1px solid rgba(255,255,255,0.08);">"you found me 🐑"</code>.<br><br>
      open an issue with the answer. first one gets my eternal gratitude + a detailed code review of your choice.
    </p>
  </div>

  <div style="background: linear-gradient(165deg, rgba(147,197,253,0.07) 0%, rgba(147,197,253,0.01) 100%); border: 1px solid rgba(147,197,253,0.18); border-radius: 18px; padding: 30px; position: relative; overflow: hidden;">
    <div style="position: absolute; top: -24px; right: -24px; width: 90px; height: 90px; background: radial-gradient(circle, rgba(147,197,253,0.18) 0%, transparent 70%); border-radius: 50%;"></div>
    <div style="width: 48px; height: 48px; background: linear-gradient(135deg, rgba(147,197,253,0.2), rgba(147,197,253,0.05)); border-radius: 14px; display: flex; align-items: center; justify-content: center; margin-bottom: 18px; border: 1px solid rgba(147,197,253,0.3);">
      <span style="font-size: 24px;">💬</span>
    </div>
    <h3 style="margin: 0 0 14px 0; font-size: 17px; font-weight: 700; color: #93c5fd;">ask me anything</h3>
    <p style="margin: 0; font-size: 13px; color: #94a3b8; line-height: 1.75;">
      • how do i start with RL?<br>
      • why does my transformer keep overfitting?<br>
      • how do i structure a proper ML project from scratch?<br>
      • what's your favorite chai spot?<br><br>
      → just open an issue. no question is too small.<br>
      → or start a discussion: <a href="https://github.com/astroknot-sheep/astroknot-sheep/discussions" style="color: #93c5fd; text-decoration: none; border-bottom: 1px solid rgba(147,197,253,0.35); font-weight: 500;">here</a>
    </p>
  </div>

  <div style="background: linear-gradient(165deg, rgba(196,181,253,0.07) 0%, rgba(196,181,253,0.01) 100%); border: 1px solid rgba(196,181,253,0.18); border-radius: 18px; padding: 30px; position: relative; overflow: hidden;">
    <div style="position: absolute; top: -24px; right: -24px; width: 90px; height: 90px; background: radial-gradient(circle, rgba(196,181,253,0.18) 0%, transparent 70%); border-radius: 50%;"></div>
    <div style="width: 48px; height: 48px; background: linear-gradient(135deg, rgba(196,181,253,0.2), rgba(196,181,253,0.05)); border-radius: 14px; display: flex; align-items: center; justify-content: center; margin-bottom: 18px; border: 1px solid rgba(196,181,253,0.3);">
      <span style="font-size: 24px;">🤝</span>
    </div>
    <h3 style="margin: 0 0 14px 0; font-size: 17px; font-weight: 700; color: #c4b5fd;">want to collaborate?</h3>
    <p style="margin: 0; font-size: 13px; color: #94a3b8; line-height: 1.75;">
      if you're working on:<br>
      • ethical AI<br>
      • financial ML experiments<br>
      • weird RL applications<br>
      • or just want to pair-program and learn…<br><br>
      …hit me up. i reply. (usually within 48 hrs.)
    </p>
  </div>

</div>

<div align="center" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; padding: 72px 24px; position: relative; overflow: hidden;">
  <div style="position: absolute; inset: 0; background: radial-gradient(ellipse at center, rgba(255,176,24,0.05) 0%, transparent 70%);"></div>

  <div style="position: relative; z-index: 2; max-width: 580px;">
    <h2 style="margin: 0 0 36px 0; font-size: 36px; font-weight: 900; background: linear-gradient(135deg, #f0f4fa 0%, #94a3b8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: -1.2px;">real talk</h2>

    <p style="margin: 0 0 28px 0; font-size: 18px; color: #cbd5e1; line-height: 1.65;">
      i'm not trying to "disrupt" anything.<br>
      i'm just:
    </p>

    <div style="display: flex; flex-direction: column; gap: 18px; margin-bottom: 36px; text-align: left; padding-left: 48px;">
      <div style="display: flex; align-items: center; gap: 16px;">
        <div style="width: 10px; height: 10px; background: #ff9d00; border-radius: 50%; box-shadow: 0 0 16px rgba(255,157,0,0.55); flex-shrink: 0;"></div>
        <span style="font-size: 16px; color: #e2e8f0; font-weight: 500;">learning in public</span>
      </div>
      <div style="display: flex; align-items: center; gap: 16px;">
        <div style="width: 10px; height: 10px; background: #3b82f6; border-radius: 50%; box-shadow: 0 0 16px rgba(59,130,246,0.55); flex-shrink: 0;"></div>
        <span style="font-size: 16px; color: #e2e8f0; font-weight: 500;">sharing half-baked ideas</span>
      </div>
      <div style="display: flex; align-items: center; gap: 16px;">
        <div style="width: 10px; height: 10px; background: #a855f7; border-radius: 50%; box-shadow: 0 0 16px rgba(168,85,247,0.55); flex-shrink: 0;"></div>
        <span style="font-size: 16px; color: #e2e8f0; font-weight: 500;">hoping one of them sticks and helps someone</span>
      </div>
    </div>

    <p style="margin: 0 0 24px 0; font-size: 15px; color: #64748b;">if that resonates —</p>

    <div style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 36px; text-align: left; padding-left: 48px; font-size: 15px; color: #94a3b8; line-height: 1.6;">
      <div>→ star a repo</div>
      <div>→ fork and break something</div>
      <div>→ open a discussion</div>
      <div>→ or just wave 👋</div>
    </div>

    <p style="margin: 0; font-size: 17px; color: #e2e8f0; font-weight: 500;">
      i see you. and i appreciate you being here.
    </p>
  </div>
</div>

<div align="center" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; padding: 48px 24px 72px; position: relative;">
  <div style="width: 80px; height: 1px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.25), transparent); margin: 0 auto 36px;"></div>

  <p style="margin: 0 0 18px 0; font-size: 14px; color: #475569; font-style: italic; line-height: 1.8;">
    p.s. if you read this whole thing:<br>
    you're either very curious or very bored.<br>
    either way — welcome. 🫶
  </p>

  <p style="margin: 0 0 36px 0; font-size: 13px; color: #334155; font-weight: 500; letter-spacing: 0.2px;">
    p.p.s. the sheep was definitely on purpose.
  </p>

  <p style="margin: 0; font-size: 11px; color: #1e293b; letter-spacing: 0.6px; text-transform: uppercase;">
    last updated: may 2026, sometime after midnight
  </p>
</div>
