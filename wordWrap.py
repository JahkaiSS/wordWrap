myLongWord = "adsfajdsfpoajdsfpojdspfojdsfijdsapoifjoisdfjoisdjfoiadjfoidjsfisdjfopijdiofj165161561651818181"
userWord = input("Enter a large word here: ")

lettersPerLine = 40

startIndex = 0
endIndex = lettersPerLine

count = 0

endCount = len(userWord)/lettersPerLine

while count <= int(endCount):
    print(userWord[startIndex:endIndex])
    startIndex += lettersPerLine
    endIndex += lettersPerLine
    count += 1
    
