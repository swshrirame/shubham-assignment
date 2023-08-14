def process_string(s):
    ascii_values = [ord(char) for char in s]
    modified_chars = [False] * len(ascii_values)

    for i in range(len(ascii_values)):
        if i == 0:
            #  No previous character
            pass
        else:
            # For invalid ASCII
            if ascii_values[ i ] == 110:
                print(f"for {ascii_values[i]}")
                ascii_values[ i + 1] = 78
                modified_chars[i] = True
            # For even ASCII
            if ascii_values[i] % 2 == 0:
                print(f"for {ascii_values[i]}")
                ascii_values[ i + 1 ] = ascii_values[ i + 1 ] + ascii_values[ i ] % 7
                modified_chars[ i ] = True
            # For odd ASCII
            if modified_chars[ i - 1 ] != False:
                print(f"for {ascii_values[i]}")
                ascii_values[ i - 1 ] = ascii_values[ i - 1 ] - ascii_values[ i ] % 5
                modified_chars[ i - 1] = True
        print(ascii_values)
        print(modified_chars)
        print()
    result = ''.join([chr(ascii_val) for ascii_val in ascii_values])
    return result


# Example usage
s = "sHQen}"
final_output = process_string(s)
print(f"Final Answer: {final_output}")
