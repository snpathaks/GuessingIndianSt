Hello👋, I'm Shalini . This repository contains basic games written in C++ and java languauge.<br>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
    <!-- Definitions -->
    <defs>
        <!-- Controller body gradient -->
        <linearGradient id="controllerGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#2a2a2a;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#1a1a1a;stop-opacity:1" />
        </linearGradient>
        
        <!-- Neon glow effects -->
        <filter id="neonGlow">
            <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="blur" />
            <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -7" result="glow" />
            <feBlend in="SourceGraphic" in2="glow" mode="normal" />
        </filter>

        <!-- Button shine -->
        <linearGradient id="buttonShine" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#444;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#333;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#222;stop-opacity:1" />
        </linearGradient>
    </defs>

    <!-- Black background -->
    <rect width="800" height="600" fill="#000000"/>

    <!-- Main Controller -->
    <g transform="translate(200,150)">
        <!-- Controller body -->
        <path d="M 200,0 
                 C 300,-30 350,0 380,50
                 C 400,100 400,200 380,250
                 C 350,300 300,330 200,300
                 C 100,330 50,300 20,250
                 C 0,200 0,100 20,50
                 C 50,0 100,-30 200,0"
              fill="url(#controllerGradient)"
              stroke="#333"
              stroke-width="3"/>

        <!-- Grip highlights -->
        <path d="M 50,50 
                 C 30,100 30,200 50,250"
              fill="none"
              stroke="#444"
              stroke-width="2"
              opacity="0.5"/>
        <path d="M 350,50 
                 C 370,100 370,200 350,250"
              fill="none"
              stroke="#444"
              stroke-width="2"
              opacity="0.5"/>

        <!-- Left Analog Stick -->
        <g transform="translate(80,120)">
            <circle cx="0" cy="0" r="25" fill="#111" stroke="#333" stroke-width="2"/>
            <circle cx="0" cy="0" r="20" fill="#222" stroke="#444" stroke-width="2"/>
            <circle cx="0" cy="0" r="15" fill="#333"/>
        </g>

        <!-- Right Analog Stick -->
        <g transform="translate(280,180)">
            <circle cx="0" cy="0" r="25" fill="#111" stroke="#333" stroke-width="2"/>
            <circle cx="0" cy="0" r="20" fill="#222" stroke="#444" stroke-width="2"/>
            <circle cx="0" cy="0" r="15" fill="#333"/>
        </g>

        <!-- D-Pad with glow -->
        <g transform="translate(80,180)" filter="url(#neonGlow)">
            <rect x="-15" y="-45" width="30" height="40" fill="#222" rx="5"/>
            <rect x="-15" y="5" width="30" height="40" fill="#222" rx="5"/>
            <rect x="-45" y="-15" width="40" height="30" fill="#222" rx="5"/>
            <rect x="5" y="-15" width="40" height="30" fill="#222" rx="5"/>
            <circle cx="0" cy="0" r="15" fill="#333"/>
        </g>

        <!-- Face Buttons with neon glow -->
        <g transform="translate(280,120)" filter="url(#neonGlow)">
            <!-- A Button -->
            <circle cx="0" cy="30" r="15" fill="#00ff00" opacity="0.8"/>
            <text x="0" y="35" text-anchor="middle" fill="white" font-size="12">A</text>
            
            <!-- B Button -->
            <circle cx="30" cy="0" r="15" fill="#ff0000" opacity="0.8"/>
            <text x="30" y="5" text-anchor="middle" fill="white" font-size="12">B</text>
            
            <!-- X Button -->
            <circle cx="-30" cy="0" r="15" fill="#0088ff" opacity="0.8"/>
            <text x="-30" y="5" text-anchor="middle" fill="white" font-size="12">X</text>
            
            <!-- Y Button -->
            <circle cx="0" cy="-30" r="15" fill="#ffff00" opacity="0.8"/>
            <text x="0" y="-25" text-anchor="middle" fill="white" font-size="12">Y</text>
        </g>

        <!-- Shoulder Buttons with shine -->
        <path d="M 50,0 
                 C 70,-20 130,-20 150,0"
              fill="url(#buttonShine)"
              stroke="#444"
              stroke-width="2"/>
        <path d="M 250,0 
                 C 270,-20 330,-20 350,0"
              fill="url(#buttonShine)"
              stroke="#444"
              stroke-width="2"/>

        <!-- Triggers with shine -->
        <path d="M 50,-20 
                 C 70,-40 130,-40 150,-20"
              fill="url(#buttonShine)"
              stroke="#444"
              stroke-width="2"/>
        <path d="M 250,-20 
                 C 270,-40 330,-40 350,-20"
              fill="url(#buttonShine)"
              stroke="#444"
              stroke-width="2"/>

        <!-- Center Panel with LED -->
        <g transform="translate(180,140)">
            <!-- Share Button -->
            <circle cx="-20" cy="0" r="10" fill="#222" stroke="#333" stroke-width="1"/>
            
            <!-- Menu Button -->
            <circle cx="20" cy="0" r="10" fill="#222" stroke="#333" stroke-width="1"/>
            
            <!-- Home Button with glow -->
            <circle cx="0" cy="0" r="15" fill="#222" filter="url(#neonGlow)"/>
            <circle cx="0" cy="0" r="12" fill="#00ff88" opacity="0.6"/>
        </g>

        <!-- Touch Pad with subtle glow -->
        <rect x="140" y="40" width="120" height="60" rx="10" fill="#181818" stroke="#333" stroke-width="1"/>
        <rect x="145" y="45" width="110" height="50" rx="8" fill="#222" opacity="0.5"/>
    </g>

    <!-- LED Status Indicators -->
    <g transform="translate(350,100)">
        <circle cx="0" cy="0" r="3" fill="#00ff88" filter="url(#neonGlow)"/>
        <circle cx="15" cy="0" r="3" fill="#00ff88" filter="url(#neonGlow)"/>
        <circle cx="30" cy="0" r="3" fill="#00ff88" filter="url(#neonGlow)"/>
        <circle cx="45" cy="0" r="3" fill="#00ff88" filter="url(#neonGlow)"/>
    </g>

    <!-- USB-C Port -->
    <rect x="380" y="280" width="40" height="10" rx="5" fill="#222" stroke="#333" stroke-width="1"/>

    <!-- Subtle Reflection Effects -->
    <path d="M 200,450 C 300,430 500,430 600,450" 
          fill="none" 
          stroke="#ffffff" 
          stroke-width="1" 
          opacity="0.1"/>
</svg>
Game 0 : The Avengers Game 🦹‍♂️🕸️⚒️.<br>
Game 1 : Lets Guess the states of India 🤔.<br>
Game 2 : Place to Escape 🏃‍➡️🏃‍♀️‍➡️.<br>
