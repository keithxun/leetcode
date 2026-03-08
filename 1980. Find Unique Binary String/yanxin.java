import java.util.*;

class Solution {
    public String findDifferentBinaryString(String[] nums) {
        Set<Integer> integersIncluded = new HashSet<Integer>();

        for (String n : nums) {
            integersIncluded.add(Integer.parseInt(n, 2));
        }

        for (int i = 0; i <= nums.length; i++) {
            if (!integersIncluded.contains(i)) {
                String uniqueInt = Integer.toBinaryString(i);
                int numZeros = nums.length - uniqueInt.length();
                uniqueInt = "0".repeat(numZeros) + uniqueInt;
                return uniqueInt;
            }
        }

        return "";
    }
}

// O(n), Cantor's Diagonal Argument
// StringBuilder ans = new StringBuilder();
// for (int i = 0; i < nums.length; i++) {
// Character curr = nums[i].charAt(i);
// ans.append(curr == '0' ? '1' : '0');
// }
// return ans.toString();