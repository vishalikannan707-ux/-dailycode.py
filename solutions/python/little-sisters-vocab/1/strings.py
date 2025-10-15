# 1. Add the prefix "un"
def add_prefix_un(word):
    return "un" + word


# 2. Make word groups with prefixes
def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    return " :: ".join([prefix] + [prefix + word for word in vocab_words[1:]])


# 3. Remove the suffix "ness" and adjust spelling
def remove_suffix_ness(word):
    root = word[:-4]  # remove 'ness'
    if root.endswith('i'):
        root = root[:-1] + 'y'  # change 'i' to 'y'
    return root


# 4. Convert adjective to verb by adding "en"
def adjective_to_verb(sentence, index):
    words = sentence.split()
    word = words[index].strip(".")  # remove period if it's at the end
    return word + "en"
