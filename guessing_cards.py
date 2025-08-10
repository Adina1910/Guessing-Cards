import tkinter as tk
# Function to generate binary-based cards
def generate_cards(max_number):
    cards = []
    bit_position = 0
    while (1 << bit_position) <= max_number:
        card = [num for num in range(1, max_number + 1) if num & (1 << bit_position)]
        cards.append(card)
        bit_position += 1
    return cards
class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Magic Number Cards 🎩✨")
        self.root.geometry("500x500")
        self.max_number = 100
        self.cards = generate_cards(self.max_number)
        self.current_card = 0
        self.guessed_number = 0
        self.bg_start = "#C8A2C8"
        self.start_btn_color = "#6A0DAD"
        self.card_colors = [
            "#A45FB9", "#8A4A9E", "#77398A",
            "#6B307C", "#6A2180", "#5B1570", "#4C0F60"
        ]
        self.encouragements = [
            "Let's see if your number is here...",
            "Let's see what have you chose!",
            "I can feel we're narrowing it down!",
            "Could this be the one? 🤔",
            "Almost there, stay with me!",
            "Looks like we’re getting really close!",
            "Final sweep — is it this?"
        ]
        # Start screen
        self.start_frame = tk.Frame(root, bg=self.bg_start)
        self.start_frame.pack(fill="both", expand=True)
        tk.Label(self.start_frame, text="Magic Number Cards Game 🎯",
                 font=("Eras Bold ITC", 20, "bold"),
                 fg="white", bg=self.bg_start).pack(pady=50)
        tk.Label(self.start_frame,
                 text=f"Think of a number between 1 and {self.max_number}.\n"
                      "I will guess it in a few questions!",
                 font=("Eras Bold ITC", 14), fg="white", bg=self.bg_start).pack(pady=20)
        tk.Button(self.start_frame, text="Start Game", font=("Eras Bold ITC", 14, "bold"),
                  bg=self.start_btn_color, fg="white",
                  command=self.start_game).pack(pady=40)
        # Game frame
        self.game_frame = tk.Frame(root)
        # Frame for card numbers
        self.card_frame = tk.Frame(self.game_frame)
        self.card_frame.pack(pady=10, padx=10)
        # Button frame
        self.btn_frame = tk.Frame(self.game_frame)
        self.btn_frame.pack(pady=10)
        self.yes_button = tk.Button(self.btn_frame, text="YES ✅", font=("Eras Bold ITC", 14, "bold"),
                                    width=10, command=lambda: self.answer(True))
        self.yes_button.grid(row=0, column=0, padx=10)

        self.no_button = tk.Button(self.btn_frame, text="NO ❌", font=("Eras Bold ITC", 14, "bold"),
                                   width=10, command=lambda: self.answer(False))
        self.no_button.grid(row=0, column=1, padx=10)
        # Encouragement label
        self.encourage_label = tk.Label(self.game_frame, text="",
                                        font=("Eras Bold ITC", 14),
                                        fg="white", wraplength=440, justify="center")
        self.encourage_label.pack(pady=15)
    def start_game(self):
        self.start_frame.pack_forget()
        self.game_frame.pack(fill="both", expand=True)
        self.show_card()
    def show_card(self):
        for widget in self.card_frame.winfo_children():
            widget.destroy()
        if self.current_card < len(self.cards):
            card_numbers = self.cards[self.current_card]
            bg_color = self.card_colors[self.current_card % len(self.card_colors)]
            # Change backgrounds
            self.game_frame.config(bg=bg_color)
            self.card_frame.config(bg=bg_color)
            self.btn_frame.config(bg=bg_color)
            self.encourage_label.config(bg=bg_color,
                                        text=self.encouragements[self.current_card % len(self.encouragements)])
            # Show numbers
            cols = 8
            for idx, num in enumerate(card_numbers):
                tk.Label(self.card_frame, text=str(num), font=("Eras Bold ITC", 12, "bold"),
                         width=4, bg=bg_color, fg="white").grid(row=idx // cols, column=idx % cols, padx=5, pady=5)
            for btn in (self.yes_button, self.no_button):
                btn.config(bg="white", fg="black", activebackground="#ddd")
        else:
            self.show_result()
    def show_result(self):
        result_popup = tk.Toplevel(self.root)
        result_popup.title("Result 🎩")
        result_popup.geometry("300x150")
        result_popup.configure(bg="#C8A2C8")
        tk.Label(result_popup, text=f"Your number is: {self.guessed_number} 🎯",
                 font=("Eras Bold ITC", 14, "bold"), bg="#C8A2C8", fg="black").pack(pady=20)
        def close_game(event=None):
            result_popup.destroy()
            self.root.destroy()
        tk.Button(result_popup, text="Yup!!", font=("Eras Bold ITC", 12, "bold"),
                  bg=self.start_btn_color, fg="white",
                  command=close_game).pack(pady=10)
        result_popup.bind("<Return>", close_game)
    def answer(self, is_yes):
        if is_yes:
            self.guessed_number += 1 << self.current_card
        self.current_card += 1
        self.show_card()
# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
