class Solution {
    public void countTrailingZeros(int[][] grid, int numRows, int[] trailingZerosEnd) {
        for (int i = 0; i < numRows; i++) {
            int firstOneIdx = -1;
            for (int j = numRows - 1; j >= 0; j--) {
                if (grid[i][j] == 1) {
                    firstOneIdx = j;
                    break;
                }
            }
            trailingZerosEnd[i] = firstOneIdx;
        }
    }

    public int minSwaps(int[][] grid) {
        int numRows = grid.length;
        int[] trailingZerosEnd = new int[numRows];
        int swaps = 0;

        countTrailingZeros(grid, numRows, trailingZerosEnd);

        for (int i = 0; i < numRows; i++) {
            int idxToSwap = i;
            while (idxToSwap < numRows && trailingZerosEnd[idxToSwap] > i) {
                idxToSwap++;
            }

            if (idxToSwap == numRows)
                return -1;

            while (idxToSwap > i) {
                int temp = trailingZerosEnd[idxToSwap];
                trailingZerosEnd[idxToSwap] = trailingZerosEnd[idxToSwap - 1];
                trailingZerosEnd[idxToSwap - 1] = temp;

                swaps++;
                idxToSwap--;
            }
        }
        return swaps;
    }
}