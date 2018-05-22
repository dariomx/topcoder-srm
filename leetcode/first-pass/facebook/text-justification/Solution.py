class Solution:
    def justify(self, line, width, maxWidth):
        n = len(line)
        spc = [1] * n
        spc[n - 1] = 0
        cont = True
        while cont:
            for i in range(n - 1):
                if width == maxWidth:
                    cont = False
                    break
                spc[i] += 1
                width += 1
        pad_word = lambda i: line[i] + (' ' * spc[i])
        return "".join(map(pad_word, range(n)))

    def left_justify(self, line, maxWidth):
        return ' '.join(line).ljust(maxWidth)

    def fullJustify(self, words, maxWidth):
        text = []
        n = len(words)
        line = []
        width = 0
        for i in range(n):
            w = words[i]
            left_spc = int(len(line) > 0)
            if left_spc + len(w) + width > maxWidth:
                text.append((line, width))
                line = []
                width = 0
                left_spc = 0
            line.append(w)
            width += left_spc + len(w)
        if line:
            text.append((line, width))
        m = len(text)
        for i in range(m - 1):
            line, width = text[i]
            if len(line) > 1:
                text[i] = self.justify(line, width, maxWidth)
            else:
                text[i] = self.left_justify(line, maxWidth)
        text[m - 1] = self.left_justify(text[m - 1][0], maxWidth)
        return text

