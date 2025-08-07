#code for stage 6
def expand_ranges(s):
    result = []
    seen = set()
    parts = s.split(',')

    for part in parts:
        part = part.strip()
        if not part:
            continue

        if ':' in part:
            range_part, step_part = part.split(':')
            step = int(step_part.strip())
        else:
            range_part = part
            step = 1

        if '-' in range_part:
            start_str, end_str = range_part.split('-')
            if not (start_str.strip().isdigit() and end_str.strip().isdigit()):
                raise ValueError(f"Invalid numeric range: '{part}'")
            start = int(start_str)
            end = int(end_str)

            if step == 0:
                raise ValueError("Step value cannot be zero.")

            # Determine direction based on start and end
            if start <= end:
                expanded = list(range(start, end + 1, step))
            else:
                expanded = list(range(start, end - 1, -step))

            for num in expanded:
                if num not in seen:
                    result.append(num)
                    seen.add(num)
        else:
            if not range_part.strip().isdigit():
                raise ValueError(f"Invalid numeric value: '{part}'")
            num = int(range_part)
            if num not in seen:
                result.append(num)
                seen.add(num)

    return result
