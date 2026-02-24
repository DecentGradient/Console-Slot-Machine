from slot_machine_logic import SlotMachine, NUM_REELS, REEL_HEIGHT, SYMBOLS, STARTING_CREDITS, MIN_BET, MAX_BET, PAYOUT_TABLE

def print_slot_machine(reels):
    # Transpose reels for printing row by row
    display_rows = []
    for i in range(REEL_HEIGHT):
        row = [reel[i] for reel in reels]
        display_rows.append(row)

    print("\n--- SLOT MACHINE ---")
    for row in display_rows:
        print(" | ".join(row))
    print("--------------------\n")

def get_bet(current_credits, min_bet, max_bet):
    while True:
        try:
            bet = int(input(f"Enter your bet ({min_bet}-{max_bet}): "))
            if not (min_bet <= bet <= max_bet):
                print("Bet must be within the specified range.")
            elif bet > current_credits:
                print("You don't have enough credits for that bet.")
            else:
                return bet
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    slot_machine = SlotMachine()
    print(f"Welcome to the Console Slot Machine! You start with {STARTING_CREDITS} credits.")

    while True:
        current_credits = slot_machine.get_credits()
        print(f"Current credits: {current_credits}")

        if current_credits < MIN_BET:
            print("You don't have enough credits to place the minimum bet. Game over!")
            break

        bet = get_bet(current_credits, MIN_BET, MAX_BET)

        if not slot_machine.deduct_bet(bet):
            # This case should ideally not be reached due to get_bet validation, but good for robustness
            print("An error occurred while deducting your bet. Please try again.")
            continue

        print(f"Bet placed: {bet}. Remaining credits: {slot_machine.get_credits()}")

        reels = slot_machine.spin()
        print_slot_machine(reels)

        winnings = slot_machine.check_win(bet)

        if winnings > 0:
            print(f"You won {winnings} credits!")
        else:
            print("No win this round.")

        print(f"Total credits after round: {slot_machine.get_credits()}")

        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Final credits:", slot_machine.get_credits())
            break

if __name__ == "__main__":
    main()
