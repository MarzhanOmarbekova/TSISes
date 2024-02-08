#Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    id = 0
    search = 0
    found = 0
    for i in range(id,len(nums)) :
        if i!= len(nums)-1:
            if nums[i] == search :
                id = i+1
                found +=1
                if found == 2:
                    search = 7 
                if found == 3:
                    return True
    return False
        


print(spy_game([1,2,4,0,0,7,5])) #--> True
print(spy_game([1,0,2,4,0,5,7])) #--> True
print(spy_game([1,7,2,0,4,5,0])) #--> False