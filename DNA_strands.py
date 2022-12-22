import re
def repeated_dna_sequence(sequence):
  n = len(sequence)
  print(n)
  k = 10#length of desired sequence
  s = set()
  output = []
  for i in range(0,n-k+1):
    current_sequence = sequence[i:i+k]
    print(current_sequence)
    if(current_sequence not in s):
      s.add(current_sequence)
    elif current_sequence not in output:
      output.append(current_sequence)
  return output

def check_invalid_dna_strand(dna):

    '''Below python code checks for a invalid DNA strand and retunr second side of DNA strand'''
    if(len(re.findall("[ATCG]",dna))!= len(dna)):
      raise ValueError("Invalid strand")
    return dna.translate(dna.maketrans("ATCG","TAGC"))
