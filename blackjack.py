import random

# Create deck
def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♥', '♦', '♣', '♠']
    deck = [rank + suit for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

# Calculate hand value (handles Aces as 1 or 11)
def hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        rank = card[:-1]
        if rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            aces += 1
            value += 11
        else:
            value += int(rank)
    # Adjust for aces
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

# Display hand
def display_hand(hand, player_name):
    print(f"{player_name}'s hand: {' | '.join(hand)}  (Value: {hand_value(hand)})")

# Dealer plays (hits on 16 or less)
def dealer_play(deck, dealer_hand):
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

# Main game
def play_blackjack():
    print("🃏 WELCOME TO BLACKJACK 🃏\n")
    
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Player turn
    while hand_value(player_hand) < 21:
        display_hand(player_hand, "Your")
        display_hand([dealer_hand[0], '??'], "Dealer's")
        
        choice = input("\nHit or Stand? (h/s): ").lower()
        if choice == 'h':
            player_hand.append(deck.pop())
        elif choice == 's':
            break
        else:
            print("Type 'h' or 's'!")

    player_score = hand_value(player_hand)

    # Dealer turn
    if player_score <= 21:
        dealer_play(deck, dealer_hand)
    
    dealer_score = hand_value(dealer_hand)

    # Show final hands
    print("\n" + "="*40)
    display_hand(player_hand, "Your final")
    display_hand(dealer_hand, "Dealer's final")
    print("="*40)

    # Determine winner
    if player_score > 21:
        print("You BUSTED! Dealer wins 💀")
    elif dealer_score > 21:
        print("Dealer BUSTED! You win the bag 💰")
    elif player_score > dealer_score:
        print("You win the bag 💰")
    elif player_score < dealer_score:
        print("Dealer wins 💀")
    else:
        print("Push — tie game 🤝")

    # Play again
    again = input("\nPlay again? (y/n): ").lower()
    if again == 'y':
        play_blackjack()

# Start the game
if __name__ == "__main__":
    play_blackjack()