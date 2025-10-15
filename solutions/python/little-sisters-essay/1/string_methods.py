# 1. Function to capitalize the title of the paper
def capitalize_title(title):
    """
    Takes a title string as input and returns it in title case,
    where the first letter of each word is capitalized.
    
    >>> capitalize_title("my hobbies")
    'My Hobbies'
    """
    return title.title()

# 2. Function to check if a sentence ends with a period
def check_sentence_ending(sentence):
    """
    Takes a sentence string as input and returns True if it ends with a period,
    otherwise returns False.
    
    >>> check_sentence_ending("I like to hike, bake, and read.")
    True
    >>> check_sentence_ending("I like to hike")
    False
    """
    # Check if the string is not empty and the last character is a period
    if sentence and sentence[-1] == '.':
        return True
    return False

# 3. Function to clean up spacing in a sentence
def clean_up_spacing(sentence):
    """
    Takes a sentence string as input and removes extra whitespace
    from the beginning and the end, returning the updated string.
    
    >>> clean_up_spacing(" I like to go on hikes with my dog.  ")
    'I like to go on hikes with my dog.'
    """
    return sentence.strip()

# 4. Function to replace words with a synonym
def replace_word_choice(sentence, old_word, new_word):
    """
    Takes a sentence string, an old_word, and a new_word as inputs.
    Replaces all instances of old_word with new_word and returns the updated string.
    
    >>> replace_word_choice("I bake good cakes.", "good", "amazing")
    'I bake amazing cakes.'
    """
    return sentence.replace(old_word, new_word)
