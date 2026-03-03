class Solution {
    public int minPartitions(String n) {
        int minNum = 0;
        for (int i = 0; i < n.length(); i++) {
            minNum = Math.max(minNum, n.charAt(i) - '0');
        }

        return minNum;
    }
}