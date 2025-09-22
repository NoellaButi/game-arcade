# memory.py
import random

EMOJIS = ["🍎", "🍌", "🍇", "🍑", "🍒", "🍉", "🍋", "🍊"]  # 8 pairs
HIDDEN = "■"


def _new_board():
    deck = EMOJIS * 2
    random.shuffle(deck)
    return deck  # length 16


def _all_matched(revealed):
    return all(revealed)


def play_cli():
    deck = _new_board()
    revealed = [False] * 16
    first = None
    moves = 0

    def show():
        for r in range(4):
            row = []
            for c in range(4):
                i = r * 4 + c
                row.append(deck[i] if revealed[i] else HIDDEN)
            print(" ".join(row))

    while not _all_matched(revealed):
        show()
        sel = input("Pick (1-16): ").strip()
        if not sel.isdigit():
            continue
        i = int(sel) - 1
        if i < 0 or i >= 16 or revealed[i]:
            continue

        if first is None:
            first = i
            revealed[i] = True
        else:
            revealed[i] = True
            moves += 1
            show()
            if deck[i] != deck[first]:
                input("No match. Press Enter to flip back.")
                revealed[i] = False
                revealed[first] = False
            first = None

    print(f"All matched in {moves} moves!")


def render_st(st):
    st.header("🧠 Memory (4×4)")

    if "mem_deck" not in st.session_state:
        st.session_state.mem_deck = _new_board()
        st.session_state.mem_revealed = [False] * 16
        st.session_state.mem_first = None
        st.session_state.mem_moves = 0
        st.session_state.mem_pending = None

    deck = st.session_state.mem_deck
    rev = st.session_state.mem_revealed

    if st.session_state.mem_pending is not None:
        a, b = st.session_state.mem_pending
        if deck[a] != deck[b]:
            rev[a] = False
            rev[b] = False
        st.session_state.mem_pending = None

    col_reset, col_moves = st.columns([1, 1])

    with col_reset:
        if st.button("Reset"):
            for key in list(st.session_state.keys()):
                if key.startswith("mem_"):
                    del st.session_state[key]
            st.rerun()

    with col_moves:
        st.metric("Moves", st.session_state.mem_moves)

    rows = [st.columns(4) for _ in range(4)]
    for r in range(4):
        for c in range(4):
            i = r * 4 + c
            label = deck[i] if rev[i] else HIDDEN
            disabled = rev[i] or _all_matched(rev) or (st.session_state.mem_pending is not None)

            if rows[r][c].button(label, key=f"mem_{i}", disabled=disabled):
                if st.session_state.mem_first is None:
                    st.session_state.mem_first = i
                    rev[i] = True
                else:
                    j = st.session_state.mem_first
                    if i != j:
                        rev[i] = True
                        st.session_state.mem_moves += 1
                        if deck[i] == deck[j]:
                            st.session_state.mem_first = None
                        else:
                            st.session_state.mem_pending = (i, j)
                            st.session_state.mem_first = None
                st.rerun()

    if _all_matched(rev):
        st.success(f"All matched! Moves: {st.session_state.mem_moves}")
