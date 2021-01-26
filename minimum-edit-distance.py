#code from Stackoverflow (https://stackoverflow.com/questions/53015099/calculating-minimum-edit-distance-for-unequal-strings-python)
def minimumEditDistance(first, second): 
    
    #Creating numpy ndarray( initialized with 0 of dimension of size of both strings
    
    matrix = np.zeros((len(first)+1,len(second)+1), dtype=np.int)
    
    
    # Cross relation loop through each character of each string with each other and
    # fill the respective index of matrxi (row,column)
    
    for i in range(len(first)+1): 
        for j in range(len(second)+1): 
            
            #First doing the boundary value analysis, if first or second string is empty so directly adding insertion cost
            if i == 0:  
                matrix[i][j] = j  
            #Second case
            elif j == 0: 
                matrix[i][j] = i
            else: 
                matrix[i][j] = min(matrix[i][j-1] + 1,  
                                   matrix[i-1][j] + 1,        
                                   matrix[i-1][j-1] + 2 if first[i-1] != second[j-1] else matrix[i-1][j-1] + 0)     
                                   # Adjusted the cost accordinly, insertion = 1, deletion=1 and substitution=2
    return matrix[len(first)][len(second)]  # Returning the final
