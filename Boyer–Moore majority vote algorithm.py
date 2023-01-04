def majority_element(nums):
    '''
    Time complexity : O(n)
    Boyer-Moore performs constant work exactly n times, so the algorithm runs in linear time.
    Space complexity : O(1)
    '''
    candidate = 0 # initalizing candidate as a majority element
    count = 0
    candidate_count =0
    n = len(nums)
    for i in range(n):   
        if(candidate_count == 0):
          candidate = nums[i]
          candidate_count+=1
        else:
          if (nums[i] == candidate):
            candidate_count+=1
          else:
            candidate_count-=1
#checking if candidate occurs more than N/2 times
    for i in range (n):
        if (nums[i] == candidate):
            count += 1
              
    if (count > n // 2):
        return candidate
    else:
        return -1  
