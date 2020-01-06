class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int N, int K) {
		//init the graph for the graph, and set all the distance to INF
        vector<int> graph(N + 1, INT_MAX);
        graph[K] = 0;
        //Bellman Ford algorithm, loop N-1 times
        for (int i = 0; i < N; i++) {
            //the new future for c++, learn from the discuss plate
            for (vector<int> e : times) {
                int u = e[0], v = e[1], w = e[2];
				//shrink the distance
                if (graph[u] != INT_MAX && graph[v] > graph[u] + w) {
                    graph[v] = graph[u] + w;
                }
            }
        }
		
        int res = 0;
		// the res is the longest distance to node K
        for (int i = 1; i <= N; i++)
            res = max(res, graph[i]);
        return res == INT_MAX ? -1 : res;
    }
};