##Answering the question: How do I judge a single card?

def get_card_points(user_input, card):
    
    total = 0

    for category in user_input:
        amount = user_input[category]
        multiplier = card.get(category,1)
        points = amount * multiplier
        total += points

    return total