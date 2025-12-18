def get_even(nums):
    even=[]
    for i in nums:
        if i%2==0:
            even.append(i)
    return even
print(get_even([1,2,3,4,5,6,7,8]))