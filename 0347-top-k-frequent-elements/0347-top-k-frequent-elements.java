
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.ArrayList;
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<Integer, Integer>();
        // int[] freq = new int[nums.length + 1]; 
        int[] res = new int[k];
        ArrayList<Integer>[] freq = new ArrayList[nums.length + 1]; 
        for(int i=0; i<nums.length + 1; i++){
            freq[i] = new ArrayList<Integer>();
        }
        for(int n: nums){
            count.put(n, count.getOrDefault(n, 0) + 1);
        }
        for(Entry<Integer, Integer> entrySet : count.entrySet()) {
            System.out.println(entrySet.getKey() + " : " + entrySet.getValue());
            freq[entrySet.getValue()].add(entrySet.getKey());
        }
        int j = k - 1;
        for(int i = freq.length - 1; i > 0; i--) {
            if(j < 0) {
                return res;
            }
            for(int n: freq[i]) {
                res[j] = n;
                j -= 1;
            }
        }
        
        return res;
    }
}