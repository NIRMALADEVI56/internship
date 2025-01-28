import tkinter as tk
import random
def play(user_choice):
    global player_score, computer_score
    user_choice = user_choice.strip().capitalize()
    choices = ["Rock","Paper","Scissors"]
    com_choice=random.choice(choices)
    if user_choice == com_choice:
        result = "It is a tie!"
    elif user_choice == "Rock" and com_choice == "Scissors":
        result = "You Win!"
        player_score += 1
    elif user_choice == "Paper" and com_choice == "Rock":
        result = "You Win!"
        player_score += 1
    elif user_choice == "Scissors" and com_choice == "Paper":
        result = "You Win!"
        player_score += 1
    else:
        result = "You Lose!"
        computer_score += 1
        user_choice_label.config(text=f"Your Choice:{user_choice}")
        com_choice_label.config(text=f"Computer Choice:{com_choice}")
        result_label.config(text=f"Result:{result}")
        player_score_label.config(text=f"Your Score:{player_score}")
        computer_score_label.config(text=f"Computer Score:{computer_score}")
def reset_game():
    global player_score,computer_score
    computer_score=0
    user_choice_label.config(text=f"Your Choice:None")
    com_choice_label.config(text="Result:None")
    player_score_label.config(text=f"Your Score:{player_score}")
    computer_score_label.config(text=f"Computer Score:{computer_score}")
window=tk.Tk()
window.title("Rock-Paper-Scissors Game")
player_score=0
computer_score=0
player_score_label=tk.Label(window,text=f"You Score:{player_score}",font=("Arial",12))
player_score_label.pack(pady=5)
computer_score_label=tk.Label(window,text=f"Computer Score:{computer_score}",font=("Arial",12))
computer_score_label.pack(pady=5)
result_label=tk.Label(window,text="Result: None",font=("Arial",12))
result_label.pack(pady=20)
rock_button=tk.Button(window,text="ROCK",font=("Helvetica",14),command=lambda:play("Rock")).pack(side="left",padx=10)
paper_button=tk.Button(window,text="PAPER",font=("Helvetiica",14),command=lambda:play("Paper")).pack(side="left",padx=10)
scissors_button=tk.Button(window,text="SCISSORS",font=("Helvetica",14),command=lambda:play("Scissors")).pack(side="left",padx=10)
reset_button=tk.Button(window,text="RESET GAME",font=("Helvetica",14),command=reset_game)
reset_button.pack(pady=20)
user_choice_label=tk.Label(window,text="YOUR CHOICE:NONE",font=("Arial",12))
user_choice_label.pack(pady=5)
com_choice_label=tk.Label(window,text="COMPUTER CHOICE:NONE",font=("Arial",12))
com_choice_label.pack(pady=5)
window.mainloop()
