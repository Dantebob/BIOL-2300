#! /usr/bin python3

gene = input("Input gene sequence? ")
def transcribe_gene(gene):
    gene = gene.lower()
    list_gene = list(gene)
    for nuc in range(0, len(list_gene)):
        if list_gene[nuc] == "t":
            list_gene[nuc] = "u"
    gene = ''.join(list_gene)
    #gene = gene.replace("t", "u")
    return gene

if __name__ == '__main__':
    transcribed_gene = transcribe_gene(gene)

    # Printing
    print(gene + "-->" + transcribed_gene)
