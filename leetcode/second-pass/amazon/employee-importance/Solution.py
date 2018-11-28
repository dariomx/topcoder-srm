class Solution:
    def getImportance(self, employees, id):
        imp = dict()
        sub = dict()
        for emp in employees:
            imp[emp.id] = emp.importance
            sub[emp.id] = emp.subordinates

        def rec(id):
            return imp[id] + sum(map(rec, sub[id]))

        return rec(id)
