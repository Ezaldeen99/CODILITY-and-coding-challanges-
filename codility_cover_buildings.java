class Solution {
    public int solution(int[] H) {
        // write your code in Java SE 8
        int length = H.length;
        int [] firstSectionMaxs = new int[length+1];
        int [] secondSectionMax = new int [length+1];
        int rightMax = 0;
        int leftMax = 0;
        for(int i = 0; i < length;i++){
            
          leftMax = Math.max(leftMax, H[i]);
          firstSectionMaxs[i + 1] = leftMax;
          
          rightMax = Math.max(rightMax, H[length - i - 1]);
          secondSectionMax[length - i - 1] = rightMax;
        }
        
        double result = Double.POSITIVE_INFINITY;
        for (int i = 0; i < length + 1; i++){
            result = Math.min(result, firstSectionMaxs[i] * i
            + secondSectionMax[i] * (length - i));
        }
        return (int) result;

    }
}
