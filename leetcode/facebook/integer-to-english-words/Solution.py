dig_names = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}

dec_names = {
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety"
}

tern_names = {
    3: "Thousand",
    6: "Million",
    9: "Billion"
}


class Solution:
    def nextWord(self, anum, i):
        n = len(anum)
        rev_i = n - 1 - i
        rev_mod3 = rev_i % 3
        next_i = i + 1
        word = []
        if rev_mod3 == 1 and anum[i] != 0:
            dec = anum[i] * 10 + anum[i + 1]
            if dec not in dec_names:
                dec -= anum[i + 1]
            else:
                next_i += 1
                rev_i -= 1
            word = [dec_names[dec]]
        elif anum[i] in dig_names:
            word = [dig_names[anum[i]]]
            if rev_mod3 == 2:
                word.append("Hundred")
        if rev_i in tern_names:
            named = False
            for i in range(i, i - 3, -1):
                if i < 0:
                    break
                if anum[i] > 0:
                    named = True
                    break
            if named:
                word.append(tern_names[rev_i])
        return word, next_i

    def numberToWords(self, num):
        anum = list(map(int, str(num)))
        if sum(anum) == 0:
            return "Zero"
        words = []
        i = 0
        while i < len(anum):
            w, i = self.nextWord(anum, i)
            words += w
        return " ".join(words).strip()
