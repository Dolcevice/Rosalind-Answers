str1 = input('First String : ')
str2 = input('Second String: ')

counter = 0
for i in range(len(str1)):
    try:
        if not str1[i] == str2[i]:
            counter += 1
    except:
        break

print(counter)
