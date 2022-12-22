# Depth first search algorithm to find the permutations of given string
result = []
def dfs(nums):
  if(len(nums) == 1):
    return [nums[:]]
  
  for i in range(0,len(nums)):
    n = nums.pop()
    permutations = dfs(nums)
    print(permutations)
    for perm in permutations:
      print((perm))
      perm = [sum(perm)+ n]
      
    result.extend(permutations)
    nums.append(n)
  return result


nums=[1,2,4,5]
n= len(nums)
dfs(nums)