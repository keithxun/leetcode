class Solution {
    public int largestSubmatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[] histogram = new int[n];
        int maxArea = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (matrix[r][c] != 0) {
                    histogram[c]++;
                } else {
                    histogram[c] = 0;
                }
            }

            int[] sorted = histogram.clone();
            Arrays.sort(sorted);
            for (int c = 0; c < n; c++) {
                int height = sorted[c];
                int width = n - c;
                maxArea = Math.max(maxArea, width*height);
            }
        }
        return maxArea;
    }
}