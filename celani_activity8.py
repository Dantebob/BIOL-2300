#! /usr/bin python3

import re
import sys

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

def translate_codons(gene):
    gene = transcribe_gene(gene)
#   try:
#       if len(gene) % 3 != 0:
#           raise ValueError("Input gene sequence length must be divisible by 3")

    codon_to_amino_acid = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M", "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "ACU": "U", "ACC": "U", "ACA": "U", "ACG": "U", "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A", "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*", "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q","AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K","GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E","UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W", "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}
    amino_acid_sequence = ""
    n = 0
    while n <= len(gene) - 3:
        codon = gene[n:n+3]
        amino_acid = codon_to_amino_acid[codon]
        n += 3
        amino_acid_sequence += amino_acid
    return amino_acid_sequence
#   except ValueError as e:
#       return str(e)

if __name__ == '__main__':
    gene = input("Input gene sequence? ").upper()
    try:
        pattern = re.compile('[^ACGTacgt]')
        match = pattern.search(gene)
        if match:
            raise ValueError(f"Error: Invalid character used = {match.group()}")
    except ValueError as e:
        print(e)
        sys.exit(1)
    try:
        if len(gene) % 3 != 0:
            raise ValueError("ERROR: The input sequence must be the coding sequence- there can be no untranslated regions (gene sequence must be divisible by 3)")
    except ValueError as e:
        print(e)
        sys.exit(1)
    transcribed_gene = transcribe_gene(gene)
    (vertical_lines, compliment_gene) = get_compliment(gene)
    # Printing
    bp_num = len(gene)
    nt_num = bp_num*2
    aa_seq = translate_codons(gene)
    aa_num = len(aa_seq)
    print("Number of base pairs in the sequence: ", str(bp_num))
    print("Number of nucleotides in the sequence: " + str(nt_num))
    print("Number of amino acids in the translated protein: " + str(aa_num))
    print
    print("""
    ---------------
    Replication
    ---------------
    """)
    print(get_replication(gene))
    print()
    print("""
    ---------------
    Transcription
    ---------------
    {gene} --> {t_gene}
    {lines}
    {c_gene}
    """.format(gene = gene, t_gene = transcribed_gene, lines = vertical_lines,
    c_gene = compliment_gene))
    print("""
    --------------
    Translation
    --------------
    {transcribed_gene} --> {aa_seq}
    """.format(transcribed_gene=transcribed_gene, aa_seq=aa_seq))
    #    print("Replication-----------")
    #    print(get_replication(gene))
