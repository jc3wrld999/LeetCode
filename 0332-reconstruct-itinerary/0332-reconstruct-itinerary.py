class Solution(object):
    def findItinerary(self, tickets):
        adj = { src: [] for src, dst in tickets }
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[src].insert(i, v)
                print(res.pop())
            return False
        dfs("JFK")
        return res
        