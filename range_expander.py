def expand_ranges(input_str: str) -> list:
    result = []
    tokens = input_str.split(',')

    for token in tokens:
        if '-' in token:
            try:
                start, end = map(int, token.split('-'))
                if start > end:
                    raise ValueError(f"Invalid range: {token}")
                result.extend(range(start, end + 1))
            except ValueError:
                raise ValueError(f"Invalid range token: {token}")
        else:
            try:
                result.append(int(token))
            except ValueError:
                raise ValueError(f"Invalid number token: {token}")

    return result

if __name__ == "__main__":
    print(expand_ranges("1-3,5,7-9"))  # Expected: [1, 2, 3, 5, 7, 8, 9]
    print(expand_ranges("5"))         # Expected: [5]
    print(expand_ranges("4-4,6"))     # Expected: [4, 6]
