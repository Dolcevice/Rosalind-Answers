comp_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
target = input()
target = target.replace(' ', '')
print()

# returns the reverse compliment of DNA strand
def get_recomp(target_str):
    reverse = target_str[::-1]
    result = ''
    for index in range(len(reverse)):
        result += comp_dict.get(reverse[index])
    return result


# create containers
loc_list = []
len_list = []

# Search through the string to find rp
# O(n) time complexity
for index1 in range(len(target)):
    if index1 + 4 > len(target):
        break
    for index2 in range(9):
        if index1 + index2 + 4 > len(target):
            break
        sub = target[index1: index1 + index2 + 4]
        if sub == get_recomp(sub):
            loc_list.append(index1 + 1)
            len_list.append(len(sub))

# print the result
for (loc, leng) in zip(loc_list, len_list):
    print(str(loc) + ' ' + str(leng))
