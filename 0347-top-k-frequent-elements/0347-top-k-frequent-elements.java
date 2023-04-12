

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<Integer, Integer>();
        int[] res = new int[k];

        for(int n: nums){
            count.put(n, count.getOrDefault(n, 0) + 1);
        }
        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());
        for(Map.Entry entry : count.entrySet()) {
            pq.add(entry);
        }
        
        for(int i = 0; i < k; i++) {
            res[i] = pq.poll().getKey();
        }
        
        return res;
    }
}