class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        m = 1
        while i<len(s) and s[i] == ' ':
            i+=1
        
        if i<len(s) and (s[i] == '+' or s[i] == '-'):
            m = int(s[i] + '1')
            i+=1
        
        num_start = i
        
        while i<len(s) and ord(s[i])>=48 and ord(s[i])<=57:
            i+=1
        
        if i == num_start:
            return 0
        
        number = m*int(s[num_start:i])
        
        if number < (-1*(2**31)):
            return -1*(2**31)
        
        elif number>(2**31)-1:
            return (2**31)-1
        
        else:
            return number