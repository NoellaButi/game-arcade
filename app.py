# app.py
from games import (
    dice_roller,
    nine_lives,
    mboka_quiz,
    slot_machine,
    number_guess,
    rps,
    robot_builder,
    tictactoe,
    memory,
    blackjack,
)

import streamlit as st

st.set_page_config(page_title="Game Arcade", page_icon="🕹️", layout="centered")

ROUTES = {
    "🎲 Dice Roller": dice_roller,
    "❤️ Nine Lives": nine_lives,
    "🧪 DRC Quiz (MCQ)": mboka_quiz,
    "🎰 Slot-Machine": slot_machine,
    "🔢 Number Guess": number_guess,
    "✊✋✌️ Rock-Paper-Scissors": rps,
    "🤖 Robot Builder": robot_builder,
    "⭕❌ Tic-Tac-Toe (minimax)": tictactoe,
    "🧠 Memory": memory,
    "🃏 Blackjack": blackjack,
}

st.sidebar.title("🕹️ Game Arcade")
choice = st.sidebar.radio("Choose a game:", list(ROUTES.keys()))
mod = ROUTES[choice]

if hasattr(mod, "render_st"):
    mod.render_st(st)
else:
    st.info("This game has no Streamlit UI yet. Run it via CLI.")
    if hasattr(mod, "play_cli"):
        st.code(f"python -m games.{mod.__name__.split('_')[-1]}")

st.sidebar.markdown("_____")
st.sidebar.caption("Built with ❤️ by Noëlla")
