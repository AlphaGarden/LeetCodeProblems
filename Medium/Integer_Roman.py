# Given an integer , convert it to a roman numeral .
#
# Input is guaranteed to be within the range from 1 to 3999.
#
class Solution(object):
    def valueOfDigit0(self,num):
        dict0 = {'0': "", '1': "I", '2': "II", '3': "III", '4': "IV",
                 '5': "V", '6': "VI", '7': "VII", '8': "VIII",'9': "IX"}
        return dict0[num]
    def valueOfDigit1(self,num):
        dict1 = {'0': "", '1': "X", '2': "XX", '3': "XXX", '4': "XL",
                 '5': "L", '6': "LX", '7': "LXX", '8': "LXXX", '9': "XC"}
        return dict1[num]
    def valueOfDigit2(self,num):
        dict2 = {'0':"",'1':"C",'2':"CC",'3':"CCC",'4':"CD",
                 '5':"D",'6':"DC",'7':"DCC",'8':"DCCC",'9':"CM"}
        return dict2[num]
    def valueOfDigit3(self,num):
        dict3 = {'0':"",'1':"M",'2':"MM",'3':"MMM"}
        return dict3[num]
    # TODO
    # def val(self,num):
    #     func0 = lambda x:self.valueOfDigit0(x)
    #     funclist = {'-1':func0}
    #     return lambda x:funclist[num]
    def intToRoman(self, s):
        res =''
        str_s = str(s)
        if str_s == '0':
            return res
        for i in range(-1,-(len(str_s)+1),-1):
            if i == -1:
                res = self.valueOfDigit0(str_s[-1])+res
            elif i==-2:
                res = self.valueOfDigit1(str_s[-2])+res
            elif i==-3:
                res = self.valueOfDigit2(str_s[-3])+res
            elif i==-4:
                res = self.valueOfDigit3(str_s[-4])+res
            else:
                print 'error on for-loop'
        return res



testnum='3009'
solution = Solution()
print solution.intToRoman(testnum)