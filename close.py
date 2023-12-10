class dijkstra_zip:
    def find_lowest_cost_node(self, costs):
        lowest_cost = 1000000
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def dijkstra(self, graph, start, final):
        node = start
        costs[start] = 0
        while node is not None:
            cost = costs[node]
            neighbors = graph[node]
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if costs[n] > new_cost:
                    costs[n] = new_cost  # 갱신
                    parents[n] = node
            processed.append(node)
            node = self.find_lowest_cost_node(costs)
        trace = []
        current = final
        while current != start:
            trace.append(current)
            current = parents[current]
        trace.append(start)
        trace.reverse()
        print(start, "에서 ", final, "까지의 정보")
        print("최단 거리 : ", costs[final])
        print("진행 과정 : ", processed)
        print("경로 : ", trace)


graph = {'A': {'B': 5, 'C': 0},
         'B': {'D': 15, 'E': 20},
         'C': {'D': 30, 'E': 35},
         'D': {'F': 20},
         'E': {'F': 10},
         'F': {}}
infinity = 1000000
costs = {'A':infinity,
         'B':infinity,
         'C':infinity,
         'D':infinity,
         'E':infinity,
         'F':infinity}
parents = { 'B':None,
            'C':None,
            'D':None,
            'E':None,
            'F':None}
    # 추적 경로를 위해 부모 설정
processed = []
    # 최단 경로를 가진 노드를 구한다.
dk=dijkstra_zip()
dk.dijkstra(graph, "A", "F")