class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<=1:
            return s
        zigzag = ['']*numRows
        for index,c in enumerate(s):
            remain = index%(2*numRows-2)
            if remain <= numRows-1:
                zigzag[remain] += c
            else:
                row = 2*numRows-2-remain
                zigzag[row] += c
        r = ''
        for i in zigzag:
            r += i
        
        return r


if __name__ == '__main__':
    r = Solution().convert("ABPAYPALISHIRINGC",3)
    r = Solution().convert("PAYPALISHIRING",4)
    r = Solution().convert("A",1)
    