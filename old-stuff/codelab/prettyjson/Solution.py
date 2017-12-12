class Solution:
    def val2str(self, val):
        qstr = str(val)
        if type(val) == str:
            qstr = "\"" + qstr + "\""
        return qstr

    def addLine(self, val, depth, res):
        indent = "".join(["\t"] * depth)
        res.append(indent + str(val))

    def pretty(self, json, depth, res):
        if type(json) == dict:
            self.addLine("{", depth, res)
            for k in json:
                line = k + ":"
                if type(json[k]) not in [list, dict]:
                    line += self.val2str(json[k])
                self.addLine(line, depth + 1, res)
                if type(json[k]) in [list, dict]:
                    self.pretty(json[k], depth + 1, res)
            self.addLine("}", depth, res)
        elif type(json) == list:
            self.addLine("[", depth, res)
            for e in json:
                self.pretty(e, depth + 1, res)
            self.addLine("]", depth, res)
        else:
            self.addLine(self.val2str(json), depth, res)

    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        res = []
        self.pretty(A, 0, res)
        return res

def myPrint(ss):
    for s in ss:
        print(s)

myPrint(Solution().prettyJSON({"id":100,"firstName":"Jack","lastName":"Jones","age":12}))
