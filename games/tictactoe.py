# tictactoe.py
import random

def check_winner(board):
    lines=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in lines:
        if board[a]==board[b]==board[c]!=" ": return board[a]
    return None

def minimax(board,player):
    opp="O" if player=="X" else "X"
    winner=check_winner(board)
    if winner=="X": return 1,None
    if winner=="O": return -1,None
    if " " not in board: return 0,None
    best=( -2,None ) if player=="X" else (2,None)
    for i in range(9):
        if board[i]==" ":
            board[i]=player
            score,_=minimax(board,opp)
            board[i]=" "
            if player=="X" and score>best[0]: best=(score,i)
            if player=="O" and score<best[0]: best=(score,i)
    return best

def play_cli():
    board=[" "]*9
    while True:
        print("\n".join(["|".join(board[i:i+3]) for i in (0,3,6)]))
        if check_winner(board) or " " not in board: break
        move=int(input("Move 1-9: "))-1
        if board[move]!=" ": continue
        board[move]="O"
        if check_winner(board) or " " not in board: break
        _,comp=minimax(board,"X")
        board[comp]="X"
    w=check_winner(board)
    print("Winner:",w if w else "Draw")

def render_st(st):
    st.header("⭕❌ Tic-Tac-Toe")
    if "ttt_board" not in st.session_state: st.session_state.ttt_board=[" "]*9
    b=st.session_state.ttt_board
    cols=[st.columns(3) for _ in range(3)]
    for r in range(3):
        for c in range(3):
            i=r*3+c
            if cols[r][c].button(b[i] if b[i]!=" " else "-",key=f"ttt_{i}"):
                if b[i]==" ":
                    b[i]="O"
                    if not check_winner(b) and " " in b:
                        _,comp=minimax(b,"X"); b[comp]="X"
    st.write(" | ".join(b[0:3])); st.write(" | ".join(b[3:6])); st.write(" | ".join(b[6:9]))
    w=check_winner(b)
    if w: st.success(f"Winner: {w}")
    elif " " not in b: st.info("Draw")
    if st.button("Reset"): st.session_state.ttt_board=[" "]*9