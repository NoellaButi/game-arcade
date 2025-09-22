# slot_machine.py
import random

SYMS = ["🍒", "🍉", "🍋", "🔔", "⭐"]
PAYOUTS = {"🍒": 3, "🍉": 4, "🍋": 5, "🔔": 10, "⭐": 20}


def _spin():
    return [random.choice(SYMS) for _ in range(3)]


def play_cli():
    balance = 100
    print("Slot Machine — start with $100")
    while balance > 0:
        try:
            bet = int(input(f"Bet (1..{balance}): ").strip())
        except ValueError:
            print("Enter a number.")
            continue

        if not (1 <= bet <= balance):
            print("Invalid bet.")
            continue

        balance -= bet
        row = _spin()
        print(" | ".join(row))
        if len(set(row)) == 1:
            win = bet * PAYOUTS[row[0]]
            print(f"You won ${win}!")
            balance += win
        else:
            print("No win.")

        if input("Again? (y/n): ").lower() != "y":
            break

    print("Final balance:", balance)


def render_st(st):
    st.header("🎰 Slot Machine")

    if "sm_bal" not in st.session_state:
        st.session_state.sm_bal = 100

    bal = st.session_state.sm_bal
    st.metric("Balance", f"${bal}")

    if bal <= 0:
        st.warning("You're out of funds. Reset to keep playing.")
        st.number_input(
            "Bet",
            min_value=0,
            max_value=0,
            value=0,
            step=1,
            disabled=True,
            key="sm_bet",
        )
        spin_disabled = True
    else:
        default_bet = min(10, bal)
        st.number_input(
            "Bet",
            min_value=1,
            max_value=bal,
            value=default_bet,
            step=1,
            key="sm_bet",
        )
        spin_disabled = False

    col_spin, col_reset = st.columns(2)
    if col_spin.button("Spin", disabled=spin_disabled):
        bet = int(st.session_state.sm_bet)
        if 1 <= bet <= st.session_state.sm_bal:
            st.session_state.sm_bal -= bet
            row = _spin()
            st.markdown(f"# {' | '.join(row)}")
            if len(set(row)) == 1:
                win_amt = bet * PAYOUTS[row[0]]
                st.success(f"You won ${win_amt}!")
                st.session_state.sm_bal += win_amt
            else:
                st.info("No win.")
        else:
            st.error("Invalid bet for current balance.")

    if col_reset.button("Reset Balance"):
        st.session_state.sm_bal = 100
        st.rerun()
