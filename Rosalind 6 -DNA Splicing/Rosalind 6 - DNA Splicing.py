# Started : 2019/07/20
# Dolcevice/Yun Ho Jung

# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are
# given in FASTA format.

# Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will
# exist for the dataset provided.)

from common.toProtein import ToProtein as tp
from common.toRNA import ToRNA as tr

with open('6rosalind.txt', 'r') as file:
    total_input = file.read()
    file.close()
target = ''
introns = []

s = total_input[total_input.index('\n') + 1:]
target = s[:s.index('>')]
s = s[s.index('>'):]
target = target.rstrip()

while True:
    if not s == '':
        if s[0] == '>':
            s = s[s.index('\n') + 1:]
        else:
            try:
                intron = s[:s.index('>') - 1]
                introns.append(intron)
                s = s[s.index('>'):]
            except:
                intron = s.rstrip()
                introns.append(intron)
                break
    else:
        break
target = target.replace('\n', '')
for intron in introns:
    target = target.replace(intron, '')

target = tr.conversion(target)
target = "".join(target.split())

target = tp.conversion(target)

outfile = open('answer.txt', 'w')
outfile.write(target)

print(target)
