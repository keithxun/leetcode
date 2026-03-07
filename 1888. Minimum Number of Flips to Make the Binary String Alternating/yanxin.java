class Solution {
    public int minFlips(String s) {
        int n = s.length();
        int minFlips = n;
        int[] mismatch = { 0, 0 };

        for (int i = 0; i < n; i++) {
            mismatch[(s.charAt(i) ^ i) & 1]++;
        }

        if (mismatch[0] == 0 || mismatch[1] == 0)
            return 0;

        for (int i = 0; i < n; i++) {
            mismatch[(s.charAt(i) ^ i) & 1]--;
            mismatch[(s.charAt(i) ^ (n + i)) & 1]++;
            minFlips = Math.min(minFlips, Math.min(mismatch[0], mismatch[1]));
        }

        return minFlips;
    }
}