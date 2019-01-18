words = input('Words: ').split()
without_duplicates = list(set(words))
sorted_list = sorted(without_duplicates)
print(','.join(sorted_list))
