from unittest import result


def AllSubLists(lijst):
    result = []
    for i in range(0,len(lijst),1):
        temp = []
        for j in range(i,len(lijst),1):
            temp.append(lijst[j])
            result.append(temp[:])

    return result


print(AllSubLists([1,2,3,4,5]))

