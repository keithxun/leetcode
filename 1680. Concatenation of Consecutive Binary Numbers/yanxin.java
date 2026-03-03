import java.math.BigInteger;

class Solution {
    public int concatenatedBinary(int n) {
        int mudulo = 1000000007;
        long decimalValue = 0;

        for (int i = 1; i <= n; i++) {
            BigInteger bigI = BigInteger.valueOf(i);
            int binaryLength = bigI.bitLength();
            long shiftedNumber = decimalValue << binaryLength;
            decimalValue = (shiftedNumber + i) % mudulo;
        }

        return (int) decimalValue;
    }
}