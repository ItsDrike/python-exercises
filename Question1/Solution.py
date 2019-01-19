def main():
    number_list = []

    for x in range(100, 8001):
        if (x % 7 == 0) and (x % 5 == 0):
            number_list.append(str(x))
    return ','.join(number_list)


if __name__ == '__main__':
    print(main())
