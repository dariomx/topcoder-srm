class Solution:
    def multiply(self, num1, num2):
        arr1 = list(map(int, reversed(num1)))
        arr2 = list(map(int, reversed(num2)))
        n1 = len(arr1)
        n2 = len(arr2)
        if n2 > n1:
            arr1, arr2 = arr2, arr1
            n1, n2 = n2, n1
        arr3 = [0] * (n1 + n2)
        rem = 0
        for j in range(n2):
            x = arr2[j]
            for i in range(n1):
                y = arr1[i]
                tmp = rem + x * y + arr3[j + i]
                arr3[j + i] = tmp % 10
                rem = tmp // 10
            arr3[j + n1] = rem
            rem = 0
        mul = ''.join(map(str, reversed(arr3)))
        mul = mul.lstrip("0")
        return "0" if not mul else mul
