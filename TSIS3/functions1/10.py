#Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set
def unique(l):
    unq=[]
    unq.append(l[0])
    for x in range(1,len(l)) :
        for i in range(len(unq)):
            if l[x] == unq[i]:
                break
            if i == len(unq)-1 :
                unq.append(l[x])
    return unq

l = [0,8,7,6,6,6,4,44,6,6,6,2,2,2]
print(unique(l))