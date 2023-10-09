#! /usr/bin python3

gene = input("Input gene sequence? ").upper()

def transcribe_gene(gene):
    gene = gene.upper()
    transcribed_gene = ""
    for nuc in gene:
        if nuc == "T":
            transcribed_gene += "U"
        else:
            transcribed_gene += nuc
    return transcribed_gene

def print_compliment(gene):
    compliment_dict={"A":"T", "C":"G", "G":"C", "T":"A"}
    gene = gene.upper()
    compliment_gene = ""
    vertical_lines = ""
    for nuc in gene:
        vertical_lines += "|"
        compliment_gene += compliment_dict[nuc]
    print(vertical_lines)
    print(compliment_gene)

if __name__ == '__main__':
    transcribed_gene = transcribe_gene(gene)
    # Printing
    print(gene + "-->" + transcribed_gene)
    print_compliment(gene)
