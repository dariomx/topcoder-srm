class Solution:
    def lemonadeChange(self, bills):
        bill_val = [5, 10, 20]
        bill_idx = {5: 0, 10: 1, 20: 2}
        bill_cnt = [0, 0, 0]
        min_bill, max_bill = 0, len(bill_val) - 1
        price = 5
        for pay in bills:
            bill_cnt[bill_idx[pay]] += 1
            rem = pay - price
            bill = max_bill
            while rem > 0 and bill >= min_bill:
                if bill_cnt[bill] == 0 or bill_val[bill] > rem:
                    bill -= 1
                else:
                    rem -= bill_val[bill]
                    bill_cnt[bill] -= 1
            if rem > 0:
                return False
        return True

