# number_guess.py
import random

LOW, HIGH = 1, 100

def _hint(diff: int) -> str:
    """Return hot/warm/cold + direction."""
    if diff == 0:
        return "Bingo!"
    d = abs(diff)
    if d <= 3:
        base = "🔥 Scorching"
    elif d <= 10:
        base = "🌡 Warm"
    else:
        base = "❄ Cold"
    direction = "too high" if diff > 0 else "too low"
    return f"{base} — {direction}"

# ---------------- CLI ---------------- #
def play_cli():
    ans = random.randint(LOW, HIGH)
    tries = 0
    print(f"Guess a number between {LOW} and {HIGH}")
    while True:
        s = input("Your guess: ").strip()
        if not s.isdigit():
            print("Enter a number.")
            continue
        g = int(s)
        if not (LOW <= g <= HIGH):
            print(f"Out of range ({LOW}–{HIGH}).")
            continue
        tries += 1
        diff = g - ans
        if diff == 0:
            print(f"Correct! {ans} in {tries} guesses.")
            break
        else:
            print(_hint(diff))

# ---------------- Streamlit ---------------- #
def render_st(st):
    st.header("🔢 Number Guess")

    if "ng_ans" not in st.session_state:
        st.session_state.ng_ans = random.randint(LOW, HIGH)
        st.session_state.ng_tries = 0

    guess = st.number_input(f"Pick a number {LOW}–{HIGH}", LOW, HIGH, (LOW + HIGH)//2, 1)

    col1, col2 = st.columns(2)
    if col1.button("Submit"):
        st.session_state.ng_tries += 1
        diff = guess - st.session_state.ng_ans
        if diff == 0:
            st.success(f"Correct! {st.session_state.ng_ans} in {st.session_state.ng_tries} guesses.")
        else:
            st.info(_hint(diff))

    if col2.button("Reset"):
        del st.session_state["ng_ans"]
        del st.session_state["ng_tries"]
        st.rerun()

    st.caption(f"Attempts: {st.session_state.get('ng_tries', 0)}")