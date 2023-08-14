def shortest_substring(s, x):

    result = []
    for i in range(len(s)):
        for j in range(i + x, len(s) + 1):
            if s[i] == s[j - 1] and len(s[i:j]) >= x:
                result.append(s[i:j])

    if result:
        shortest_length = min(len(substr) for substr in result)
        shortest_substrings = [substr for substr in result if len(substr) == shortest_length]
        for substr in shortest_substrings:
            print(substr)


if __name__ == "__main__":
    s = "abccdbacca"

    for x in range(3,9):
        print(f"x = {x}")
        shortest_substring(s, x)