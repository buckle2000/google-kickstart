import sys, re, string

input_ = sys.stdin.read().strip()

def decompressed_length(s):
    result = 0
    i = 0
    while i < len(s):
        c = s[i]
        if c in string.ascii_uppercase:
            result += 1
            i+=1
        else:
            match = re.match(r"\((\d+)x(\d+)\)", s[i:])
            span_start, span_end = match.span()
            assert span_start == 0
            i += span_end
            length, repetition = map(int, match.groups())
            result += length * repetition
            i += length
    return result

def decompressed_length2(s):
    result = 0
    i = 0
    while i < len(s):
        c = s[i]
        if c in string.ascii_uppercase:
            result += 1
            i+=1
        else:
            match = re.match(r"\((\d+)x(\d+)\)", s[i:])
            span_start, span_end = match.span()
            assert span_start == 0
            i += span_end
            length, repetition = map(int, match.groups())
            result += decompressed_length2(s[i:i+length]) * repetition
            i += length
    return result

# for match in re.finditer(r"(\d+)x(\d+)", input_):
#     length, repetition = map(int, match.groups())
#     result += length * (repetition - 1)

print(decompressed_length(input_))
print(decompressed_length2(input_))