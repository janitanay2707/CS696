def hello():
    print("Hello world")
    return 0

def percent_decimal(i):
    if i > 1:
        return(i/100)
    else:
        return (i*100)

def exponent(integer , power):
    for integer in range(power):
        number = integer * integer
    return number

def complement(dna):
    if 'C' in dna:
        dna.replace("C","G")
    elif 'G' in dna:
            dna.replace("G","C")
    elif 'A' in dna:
        dna.replace("A","T")
    elif 'T' in dna:
        dna.replace("T","A")
