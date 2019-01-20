def main(inp):
    words = inp.split()
    without_duplicates = list(set(words))
    sorted_list = sorted(without_duplicates)
    return ','.join(sorted_list)

if __name__ == '__main__':
    print(main(input('Words: ')))
