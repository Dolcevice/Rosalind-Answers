comp_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
target = input()
target = target.replace(' ', '')


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
# n^2 time complexity
for index1 in range(len(target)):
    for index2 in range(len(target) - index1 - 3):
        sub = target[index1: index1 + index2 + 4]
        if sub == get_recomp(sub):
            loc_list.append(index1 + 1)
            len_list.append(index2 + 4)

# print the result
for (loc, leng) in zip(loc_list, len_list):
    print(str(loc) + ' ' + str(leng))
