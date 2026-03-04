class Solution {
    public int numSpecial(int[][] mat) {
        int rowLength = mat.length;
        int colLength = mat[0].length;
        int[] rowOnes = new int[rowLength];
        int[] colOnes = new int[colLength];

        for (int r = 0; r < rowLength; r++) {
            for (int c = 0; c < colLength; c++) {
                if (mat[r][c] == 1) {
                    rowOnes[r]++;
                    colOnes[c]++;
                }
            }
        }

        int special = 0;
        for (int r = 0; r < rowLength; r++) {
            for (int c = 0; c < colLength; c++) {
                if (mat[r][c] == 1 && rowOnes[r] == 1 && colOnes[c] == 1) {
                    special++;
                }
            }
        }

        return special;
    }
}