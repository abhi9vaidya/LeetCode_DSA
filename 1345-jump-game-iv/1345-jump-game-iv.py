class Solution:
    def minJumps(self, a: List[int]) -> int:
        g,cur,visited = defaultdict(list),[0],{0}
        for i,v in enumerate(a): g[v].append(i)

        for step,nex in ((step,[]) for step in count()):
            for i in cur:
                if i==len(a)-1: return step
                for j in chain([i-(i>0),i+1],a[i] in g and g.pop(a[i]) or []):
                    if j not in visited: visited.add(j); nex.append(j)

            cur = nex