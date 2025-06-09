class Solution(object):
    def romanToInt(self, s):
        rm = {
            1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C',
            500: 'D', 1000: 'M', 4: 'IV', 9: 'IX',
            40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'
        }

        n = s
        roman = ""
        temp = ""

        if n >= 1000:
            thousandOccur = n // 1000
            temp = rm[1000] * thousandOccur
            roman += temp
            temp = ""
            n -= 1000 * thousandOccur

        if n >= 900:
            roman+=rm[900]
            n-=900

        if n >= 500:
                rem = (n - 500) // 100
                temp = 'D' + rm[100] * rem
                roman += temp
                temp = ""
                n -= 500 + 100 * rem

        if n >= 400:
            roman+=rm[400]
            n-=400

        if n >= 100:
            hundredOccur = n // 100
            temp = rm[100] * hundredOccur
            roman += temp
            temp = ""
            n -= 100 * hundredOccur

        if n  >= 90:
            roman+=rm[90]
            n-=90

        if n >= 50:
                rem = (n - 50) // 10
                temp = rm[50] + rm[10] * rem
                roman += temp
                temp = ""
                n -= 50 + 10 * rem

        if n >= 40:
            roman+=rm[40]
            n-=40

        if n >= 10:
            temOccur = n // 10
            temp = rm[10] * temOccur
            roman += temp
            temp = ""
            n -= 10 * temOccur
        
        if n >= 9:
            roman+=rm[9]
            n-=9
        
        if n >= 5:
                rem = n - 5
                temp = rm[5] + rm[1] * rem
                roman += temp
                temp = ""
                n -= 5 + rem

        if n == 4:
            roman += rm[4]
            n -= 4

        if n >= 1:
            rem = n
            temp = rm[1] * rem
            roman += temp
            n -= rem

        print(roman)

s1 = Solution()
