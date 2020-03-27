from sars_cov_2 import sars_cov

#decode dna into codons.
#no transcriptions b/c ths is a virus and its rna.
#virus is rna only - were just going to do translation.

#genetic code table
from collections import defaultdict
table = defaultdict()
#Inverse table for the standard genetic code (compressed using IUPAC notation) 
# dup
# Asn or Asp / B  AAU, AAC; GAU, GAC
# Gln or Glu / Z  CAA, CAG; GAA, GAG
# START AUG
# met the start codon...
tt = """Ala / A GCU, GCC, GCA, GCG
Ile / I AUU, AUC, AUA
Arg / R CGU, CGC, CGA, CGG; AGA, AGG
Leu / L CUU, CUC, CUA, CUG; UUA, UUG
Asn / N AAU, AAC
Lys / K AAA, AAG
Asp / D GAU, GAC
Met / M AUG
Phe / F UUU, UUC
Cys / C UGU, UGC
Pro / P CCU, CCC, CCA, CCG
Gln / Q CAA, CAG
Ser / S UCU, UCC, UCA, UCG; AGU, AGC
Glu / E GAA, GAG
Thr / T ACU, ACC, ACA, ACG
Trp / W UGG
Gly / G GGU, GGC, GGA, GGG
Tyr / Y UAU, UAC
His / H CAU, CAC
Val / V GUU, GUC, GUA, GUG
STOP    UAA, UGA, UAG
""".strip()
for t in tt.split("\n"):
  k = t[:len("Val / V")].strip()
  v = t[len("Val / V "):]
  if '/' in k:
    k = k.split("/")[-1].strip()
  v = v.replace(",", "").replace(";", "").lower().replace("u", "t").split(" ")
  for vv in v:
    if vv in table:
      print("dup", vv)
    table[vv.strip()] = k

#for k,v in table.items():
#    print(k,v)

# a t c g u.
# u's b/c its rna ...?
# well replace it with the t's

# which letters correspond to which dna sequence.

# stick tog
# translation - amino acid - fold proteins
 

#amino acid chain
amino_acid = []
for i in range(3):
    for j in range(i,len(sars_cov)-3,3):
        amino_acid.append(table[sars_cov[j:j+3]])
amino_acid = ''.join(amino_acid)


#one for example 
#membrane glycoprotein
"""
MADSNGTITVEELKKLLEQWNLVIGFLFLTWICLLQFAYANRNR
FLYIIKLIFLWLLWPVTLACFVLAAVYRINWITGGIAIAMACLVGLMWLSYFIASFRL
FARTRSMWSFNPETNILLNVPLHGTILTRPLLESELVIGAVILRGHLRIAGHHLGRCD
IKDLPKEITVATSRTLSYYKLGASQRVAGDSGFAAYSRYRIGNYKLNTDHSSSSDNIA
LLVQ
"""
# part of membrane glycoprotein
print(amino_acid.find("MADSNGTITVEELKKLLEQWNLVIGFLFLTWICLLQFAYANRNR"))

#list(filter(lambda x: len(x) > 100, amino_acid.split("STOP")))


# TODO match https://www.ncbi.nlm.nih.gov/nuccore/NC_045512
# using our genetic code table to break list proteins like in above line ^
# https://www.khanacademy.org/science/biology/gene-expression-central-dogma/central-dogma-transcription/a/the-genetic-code-discovery-and-properties
#proteins
for i in amino_acid.split("STOP"):
    print(i)

