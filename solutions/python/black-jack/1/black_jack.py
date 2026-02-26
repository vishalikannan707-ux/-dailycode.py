def value_of_card(card):
    """Return the Blackjack value of a single card."""
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1  # Fixed value for ace in this function
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Return the card with the higher value. If equal, return both as a tuple."""
    val_one = value_of_card(card_one)
    val_two = value_of_card(card_two)

    if val_one > val_two:
        return card_one
    elif val_two > val_one:
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one, card_two):
    """Decide the value of an upcoming ace based on the other two cards in hand."""
    total = value_of_card(card_one) + value_of_card(card_two)

    if card_one == 'A' or card_two == 'A':
        return 1
    elif total + 11 <= 21:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    """Check if the two cards make a 'blackjack' hand (Ace + 10-point card)."""
    ten_cards = ['10', 'J', 'Q', 'K']
    return (card_one == 'A' and card_two in ten_cards) or \
           (card_two == 'A' and card_one in ten_cards)


def can_split_pairs(card_one, card_two):
    """Check if the hand can be split into two separate hands."""
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Check if the player can double down (hand totals 9, 10, or 11)."""
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in [9, 10, 11]


# -----------------------
# Example usage (optional)
# -----------------------
if __name__ == "__main__":
    print("value_of_card('K') =", value_of_card('K'))         # 10
    print("value_of_card('4') =", value_of_card('4'))         # 4
    print("value_of_card('A') =", value_of_card('A'))         # 1

    print("higher_card('K', '10') =", higher_card('K', '10')) # ('K', '10')
    print("higher_card('4', '6') =", higher_card('4', '6'))   # '6'
    print("higher_card('K', 'A') =", higher_card('K', 'A'))   # 'K'

    print("value_of_ace('6', 'K') =", value_of_ace('6', 'K')) # 1
    print("value_of_ace('7', '3') =", value_of_ace('7', '3')) # 11

    print("is_blackjack('A', 'K') =", is_blackjack('A', 'K')) # True
    print("is_blackjack('10', '9') =", is_blackjack('10', '9')) # False

    print("can_split_pairs('Q', 'K') =", can_split_pairs('Q', 'K')) # True
    print("can_split_pairs('10', 'A') =", can_split_pairs('10', 'A')) # False

    print("can_double_down('A', '9') =", can_double_down('A', '9')) # True
    print("can_double_down('10', '2') =", can_double_down('10', '2')) # False

 


