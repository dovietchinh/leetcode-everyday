from typing import *
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack and self.min_stack[-1] < val:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
                    

if __name__ == '__main__':
    import random
    for _ in range(1000):
        array = [random.randint(1,100) for i in range(20)]
        array.sort()
        k = random.randint(1,10)
        array = array[-k:] + array[:-k]
        min_value = min(array)
        r = Solution().findMin(array)
    assert r == min_value,"Not equal {} {}".format(r,min_value)
    