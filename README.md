# Game Arcade 🕹️🎲  
Play 10 classic mini-games in one place — via **Streamlit web app** or **CLI**.

![Language](https://img.shields.io/badge/language-Python-blue.svg) 
![App](https://img.shields.io/badge/app-Streamlit-red.svg) 
![Modes](https://img.shields.io/badge/modes-CLI%20%2B%20Web-7957D5.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg) 
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://game-arcade-noella-buti.streamlit.app)

---

✨ **Overview**  

This project is a modular **mini-game arcade** where each game works in **two modes**:  
- 🖥️ **Streamlit app** — play in the browser  
- 💻 **CLI mode** — run each game standalone in the terminal  

All games live in `games/` with a common interface (`play_cli()` and `render_st(st)`), making the code clean, reusable, and expandable.  

🎮 **Included Games**  
- 🎲 Dice Roller — roll N dice with ASCII art  
- ❤️ Nine Lives — word guessing with no-repeat deck  
- 🧪 Mboka Quiz (DRC) — 100 questions with explanations & images  
- 🎰 Slot Machine — 3-reel with credits & payouts  
- 🔢 Number Guess — hot/warm/cold + higher/lower hints  
- ✊✋✌️ Rock–Paper–Scissors — best of 5 vs computer  
- 🤖 Robot Builder — budget build with live SVG robot preview  
- ⭕❌ Tic-Tac-Toe (minimax) — unbeatable AI  
- 🧠 Memory — 4×4 concentration with move counter  
- 🃏 Blackjack — single-deck, dealer hits to 17  

---

🛠️ **Workflow**  

- Build each game as a module inside `games/`  
- Import modules into `app.py` to auto-register in Streamlit sidebar  
- Use `st.session_state` for per-game state handling  
- Deploy via Streamlit Cloud (1-click)  

📁 **Repository Layout**  
```bash
game-arcade/
├─ app.py             # Streamlit hub
├─ games/             # all 10 games
│  ├─ dice_roller.py
│  ├─ nine_lives.py
│  ├─ mboka_quiz.py
│  ├─ slot_machine.py
│  ├─ number_guess.py
│  ├─ rps.py
│  ├─ robot_builder.py
│  ├─ tictactoe.py
│  ├─ memory.py
│  └─ blackjack.py
├─ requirements.txt   # streamlit>=1.34
├─ .gitignore
├─ README.md
└─ LICENSE
```

🚦 **Demo**

Run locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Run a specific game (CLI):
```bash
python -m games.blackjack
python -m games.mboka_quiz
```

🔍 **Features**

- 10 self-contained games in one hub
- Streamlit UI + CLI fallback
- Randomized logic (non-repeating words in Nine Lives)
- SVG-based robot builder with real illustration
- Quiz with explanations & images always shown
- Expandable: drop new `games/foo.py` with the 2 functions, and it just works

🚀 **Deployment**

This arcade is deployed on Streamlit Cloud:

👉 [Try it here](https://game-arcade-noellabuti.streamlit.app)

📜 License

MIT (see [LICENSE](LICENSE))
