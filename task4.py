def validate_brackets(bracket_string):
    open = ["[", "{", "("]
    pairs = {"]": "[]", "}": "{}", ")": "()"}

    bstack = []

    for char in bracket_string:
        if char in open:
            bstack.append(char)
        else:
            last_bracket = bstack.pop()
            if pairs[char] != last_bracket + char:
                return "False"
    return "True"


t = "{[]}"
f = "{[]}()[{]"

print(validate_brackets(t))
print(validate_brackets(f))
