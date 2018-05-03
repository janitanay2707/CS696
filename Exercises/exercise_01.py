def hello():
    print("Hello world")
    return 0

def percent_decimal(i):
    if i > 1:
        return(i/100)
    else:
        return (i*100)

def exponent(integer , power):
    number = 1
    for x in range(power):
        number = number * integer
    return number

def complement(dna):
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
hello()
print(percent_decimal(0.1))
print(exponent(3,2))
print(complement("AGTCG"))
