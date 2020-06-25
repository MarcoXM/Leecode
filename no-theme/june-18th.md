## june 18th



```go

func criticalConnections(n int, connections [][]int) [][]int {
    graph := make(map[int][]int)
    set := make(map[[2]int]bool)
    ans := make([][]int,0)
    rank := make([]int,n)
    for _, x :=range connections{
        graph[x[0]] = append(graph[x[0]],x[1])
        graph[x[1]] = append(graph[x[1]],x[0])
        sort.Ints(x)
        set[[2]int{x[0],x[1]}] = true
    }
    // 初始化,为-1, 还没遍历时的深度.
    for i:= 0; i < n; i++ {
        rank[i] = -1
    }
    
    var dfs func(node, parent, depth int ) int
    dfs = func(node, parent, depth int) int{
        if rank[node] >= 0 {
            return rank[node]
        }
        rank[node] = depth
        minDepth := n
        for _, next_node := range graph[node]{
            if next_node == parent {
                continue
            }
            // 孩子的深度与自己的深度比较
            nextdepth := dfs(next_node,node,depth + 1)
            if nextdepth <= depth {
                x := swap(node, next_node)
                set[x] = false
            }
            minDepth = min(minDepth,nextdepth)
        }
        return minDepth
    }
    
    dfs(0,-1,0)
    for _,x :=range connections{
        if set[swap(x[0],x[1])] == true{
            ans = append(ans,x)
        } 
    }

    return ans
    
}
func swap(a ,b int) [2]int {
    if a< b {
        return [2]int{a,b}
    }
    return [2]int{b,a}
}

func min(a,b int) int{
    if a< b {
        return a
    }
    return b
}
```

