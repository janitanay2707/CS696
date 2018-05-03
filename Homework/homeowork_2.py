class String_Aligner:


    def _init_(self, string1, string2):
        self.s1 = string1
        self.s2 = string2
        return

    def hamming_dist(self):

        miss_match = 0
        add = abs(len(self.s1)-len(self.s2))
        for (base_s, base_t) in zip(self.s1, self.s2):
            if base_s != base_t:
                miss_match += 1
        result = miss_match + add
        return result

    def empty_matrix(self):
        return [[0 for i in range(len(self.s2)+1)] for j in range(len(self.s1)+1)]

    def init_needleman_wunsch_matrix(self):
        empty_matrix = self.empty_matrix()
        for i in range(1, len(self.s1)+1):
            empty_matrix[i][0] = empty_matrix[i-1][0]-1
        empty_matrix[0] =[x for x in range(0,-len(self.s2)-1,-1)]

        return empty_matrix

    def needleman_wunsch_fill(self):
        matrix = self.init_needleman_wunsch_matrix() # Building on the previous definition

        def score_cell(i,j):
            match = 1
            mismatch = -1
            indel = -1

            up = matrix[i-1][j] + indel
            left = matrix[i][j-1] + indel
            if self.s1[i-1] == self.s2[j-1]:
                diag = matrix[i-1][j-1] + match
            else:
                diag = matrix[i-1][j-1] + mismatch
            return max (up, left, diag)
        for i in range(1, len(self.s1)+1):
            for j in range(1, len(self.s2)+1):
                matrix[i][j] = score_cell(i, j)
        return matrix

    def smith_waterman_fill(self):
        matrix = self.empty_matrix() # Building on the previous definition

        def score_cell(i,j):
            match = 3
            mismatch = -3
            indel = -2

            up = matrix[i - 1][j] + indel
            left = matrix[i][j - 1] + indel
            if self.s1[i - 1] == self.s2[j - 1]:
                diag = matrix[i - 1][j - 1] + match
            else:
                diag = matrix[i - 1][j - 1] + mismatch
            return max(up, left, diag,0)

        for i in range(1, len(self.s1) + 1):
            for j in range(1, len(self.s2) + 1):
                matrix[i][j] = score_cell(i, j)
        return matrix

def is_dna(string):
    dna_char = set(['A', 'T', 'C', 'G'])
    return len([char for char in string if char not in dna_char]) == 0


def is_rna(string):
    rna_char = set(['C', 'U', 'A', 'G'])
    return len([char for char in string if char not in rna_char]) == 0


def is_protein(string):

    protein_char = set(['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'K', 'L', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'])
    return len([char for char in string if char not in protein_char]) == 0


import urllib.request as ur
import re
def get_sra_xml(sra_run_id):
    url = "http://www.ncbi.nlm.nih.gov/Traces/sra/?run={}&experimental=1&retmode=xml".format(sra_run_id)
    t = ur.urlopen(url).read().decode()
    return t


def get_filesize(string):
    data = get_sra_xml('SRR3403834')
    return int(re.search("size=\"(.*?)\"", data).group(1)) / 1e9


def get_protein_fasta(uniprot_id):
    url = "http://www.uniprot.org/uniprot/{}.fasta".format(uniprot_id)
    y = ur.urlopen(url).read().decode()
    t = y[y.find('\n') + 1:]
    line = t.replace('\n','')

    return (line)


