class Solution:
    def smallestNumber(self, num: int) -> int:
        negative = num < 0
        digits = list(str(abs(num)))
        digits.sort(reverse=negative) 
        if not negative and digits[0] == '0':
            for i in range(1, len(digits)):
                if digits[i] != '0':
                    digits[0], digits[i] = digits[i], digits[0]
                    break
        smallest = int("".join(digits))
        return -smallest if negative else smallest