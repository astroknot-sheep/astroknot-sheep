<!-- hey. thanks for stopping by. -->

```aura width=800 height=340
<div style={{
  display: 'flex',
  flexDirection: 'column',
  width: '100%',
  height: '100%',
  background: '#05080e',
  position: 'relative',
  overflow: 'hidden',
  padding: '48px 64px 44px',
}}>
  <style>{`
    @keyframes pulse-warm {
      0%,100% { opacity: .65; transform: scale(1); }
      50%      { opacity: 1;   transform: scale(1.07); }
    }
    @keyframes pulse-cool {
      0%,100% { opacity: .4;  transform: scale(1); }
      50%      { opacity: .85; transform: scale(1.1); }
    }
    @keyframes sheep-bob {
      0%,100% { transform: rotate(-7deg) translateY(0px); }
      50%      { transform: rotate(7deg)  translateY(-10px); }
    }
    @keyframes handle-glow {
      0%,100% { opacity: .7; }
      50%      { opacity: 1; }
    }
    #orb-warm  { animation: pulse-warm  5s ease-in-out infinite; }
    #orb-cool  { animation: pulse-cool  6s ease-in-out infinite; }
    #sheep-bob { animation: sheep-bob   2.8s ease-in-out infinite; }
    #handle    { animation: handle-glow 4s ease-in-out infinite; }
  `}</style>

  <div style={{
    position: 'absolute', top: 0, left: 0, right: 0, bottom: 0,
    backgroundImage: 'linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px)',
    backgroundSize: '44px 44px',
    display: 'flex',
  }} />

  <div id="orb-warm" style={{
    position: 'absolute', top: -160, right: -120,
    width: 580, height: 580,
    borderRadius: '50%',
    background: 'radial-gradient(circle, rgba(255,165,20,0.42) 0%, rgba(255,110,0,0.18) 38%, transparent 66%)',
    display: 'flex',
  }} />

  <div id="orb-cool" style={{
    position: 'absolute', bottom: -140, left: -80,
    width: 420, height: 420,
    borderRadius: '50%',
    background: 'radial-gradient(circle, rgba(60,130,255,0.22) 0%, transparent 64%)',
    display: 'flex',
  }} />

  <div style={{ display: 'flex', alignItems: 'flex-end', gap: 24, marginBottom: 20, position: 'relative' }}>
    <span style={{
      fontSize: 118,
      fontWeight: 900,
      color: '#edf0f7',
      letterSpacing: '-7px',
      lineHeight: 1,
    }}>hi.</span>
    <div id="sheep-bob" style={{ display: 'flex', marginBottom: 12 }}>
      <span style={{ fontSize: 70 }}>🐑</span>
    </div>
  </div>

  <div style={{ display: 'flex', alignItems: 'center', gap: 16, marginBottom: 24, position: 'relative' }}>
    <span style={{ fontSize: 24, color: '#38455a', fontWeight: 400 }}>i'm</span>
    <span style={{
      fontSize: 46,
      fontWeight: 900,
      color: '#ffb018',
      letterSpacing: '-2.2px',
    }}>dhriman</span>
    <div id="handle" style={{
      display: 'flex',
      alignItems: 'center',
      background: 'rgba(255,176,24,0.09)',
      border: '1px solid rgba(255,176,24,0.28)',
      borderRadius: 30,
      padding: '7px 18px',
      marginLeft: 6,
    }}>
      <span style={{ fontSize: 13, color: '#886010', letterSpacing: '0.6px' }}>@astroknot-sheep</span>
    </div>
  </div>

  <span style={{
    fontSize: 13,
    color: '#28354a',
    letterSpacing: '1.2px',
    textTransform: 'uppercase',
    position: 'relative',
  }}>
    building small things  ·  learning in public  ·  the sheep is on purpose
  </span>
</div>
```

i don't have a grand mission statement.  
i just like building small things that *might* help someone.

---

## what i'm fiddling with right now

