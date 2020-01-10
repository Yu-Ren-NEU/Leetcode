//ry

class Solution {
    int res = 0;
    int lenx = 0;
    int leny = 0;
    public int islandPerimeter(int[][] grid) {
        lenx = grid.length;
        if(lenx == 0) return res;
        leny = grid[0].length;
        for(int x = 0; x < lenx; x++) {
            for(int y = 0; y < leny; y++) {
                if(grid[x][y] == 1) {
                    helper(grid, x, y);
                    return res;
                }
            }
        }
        return res;
    }
    private void helper(int[][] grid, int x, int y) {
        if(x < 0 || y < 0 || x > lenx - 1 || y > leny - 1) {
            res++;
            return;
        }
        if(grid[x][y] == 0) {
            res++;
            return;
        }
        if(grid[x][y] == 1) {
            grid[x][y] = 2;
            helper(grid, x - 1, y);
            helper(grid, x + 1, y);
            helper(grid, x, y - 1);
            helper(grid, x, y + 1);
        }
    }
}
