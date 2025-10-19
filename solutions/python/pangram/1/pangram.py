def is_pangram(sentence):
    # Step 1: Convert the sentence to lowercase
    sentence = sentence.lower()
    
    # Step 2: Create an empty set to store unique letters
    letters = set()
    
    # Step 3: Loop through each character in the sentence
    for char in sentence:
        if char.isalpha():  # Check if the character is a letter
            letters.add(char)
    
    # Step 4: Check if the set has 26 letters
    return len(letters) == 26
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
print(is_pangram("Hello, world!"))                                # False
print(is_pangram("Pack my box with five dozen liquor jugs"))      # True
