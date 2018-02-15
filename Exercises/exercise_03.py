import os
import sys
def fasta_folder_to_dict(folder_path):
    fasta={}
    for file in os.listdir(folder_path):
        if not file.endswith('.fasta'):
            continue
        with open(folder_path + '/'+ file) as file_one:
            for line in file_one:
                line = line.strip()
                if not line:
                    continue
                if line.startswith(">"):
                    active_sequence_name = line[1:]
                    if active_sequence_name not in fasta:
                        fasta[active_sequence_name] = []
                    continue
                sequence = line
                fasta[active_sequence_name].append(line)
    return fasta

print(fasta_folder_to_dict("../CS696"))