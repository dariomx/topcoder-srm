import static java.lang.Math.abs;

class Solution {
    private int binSum(int a, int b) {
        int sum, carry;
        do {
            sum = a ^ b;
            carry = a & b;
            a = sum;
            b = carry << 1;
        } while (carry != 0);
        return sum;
    }

    public int getSum(int a, int b) {
        a = a < 0? binSum(~abs(a), 1) : a;
        b = b < 0? binSum(~abs(b), 1) : b;
        return binSum(a, b);
    }
}