# app.py
import streamlit as st
from games import (
    dice_roller, nine_lives, mboka_quiz, slot_machine, number_guess,
    rps, robot_builder, tictactoe, memory, blackjack
)

st.set_page_config(page_title="Game Arcade", page_icon="🕹️", layout="centered")

ROUTES = {
    "Dice Roller": dice_roller.render_st,
    "Nine Lives": nine_lives.render_st,
    "Mboka Quiz (DRC)": mboka_quiz.render_st,
    "Slot Machine": slot_machine.render_st,
    "Number Guess": number_guess.render_st,
    "Rock–Paper–Scissors": rps.render_st,
    "Robot Builder": robot_builder.render_st,
    "Tic-Tac-Toe": tictactoe.render_st,
    "Memory": memory.render_st,
    "Blackjack": blackjack.render_st,
}

st.title("🎮 Game Arcade")
game = st.selectbox("Pick a game", list(ROUTES.keys()))
ROUTES[game](st)
