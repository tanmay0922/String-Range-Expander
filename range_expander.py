#code for stage 4 
def expand_ranges(s):
    result = []
    parts = s.split(',')

    for part in parts:
        part = part.strip()

        if '-' in part:
            start_str, end_str = part.split('-')

            # Validate that both start and end are integers
            if not start_str.strip().isdigit() or not end_str.strip().isdigit():
                raise ValueError(f"Invalid range: '{part}'")

            start, end = int(start_str), int(end_str)

            if start <= end:
                result.extend(range(start, end + 1))
            else:
                # Handle reversed ranges
                result.extend(range(start, end - 1, -1))
        else:
            # Validate standalone number
            if not part.isdigit():
                raise ValueError(f"Invalid number: '{part}'")
            result.append(int(part))

    return result


if __name__ == "__main__":
    import sys
    input_str = sys.argv[1]
    print(expand_ranges(input_str))
