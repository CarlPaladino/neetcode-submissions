class Solution:
    def isPalindrome(self, s: str) -> bool:
        sAlpha = ""
        reversedStringAlpha = ""
        for i in range(len(s) - 1, -1, -1):
            if str.isalnum(s[i]):
                reversedStringAlpha += s[i].lower()

        for i in range(0, len(s) - 1, 1):
            if str.isalnum(s[i]):
                sAlpha += s[i].lower()

        for i in range(len(sAlpha)):
            if sAlpha[i] == reversedStringAlpha[i]:
                continue
            else:
                return False

        return True