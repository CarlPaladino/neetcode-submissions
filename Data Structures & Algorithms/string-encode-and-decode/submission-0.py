class Solution:

    def encode(self, strs: List[str]) -> str:
        shift = 2
        newIndexDelim = "^"
        encodedString = ""
        for word in strs:
            encodedString += str(len(word)) + newIndexDelim
            for char in word:
                encodedString += chr(ord(char) + shift)
        return encodedString

    def decode(self, s: str) -> List[str]:
        shift = 2
        newIndexDelim = "^"
        decodedWords = []
        currentWord = ""
        currentLength = ""
        charIndex = 0

        while charIndex < len(s):
            if s[charIndex] == newIndexDelim:
                for i in range(charIndex + 1, charIndex + 1 + int(currentLength)):
                    currentWord += chr(ord(s[i]) - shift)
                
                decodedWords.append(currentWord)
                currentWord = ""
                charIndex += int(currentLength)
                currentLength = ""
            else:
                currentLength += s[charIndex]
            
            charIndex += 1

        return decodedWords