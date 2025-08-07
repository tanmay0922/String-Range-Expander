#code for stage 5
def expand_ranges(s):
    result = []
    parts = s.split(',')

    for part in parts:
        part = part.strip()

        # Handle ranges with optional step: e.g., "1-10:2"
        if '-' in part:
            if ':' in part:
                range_part, step_str = part.split(':')
                start_str, end_str = range_part.split('-')
            else:
                start_str, end_str = part.split('-')
                step_str = None

            if not start_str.strip().isdigit() or not end_str.strip().isdigit():
                raise ValueError(f"Invalid range: '{part}'")

            start, end = int(start_str), int(end_str)

            # Handle optional step
            if step_str is not None:
                if not step_str.strip().isdigit():
                    raise ValueError(f"Invalid step in range: '{part}'")
                step = int(step_str)
                if step <= 0:
                    raise ValueError(f"Step must be positive: '{part}'")
            else:
                step = 1

            if start <= end:
                result.extend(range(start, end + 1, step))
            else:
                result.extend(range(start, end - 1, -step))
        
        else:
            # Validate standalone number
            if not part.isdigit():
                raise ValueError(f"Invalid number: '{part}'")
            result.append(int(part))

    return result
