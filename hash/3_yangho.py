from itertools import combinations
def solution(clothes):
    answer = 0
    cateDict = {}
    for item in clothes:
        if item[1] in cateDict:
            cateDict[item[1]] += 1
        else:
            cateDict[item[1]] = 1

    keys = cateDict.keys()
    for i in range(1, len(cateDict) + 1):
        clist = combinations(keys, i)
        for com in clist:
            temp = 1
            for ca in com:
                temp *= cateDict[ca]
            answer += temp
    return answer


if __name__ == '__main__':
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    #clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    # 0.14ms, 4.33ms
    answer = solution(clothes)
    print(answer)