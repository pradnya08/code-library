class Solution(object):
   

    def addStrings(self, num1, num2):
        res = []
        pos1 = len(num1) - 1
        pos2 = len(num2) - 1
        carry = 0
                while pos1 >= 0 or pos2 >= 0 or carry == 1:
            digit1 = digit2 = 0
            if pos1 >= 0:
                digit1 = ord(num1[pos1]) - ord('0')
            if pos2 >= 0:
                digit2 = ord(num2[pos2]) - ord('0')
            res.append(str((digit1 + digit2 + carry) % 10))
            carry = (digit1 + digit2 + carry) / 10
            pos1 -= 1
            pos2 -= 1

        return ''.join(res[::-1])