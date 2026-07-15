class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        allCharsS = {}

        for i in range(len(s)):
            if s[i] in allCharsS:
                continue
            else:
                thisCharCounter = 1
                for j in range(i + 1, len(s)):
                    if s[j] == s[i]:
                        thisCharCounter += 1
                allCharsS[s[i]] = thisCharCounter

        allCharsT = {}
        for i in range(len(t)):
            if t[i] in allCharsT:
                continue
            thisCharCounter = 1
            for j in range(i + 1, len(t)):
                if t[j] == t[i]:
                    thisCharCounter += 1
            allCharsT[t[i]] = thisCharCounter
            
            if t[i] not in allCharsS or allCharsS[t[i]] != allCharsT[t[i]]:
                return False
        return True