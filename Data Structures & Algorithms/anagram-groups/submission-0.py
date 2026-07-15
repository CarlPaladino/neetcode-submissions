class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrings = {}
        for currStr in strs:
            currSorted = ''.join(sorted(currStr))
            if currSorted in sortedStrings:
                sortedStrings[currSorted].append(currStr)
            else:
                sortedStrings[currSorted] = [currStr]
        
        return list(sortedStrings.values())