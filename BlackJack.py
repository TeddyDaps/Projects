import tkinter as tk
from tkinter import messagebox
import random

class BlackjackGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack Game")

        # Initialize game state variables
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []
        self.current_user = None

        # Create GUI elements
        self.frame = tk.Frame(root)
        self.frame.pack()

        # Player's hand label
        self.player_hand_label = tk.Label(self.frame, text="Player Hand:", font=("Arial", 12))
        self.player_hand_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Player's cards label
        self.player_cards_label = tk.Label(self.frame, text="", font=("Arial", 12))
        self.player_cards_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Dealer's hand label
        self.dealer_hand_label = tk.Label(self.frame, text="Dealer Hand:", font=("Arial", 12))
        self.dealer_hand_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        # Dealer's cards label
        self.dealer_cards_label = tk.Label(self.frame, text="", font=("Arial", 12))
        self.dealer_cards_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        # Buttons frame
        self.buttons_frame = tk.Frame(self.frame)
        self.buttons_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        # Deal button
        self.deal_button = tk.Button(self.buttons_frame, text="Deal", font=("Arial", 12), command=self.deal)
        self.deal_button.grid(row=0, column=0, padx=5)

        # Hit button
        self.hit_button = tk.Button(self.buttons_frame, text="Hit", font=("Arial", 12), command=self.hit)
        self.hit_button.grid(row=0, column=1, padx=5)

        # Stand button
        self.stand_button = tk.Button(self.buttons_frame, text="Stand", font=("Arial", 12), command=self.stand)
        self.stand_button.grid(row=0, column=2, padx=5)

        # Double Down button
        self.double_button = tk.Button(self.buttons_frame, text="Double Down", font=("Arial", 12), command=self.double_down)
        self.double_button.grid(row=0, column=3, padx=5)

        # Initialize the game
        self.initialize_game()

    def initialize_game(self):
        self.deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
        random.shuffle(self.deck)
        self.player_hand = []
        self.dealer_hand = []
        self.update_gui()
        self.enable_buttons(["deal"])

    def deal(self):
        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]
        self.update_gui()

        player_score = self.calculate_score(self.player_hand)
        if player_score == 21:
            messagebox.showinfo("Blackjack", "Player has Blackjack!")
            self.stand()
        else:
            self.enable_buttons(["hit", "stand", "double"])

    def hit(self):
        self.player_hand.append(self.deck.pop())
        self.update_gui()

        player_score = self.calculate_score(self.player_hand)
        if player_score > 21:
            messagebox.showinfo("Bust", "Player busted!")
            self.stand()

    def stand(self):
        self.enable_buttons(["deal"])
        self.dealer_turn()

    def double_down(self):
        self.player_hand.append(self.deck.pop())
        self.update_gui()

        player_score = self.calculate_score(self.player_hand)
        if player_score > 21:
            messagebox.showinfo("Bust", "Player busted!")
            self.stand()
        else:
            self.stand()

    def dealer_turn(self):
        while self.calculate_score(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.pop())
        self.update_gui()
        self.determine_winner()

    def determine_winner(self):
        player_score = self.calculate_score(self.player_hand)
        dealer_score = self.calculate_score(self.dealer_hand)

        if player_score > 21:
            messagebox.showinfo("Result", "Player busts. Dealer wins.")
        elif dealer_score > 21:
            messagebox.showinfo("Result", "Dealer busts. Player wins.")
        elif player_score > dealer_score:
            messagebox.showinfo("Result", "Player wins.")
        elif dealer_score > player_score:
            messagebox.showinfo("Result", "Dealer wins.")
        else:
            messagebox.showinfo("Result", "It's a tie.")

    def calculate_score(self, hand):
        score = 0
        num_aces = 0
        for card in hand:
            if card in ['J', 'Q', 'K']:
                score += 10
            elif card == 'A':
                num_aces += 1
            else:
                score += int(card)
        for _ in range(num_aces):
            if score + 11 <= 21:
                score += 11
            else:
                score += 1
        return score

    def update_gui(self):
        self.player_cards_label.config(text=", ".join(self.player_hand) + " (Score: " + str(self.calculate_score(self.player_hand)) + ")")
        if len(self.dealer_hand) > 1:
            dealer_display = ", ".join(self.dealer_hand[:-1]) + ", [Hidden Card]"
            if self.calculate_score(self.player_hand) > 21:
                dealer_display = ", ".join(self.dealer_hand)
            self.dealer_cards_label.config(text=dealer_display + " (Score: ?)")
        if self.calculate_score(self.player_hand) > 21:
            self.dealer_cards_label.config(text=", ".join(self.dealer_hand) + " (Score: " + str(self.calculate_score(self.dealer_hand)) + ")")

    def enable_buttons(self, buttons):
        self.deal_button.config(state="normal" if "deal" in buttons else "disabled")
        self.hit_button.config(state="normal" if "hit" in buttons else "disabled")
        self.stand_button.config(state="normal" if "stand" in buttons else "disabled")
        self.double_button.config(state="normal" if "double" in buttons else "disabled")

if __name__ == "__main__":
    root = tk.Tk()
    game = BlackjackGame(root)
    root.mainloop()
