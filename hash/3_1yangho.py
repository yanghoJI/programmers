
def solution(clothes):
    answer = 1
    cateDict = {}
    for item in clothes:
        if item[1] in cateDict:
            cateDict[item[1]] += 1
        else:
            cateDict[item[1]] = 1

    for key in cateDict.keys():
        answer *= cateDict[key] + 1
    return answer - 1


if __name__ == '__main__':
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    #clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    # 0.14ms, 4.33ms
    answer = solution(clothes)
    print(answer)