```aura width=800 height=228
<div style={{
  display: 'flex',
  alignItems: 'stretch',
  width: '100%',
  height: '100%',
  background: '#05080e',
  padding: '20px 22px',
  gap: 16,
  position: 'relative',
  overflow: 'hidden',
}}>
  <style>{`
    @keyframes card-glow-green {
      0%,100% { box-shadow: 0 0 18px rgba(125,211,168,0.08); }
      50%      { box-shadow: 0 0 36px rgba(125,211,168,0.22); }
    }
    @keyframes card-glow-blue {
      0%,100% { box-shadow: 0 0 18px rgba(147,197,253,0.08); }
      50%      { box-shadow: 0 0 36px rgba(147,197,253,0.22); }
    }
    @keyframes card-glow-purple {
      0%,100% { box-shadow: 0 0 18px rgba(196,181,253,0.08); }
      50%      { box-shadow: 0 0 36px rgba(196,181,253,0.22); }
    }
    #card-green  { animation: card-glow-green  3s   ease-in-out infinite; }
    #card-blue   { animation: card-glow-blue   3.6s ease-in-out infinite; }
    #card-purple { animation: card-glow-purple 4.2s ease-in-out infinite; }
  `}</style>

  <div id="card-green" style={{
    display: 'flex', flexDirection: 'column', flex: 1,
    background: 'linear-gradient(160deg, rgba(125,211,168,0.07) 0%, rgba(125,211,168,0.02) 100%)',
    borderTop: '1px solid rgba(125,211,168,0.22)',
    borderRight: '1px solid rgba(125,211,168,0.1)',
    borderBottom: '1px solid rgba(125,211,168,0.1)',
    borderLeft: '3px solid #7dd3a8',
    borderRadius: '2px 14px 14px 2px',
    padding: '22px 22px',
  }}>
    <span style={{ fontSize: 28, marginBottom: 12 }}>📈</span>
    <span style={{ fontSize: 14, fontWeight: 800, color: '#7dd3a8', marginBottom: 8, letterSpacing: '-0.3px' }}>finance_transformer</span>
    <span style={{ fontSize: 12, color: '#4a5a64', lineHeight: 1.65, flex: 1 }}>
      can transformers read stock charts? pytorch playground adapting attention for financial time-series.
    </span>
    <div style={{
      display: 'flex', marginTop: 14, alignSelf: 'flex-start',
      background: 'rgba(125,211,168,0.08)', borderRadius: 6, padding: '4px 10px',
      border: '1px solid rgba(125,211,168,0.15)',
    }}>
      <span style={{ fontSize: 10, color: '#4a8060', letterSpacing: '0.4px' }}>python · pytorch</span>
    </div>
  </div>

  <div id="card-blue" style={{
    display: 'flex', flexDirection: 'column', flex: 1,
    background: 'linear-gradient(160deg, rgba(147,197,253,0.07) 0%, rgba(147,197,253,0.02) 100%)',
    borderTop: '1px solid rgba(147,197,253,0.22)',
    borderRight: '1px solid rgba(147,197,253,0.1)',
    borderBottom: '1px solid rgba(147,197,253,0.1)',
    borderLeft: '3px solid #93c5fd',
    borderRadius: '2px 14px 14px 2px',
    padding: '22px 22px',
  }}>
    <span style={{ fontSize: 28, marginBottom: 12 }}>🎲</span>
    <span style={{ fontSize: 14, fontWeight: 800, color: '#93c5fd', marginBottom: 8, letterSpacing: '-0.3px' }}>DQN for Ludo</span>
    <span style={{ fontSize: 12, color: '#4a5a64', lineHeight: 1.65, flex: 1 }}>
      teaching AI to beat my cousins. double DQN + prioritized replay + mandatory chai breaks.
    </span>
    <div style={{
      display: 'flex', marginTop: 14, alignSelf: 'flex-start',
      background: 'rgba(147,197,253,0.08)', borderRadius: 6, padding: '4px 10px',
      border: '1px solid rgba(147,197,253,0.15)',
    }}>
      <span style={{ fontSize: 10, color: '#4a6898', letterSpacing: '0.4px' }}>RL · double DQN</span>
    </div>
  </div>

  <div id="card-purple" style={{
    display: 'flex', flexDirection: 'column', flex: 1,
    background: 'linear-gradient(160deg, rgba(196,181,253,0.07) 0%, rgba(196,181,253,0.02) 100%)',
    borderTop: '1px solid rgba(196,181,253,0.22)',
    borderRight: '1px solid rgba(196,181,253,0.1)',
    borderBottom: '1px solid rgba(196,181,253,0.1)',
    borderLeft: '3px solid #c4b5fd',
    borderRadius: '2px 14px 14px 2px',
    padding: '22px 22px',
  }}>
    <span style={{ fontSize: 28, marginBottom: 12 }}>📦</span>
    <span style={{ fontSize: 14, fontWeight: 800, color: '#c4b5fd', marginBottom: 8, letterSpacing: '-0.3px' }}>other experiments</span>
    <span style={{ fontSize: 12, color: '#4a5a64', lineHeight: 1.65, flex: 1 }}>
      agents · ML projects · sandboxes and some very fresh sprouts 🌱 still finding their feet.
    </span>
    <div style={{
      display: 'flex', marginTop: 14, alignSelf: 'flex-start',
      background: 'rgba(196,181,253,0.08)', borderRadius: 6, padding: '4px 10px',
      border: '1px solid rgba(196,181,253,0.15)',
    }}>
      <span style={{ fontSize: 10, color: '#6a5890', letterSpacing: '0.4px' }}>various</span>
    </div>
  </div>
</div>
```

