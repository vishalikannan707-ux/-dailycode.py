def rotate(text, key):
    result = []

    for char in text:
        if char.isupper():
            # Shift uppercase letters
            rotated = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            result.append(rotated)
        elif char.islower():
            # Shift lowercase letters
            rotated = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            result.append(rotated)
        else:
            # Leave non-alphabetic characters unchanged
            result.append(char)

    return ''.join(result)
from rotational_cipher import rotate

print(rotate('omg', 5))  # Output: trl
print(rotate('c', 0))    # Output: c
print(rotate('Cool', 26)) # Output: Cool
print(rotate('The quick brown fox jumps over the lazy dog.', 13))
# Output: Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
