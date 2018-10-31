# best album

def solution(genres, plays):
    infodict = {}
    for i in range(len(genres)):
        if genres[i] in infodict:
            infodict[genres[i]][0] += plays[i]
            infodict[genres[i]][1].append((i, plays[i]))
        else:
            infodict[genres[i]] = []
            infodict[genres[i]].append(plays[i])
            infodict[genres[i]].append([(i, plays[i])])

    infolist = list(infodict.items())
    infolist = sorted(infolist, key=lambda x:x[1][0], reverse=True)
    answer = []
    for item in infolist:
        idxlist = item[1][1]
        idxlist = sorted(idxlist, key=lambda x:x[1], reverse=True)
        for idx in idxlist[:min(len(idxlist), 2)]: answer.append(idx[0])

    return answer

genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]

sol = solution(genres, plays)
print(sol)
