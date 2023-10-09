#! /usr/bin python3

from Bio.Seq import Seq
gene_name = input("Enter the gene name: ")
gene_func = input("Enther the gene function: ")
str_gene = input("Enter the gene nucleotide sequence: ")

gene_seq = Seq(str_gene)
transcript = gene_seq.transcribe()
aa_seq = transcript.translate()

#number of base pairs, nucleotides, and amino acids.
bp_num = len(gene_seq)
nt_num = bp_num*2
aa_num = len(aa_seq)

#display info to user
print("Gene name: " + gene_name)
print("Gene function: " + gene_func)
print("Gene sequence: " + gene_seq)
print("Gene length (bp): " + str(bp_num))
print("Gene length (nt): " + str(nt_num))
print("Amino acid sequence: " + aa_seq)
print("Amino acid sequence length: " + str(aa_num))

