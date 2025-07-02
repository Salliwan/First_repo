from random import sample


def get_numbers_ticket(min, max, quantity):

    if not (1 <= min <= max <= 1000) or not (quantity <= max - min + 1):
        return []
    else:
        return sorted(sample(range(min, max+1), quantity))
