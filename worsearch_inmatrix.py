def wordsearch(i,j,A,word,m):
  """Depth first search algorithm to find given string is present in the matrix or not"""
  surrounding_indices = [[i,j+1],[i+1,j],[i,j-1],[i-1,j-1]]
  for each_index in surrounding_indices:
      if each_index[0] <= len(A)-1 and each_index[1] <=len(A[0])-1 and  A[each_index[0]][each_index[1]]==word[m]:
         m=m+1

         if(m == len(word)-1):
           print(m)
           return True
           break
         A[each_index[0]][each_index[1]] =1
         wordsearch(each_index[0],each_index[1],A,word,m)
         
def main_search(A,word):
  m=0
  for i in range(0,len(A)):
    for j in range(0,len(A[0])):
      if (A[i][j] == word[m]):
          m=+1
          return wordsearch(i,j,A,word,m)


