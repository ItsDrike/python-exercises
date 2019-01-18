def isArmstrong(number):
    fint = 0
    num = str(number)
    nums = list(num)

    for x in nums:
        fint = fint + int(x) ** 3
    if fint == number:
        return True
    return False


for i in range(1, 100000):
    i += 1
    if isArmstrong(i):
        print(f"{i} is an Armstrong Number")

    print(f"Currently on number {i}", end='\r')
