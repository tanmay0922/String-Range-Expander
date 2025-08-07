import re
from typing import List

def expand_ranges(s: str, delimiters: List[str] = ["-", "..", "to", "~"]) -> List[int]:
    result = []
    # Sort delimiters by length so '..' is checked before '.'
    sorted_delimiters = sorted(delimiters, key=lambda d: -len(d))
    delimiter_pattern = '|'.join(re.escape(d) for d in sorted_delimiters)
    
    parts = s.split(',')
    for part in parts:
        part = part.strip()
        match = re.match(rf'^(\d+)\s*(?:{delimiter_pattern})\s*(\d+)$', part)
        if match:
            start, end = int(match.group(1)), int(match.group(2))
            result.extend(range(start, end + 1))
        else:
            if part.isdigit():
                result.append(int(part))
            else:
                raise ValueError(f"Invalid input segment: {part}")
    return result
