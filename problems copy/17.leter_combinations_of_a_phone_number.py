from typing import *
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"],
        }
        res = []
        head = []
        a = ""
        for digit in digits:
            posible = dictionary[digit]
            for j in posible:
                pass
def tail(arrays,tail=""):
    if len(arrays)==0:
        return [tail]
    else:
        # dp_smt(arrays)
        pass

    text = [""] * len(arrays)

def make_combination(left,tail):



        








            

            
        
