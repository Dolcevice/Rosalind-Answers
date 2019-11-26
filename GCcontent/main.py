filename = input("Filename : ")

with open(filename, 'r') as file:
    content = file.read()
    file.close()

content_original = content

def strip_dna_list(total_input : str):
    name_list = []
    dna_list = []
    while True:
        if not total_input == '':
            if total_input[0] == '>':
                name = total_input[total_input.index('>')+1:total_input.index('\n')]
                name = name.replace('\n', '')
                name_list.append(name)
                total_input = total_input[total_input.index('\n') + 1:]
            else:
                try:
                    dna = total_input[:total_input.index('>') - 1]
                    dna = dna.replace('\n', '')
                    dna_list.append(dna)
                    total_input = total_input[total_input.index('>'):]
                except:
                    dna = total_input.rstrip()
                    dna = dna.replace('\n', '')
                    dna_list.append(dna)
                    break
        else:
            break
    return dna_list, name_list

def calculate_gc_content(dna : str):
    total = len(dna)
    gccon= 0
    for ch in dna:
        if ch == 'G' or ch == 'C':
            gccon += 1

    print(gccon)
    print(total)

    return float(gccon) / float(total)



target_list, name_list = strip_dna_list(content)

maximus : str = ''
maximum_value : float = 0.0
for i in range(len(target_list)):
    gcp = calculate_gc_content(target_list[i])
    if gcp > maximum_value:
        maximus = name_list[i]
        maximum_value = gcp

print(maximus)
print(maximum_value * 100.0)