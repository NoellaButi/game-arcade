# rps.py
import random

CHOICES = ["rock", "paper", "scissors"]


def play_cli():
    while True:
        comp = random.choice(CHOICES)
        pick = input("rock/paper/scissors: ").lower()
        if pick not in CHOICES:
            continue

        print("You:", pick, "Comp:", comp)
        if pick == comp:
            print("Tie")
        elif (
            (pick == "rock" and comp == "scissors")
            or (pick == "scissors" and comp == "paper")
            or (pick == "paper" and comp == "rock")
        ):
            print("You win!")
        else:
            print("Lose")

        if input("Again? y/n: ") != "y":
            break


def render_st(st):
    st.header("✊✋✌️ Rock-Paper-Scissors")
    choice = st.radio("Your choice", CHOICES)
    if st.button("Play"):
        comp = random.choice(CHOICES)
        st.write("Computer:", comp)
        if choice == comp:
            st.info("Tie")
        elif (
            (choice == "rock" and comp == "scissors")
            or (choice == "scissors" and comp == "paper")
            or (choice == "paper" and comp == "rock")
        ):
            st.success("You win!")
        else:
            st.error("You lose")
