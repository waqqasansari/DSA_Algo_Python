def findsubstring(s, words):
    if not s or not words:
        return []
    
    word_len = len(words[0])
    num_words = len(words)
    total_len = word_len * num_words

    if len(s) < total_len:
        return []
    
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1

        else:
            word_count[word] = 1

    result = []

    # Check every possible starting position
    for i in range(word_len):
        left = i
        right = i
        current_count = {}
        while right + word_len <= len(s):
            word = s[right:right + word_len]
            print(word)

    pass

st = "barfoothefoobarman"
w = ["foo","bar"]
findsubstring(st, w)