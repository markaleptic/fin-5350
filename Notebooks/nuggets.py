nuggetVarOne = 6
nuggetVarTwo = 9
nuggetVarThree = 20
CONST_NUGGET_ONE = nuggetVarOne
CONST_NUGGET_TWO = nuggetVarTwo
CONST_NUGGET_THR = nuggetVarThree

potentialSolutions = []


def main():
  maxCount = 1000 
  for x in range(1, maxCount):
    if not findNuggets(x):
      potentialSolutions.append(str(x))

  if (len(potentialSolutions) > 0):
    print ("The maxium number of McNuggets you cannot purchase with %d, %d, and %d McNuggets per purchase is %s" % (nuggetVarOne, nuggetVarTwo, nuggetVarThree, potentialSolutions[len(potentialSolutions)-1]))
  else:
    print("There was an error. Please try again.")

def findNuggets(remainder):
  nuggetVarOne    = remainder - CONST_NUGGET_ONE
  nuggetVarTwo    = remainder - CONST_NUGGET_TWO
  nuggetVarThree  = remainder - CONST_NUGGET_THR
  
  if nuggetVarOne == 0:
    return True
  elif nuggetVarTwo == 0:
    return True
  elif nuggetVarThree == 0:
    return True
  elif nuggetVarOne < 0:
    return False
  return findNuggets(nuggetVarOne) or findNuggets(nuggetVarTwo) or findNuggets(nuggetVarThree)


main()
