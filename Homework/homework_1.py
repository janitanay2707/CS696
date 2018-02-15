#String functions
def fast_complement(dna):
    complementary_string = ""
    for s in dna:
        if s=="C":
            complementary_string+=str('G')
        elif s=="A":
            complementary_string+=str('T')
        elif s=="T":
            complementary_string+=str('A')
        else:
            complementary_string+=str('C')
    return complementary_string

def remove_interval(s,start,stop):
    return s[:start]+s[stop+1:]


def kmer_list(s,k):
    kmer=[]
    n=len(s)
    for i in range(0,n-k+1):
        kmer.append(s[i:i+k])
    return kmer

def kmer_set(s,k):
    kmer=set()
    n=len(s)
    for i in range(0,n-k+1):
        kmer.add(s[i:i+k])
    return kmer


def kmer_dict(s,k):
    count={}
    n=len(s)-k+1
    for i in range(n):
        kmer=s[i:i+k]
        if kmer not in count:
            count[kmer]=0
        count[kmer] += 1
    return count

#Reading files
def head(file_name):
   with open(file_name) as myfile:
       first10lines=myfile.readlines()[0:10]
       print(first10lines)

def tail(file_name):
    with open(file_name) as f:
        lines=f.readlines()
        l=str(lines)
        print(l)

print(tail("random_dna.txt"))
def print_even(file_name):
    with open(file_name) as f:
        count=0
        for line in f:
            count=count+1
            if count%2 ==0:
                print(line)

def csv_list(file_name):
    import csv
    with open(file_name) as f:
        r=csv.reader(f, delimiter='\t')
        l=list(r)
    return l

##
def get_csv_column(file_name,column):
    import csv
    column_list=[]
    with open(file_name) as f:
         for line in f.readlines():
            column_list.append(line.split(",")[column])
    return column_list


def fasta_seqs(file_name):
    with open(file_name, 'r') as fd:
        sequence = []
        for line in fd.readlines():
            if  not '>' in line:
                key = line.replace('\n','')
                sequence.append(key)
            else:
                continue
    return sequence

def fasta_header(file_name):
    with open(file_name, 'r') as fd:
        headers = []
        for line in fd.readlines():
            if '>' in line:
                key = line.strip()[1:]
                headers.append(key)
            else:
                continue
    return headers

def fasta_dict(file_name):
        with open(file_name, 'r') as fd:
            dict = {}
            key = ''
            for line in fd.readlines():
                if '>' in line:
                    key = line.strip()[1:]
                else:
                    dict[key] = line.replace('\n','')

        return dict

##
def fastq_to_fasta(file_name,new_name=None):
    fastq_dict=fasta_dict(file_name)
    f = open(new_name+'.fasta',"w")
    f.write(fastq_dict)


##
def reverse_complement(dna):
    return fast_complement(dna[::-1])

def transcribe(dna):
    rna_seq = dna.replace('T', 'U')
    return(rna_seq)

def translate(rna):
    RNA_CODON_TABLE   = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
           "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
           "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
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

    protein_seq = ''
    for n in range(0, len(rna), 3):
        if rna[n:n+3] in RNA_CODON_TABLE:
            protein_seq += RNA_CODON_TABLE[rna[n:n+3]]
    return protein_seq.replace("*","")


def reading_frames(dna):
    frames = {'+1': [], '+2': [], '+3': [], '-1': [], '-2': [], '-3': []}
    seq_rev = reverse_complement(dna)
    for j in range(0, 3):
        temp = ''.join([dna[j::]])
        temp_rev = ''.join([seq_rev[j::]])
        seq_trans = translate(temp)
        seq_rev_trans = translate(temp_rev)
        if j == 0:
            frames['+1'] = seq_trans
            frames['-1'] = seq_rev_trans
        if j == 1:
            frames['+2'] = seq_trans
            frames['-2'] = seq_rev_trans
        if j == 2:
            frames['+3'] = seq_trans
            frames['-3'] = seq_rev_trans
    return frames




