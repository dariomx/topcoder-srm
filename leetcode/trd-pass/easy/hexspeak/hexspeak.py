class Solution:
    def toBaseRev(self, x, base):
        while x > 0:
            x, r = divmod(x, base)
            yield r

    def toHexspeak(self, num: str) -> str:
        hexEnc = {0: "O", 1: "I", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E",
                  15: "F"}
        ans = ""
        for h in self.toBaseRev(int(num), base=16):
            enc = hexEnc.get(h, None)
            if enc is None:
                return "ERROR"
            else:
                ans += enc
        return ans[::-1]
