from typing import List


def compress(self, chars: List[str]) -> int:
    s = ""
    prev = ""
    count = 1
    for ch in chars:
        if ch == prev:
            count += 1
        else:
            if prev:
                s += prev
                if count > 1:
                    s += str(count)
                count = 1
            prev = ch
    if prev:
        s += prev
        if count > 1:
            s += str(count)
    chars.clear()
    chars.extend(list(s))
    return len(s)
