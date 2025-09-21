# dice_roller.py
import random

DICE_ART = {
    1: ("┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"),
    2: ("┌─────────┐", "│ ●       │", "│         │", "│       ● │", "└─────────┘"),
    3: ("┌─────────┐", "│ ●       │", "│    ●    │", "│       ● │", "└─────────┘"),
    4: ("┌─────────┐", "│ ●     ● │", "│         │", "│ ●     ● │", "└─────────┘"),
    5: ("┌─────────┐", "│ ●     ● │", "│    ●    │", "│ ●     ● │", "└─────────┘"),
    6: ("┌─────────┐", "│ ●     ● │", "│ ●     ● │", "│ ●     ● │", "└─────────┘"),
}

def play_cli():
    n = int(input("How many dice? "))
    rolls = [random.randint(1, 6) for _ in range(n)]
    for row in range(5):
        print("  ".join(DICE_ART[r][row] for r in rolls))
    print("Total:", sum(rolls))

def render_st(st):
    st.header("🎲 Dice Roller")
    n = st.slider("Number of dice", 1, 10, 2)
    if st.button("Roll"):
        rolls = [random.randint(1, 6) for _ in range(n)]
        lines = ["  ".join(DICE_ART[r][row] for r in rolls) for row in range(5)]
        # st.code renders in a monospace block and preserves spacing
        st.code("\n".join(lines))
        st.success(f"Total: {sum(rolls)}  |  Rolls: {rolls}")