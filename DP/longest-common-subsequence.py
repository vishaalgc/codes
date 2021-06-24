def longestCommonSubsequence(text1,text2):
    """
    :type text1: str
    :type text2: str
    :rtype: int
    """
    def printer(lt):
        for i in range(len(lt)):
            x = ''
            for j in range(len(lt[i])):
                x += str(lt[i][j])+" "
            print(x)

    lt = []
    eachRow = [0]*(len(text1)+1)
    for i in text2:
        lt.append(list(eachRow))
    lt.append(list(eachRow))

    for row in range(1,len(lt)):
        for col in range(1,len(lt[row])):
            if text1[col-1] == text2[row-1]:
                lt[row][col] = lt[row-1][col-1]+1
            else:
                lt[row][col] = max(lt[row-1][col],lt[row][col-1])
    
    return lt[len(text2)][len(text1)]

A = "abcba"
B= "abcbcba"

print(longestCommonSubsequence(A,B))