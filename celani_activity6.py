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

def get_compliment(gene):
    compliment_dict={"A":"T", "C":"G", "G":"C", "T":"A"}
    gene = gene.upper()
    compliment_gene = ""
    vertical_lines = "|" * len(gene)
    for nuc in gene:
        compliment_gene += compliment_dict[nuc]
    return (vertical_lines, compliment_gene)

def print_replication(gene):
    gene = gene.upper()
    (vertical_lines, compliment_gene) = get_compliment(gene)
    print(" " * (len(gene) + 2), gene)
    print(" " * len(gene), "/", vertical_lines)
    print(gene, " ", compliment_gene)
    print(vertical_lines)
    print(compliment_gene, " ", gene)
    print(" " * len(gene), "\\", vertical_lines)
    print(" " * (len(gene) + 2), compliment_gene)


if __name__ == '__main__':
    transcribed_gene = transcribe_gene(gene)
    # Printing
    (vertical_lines, compliment_gene) = get_compliment(gene)
    print(vertical_lines)
    print(compliment_gene)
    print()
    print("Replication-----------")
    print_replication(gene)
    print("Transcription---------")
    print(gene + "-->" + transcribed_gene)
    print("Translation------------")

