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

def get_replication(gene):
    gene = gene.upper()
    (vertical_lines, compliment_gene) = get_compliment(gene)
    spaces = " " * len(gene)
    replication = (
       f"{spaces} {gene}\n"
       f"{spaces}/{vertical_lines}\n"
       f"{gene} {compliment_gene}\n"
       f"{vertical_lines}\n"
       f"{compliment_gene} {gene}\n"
       f"{spaces}\{vertical_lines}\n"
       f"{spaces} {compliment_gene}")
    return replication

if __name__ == '__main__':
    # Printing
    print("Replication-----------")
    print(get_replication(gene))
    print()
    print("Transcription---------")
    transcribed_gene = transcribe_gene(gene)
    print(gene + "-->" + transcribed_gene)
    (vertical_lines, compliment_gene) = get_compliment(gene)
    print(vertical_lines)
    print(compliment_gene)