<details open>
<summary><strong>📈 finance_transformer</strong> — can transformers read stock charts?</summary>
<br>
• python + pytorch playground<br>
• adapting attention for continuous financial time-series<br>
• spoiler: sometimes it works. mostly it confuses noise for signal. still fun.<br>
👉 <a href="https://github.com/astroknot-sheep/finance_transformer">see the code</a>
</details>

<details>
<summary><strong>🎲 DQN for Ludo</strong> — teaching AI to play better than my cousins</summary>
<br>
• double dqn + prioritized replay + chai breaks<br>
• math notes included (no jargon without explanation)<br>
👉 <a href="https://github.com/astroknot-sheep/Reinforcement_Learning_DQN_for_Ludo">see the code</a>
</details>

<details>
<summary><strong>📦 other experiments</strong></summary>
<br>
• <a href="https://github.com/astroknot-sheep/TWS_WriterAgent">TWS_WriterAgent</a> — playful agent prototyping<br>
• <a href="https://github.com/astroknot-sheep/ML_project_final">ML_project_final</a> — completed learning journey<br>
• <a href="https://github.com/astroknot-sheep/mlproject">mlproject</a> — early sandbox<br>
• <a href="https://github.com/astroknot-sheep/data-gravity-portfolio">data-gravity-portfolio</a> — fresh sprouts 🌱
</details>

---

## tools i use (and sometimes fight with)

