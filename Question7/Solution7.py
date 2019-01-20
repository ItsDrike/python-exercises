def isArmstrong(number):
    fint = 0
    num = str(number)
    nums = list(num)

    for x in nums:
        fint = fint + int(x) ** 3
    if fint == number:
        return True
    return False


def main():
    armstrong_nums = []

    for i in range(1, 100001):
        if isArmstrong(i):
            armstrong_nums.append(str(i))
        # I've added this print just as a decoration, if you want it faster, remove it
        print(f'Currently on number {i}', end='\r')
    # Just to clear last print
    print(' ' * 26, end='\r')
    return ','.join(armstrong_nums)


if __name__ == '__main__':
    print(main())
