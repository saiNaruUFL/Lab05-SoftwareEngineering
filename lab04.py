from stringdata import get_data
import time

#function used to find the time differenc between different linear and binaary search
#given dataset and target value to find in the dataset
def findTimes(target,dataSet):
    print("------------------")
    print("Time for Finding '" + target + "' with Linear Search: ")    
    beginTime = time.time()  #storing begin Time
    idxFound = linear_search(dataSet,target)
    print(time.time()-beginTime) #calculating time taken for algorithim based on currentTime and beginTime
    print("Idx Found:",idxFound)

    print("------------------")
    print("Time for Finding '" + target + "' with Binary Search: ")    
    beginTime = time.time()
    idxFound = binary_search(dataSet,target)
    print(time.time()-beginTime)
    print("Idx Found:",idxFound)

#simple linear search,sweeping from left of dataset to right of
#dataset to see if a target value exists. Returns the index if found
#or returns -1 if not found
def linear_search(data, target):
    for idx in range(0,len(data)):
        if(target == data[idx]):
            return idx

    return -1

#usign binary search to find target data
#data is already sorted and using lower, higher, and middle and 
#likewise changing middle value based on search space
def binary_search(data,target):
        
    lower = 0
    higher = len(data)

    while(lower < higher):
        middle = (lower + higher) // 2

        if(data[middle] == target):
            return middle

        elif(data[middle] < target):
            lower = middle + 1
        else:
            higher = middle

    return -1


if __name__ == "__main__":
    #get_data() usess function form 'stringdata.py' to collect dataset
    dataSet = get_data()

    findTimes("not_here",dataSet)
    print("")
    findTimes("mzzzz",dataSet)
    print("")
    findTimes("aaaaa",dataSet)


