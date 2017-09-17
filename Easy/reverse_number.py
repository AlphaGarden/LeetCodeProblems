class Solution(object):
    def reverse(self, x):
        x_str = str(abs(x))
        signed = 1 if x > 0 else -1
        reversed_num = int(x_str[::-1])
        if signed > 0:
            if reversed_num > 0x7FFFFFFF:
                return 0
            else:
                return reversed_num
        else:
            if -reversed_num < -0x80000000:
                return 0
            else:
                return int(-reversed_num)

s = Solution()
print(s.reverse(-2147483648))
print(-8463847412<-0x80000000)
