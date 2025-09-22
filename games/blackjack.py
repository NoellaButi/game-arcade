# blackjack.py
import random
import streamlit as st

# ---------------- CLI MODE ---------------- #
def _make_deck():
    return [r + s for r in "A23456789TJQK" for s in "♠♥♦♣"]


def play_cli():
    deck = _make_deck()
    random.shuffle(deck)
    bank = 100
    print("Blackjack — start with $100")
    while True:
        bet = input(f"Bet (1..{bank}): ")
        if not bet.isdigit():
            print("Enter number.")
            continue
        bet = int(bet)
        if bet <= 0 or bet > bank:
            print("Invalid bet.")
            continue
        bank -= bet
        player = [deck.pop(), deck.pop()]
        dealer = [deck.pop(), deck.pop()]
        pv = _value(player)
        dv = _value(dealer)
        print("You:", player, pv)
        print("Dealer:", dealer[0], "?")
        if pv > dv:
            print("You win!")
            bank += bet * 2
        elif pv == dv:
            print("Push.")
            bank += bet
        else:
            print("Dealer wins.")
        if len(deck) < 15:
            deck = _make_deck()
            random.shuffle(deck)
        if input("Play again? (y/n): ").lower() != "y":
            break


def _value(hand):
    # Simplified blackjack values
    return sum("23456789TJQK".index(c[0]) % 10 + 1 for c in hand)


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

    def draw(n):
        d = st.session_state.bj_deck
        if len(d) < n:
            st.session_state.bj_deck = _make_deck()
            random.shuffle(st.session_state.bj_deck)
            d = st.session_state.bj_deck
        return [d.pop() for _ in range(n)]

    bank = st.session_state.bj_bank
    colB, colBet, colReset = st.columns([1, 1, 1])
    with colB:
        st.metric("Bank", f"${bank}")
    with colBet:
        st.session_state.bj_bet = st.number_input(
            "Bet", min_value=1, max_value=max(1, bank), value=st.session_state.bj_bet
        )
    with colReset:
        if st.button("Reset Game"):
            for k in list(st.session_state.keys()):
                if k.startswith("bj_"):
                    del st.session_state[k]
            st.experimental_rerun()

    if st.button("Deal"):
        st.session_state.bj_player = draw(2)
        st.session_state.bj_dealer = draw(2)
        st.session_state.bj_bank -= st.session_state.bj_bet

    if st.session_state.bj_player:
        st.write("Player:", st.session_state.bj_player)
        st.write("Dealer:", st.session_state.bj_dealer[0], "?")
