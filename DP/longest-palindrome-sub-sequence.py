def longestPalindrome( s):
    """
    :type s: str
    :rtype: str
    """
    def printer(lt):
        for i in range(len(lt)):
            x = ''
            for j in range(len(lt[i])):
                x += str(lt[i][j])+" "
            print(x)

    # base case
    if s == s[::-1]:
        return s
    
    rows_count = len(s)
    cols_count = rows_count
    
    lt = [[0 for x in range(cols_count)] for x in range(rows_count)]
    
    # Set all diagonals 1
    rowCol = 0
    while rowCol < rows_count:
        lt[rowCol][rowCol] = 1
        rowCol+=1

    row = 0
    col = 1
    while True:
        lastCol = col
        if lastCol == cols_count:
            break
        while row < rows_count and col < cols_count:
            if s[row] == s[col]:
                lt[row][col] = lt[row+1][col-1]+2
            else:
                lt[row][col] = max(lt[row+1][col],lt[row][col-1])
            row+=1
            col+=1
        
        row = 0
        col = lastCol+1

    printer(lt)
    
    return lt[0][cols_count-1]

s = "bebdeeedaddecebbbbbabebedc"
s = "agbdba"
print(longestPalindrome(s))
