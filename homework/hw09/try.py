def check(num):
    count = 0
    for i in range(2,num):
        if num / i == 0:
            count += 1
            if i not in [2, 3, 5]:
                return False
    if count == 0:
        return False
    return True

def findit(num):
    for _ in range(10000):
        num += 1
        if check(num):
            return num
    return 2
