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

    # for row in range(rows_count):
    #     for col in range(row+1,cols_count):
    #         if s[row] == s[col] and s[row-1] == s[col-1]:
    #             lt[row][col] = 1

    row = 0
    col = 1
    while True:
        lastCol = col
        if lastCol == cols_count:
            break
        while row < rows_count and col < cols_count:
            if s[row] == s[col] and (col-row <= 1 or lt[row+1][col-1] == 1):
                lt[row][col] = 1
            row+=1
            col+=1
        row = 0
        col = lastCol+1

    printer(lt)
    # from right top corner diagonally

    row = 0
    col = cols_count-1

    while True:
        lastCol = col
        while row < rows_count and col < cols_count:
            if lt[row][col] == 1:
                print(row,col)
                return s[row:col+1]
            row+=1
            col+=1
        row = 0
        col = lastCol-1

s = "bebdeeedaddecebbbbbabebedc"
print(longestPalindrome(s))
