# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        sA = list(map(str, numbers))
        B = self.bubble(sA)
        return int(''.join(B))

    def compare(self, a, b):
        if a + b >= b + a:
            return True
        else:
            return False

    def bubble(self, arr):
        n = len(arr)
        for i in range(1, n):
            for j in range(n - i):
                if self.compare(arr[j], arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


A=[3,321,32]
sol=Solution()
print(sol.PrintMinNumber(A))
