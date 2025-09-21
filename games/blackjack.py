# blackjack.py
import random

RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
SUITS = ["♠","♥","♦","♣"]

def _make_deck():
    return [(r,s) for r in RANKS for s in SUITS]

def _value(hand):
    total, aces = 0, 0
    for r,_ in hand:
        if r in ("J","Q","K","10"):
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
    return " ".join(f"{r}{s}" for r,s in hand) if hand else "—"

# ---------------- CLI MODE ---------------- #
def play_cli():
    deck = _make_deck(); random.shuffle(deck)
    bank = 100
    print("Blackjack — start with $100")
    while bank > 0:
        bet = input(f"Bet (1..{bank}): ")
        if not bet.isdigit():
            print("Enter number."); continue
        bet = int(bet)
        if bet <= 0 or bet > bank:
            print("Invalid bet."); continue
        bank -= bet

        # deal
        player = [deck.pop(), deck.pop()]
        dealer = [deck.pop(), deck.pop()]
        print("Dealer:", dealer[0][0]+dealer[0][1], " ??")
        print("You   :", _hand_str(player), "=", _value(player))

        # player turn
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
            # dealer plays
            print("Dealer shows:", _hand_str(dealer), "=", _value(dealer))
            while _value(dealer) < 17:
                dealer.append(deck.pop())
                print("Dealer:", _hand_str(dealer), "=", _value(dealer))
            dv = _value(dealer)
            if dv > 21 or pv > dv:
                print("You win!"); bank += bet*2
            elif pv == dv:
                print("Push."); bank += bet
            else:
                print("Dealer wins.")

        if len(deck) < 15:
            deck = _make_deck(); random.shuffle(deck)
        if input("Play again? (y/n): ").lower() != "y":
            break
    print("Bank:", bank)

# ---------------- STREAMLIT MODE ---------------- #
def render_st(st):
    st.header("🃏 Blackjack")
    if "bj_deck" not in st.session_state:
        st.session_state.bj_deck = _make_deck(); random.shuffle(st.session_state.bj_deck)
        st.session_state.bj_player = []
        st.session_state.bj_dealer = []
        st.session_state.bj_bank = 100
        st.session_state.bj_bet = 10
        st.session_state.bj_phase = "bet"

    def draw(n=1):
        d = st.session_state.bj_deck
        if len(d) < n:
            st.session_state.bj_deck = _make_deck(); random.shuffle(st.session_state.bj_deck); d = st.session_state.bj_deck
        return [d.pop() for _ in range(n)]

    bank = st.session_state.bj_bank

    colB, colBet, colReset = st.columns([1,1,1])
    with colB: st.metric("Bank", f"${bank}")
    with colBet:
        st.session_state.bj_bet = st.number_input("Bet", min_value=1, max_value=max(1, bank),
                                                 value=min(10, bank), step=1)
    with colReset:
        if st.button("Reset Game"):
            for k in list(st.session_state.keys()):
                if k.startswith("bj_"): del st.session_state[k]
            st.experimental_rerun()

    phase = st.session_state.bj_phase
    p, d = st.session_state.bj_player, st.session_state.bj_dealer

    def deal():
        bet = int(st.session_state.bj_bet)
        st.session_state.bj_bank -= bet
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
        pv, dv = _value(st.session_state.bj_player), _value(st.session_state.bj_dealer)
        bet = int(st.session_state.bj_bet)
        if pv > 21:
            outcome = "bust"
        elif dv > 21 or pv > dv:
            outcome = "win"; st.session_state.bj_bank += bet*2
        elif pv == dv:
            outcome = "push"; st.session_state.bj_bank += bet
        else:
            outcome = "lose"
        st.session_state.bj_outcome = outcome
        st.session_state.bj_phase = "showdown"

    st.write("---")
    if phase == "bet":
        st.write("Place your bet then press **Deal**.")
        if bank <= 0:
            st.error("Out of funds. Reset to start over.")
        if st.button("Deal", disabled=bank<=0):
            deal()

    elif phase in ("play", "showdown"):
        dv = _value(d) if phase == "showdown" else _value([d[0]])  # hide one card
        st.subheader(f"Dealer: {dv if phase=='showdown' else '??'}")
        st.code(" ".join([f"{r}{s}" for r,s in (d if phase=='showdown' else [d[0]])]) or "—")

        st.subheader(f"You: {_value(p)}")
        st.code(" ".join(f"{r}{s}" for r,s in p) or "—")

        if phase == "play":
            col1, col2 = st.columns(2)
            with col1: st.button("Hit", on_click=hit)
            with col2: st.button("Stand", on_click=stand)
        else:
            outcome = st.session_state.get("bj_outcome")
            if outcome == "win": st.success("You win! 🎉")
            elif outcome == "push": st.info("Push.")
            elif outcome == "bust": st.error("Bust — you lose.")
            else: st.error("Dealer wins.")
            if st.button("Next Hand"):
                st.session_state.bj_player, st.session_state.bj_dealer = [], []
                st.session_state.bj_phase = "bet"