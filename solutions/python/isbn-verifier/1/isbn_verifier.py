def is_valid(isbn):
    # Remove dashes from the ISBN
    isbn = isbn.replace('-', '')
    
    # ISBN-10 must be exactly 10 characters
    if len(isbn) != 10:
        return False

    total = 0

    for i in range(10):
        char = isbn[i]

        if i == 9 and char == 'X':
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            return False  # Invalid character
        
        weight = 10 - i
        total += value * weight

    return total % 11 == 0
