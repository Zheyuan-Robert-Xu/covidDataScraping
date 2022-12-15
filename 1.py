def solution(S):
    #required variables
    count = 0
    result = -1
    fragLength = 0
    fragment = []
    #Loops through each letter in given string 'S'
    for i in range(len(S)):
        #If it is an upper case letter
        if S[i].isupper():
            #Gets the lower case of it
            oppCase = S[i].lower()
            #Checks if it is in 'S'
            if oppCase in S[i:] or oppCase.lower() in fragment or oppCase.upper() in fragment:
                #If yes increments count by 1
                count += 1
                fragment.append(oppCase)
            else:
                #Otherwise sets count to 0
                count = 0
                if result != -1:
                    fragLength = result
                    fragment.clear()
    elif S[i].islower():
        #If the letter is lower case letter
        #Gets the upper case of it
        oppCase = S[i].upper()
        #Checks if oppCase is in 'S'
        if oppCase in S[i:] or oppCase.lower() in fragment or oppCase.upper() in fragment:
            #If yes increments count by
            count += 1
            fragment.append(oppCase)
        else:
            #Otherwise sets it to 0
            count = 0
            if result != -1:
                fragLength = result
            fragment.clear()
    #If count is above 1 (atleast 2 subsequent elements are found)
    if count > 1:
        result = count
        #Gets the shortest fragment length
    if fragLength < result and fragLength > 0:
        result = fragLength

#returns result after for loop is executed completely
    return result