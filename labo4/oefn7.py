
def checkSublist(kleinseList,groteList):
    if len(kleinseList) == 0:
        return True
    elif len(kleinseList) == 1:
        if kleinseList[0] in groteList:
            return True
    else:
        if kleinseList[0] in groteList:
            for i in range(0,len(kleinseList),1):
                if (groteList[groteList.index(kleinseList[0]+i)]) != kleinseList[i]:
                    return False
            return True
        else:
            return False


klein = [2,4]
groot = [1,2,3,4]
print(checkSublist(klein,groot))