<!-- hey. thanks for stopping by. -->

```aura width=800 height=230
<div style={{
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
  width: '100%',
  height: '100%',
  background: 'linear-gradient(155deg, #0b0e14 0%, #0e1119 55%, #10151f 100%)',
  padding: '0 56px',
  overflow: 'hidden',
}}>
  <style>{`
    @keyframes wobble {
      0%, 100% { transform: rotate(-4deg) scale(1); }
      50% { transform: rotate(4deg) scale(1.08); }
    }
    #sheep { animation: wobble 2.8s ease-in-out infinite; }
    @keyframes shimmer {
      0% { opacity: 0.5; }
      50% { opacity: 1; }
      100% { opacity: 0.5; }
    }
    #handle { animation: shimmer 4s ease-in-out infinite; }
  `}</style>

  <div style={{ display: 'flex', alignItems: 'center', gap: 18, marginBottom: 14 }}>
    <span style={{
      fontSize: 76,
      fontWeight: 900,
      color: '#eef0f5',
      letterSpacing: '-4px',
      lineHeight: 1,
    }}>hi.</span>
    <span id="sheep" style={{ fontSize: 48, display: 'flex', transformOrigin: 'bottom center' }}>🐑</span>
  </div>

  <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginBottom: 20 }}>
    <span style={{ fontSize: 20, color: '#4a5566', fontWeight: 400 }}>i'm</span>
    <span style={{
      fontSize: 34,
      fontWeight: 800,
      color: '#f5c87e',
      letterSpacing: '-1.2px',
    }}>dhriman</span>
    <div id="handle" style={{
      display: 'flex',
      alignItems: 'center',
      background: 'rgba(245,200,126,0.07)',
      border: '1px solid rgba(245,200,126,0.2)',
      borderRadius: 24,
      padding: '5px 14px',
      marginLeft: 2,
    }}>
      <span style={{ fontSize: 12, color: '#9a7a3a', letterSpacing: '0.5px' }}>@astroknot-sheep</span>
    </div>
  </div>

  <div style={{ display: 'flex', alignItems: 'center', gap: 20 }}>
    <span style={{ fontSize: 13, color: '#333d4f', letterSpacing: '0.4px' }}>
      building small things  ·  learning in public  ·  the sheep is on purpose
    </span>
  </div>
</div>
```

i don't have a grand mission statement.  
i just like building small things that *might* help someone.

---

## what i'm fiddling with right now

