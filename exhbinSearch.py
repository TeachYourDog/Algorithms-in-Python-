def exhSearch(num):
    j=0
    for i in range(1,101):
        if num == i:
            return j 
           
        else: 
            j += 1 


def evenMid(binmax, binmin):
        value = int(binmax + binmin)
        if value % 2 == 0:
            binmid = value / 2
            return binmid
        else: 
            binmid = (value-1) / 2
            return binmid


def updateValues(binmax, binmin, binmid, num):

    if num > binmid:
        binmax = binmax
        binmin = binmid 
        binmid = evenMid(binmax, binmin)
        return binmax, binmin, binmid
    else: 
        binmax = binmid
        binmin = binmin 
        binmid = evenMid(binmax, binmin)
        return binmax, binmin, binmid 


def binCheck(binmax, binmin, binmid, num):
    if binmax == num or binmin == num or binmid == num:
        return True
    else: 
        
        return False


def binSearch(num, searchSize): 
    binmax = searchSize
    binmin = 1 
    binmid = evenMid(binmax, binmin)
    j = 1
    
    for i in range(searchSize):

        if binCheck(binmax, binmin, binmid, num) == True:
            return j 

        else: 
            values = updateValues(binmax, binmin, binmid, num)
            binmax = values[0]
            binmin = values[1]
            binmid = values[2]
            j += 1
            i += 1


def results(num, searchSize):
    factor = exhSearch(num) / binSearch(num, searchSize)
    print("The exhaustive search found ", num, " in ", exhSearch(num), " steps. The binary search found ", num, " in ", binSearch(num, searchSize), " steps. The binary search is ", factor, " times faster than the exhaustive search.")


num = input("What integer do you want to find?")
searchSize = input("What is the size of the set of integers you want to search?")

results(int(num), int(searchSize))