class Solution {
    public int numIslands(char[][] grid) {
        if (grid.length == 0 || grid[0].length == 0) return 0;
        int count = 0;
        for(int r = 0; r < grid.length; r++) {
            for(int c = 0;  c < grid[0].length; c++) {
                if(grid[r][c] == '1') {
                    count++;
                    bfs(grid, r, c);
                }
            }
        }
        return count;
    }
    public void bfs(char[][] grid, int r, int c) {
        if(r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] == '0') return;
        grid[r][c] = '0';
        bfs(grid, r+1, c);
        bfs(grid, r-1, c);
        bfs(grid, r, c+1);
        bfs(grid, r, c-1);
        
    }
}