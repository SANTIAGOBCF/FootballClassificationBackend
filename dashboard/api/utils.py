def positionPlayer(num):
    if num == 0:
        return "Goalkeeper"
    if num == 1:
        return "Defender"
    if num == 2:
        return "Mieldfielder"
    if num == 3:
        return "Atacker"
    else:
       return "No categorizado"
   
def generateResult(res,indices):
    answer=[]
    for i in range(4):
        ans=f"{res[indices[i]]} - {positionPlayer(indices[i])}"
        answer.append(ans)
    return answer
            
def dictToList(dictData):
    dictList=[]
    for value in dictData:
        dictList.append(value)
    return dictList 