```aura width=800 height=196
<div style={{
  display: 'flex',
  alignItems: 'stretch',
  width: '100%',
  height: '100%',
  background: '#0b0e14',
  padding: '18px 20px',
  gap: 14,
}}>

  <div style={{
    display: 'flex',
    flexDirection: 'column',
    flex: 1,
    background: 'rgba(125, 211, 168, 0.04)',
    border: '1px solid rgba(125, 211, 168, 0.12)',
    borderRadius: 12,
    padding: '18px 20px',
  }}>
    <span style={{ fontSize: 24, marginBottom: 10 }}>📈</span>
    <span style={{
      fontSize: 13,
      fontWeight: 700,
      color: '#7dd3a8',
      marginBottom: 7,
      letterSpacing: '-0.2px',
    }}>finance_transformer</span>
    <span style={{ fontSize: 12, color: '#56636e', lineHeight: 1.6, flex: 1 }}>
      can transformers read stock charts? python + pytorch playground adapting attention for continuous financial time-series.
    </span>
    <div style={{ display: 'flex', marginTop: 12 }}>
      <div style={{
        display: 'flex',
        background: 'rgba(125,211,168,0.07)',
        borderRadius: 5,
        padding: '3px 9px',
        border: '1px solid rgba(125,211,168,0.12)',
      }}>
        <span style={{ fontSize: 10, color: '#4a7a60', letterSpacing: '0.3px' }}>python · pytorch</span>
      </div>
    </div>
  </div>

  <div style={{
    display: 'flex',
    flexDirection: 'column',
    flex: 1,
    background: 'rgba(147, 197, 253, 0.04)',
    border: '1px solid rgba(147, 197, 253, 0.12)',
    borderRadius: 12,
    padding: '18px 20px',
  }}>
    <span style={{ fontSize: 24, marginBottom: 10 }}>🎲</span>
    <span style={{
      fontSize: 13,
      fontWeight: 700,
      color: '#93c5fd',
      marginBottom: 7,
      letterSpacing: '-0.2px',
    }}>DQN for Ludo</span>
    <span style={{ fontSize: 12, color: '#56636e', lineHeight: 1.6, flex: 1 }}>
      teaching AI to play better than my cousins. double DQN + prioritized replay + chai breaks.
    </span>
    <div style={{ display: 'flex', marginTop: 12 }}>
      <div style={{
        display: 'flex',
        background: 'rgba(147,197,253,0.07)',
        borderRadius: 5,
        padding: '3px 9px',
        border: '1px solid rgba(147,197,253,0.12)',
      }}>
        <span style={{ fontSize: 10, color: '#4a6a9a', letterSpacing: '0.3px' }}>RL · double DQN</span>
      </div>
    </div>
  </div>

  <div style={{
    display: 'flex',
    flexDirection: 'column',
    flex: 1,
    background: 'rgba(196, 181, 253, 0.04)',
    border: '1px solid rgba(196, 181, 253, 0.12)',
    borderRadius: 12,
    padding: '18px 20px',
  }}>
    <span style={{ fontSize: 24, marginBottom: 10 }}>📦</span>
    <span style={{
      fontSize: 13,
      fontWeight: 700,
      color: '#c4b5fd',
      marginBottom: 7,
      letterSpacing: '-0.2px',
    }}>other experiments</span>
    <span style={{ fontSize: 12, color: '#56636e', lineHeight: 1.6, flex: 1 }}>
      agents · ML projects · sandboxes · and some fresh sprouts 🌱 still finding their feet.
    </span>
    <div style={{ display: 'flex', marginTop: 12 }}>
      <div style={{
        display: 'flex',
        background: 'rgba(196,181,253,0.07)',
        borderRadius: 5,
        padding: '3px 9px',
        border: '1px solid rgba(196,181,253,0.12)',
      }}>
        <span style={{ fontSize: 10, color: '#6a5a8a', letterSpacing: '0.3px' }}>various</span>
      </div>
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

```aura width=800 height=72
<div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%',
  height: '100%',
  background: '#0b0e14',
  padding: '0 52px',
  gap: 10,
}}>
  <style>{`
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(6px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    .pill { animation: fadeUp 0.4s ease both; }
    #p0 { animation-delay: 0.00s; }
    #p1 { animation-delay: 0.07s; }
    #p2 { animation-delay: 0.14s; }
    #p3 { animation-delay: 0.21s; }
    #p4 { animation-delay: 0.28s; }
    #p5 { animation-delay: 0.35s; }
    #p6 { animation-delay: 0.42s; }
  `}</style>

  <div id="p0" class="pill" style={{
    display: 'flex', alignItems: 'center',
    padding: '7px 16px',
    background: 'rgba(255,255,255,0.04)',
    border: '1px solid rgba(255,255,255,0.08)',
    borderRadius: 8,
  }}>
    <span style={{ fontSize: 13, color: '#8892a4', letterSpacing: '0.2px' }}>python</span>
  </div>

  <div id="p1" class="pill" style={{
    display: 'flex', alignItems: 'center',
    padding: '7px 16px',
    background: 'rgba(255,255,255,0.04)',
    border: '1px solid rgba(255,255,255,0.08)',
    borderRadius: 8,
  }}>
    <span style={{ fontSize: 13, color: '#8892a4', letterSpacing: '0.2px' }}>pytorch</span>
  </div>

  <div id="p2" class="pill" style={{
    display: 'flex', alignItems: 'center',
    padding: '7px 16px',
    background: 'rgba(255,255,255,0.04)',
    border: '1px solid rgba(255,255,255,0.08)',
    borderRadius: 8,
  }}>
    <span style={{ fontSize: 13, color: '#8892a4', letterSpacing: '0.2px' }}>typescript</span>
  </div>

  <div id="p3" class="pill" style={{
    display: 'flex', alignItems: 'center',
    padding: '7px 16px',
    background: 'rgba(255,255,255,0.04)',
    border: '1px solid rgba(255,255,255,0.08)',
    borderRadius: 8,
  }}>
    <span style={{ fontSize: 13, color: '#8892a4', letterSpacing: '0.2px' }}>git</span>
  </div>

  <div id="p4" class="pill" style={{
    display: 'flex', alignItems: 'center',
    padding: '7px 16px',
    background: 'rgba(255,255,255,0.04)',
    border: '1px solid rgba(255,255,255,0.08)',
    borderRadius: 8,
  }}>
    <span style={{ fontSize: 13, color: '#8892a4', letterSpacing: '0.2px' }}>jupyter</span>
  </div>

  <div id="p5" class="pill" style={{
    display: 'flex', alignItems: 'center',
    padding: '7px 16px',
    background: 'rgba(255,255,255,0.04)',
    border: '1px solid rgba(255,255,255,0.08)',
    borderRadius: 8,
  }}>
    <span style={{ fontSize: 13, color: '#8892a4', letterSpacing: '0.2px' }}>vs code</span>
  </div>

  <div id="p6" class="pill" style={{
    display: 'flex', alignItems: 'center',
    padding: '7px 16px',
    background: 'rgba(245,200,126,0.08)',
    border: '1px solid rgba(245,200,126,0.2)',
    borderRadius: 8,
  }}>
    <span style={{ fontSize: 13, color: '#c4923a', letterSpacing: '0.2px' }}>chai ☕</span>
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
