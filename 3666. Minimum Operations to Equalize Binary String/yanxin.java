class Solution {
    public int calNumZeros(String s, int n) {
        int zeros = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '0') {
                zeros++;
            }
        }

        return zeros;
    }

    public int calMinNumOperations (int zeros, int k) {
        int numOperations = (int) Math.ceil((double) zeros / k);

        if (k % 2 == 1) {
            if ((zeros % 2) != (numOperations % 2)) {
                numOperations++;
            }
        }

        return numOperations;
    }
    
    public int minOperations(String s, int k) {
        int n = s.length();
        int zeros = calNumZeros(s, n);

        if (zeros == 0) return 0;

        if (k == n) {
            return (zeros == n) ? 1 : -1;
        }

        // if k is even, total flips (numOperations*k) is always even. hence zeros must be even
        if ((k % 2 == 0) && (zeros % 2 == 1)) return -1;

        // if k is odd, then parity is determined by numOperations.
        // parity of numOperations*k has to be the same as parity of zeros
        int numOperations = calMinNumOperations(zeros, k);
       
        // each index can only be flipped at most numOperations times.
        // each operation can only flip an index at most once
        int unchanged = n - k;
        while (true) {
            boolean validConstraints = false;
            if (numOperations % 2 == 0) {
                validConstraints = numOperations * unchanged >= zeros;
            } else {
                validConstraints = numOperations * unchanged >= (n-zeros);
            }

            if (validConstraints) return numOperations;

            numOperations++;
            if (k % 2 == 1) {
                if ((zeros % 2) != (numOperations % 2)) {
                    numOperations++;
                }
            }
        }
    }
}