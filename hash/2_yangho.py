def solution(phone_book):
    for i in range(len(phone_book)):
        pivot = phone_book[i]
        for j in range(i+1, len(phone_book)):
            strlen = min(len(pivot), len(phone_book[j]))
            if pivot[:strlen] == phone_book[j][:strlen]:
                return False
    return True


if __name__ == '__main__':
    phone_book = ["113", "12340", "123440", "12345", "98346"]
    #phone_book = ["911", "97625999", "91125426"]
    # 0.14ms, 4.33ms
    answer = solution(phone_book)
    print(answer)