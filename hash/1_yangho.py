def solution(participant, completion):
    nameDict = {}
    for name in participant:
        if name in nameDict:
            nameDict[name] += 1
        else:
            nameDict[name] = 1

    for name in completion:
        if nameDict[name] == 1:
            nameDict.pop(name)
        else:
            nameDict[name] -= 1

    answer = nameDict.popitem()[0]
    return answer


if __name__ == '__main__':
    participant = ['mislav', 'stanko', 'mislav', 'ana']
    completion = ['stanko', 'ana', 'mislav']
    answer = solution(participant, completion)
    print(answer)