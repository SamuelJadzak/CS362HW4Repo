def listAvg(list):
    average = 0
    for x in list:
        average = x + average
    if(average != 0):
        average = average/len(list)
        return average
    else:
        raise ValueError("the list is empty")
