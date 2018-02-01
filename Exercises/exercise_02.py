def first_element(mylist,n):
    list=mylist
    return list[:n]

def last_element(mylist,n):
    list=mylist
    return list[-n:]

def n_elements(my_list,start,n):
    return my_list[start:n]

def count_letters(s):
    i=s
    d = {x: i.count(x) for x in i}
    return d

def protein_wigth(protein):
    weight=0
    AMINO_ACID_WEIGHTS = {'A': 71.04, 'C': 103.01, 'D': 115.03, 'E': 129.04, 'F': 147.07,
                          'G': 57.02, 'H': 137.06, 'I': 113.08, 'K': 128.09, 'L': 113.08,
                          'M': 131.04, 'N': 114.04, 'P': 97.05, 'Q': 128.06, 'R': 156.10,
                          'S': 87.03, 'T': 101.05, 'V': 99.07, 'W': 186.08, 'Y': 163.06}
    for x in protein:
        weight = weight + AMINO_ACID_WEIGHTS[x]
    return weight



