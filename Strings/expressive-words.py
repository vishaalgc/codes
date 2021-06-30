class Solution(object):
    def expressiveWords(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        # if chars are not mathing break
        # count consec of s char - c1
        # count consec of word char - c2
        # if c1 < c2: BREAK
        # if c2 == c1: CONTINUE
        # if c2 < c1: get Diff. If diff is < 3 then BREAK

        st = list(s)
        mp = {}
        countConsec = 0

        minimisedStr = []
        startI = 0
        for i in range(len(st)):
            countConsec+=1
            if i+1 >= len(st) or st[i] != st[i+1]:
                mp[startI] = countConsec
                minimisedStr.append(st[i])
                countConsec = 0
                startI+=1
        outCount = 0
        for word in words:
            startIndexS = 0
            startIndexW = 0
            possible = True
            if len(word) > len(s):
                continue
            while startIndexW < len(word):
                if minimisedStr[startIndexS] != word[startIndexW]:
                    possible = False
                    break
                c1 = mp[startIndexS]
                startIndexS+=1
                c2 = 0
                for i in range(startIndexW,len(word)):
                    c2+=1
                    if i+1 >= len(word) or word[i] != word[i+1]:
                        startIndexW = i+1
                        break
                if c1 == c2:
                    continue
                if c1 < c2 or c1 < 3:
                    possible = False
                    break
                
            if possible:
                outCount+=1
        return outCount

s = "heeellooo"
words = ["hello", "hi", "helo","heello"]
x = Solution()
y = x.expressiveWords(s,words)
print(y)