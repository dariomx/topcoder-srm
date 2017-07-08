class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        sen_len = sum(map(len, sentence)) + len(sentence)
        i, j, k = 0, 0, 0
        num_words = len(sentence)
        while i < rows:
            if j == 0:
                folds = cols / sen_len
                if folds > 0:
                    k += folds * num_words
                    j += folds * sen_len - 1
            spc_len = 1 if j > 0 else 0
            word_len = spc_len + len(sentence[k % num_words])
            if j + word_len <= cols:
                j += word_len
                k += 1
            else:
                i += 1
                j = 0
                if k % num_words == 0:
                    return (rows / i) * (k / num_words) + \
                        self.wordsTyping(sentence, rows % i, cols)
        return k / num_words


sentence, rows, cols = ["a", "bcd", "e"], 3, 6
sentence, rows, cols = ["i", "had", "apple", "pie"], 4, 5
sentence, rows, cols = ["f", "p", "a"], 8, 7
sentence, rows, cols = ["a", "bcd"], 20000, 20000
print(Solution().wordsTyping(sentence, rows, cols))