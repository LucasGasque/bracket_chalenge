#!/bin/python3

# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.
def isBalanced(brackets):

    brackets = list(brackets)

    pair = {"(": ")", "[": "]", "{": "}"}

    mirror = []

    parenteses, colchetes, chaves = 0, 0, 0

    for bracket in brackets:
        if bracket in pair.values() and bracket != mirror[len(mirror) - 1]:
            return "NO"

        if bracket == "(":
            parenteses += 1
            mirror.append(pair[bracket])

        if bracket == ")":
            parenteses -= 1
            mirror.pop()

        if bracket == "[":
            colchetes += 1
            mirror.append(pair[bracket])

        if bracket == "]":
            colchetes -= 1
            mirror.pop()

        if bracket == "{":
            chaves += 1
            mirror.append(pair[bracket])

        if bracket == "}":
            chaves -= 1
            mirror.pop()

        if parenteses < 0 or colchetes < 0 or chaves < 0:
            return "NO"

    if parenteses > 0 or colchetes > 0 or chaves > 0:
        return "NO"

    return "YES"


if __name__ == "__main__":

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep="\n")
