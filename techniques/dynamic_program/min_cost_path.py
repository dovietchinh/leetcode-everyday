def min_cost_path_top_down(cost,m,n):
    if not hasattr(min_cost_path_top_down,'memo'):
        min_cost_path_top_down.memo = [[-1 for _ in range(m)] for _ in range(n)]
    if min_cost_path_top_down.memo[m][n] != -1:
        return min_cost_path_top_down.memo[m][n]
    if m < 0 or n < 0:
        return float('inf')
    elif m == 0 and n == 0:
        return cost[m][n]
    else:
        res = cost[m][n] + min(min_cost_path_top_down(cost,m-1,n-1),
                                min_cost_path_top_down(cost,m-1,n),
                                min_cost_path_top_down(cost,m,n-1))
        min_cost_path_top_down.memo[m][n] = res
        return res

    
def min_cost_path_bottom_up(cost,m,n):
    if m < 0 or n < 0:
        return float('inf')
    elif m == 0 and n == 0:
        return cost[m][n]
    else:
        for i in range(1,m+1):
            cost[i][0] += cost[i-1][0]
        for j in range(1,n+1):
            cost[0][j] += cost[0][j-1]
        for i in range(1,m+1):
            for j in range(1,n+1):
                cost[i][j] += min(cost[i-1][j-1],cost[i-1][j],cost[i][j-1])