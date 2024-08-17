def group_anagrams(strs):
    anagram_map = {}

    for word in strs:
        sorted_word = ''.join(sorted(word))

        if sorted_word not in anagram_map:
            anagram_map[sorted_word] = []
        anagram_map[sorted_word].append(word)

    return list(anagram_map.values())


# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(f"Grouped anagrams: {group_anagrams(strs)}")