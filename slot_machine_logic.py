import random

NUM_REELS = 3
REEL_HEIGHT = 3
SYMBOLS = ["🍒", "🍋", "🔔", "⭐", "7"]
STARTING_CREDITS = 1000
MIN_BET = 10
MAX_BET = 100
PAYOUT_TABLE = {3: 10, 2: 2}

class SlotMachine:
    def __init__(self, initial_credits=STARTING_CREDITS):
        self.credits = initial_credits
        self.symbols = SYMBOLS
        self.num_reels = NUM_REELS
        self.reel_height = REEL_HEIGHT
        self.payout_table = PAYOUT_TABLE
        self.current_reels = []

    def spin(self):
        self.current_reels = []
        for _ in range(self.num_reels):
            reel = [random.choice(self.symbols) for _ in range(self.reel_height)]
            self.current_reels.append(reel)
        return self.current_reels

    def check_win(self, bet):
        winnings = 0
        # Check central horizontal payline
        payline = [self.current_reels[reel_idx][self.reel_height // 2] for reel_idx in range(self.num_reels)]

        # Simplified win check: count matching symbols in the payline
        # If all symbols are the same:
        if len(set(payline)) == 1:
            matching_count = self.num_reels # All symbols match
            if matching_count in self.payout_table:
                winnings = bet * self.payout_table[matching_count]
        # If two symbols are the same (and not all three)
        elif len(set(payline)) == 2:
            # Check if any symbol appears twice
            for symbol in set(payline):
                if payline.count(symbol) == 2:
                    matching_count = 2
                    if matching_count in self.payout_table:
                        winnings = bet * self.payout_table[matching_count]
                    break # Only one pair can exist in 3 reels


        if winnings > 0:
            self.add_winnings(winnings)
        return winnings

    def get_credits(self):
        return self.credits

    def deduct_bet(self, amount):
        if amount > self.credits:
            return False
        self.credits -= amount
        return True

    def add_winnings(self, amount):
        self.credits += amount
