def majority_element(nums):
    '''
    Time complexity : O(n)

    Boyer-Moore performs constant work exactly nnn times, so the algorithm runs in linear time.

    Space complexity : O(1)O(1)O(1)


    '''
    count=0
    res=0
    for num in nums:   
        if(count==0):
            res=-1
        count+=(1 if num == res else -1)
    return res
        