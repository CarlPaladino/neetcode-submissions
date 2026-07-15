class Solution:
    shift = 1
    newIndexDelim = "^"
    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for word in strs:
            encodedString += str(len(word)) + self.newIndexDelim
            for char in word:
                encodedString += chr(ord(char) + self.shift)
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedWords = []
        currentWord = ""
        currentLength = ""
        charIndex = 0

        while charIndex < len(s):
            if s[charIndex] == self.newIndexDelim:
                for i in range(charIndex + 1, charIndex + 1 + int(currentLength)):
                    currentWord += chr(ord(s[i]) - self.shift)
                
                decodedWords.append(currentWord)
                currentWord = ""
                charIndex += int(currentLength)
                currentLength = ""
            else:
                currentLength += s[charIndex]
            
            charIndex += 1

        return decodedWords