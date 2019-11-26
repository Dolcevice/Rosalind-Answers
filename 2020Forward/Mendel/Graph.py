class Node:
    def __init__(self, name, con):
        self.name = name
        self.content = con



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

target_list, name_list = strip_dna_list(content)
node_list = []

for i in range(len(target_list)):
    node_list.append(Node(name_list[i], target_list[i]))

adj_list = []

for node in node_list:
    for node2 in node_list:
        if not node.name == node2.name:
            if node2.content[0:3] == node.content[-3:]:
                adj_list.append([node, node2])

for con in adj_list:
    print(con[0].name, con[1].name)
