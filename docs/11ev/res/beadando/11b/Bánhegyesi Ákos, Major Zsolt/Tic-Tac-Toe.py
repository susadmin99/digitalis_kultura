import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.root.resizable(width=False, height=False)
        self.root.configure(bg='white')

        self.buttons = [[tk.Button() for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(
                    width=10, height=4, font=("Arial", 24),bg = 'white',
                    command=lambda row=i, col=j: self.play(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j,padx=5,pady=5)

        self.player = "X"
        self.score_X = 0
        self.score_O = 0
        self.message = tk.Label(text='',bg = 'white',font=("Arial", 36))
        self.message.grid(row=3, column=0, columnspan=3,padx=5,pady=5)
        self.create_replay_button()
        self.turn_label = tk.Label(text=f"Player {self.player}'s turn",bg = 'white',font=("Arial", 36))
        self.turn_label.grid(row=4, column=0, columnspan=3,padx=5,pady=5)
        self.score_label = tk.Label(text=f"X: {self.score_X} - O: {self.score_O}",bg = 'white',font=("Arial", 48))
        self.score_label.grid(row=5, column=0, columnspan=3,padx=5,pady=5)

    def play(self, row, col):
        if self.buttons[row][col]["text"] != "":
            return
        self.buttons[row][col].config(text=self.player)
        if self.player == "X":
            self.buttons[row][col].config(fg = 'red')
        else:
            self.buttons[row][col].config(fg = 'blue')
        self.check_win(self.player)
        self.turn_label.config(text=f"Player {self.player}'s turn")
        self.player = "O" if self.player == "X" else "X"

    def check_win(self, player):
        for i in range(3):
            if self.buttons[i][0]["text"] == player and self.buttons[i][1]["text"] == player and self.buttons[i][2]["text"] == player:
                self.end_game(player)
                return
            if self.buttons[0][i]["text"] == player and self.buttons[1][i]["text"] == player and self.buttons[2][i]["text"] == player:
                self.end_game(player)
                return
        if self.buttons[0][0]["text"] == player and self.buttons[1][1]["text"] == player and self.buttons[2][2]["text"] == player:
            self.end_game(player)
            return
        if self.buttons[0][2]["text"] == player and self.buttons[1][1]["text"] == player and self.buttons[2][0]["text"] == player:
            self.end_game(player)
            return
        full = True
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]["text"] == "":
                    full = False
                    break
            if not full:
                break
        if full:
            self.end_game("Tie")

    def end_game(self, winner):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state="disable")
        if winner == "Tie":
            self.message.config(text="It's a Tie!")
        else:
            self.message.config(text=f"Player {winner} wins!")
            if winner == "X":
                self.score_X += 1
            else:
                self.score_O += 1
            self.score_label.config(text=f"X: {self.score_X} - O: {self.score_O}")
        self.replay_button.config(state="normal")

    def create_replay_button(self):
        self.replay_button = tk.Button(text="Replay", command=self.replay, state="disable")
        self.replay_button.grid(row=6, column=0, columnspan=3,padx=5,pady=5)

    def replay(self):
        self.player = "X"
        self.turn_label.config(text=f"Player {self.player}'s turn")
        self.message.config(text='')
        self.replay_button.config(state="disable")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state="normal")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()