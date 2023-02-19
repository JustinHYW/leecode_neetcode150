"""

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

"""

class Solution:
    def myAtoi(self, s: str) -> int:
        """
        build integer one at a time
        3 cases
            num is less than 32 bit
            num is more than 32 bit
            num is equal to 32 bit


        """
        INT_MAX = pow(2, 31)-1
        INT_MIN = -pow(2, 31)
        sign = 1
        res = 0
        index = 0
        n =len(s)


        while index < n and s[index] == " ":
            index+=1

        if index < n and s[index] == "+":
            sign = 1
            index +=1
        elif index < n and s[index] == "-":
            sign = -1
            index +=1

        while index < n and s[index].isdigit():
            digit = int(s[index])

            if(( res > INT_MAX // 10) or (res == INT_MAX//10 and digit > INT_MAX % 10)) :
                return INT_MAX if sign == 1 else INT_MIN

            res = 10 * res + digit #pay attention
            index += 1

        return sign * res