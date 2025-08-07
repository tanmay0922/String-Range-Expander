# code for stage 7
def expand_ranges(s, output_format="list"):
    result = []
    seen = set()
    parts = s.split(',')

    for part in parts:
        part = part.strip()
        if not part:
            continue

        if ':' in part:
            range_part, step_part = part.split(':')
            step = int(step_part)
        else:
            range_part = part
            step = 1

        if '-' in range_part:
            start_str, end_str = range_part.split('-')
            start = int(start_str)
            end = int(end_str)

            if start <= end:
                rng = range(start, end + 1, step)
            else:
                rng = range(start, end - 1, -step)
        else:
            rng = [int(range_part)]

        for num in rng:
            if num not in seen:
                result.append(num)
                seen.add(num)

    if output_format == "list":
        return result
    elif output_format == "csv":
        return ",".join(str(x) for x in result)
    elif output_format == "set":
        return set(result)
    else:
        raise ValueError(f"Invalid output_format: {output_format}")
