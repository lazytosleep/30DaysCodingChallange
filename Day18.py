'''
Min path sum:
'''

def minPathSum(table):
    memoizeArray = [ [ 0 for j in range(len(table[0])) ] for i in range(len(table)) ]
    minVal = 0

    for i in range(0, len(table)):
        cols = table[i]
        for j in range(0, len(cols)):
            if i ==0 and j == 0:
                memoizeArray[i][j] = table[i][j]
            elif i == 0:
                memoizeArray[i][j] = memoizeArray[i][j-1]  + table[i][j]
            elif j == 0:
                memoizeArray[i][j] = memoizeArray[i-1][j]  + table[i][j]
            else:
                memoizeArray[i][j] = min(memoizeArray[i][j-1], memoizeArray[i-1][j]) + table[i][j]
            minVal = memoizeArray[i][j]
    return minVal


print(minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))


    



