# nine_lives.py
import random

WORDS = ["pizza", "fairy", "teeth", "shirt", "otter", "plane", "brush", "horse", "light"]
HEART = "❤️"

# ---------------- CLI ---------------- #
def play_cli():
    deck = _new_deck()
    last = None
    while True:
        secret = _deal_word(deck, last)
        last = secret
        clue = ["_"] * len(secret)
        lives = 9
        guessed = set()

        while lives > 0 and "_" in clue:
            print("\nWord:", " ".join(clue), " Lives:", HEART * lives, " Guessed:", " ".join(sorted(guessed)) or "_")
            g = input("Guess a letter or the word: ").strip().lower()
            if not g:
                continue
            if len(g) > 1:
                if g == secret:
                    clue = list(secret)
                    break
                lives -= 1
            else:
                if g in guessed:
                    print("Already tried.")
                    continue
                guessed.add(g)
                hits = 0
                for i, ch in enumerate(secret):
                    if ch == g and clue[i] == "_":
                        clue[i] = g
                        hits += 1
                if hits == 0:
                    lives -= 1

        print("You won!" if "_" not in clue else f"You lost! Word: {secret}")
        if input("Next word? (y/n): ").lower() != "y":
            break

def _new_deck():
    deck = WORDS[:]  # copy
    random.shuffle(deck)
    return deck

def _deal_word(deck, last_word=None):
    """Pop next word from deck; reshuffle when empty; avoid immediate repeat vs last_word."""
    if not deck:
        deck[:] = _new_deck()
    # avoid back-to-back duplicate if there is more than 1 unique word
    if last_word is not None and len(set(WORDS)) > 1:
        # try up to len(deck) times to avoid last_word
        for _ in range(len(deck)):
            w = deck.pop()
            if w != last_word:
                return w
            # put it back temporarily to avoid losing it
            deck.insert(0, w)
        # if we couldn't avoid, just pop
    return deck.pop()

# ---------------- Streamlit ---------------- #
def render_st(st):
    st.header("❤️ Nine Lives")

    # one-time init
    if "nl_deck" not in st.session_state:
        st.session_state.nl_deck = _new_deck()
        st.session_state.nl_last = None
        _start_new_round(st)

    # status
    secret = st.session_state.nl_secret
    clue   = st.session_state.nl_clue
    lives  = st.session_state.nl_lives
    guessed= st.session_state.nl_guessed

    col1, col2 = st.columns(2)
    with col1:
        st.write("**Word:**", " ".join(clue))
    with col2:
        st.write("**Lives:**", "❤" * max(0, lives))
    st.caption(f"Guessed: {' '.join(sorted(guessed)) if guessed else '_'}")

    with st.form("nl_form", clear_on_submit=False):
        guess = st.text_input("Guess a letter or the whole word:", key="nl_input")
        c1, c2, c3 = st.columns(3)
        submitted = c1.form_submit_button("Submit Guess")
        next_word = c2.form_submit_button("Next Word")
        reset_all = c3.form_submit_button("Reset Deck")

    if reset_all:
        st.session_state.nl_deck = _new_deck()
        st.session_state.nl_last = None
        _start_new_round(st)
        st.rerun()

    if next_word:
        _start_new_round(st)
        st.rerun()

    if submitted:
        g = (guess or "").strip().lower()
        if g and lives > 0 and "_" in clue:
            if len(g) > 1:
                if g == secret:
                    st.session_state.nl_clue = list(secret)
                else:
                    st.session_state.nl_lives -= 1
            else:
                if g.isalpha() and g not in guessed:
                    guessed.add(g)
                    hits = 0
                    for i, ch in enumerate(secret):
                        if ch == g and clue[i] == "_":
                            clue[i] = g
                            hits += 1
                    if hits == 0:
                        st.session_state.nl_lives -= 1
        st.rerun()

    if "_" not in st.session_state.nl_clue:
        st.success(f"You won! Word: {secret}")
    elif st.session_state.nl_lives <= 0:
        st.error(f"You lost! Word was: {secret}")


def _start_new_round(st):
    """Start a new round using the deck, avoiding immediate repeats."""
    secret = _deal_word(st.session_state.nl_deck, st.session_state.get("nl_last"))
    st.session_state.nl_last = secret
    st.session_state.nl_secret = secret
    st.session_state.nl_clue = ["_"] * len(secret)
    st.session_state.nl_lives = 9
    st.session_state.nl_guessed = set()