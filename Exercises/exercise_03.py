import os

def fasta_folder_to_dict(folder_path):
    """
    Constructs a dictionary of all of the FASTA formatted entries from a folder containing FASTA files.
    :param folder_path: string
    :return: dictionary
    """
    dict = {}
    for file in os.listdir(folder_path):
        if not file.endswith('.fasta'):
            continue
        with open(folder_path + '/' + file, 'r') as infile:
            infile = infile.read()
            seqs = infile.split('>')
            seqs = seqs[1:]
            d = ''
            for seq in seqs:
                try:
                    x = seq.split('\n', 1)
                    header = x[0]
                    sequence = x[1].replace('\n', '')

                    if d != header:
                        dict[header] = sequence
                        d = header
                    else:
                        del dict[header]
                    if sequence == '':
                        del dict[header]

                    for i in range(len(sequence)):
                        if sequence[i] != 'G' and sequence[i] != 'A' and sequence[i] != 'T' and sequence[i] != 'C':
                            del dict[header]
                            break

                except:
                    print('Please Check Fasta Files')

    for fasta_keys, fasta_values in dict.items():
        print('Key: {}\tValue:{}'.format(fasta_keys, fasta_values))

    return dict
