def rc(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] for base in dna[::-1]])

def percent_decimal(numbers):
    return [x/100 if x > 1 else x * 100 for x in numbers]

def multiple_proteins_from_rna(rna):
        C2AA = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
                       "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
                       "UAU": "Y", "UAC": "Y", "UAA": "", "UAG": "",
                       "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
                       "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
                       "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                       "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
                       "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                       "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
                       "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                       "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
                       "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
                       "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
                       "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                       "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
                       "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}
        return  ["".join([C2AA[rna[i:i+3]] for i in range(0, len(rna), 3)])[x:] for x,y in enumerate("".join([C2AA[rna[i:i+3]] for i in range(0, len(rna), 3)]))if y == "M"]

