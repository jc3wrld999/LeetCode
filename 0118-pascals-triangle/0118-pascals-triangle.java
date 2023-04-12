// Leetcode 118. Pascal's Triangle
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> output = new ArrayList<>();
        List<Integer> cur = new ArrayList<>();
        for(int i = 0;i < numRows; i++) {
            cur.add(0, 1);
            for(int x = 1;x < cur.size() - 1; x++){
                cur.set(x, cur.get(x) + cur.get(x+1));
            }
            output.add(new ArrayList<>(cur));
        }
        return output;
    }
}