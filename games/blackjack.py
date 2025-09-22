# blackjack.py
import random

RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
SUITS = ["♠", "♥", "♦", "♣"]


def _make_deck():
    return [(r, s) for r in RANKS for s in SUITS]


def _value(hand):
    total = 0
    aces = 0
    for r, _ in hand:
        if r in {"J", "Q", "K", "10"}:
            total += 10
        elif r == "A":
            aces += 1
            total += 1
        else:
            total += int(r)
    while aces > 0 and total + 10 <= 21:
        total += 10
        aces -= 1
    return total


def _hand_str(hand):
    return " ".join(f"{r}{s}" for r, s in hand) if hand else "—"


# ---------------- CLI MODE ---------------- #
def play_cli():
    deck = _make_deck()
    random.shuffle(deck)
    bank = 100
    print("Blackjack — start with $100")
    while bank > 0:
        bet = input(f"Bet (1..{bank}): ")
        if not bet.isdigit():
            print("Enter number.")
            continue

        bet_int = int(bet)
        if bet_int <= 0 or bet_int > bank:
            print("Invalid bet.")
            continue
        bank -= bet_int

        player = [deck.pop(), deck.pop()]
        dealer = [deck.pop(), deck.pop()]
        print("Dealer:", dealer[0][0] + dealer[0][1], " ??")
        print("You   :", _hand_str(player), "=", _value(player))

        while _value(player) < 21:
            move = input("Hit or Stand? (h/s): ").lower().strip()
            if move == "h":
                player.append(deck.pop())
                print("You:", _hand_str(player), "=", _value(player))
            else:
                break

        pv = _value(player)
        if pv > 21:
            print("Bust! You lose.")
        else:
            print("Dealer shows:", _hand_str(dealer), "=", _value(dealer))
            while _value(dealer) < 17:
                dealer.append(deck.pop())
                print("Dealer:", _hand_str(dealer), "=", _value(dealer))
            dv = _value(dealer)
            if dv > 21 or pv > dv:
                print("You win!")
                bank += bet_int * 2
            elif pv == dv:
                print("Push.")
                bank += bet_int
            else:
                print("Dealer wins.")

        if len(deck) < 15:
            deck = _make_deck()
            random.shuffle(deck)

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break

    print("Bank:", bank)


# ---------------- STREAMLIT MODE ---------------- #
def render_st(st):
    st.header("🃏 Blackjack")

    if "bj_deck" not in st.session_state:
        st.session_state.bj_deck = _make_deck()
        random.shuffle(st.session_state.bj_deck)
        st.session_state.bj_player = []
        st.session_state.bj_dealer = []
        st.session_state.bj_bank = 100
        st.session_state.bj_bet = 10
        st.session_state.bj_phase = "bet"

    def draw(n=1):
        deck = st.session_state.bj_deck
        if len(deck) < n:
            st.session_state.bj_deck = _make_deck()
            random.shuffle(st.session_state.bj_deck)
            deck = st.session_state.bj_deck
        return [deck.pop() for _ in range(n)]

    bank = st.session_state.bj_bank
    col_bank, col_bet, col_reset = st.columns([1, 1, 1])

    with col_bank:
        st.metric("Bank", f"${bank}")

    with col_bet:
        st.session_state.bj_bet = st.number_input(
            "Bet",
            min_value=1,
            max_value=max(1, bank),
            value=min(10, bank),
            step=1,
        )

    with col_reset:
        if st.button("Reset Game"):
            for key in list(st.session_state.keys()):
                if key.startswith("bj_"):
                    del st.session_state[key]
            st.rerun()

    phase = st.session_state.bj_phase
    player = st.session_state.bj_player
    dealer = st.session_state.bj_dealer

    def deal():
        bet_val = int(st.session_state.bj_bet)
        st.session_state.bj_bank -= bet_val
        st.session_state.bj_player = draw(2)
        st.session_state.bj_dealer = draw(2)
        st.session_state.bj_phase = "play"

    def hit():
        st.session_state.bj_player += draw(1)
        if _value(st.session_state.bj_player) >= 21:
            stand()

    def stand():
        while _value(st.session_state.bj_dealer) < 17:
            st.session_state.bj_dealer += draw(1)

        pv = _value(st.session_state.bj_player)
        dv = _value(st.session_state.bj_dealer)
        bet_val = int(st.session_state.bj_bet)

        if pv > 21:
            outcome = "bust"
        elif dv > 21 or pv > dv:
            outcome = "win"
            st.session_state.bj_bank += bet_val * 2
        elif pv == dv:
            outcome = "push"
            st.session_state.bj_bank += bet_val
        else:
            outcome = "lose"

        st.session_state.bj_outcome = outcome
        st.session_state.bj_phase = "showdown"

    st.write("---")
    if phase == "bet":
        st.write("Place your bet then press **Deal**.")
        if bank <= 0:
            st.error("Out of funds. Reset to start over.")
        if st.button("Deal", disabled=bank <= 0):
            deal()

    elif phase in {"play", "showdown"}:
        dv = _value(dealer) if phase == "showdown" else _value([dealer[0]])
        st.subheader(f"Dealer: {dv if phase == 'showdown' else '??'}")
        dealer_cards = dealer if phase == "showdown" else [dealer[0]]
        st.code(" ".join([f"{r}{s}" for r, s in dealer_cards]) or "—")

        st.subheader(f"You: {_value(player)}")
        st.code(" ".join(f"{r}{s}" for r, s in player) or "—")

        if phase == "play":
            col1, col2 = st.columns(2)
            with col1:
                st.button("Hit", on_click=hit)
            with col2:
                st.button("Stand", on_click=stand)
        else:
            outcome = st.session_state.get("bj_outcome")
            if outcome == "win":
                st.success("You win! 🎉")
            elif outcome == "push":
                st.info("Push.")
            elif outcome == "bust":
                st.error("Bust — you lose.")
            else:
                st.error("Dealer wins.")
            if st.button("Next Hand"):
                st.session_state.bj_player = []
                st.session_state.bj_dealer = []
                st.session_state.bj_phase = "bet"
