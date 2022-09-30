#algorithm to find occurences of 'TATA'
sequence = 'TGCAATGCTGACTTATAGCGCTATATATATATA'
print(sequence)
motif = 'TATA'
l=len(motif)
pos = 0
sum = 0
for base in sequence:
    if sequence[pos:pos+l] == motif:
        print(f'start {pos+1} end {pos+l}')
        sum+=1
    pos+=1
print(f'number of occurences {sum}')

#calculate CG content of a sequence
DNA_sequence = 'GTGGCTTAAGAGGGGAGTCGTCACAGGCGTCAAGTCTTCTTTCTAAAGCCGGGGACCTGG'

gc_n = 0
l=len(DNA_sequence)
for base in DNA_sequence:
    if base == 'C' or base == 'G':
        gc_n+=1
gc_content = gc_n/l*100
print(gc_n)
print(f'GC content is {round(gc_content)} %')

#calculate Hamming Distance
sequence_1 = 'TACAATGCTGACTTATAGCGCTATATATATATA'
sequence_2 = 'TGCAATGCAGACGTATAGCGCTATATATGTATA'
l1=len(sequence_1)
l2=len(sequence_2)
print(l1)
print(l2)
pos=0
ham=0

for base in sequence_1:
    if base != sequence_2[pos]:
        ham+=1
    pos+=1
print(ham)

#consensus sequence
motif_list = ['ATCCAGCT', 'GGGCAACT', 'ATGGATCT', 'AAGCAACC', 'TTGGAACT', 'ATGCCATT', 'ATGGCACT']
pos=0
motif_list[0][pos]
l=len(motif_list[0])
consensus=[]
position={}

for base in range (0,l):
    bases ={'A':0, 'C':0,'G':0, 'T':0}
    for element in motif_list:
        if element[base] == 'A':
            bases['A']+=1
        elif element[base] == 'C':
            bases['C']+=1
        elif element[base] == 'G':
            bases['G']+=1
        elif element[base] == 'T':
            bases['T']+=1
    position[base] = bases
print (position)

for pos in position.keys:
    if value['A']>value['C'] and value['A']>value['G'] and value['A']>value['T']:
        consensus[base] ='A'
    elif value['C']>value['A'] and value['C']>value['G'] and value['C']>value['T']:
        consensus[base] ='C'
    elif value['G']>value['A'] and value['G']>value['C'] and value['G']>value['T']:
        consensus[base] ='G'
    elif value['T']>value['A'] and value['T']>value['C'] and value['T']>value['G']:
        consensus[base] ='T'
    print(consensus[base])

