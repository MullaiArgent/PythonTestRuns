def isBalanced(brackets):
    stack = []
    openers = ["(", "{", "["]
    d = {")": "(", "}": "{", "]": "["}

    for bracket in brackets:
        if bracket in openers:
            stack.append(bracket)
            brackets = brackets[1:]
            print(brackets)
        else:
            if stack[-1] != d[bracket]:
                return "NO"
            else:
                stack.pop()
                brackets = brackets[1:]
    if stack:
        return "NO"
    if len(brackets) != 0:
        return "NO"
    return "YES"

print(isBalanced("{{]][[]][{{}}"))