def longest_unique_substring(s):
    char_index = {}
    max_length = 0
    start = 0

    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length


string_input = "abcabcbb"
print(f"Length of longest substring without repeating characters: {longest_unique_substring(string_input)}")
