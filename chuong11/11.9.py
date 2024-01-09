def luckey_numbers(nums):

    for i in nums:
        if i%7==0:
            return True
    return False
nums = [2,6,7,9]
result = luckey_numbers(nums)   
print(result) 