```aura width=800 height=90
<div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%',
  height: '100%',
  background: '#05080e',
  padding: '0 32px',
  position: 'relative',
  overflow: 'hidden',
}}>
  <style>{`
    @keyframes fadeSlide {
      from { opacity: 0; transform: translateY(8px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    .pill { animation: fadeSlide .5s ease both; }
    #t0{animation-delay:.05s} #t1{animation-delay:.12s} #t2{animation-delay:.19s}
    #t3{animation-delay:.26s} #t4{animation-delay:.33s} #t5{animation-delay:.40s}
    #t6{animation-delay:.47s}
    @keyframes chai-pulse {
      0%,100% { box-shadow: 0 0 0px rgba(255,176,24,0); }
      50%      { box-shadow: 0 0 16px rgba(255,176,24,0.35); }
    }
    #chai { animation: chai-pulse 2.5s ease-in-out infinite; }
  `}</style>

  <div style={{
    display: 'flex', alignItems: 'center',
    marginRight: 28, paddingRight: 28,
    borderRight: '1px solid rgba(255,255,255,0.07)',
  }}>
    <span style={{ fontSize: 11, color: '#28354a', letterSpacing: '1.4px', textTransform: 'uppercase' }}>stack</span>
  </div>

  <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
    <div id="t0" class="pill" style={{ display:'flex', alignItems:'center', padding:'9px 18px', background:'rgba(255,255,255,0.04)', border:'1px solid rgba(255,255,255,0.09)', borderRadius:9 }}>
      <span style={{ fontSize:13, color:'#7a8898', letterSpacing:'0.2px' }}>python</span>
    </div>
    <div id="t1" class="pill" style={{ display:'flex', alignItems:'center', padding:'9px 18px', background:'rgba(255,255,255,0.04)', border:'1px solid rgba(255,255,255,0.09)', borderRadius:9 }}>
      <span style={{ fontSize:13, color:'#7a8898', letterSpacing:'0.2px' }}>pytorch</span>
    </div>
    <div id="t2" class="pill" style={{ display:'flex', alignItems:'center', padding:'9px 18px', background:'rgba(255,255,255,0.04)', border:'1px solid rgba(255,255,255,0.09)', borderRadius:9 }}>
      <span style={{ fontSize:13, color:'#7a8898', letterSpacing:'0.2px' }}>typescript</span>
    </div>
    <div id="t3" class="pill" style={{ display:'flex', alignItems:'center', padding:'9px 18px', background:'rgba(255,255,255,0.04)', border:'1px solid rgba(255,255,255,0.09)', borderRadius:9 }}>
      <span style={{ fontSize:13, color:'#7a8898', letterSpacing:'0.2px' }}>git</span>
    </div>
    <div id="t4" class="pill" style={{ display:'flex', alignItems:'center', padding:'9px 18px', background:'rgba(255,255,255,0.04)', border:'1px solid rgba(255,255,255,0.09)', borderRadius:9 }}>
      <span style={{ fontSize:13, color:'#7a8898', letterSpacing:'0.2px' }}>jupyter</span>
    </div>
    <div id="t5" class="pill" style={{ display:'flex', alignItems:'center', padding:'9px 18px', background:'rgba(255,255,255,0.04)', border:'1px solid rgba(255,255,255,0.09)', borderRadius:9 }}>
      <span style={{ fontSize:13, color:'#7a8898', letterSpacing:'0.2px' }}>vs code</span>
    </div>
    <div id="chai" class="pill" style={{ display:'flex', alignItems:'center', padding:'9px 18px', background:'rgba(255,176,24,0.1)', border:'1px solid rgba(255,176,24,0.28)', borderRadius:9 }}>
      <span style={{ fontSize:13, color:'#c4841a', letterSpacing:'0.2px' }}>chai ☕</span>
    </div>
  </div>
</div>
```

i'm not an expert in any of these.  
i just keep showing up.

---

## want to interact? here's how. (no bots, no dead links)

### 🎲 quick game
guess which repo has a hidden comment that says `"you found me 🐑"`.  
open an issue with the answer. first one gets my eternal gratitude + a detailed code review of your choice.

### 💬 ask me anything
- how do i start with RL?
- why does my transformer keep overfitting?
- how do i structure a proper ML project from scratch?
- what's your favorite chai spot?

→ just open an issue. no question is too small.  
→ or start a discussion: [here](https://github.com/astroknot-sheep/astroknot-sheep/discussions)

### 🤝 want to collaborate?
if you're working on:
- ethical AI
- financial ML experiments
- weird RL applications
- or just want to pair-program and learn…

…hit me up. i reply. (usually within 48 hrs.)

---

## real talk

i'm not trying to "disrupt" anything.  
i'm just:

- learning in public  
- sharing half-baked ideas  
- hoping one of them sticks and helps someone

if that resonates —  
→ star a repo  
→ fork and break something  
→ open a discussion  
→ or just wave 👋

i see you. and i appreciate you being here.

---

> p.s. if you read this whole thing:  
> you're either very curious or very bored.  
> either way — welcome. 🫶  
>   
> p.p.s. the sheep was definitely on purpose.

<!-- last updated: may 2026, sometime after midnight -->
