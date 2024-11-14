def find_five(num):
    for n in num:
        if n == 5:
            print("Found 5")
            break
    else:
            print("Not found")
            
find_five([1,2,3,4,4,5,44])


def find_fivess(nums):
    for num in nums:
        if num == 5:
            print("Found 5")
            break
    else:
        print("5 is not on the list")
        
find_fivess([1,2,3,4,4,5,5,5,4])