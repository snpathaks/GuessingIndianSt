Hello👋, I'm Shalini . This repository contains basic games written in C++ and java languauge.<br>
<h1>Basic games:</h1>
<h5>By Shalini......</h5>
<svg viewBox="0 0 800 300" xmlns="http://www.w3.org/2000/svg">
  <!-- Chess Board (Left) -->
  <g transform="translate(50,50)">
    <!-- Board -->
    <rect x="0" y="0" width="200" height="200" fill="#fff" stroke="#000"/>
    <!-- Grid -->
    <g id="chess-squares">
      <pattern id="chess-pattern" width="25" height="25" patternUnits="userSpaceOnUse">
        <rect width="25" height="25" fill="#fff"/>
        <rect width="25" height="25" fill="#8B4513"/>
      </pattern>
      <g id="rows">
        <rect width="200" height="200" fill="url(#chess-pattern)"/>
        <g transform="translate(25,0)">
          <rect width="200" height="200" fill="url(#chess-pattern)"/>
        </g>
      </g>
    </g>
    <!-- Some Chess Pieces (simplified) -->
    <circle cx="25" cy="25" r="10" fill="#000"/>
    <circle cx="75" cy="25" r="10" fill="#000"/>
    <circle cx="25" cy="175" r="10" fill="#fff" stroke="#000"/>
    <circle cx="75" cy="175" r="10" fill="#fff" stroke="#000"/>
    <text x="100" y="230" text-anchor="middle" fill="#000">Chess</text>
  </g>

  <!-- Carrom Board (Middle) -->
  <g transform="translate(300,50)">
    <!-- Main Board -->
    <rect x="0" y="0" width="200" height="200" fill="#f4d03f" stroke="#000" stroke-width="2"/>
    <!-- Corner Pockets -->
    <circle cx="0" cy="0" r="15" fill="#000"/>
    <circle cx="200" cy="0" r="15" fill="#000"/>
    <circle cx="0" cy="200" r="15" fill="#000"/>
    <circle cx="200" cy="200" r="15" fill="#000"/>
    <!-- Center Circle -->
    <circle cx="100" cy="100" r="30" fill="none" stroke="#800000" stroke-width="2"/>
    <!-- Some Carrom Men -->
    <circle cx="90" cy="90" r="8" fill="#fff" stroke="#000"/>
    <circle cx="110" cy="90" r="8" fill="#000"/>
    <circle cx="90" cy="110" r="8" fill="#000"/>
    <circle cx="110" cy="110" r="8" fill="#fff" stroke="#000"/>
    <text x="100" y="230" text-anchor="middle" fill="#000">Carrom</text>
  </g>

  <!-- Sudoku Grid (Right) -->
  <g transform="translate(550,50)">
    <!-- Main Grid -->
    <rect x="0" y="0" width="200" height="200" fill="#fff" stroke="#000" stroke-width="2"/>
    <!-- Vertical Lines -->
    <line x1="66" y1="0" x2="66" y2="200" stroke="#000" stroke-width="2"/>
    <line x1="133" y1="0" x2="133" y2="200" stroke="#000" stroke-width="2"/>
    <!-- Horizontal Lines -->
    <line x1="0" y1="66" x2="200" y2="66" stroke="#000" stroke-width="2"/>
    <line x1="0" y1="133" x2="200" y2="133" stroke="#000" stroke-width="2"/>
    <!-- Sample Numbers -->
    <text x="30" y="40" font-size="20">5</text>
    <text x="97" y="40" font-size="20">3</text>
    <text x="164" y="40" font-size="20">7</text>
    <text x="30" y="106" font-size="20">6</text>
    <text x="97" y="106" font-size="20">1</text>
    <text x="164" y="172" font-size="20">9</text>
    <text x="100" y="230" text-anchor="middle" fill="#000">Sudoku</text>
  </g>
</svg>

Game 0 : The Avengers Game 🦹‍♂️🕸️⚒️.<br>
Game 1 : Lets Guess the states of India 🤔.<br>
Game 2 : Place to Escape 🏃‍➡️🏃‍♀️‍➡️.<br>
