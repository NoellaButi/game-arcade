# rps.py
import random

CHOICES = ["rock", "paper", "scissors"]

def play_cli():
    while True:
        comp = random.choice(CHOICES)
        p = input("rock/paper/scissors: ").lower()
        if p not in CHOICES: continue
        print(f"You:", p, " Comp:", comp)
        if p == comp: print("Tie")
        elif (p == "rock" and comp == "scissors") or (p == "scissors" and comp == "paper") or (p == "paper" and comp == "rock"):
            print("You win!")
        else: print("Lose")
        if input("Again? y/n: ") != "y": break

def render_st(st):
    st.header("✊✋✌️ Rock-Paper-Scissors")
    c = st.radio("Your choice", CHOICES)
    if st.button("Play"):
        comp = random.choice(CHOICES)
        st.write("Computer", comp)
        if c == comp: st.info("Tie")
        elif (c == "rock" and comp == "scissors") or (c == "scissors" and comp == "paper") or (c == "paper" and comp == "rock"):
            st.success("You win!")
        else: st.error("You lose")