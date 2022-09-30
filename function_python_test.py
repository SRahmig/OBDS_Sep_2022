#function to give complement of DNA sequence
def complement_base(base):
    output = None
    if base == 'A':
        output = 'T'
    elif base == 'G':
        output = 'C'
    elif base == 'C':
        output = 'G'
    elif base == 'T':
        output = 'A'
    else:
        output = 'N'
    return output

sequence = 'AAAABCCCGGT'
complement = ''
for base in sequence:
    complement += complement_base(base)
print(complement)

#function to give reverse of string
def reverse_string(input_string):
    output = ''
    l=len(input_string)                 #get length of string
    for i in range (l-1, -1, -1):       #index string in reverse order
        output +=input_string[i]
    return output


input_string = 'AAAACCCGGT'
reverse_string(input_string)

#function to give reverse complement of sequence
def reverse_complement(sequence):
    reverse = ''
    output = None
    l=len(sequence)                     #get length of string
    for i in range (l-1, -1, -1):       #index string in reverse order
        if sequence[i] == 'A':          #for each index check input and get complement base
            output = 'T'
        elif sequence[i] == 'G':
            output = 'C'
        elif sequence[i] == 'C':
            output = 'G'
        elif sequence[i] == 'T':
            output = 'A'
        else:
            output = 'N'
        reverse +=output                #add each base to 'reverse'
    return reverse

DNA = 'AGCTTAGCHACGT'
rev_com = reverse_complement(DNA)
print(rev_com)