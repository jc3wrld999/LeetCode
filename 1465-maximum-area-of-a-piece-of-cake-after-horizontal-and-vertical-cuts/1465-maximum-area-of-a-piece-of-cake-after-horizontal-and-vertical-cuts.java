import java.util.Arrays;

class Solution {
    public int maxArea(int h, int w, int[] hc, int[] vc) {
        Arrays.sort(hc);
        Arrays.sort(vc);
        int max_h = Math.max(hc[0], h - hc[hc.length - 1]);
        int max_v = Math.max(vc[0], w - vc[vc.length - 1]);
        for(int i = 1;i < hc.length; i ++) {
            max_h = Math.max(hc[i] - hc[i-1], max_h);
        }
        for(int i = 1;i < vc.length; i ++) {
            max_v = Math.max(vc[i] - vc[i-1], max_v);
        }
        return (int)((long)max_h * max_v % 1000000007);
    }
}