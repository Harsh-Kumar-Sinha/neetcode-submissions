class Solution:

    def create_valid_text(self, s:str) -> str:
        data = ""
        for i in s:
            if i.isalpha() or i.isnumeric():
                data += i

        return data.lower()

    def isPalindrome(self, s: str) -> bool:
        data = self.create_valid_text(s)
        start, end = 0, len(data)-1

        if len(data) < 2:
            return True

        while start < end:
            if data[start] != data[end]:
                return False

            start += 1
            end -= 1 
        return True

        