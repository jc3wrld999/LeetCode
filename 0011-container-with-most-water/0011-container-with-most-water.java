// import Math.*;
class Solution {
    public int maxArea(int[] height) {
        int l = 0;
        int r = height.length -1;
        int res = 0;
        while(l < r){
            int w = (r - l) * Math.min(height[l], height[r]);
            if(height[l] < height[r]){
                l += 1;
            }else{
                r -= 1;
            }
            res = Math.max(res, w);
        }
        return res;
    }
}