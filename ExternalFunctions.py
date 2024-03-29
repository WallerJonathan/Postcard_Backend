import json
import random


# pre-conditions: pass in the dictionary and file path of the json file
# post-conditions: creates a json file in the file path
def makeJson(myDict, filePath):
    try:
        with open(filePath, "w") as json_file:
            json.dump(myDict, json_file, indent=4)
        print(f"The JSON file '{filePath}' has been created or written to.")
    except Exception as e:
        print(f"An error occurred: {e}")


# pre-conditions: takes in a list
# post-condtions: shuffles the list (but doesn't return the list)
def shuffleList(L):
    random.shuffle(L)

# pre-conditions: takes in a list
# post-conditions: 
# This function shuffles each sublist to randomize the order of elements, 
# and then splits these shuffled sublists into new sublists, each containing exactly three elements. 
# The function accumulates these groups of three into a new sublist for each original sublist, 
# and appends these new sublists to the resultList. The function returns resultList, which is a list of lists of lists, 
# where each inner-most list contains exactly three elements.
def randomSplitIntoDays(L):
    resultList = []
    for sublist in L:
        random.shuffle(sublist)
        newSubList = []
        while len(sublist) >= 3:  # As long as there are at least 3 elements
            tempSubList = sublist[:3]  # Take the first 3 elements
            newSubList.append(tempSubList)
            sublist = sublist[3:]  # Update the sublist excluding the first 3 elements
        resultList.append(newSubList)
    return resultList
