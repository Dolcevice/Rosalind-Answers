file = open('rosalind_cons.txt', 'r')
target = file.read()

d_list = []


class DNAcon:
    def __init__(self):
        self.A = 0
        self.C = 0
        self.G = 0
        self.T = 0

    def add_A(self, value):
        self.A += value

    def add_C(self, value):
        self.C += value

    def add_G(self, value):
        self.G += value

    def add_T(self, value):
        self.T += value


def inserter(target_str, target_list):
    raw = target_str
    while not raw.isspace() or len(raw) == 0:
        if raw[0] == '>':
            raw = raw[raw.index('\n') + 1:]
            try:
                loc = raw[0: raw.index('>')]
                loc = loc.replace('\n', '')
                target_list.append(loc)
            except:
                loc = raw[0:]
                loc = loc.replace('\n', '')
                target_list.append(loc)
                return
            raw = raw[raw.index('>'):]

        else:
            return


inserter(target, d_list)

maxlen = 0
for con in d_list:
    see = len(con)
    if see >= maxlen:
        maxlen = see

matrix = []

for i in range(maxlen):
    target = DNAcon()
    for con in d_list:
        try:
            val = con[i]
            if val == 'A':
                target.add_A(1)
            elif val == 'C':
                target.add_C(1)
            elif val == 'G':
                target.add_G(1)
            elif val == 'T':
                target.add_T(1)
        except:
            continue
    matrix.append(target)

consensus = ''
for dna in matrix:
    maximum = 0
    val = ''

    if dna.A >= maximum:
        maximum = dna.A
        val = 'A'
    if dna.C >= maximum:
        maximum = dna.C
        val = 'C'
    if dna.G >= maximum:
        maximum = dna.G
        val = 'G'
    if dna.T >= maximum:
        maximum = dna.T
        val = 'T'

    consensus += val

print(consensus)

for i in range(4):
    if i == 0:
        print('A:', end=' ')
        for dna in matrix:
            print(dna.A, end=' ')
    elif i == 1:
        print('C:', end=' ')
        for dna in matrix:
            print(dna.C, end=' ')
    elif i == 2:
        print('G:', end=' ')
        for dna in matrix:
            print(dna.G, end=' ')
    elif i == 3:
        print('T:', end=' ')
        for dna in matrix:
            print(dna.T, end=' ')
    print()
