def is_isogram(word):
    # Step 1: Normalize the input to lowercase
    word = word.lower()

    # Step 2: Create a set to keep track of seen letters
    seen_letters = set()

    # Step 3: Loop through each character
    for char in word:
        # Step 4: Ignore spaces and hyphens
        if char == ' ' or char == '-':
            continue
        
        # Step 5: Check for duplicate letters
        if char in seen_letters:
            return False  # Duplicate found, not an isogram
        else:
            seen_letters.add(char)

    # Step 6: If no duplicates found, it's an isogram
    return True
