from Clases import *

class WayBuilderClass:
    building=None;
    paths = None
    dijkstra_weight = None
    dijkstra_connectons=None
    max_id = -1

    def __init__(self,building):
        self.building=building
        self.init_pre_count()
        return

    def init_pre_count(self):
        for tmp_point in self.building.graph.points:
            if tmp_point.id >= self.max_id: self.max_id = tmp_point.id
        self.max_id+=1
        self.paths=[self.max_id]
        self.dijkstra_weight = []
        for i in range(self.max_id):
            self.dijkstra_weight.append([10000] * self.max_id)
        for conection in self.building.graph.connections:
            self.dijkstra_weight[conection.point1][conection.point2]=conection.connection_weight

    def dijkstra(self, start,stop):
        self.dijkstra_connectons = []
        for i in range(0, len(self.dijkstra_weight)):
            self.dijkstra_connectons.append([])
            for j in range(0, len(self.dijkstra_weight[i])):
                if (self.dijkstra_weight[i][j] < 10000):
                    self.dijkstra_connectons[i].append(j)

        print(self.dijkstra_connectons)

        size = self.max_id
        INF = 10 ** 10

        dist = [INF] * size
        dist[start] = 0
        prev = [None] * size
        used = [False] * size
        min_dist = 0
        min_vertex = start
        while min_dist < INF:
            i = min_vertex
            used[i] = True
            for j in self.dijkstra_connectons[i]:
                if dist[i] + self.dijkstra_weight[i][j] < dist[j]:
                    dist[j] = dist[i] + self.dijkstra_weight[i][j]
                    prev[j] = i
            min_dist = INF
            for i in range(size):
                if not used[i] and dist[i] < min_dist:
                    min_dist = dist[i]
                    min_vertex = i

        #print('dist massive')
        #print(dist)
        #print('print path')

        self.paths = []
        while stop is not None:
            self.paths.append(stop)
            stop = prev[stop]
        self.paths = self.paths[::-1]
        #print(self.paths)
        #print('sum')
        sum = 0
        for i in range(0, len(self.paths) - 1):
            sum += self.dijkstra_weight[self.paths[i]][self.paths[i + 1]]
            #print(sum)
        return sum


    def request_path(self,start,stop):
        weight = self.dijkstra(start,stop)
        print(self.paths)

        path = Path()

        path.weight=weight

        for point_id in self.paths:
            for point in self.building.graph.points:
                if point.id==point_id:
                    path.points.append(point)
                    break


        for i in range(0,len(path.points)-1):
            for connection in self.building.graph.connections:
                if connection.point1==path.points[i].id and connection.point2==path.points[i+1].id:
                    path.connections.append(connection)


        floors_set=set()
        for point in path.points:
            floors_set.add(point.floor_index)
        for floor in floors_set:
            path.floors.append(floor)


        # нужен рерайтер картинок
        return path




    def psi_init(self):
        self.dijkstra_weight = []
        self.max_id = 10
        self.paths = [0]*self.max_id

        for i in range(self.max_id):
            self.dijkstra_weight.append([10000] * self.max_id)

        self.dijkstra_weight[1][2] = 5
        self.dijkstra_weight[2][1] =5
        self.dijkstra_weight[2][3] = 10
        self.dijkstra_weight[3][2] = 10
        self.dijkstra_weight[3][4] = 1
        self.dijkstra_weight[4][3] = 1
        self.dijkstra_weight[4][5] = 1
        self.dijkstra_weight[5][4] = 1
        self.dijkstra_weight[5][8] = 1
        self.dijkstra_weight[8][5] = 1
        self.dijkstra_weight[8][9] = 1
        self.dijkstra_weight[9][8] = 1
        self.dijkstra_weight[3][6] = 3
        self.dijkstra_weight[6][3] = 3
        self.dijkstra_weight[6][7] = 6
        self.dijkstra_weight[7][6] = 6
        self.dijkstra_weight[7][9] = 8
        self.dijkstra_weight[9][7] = 8
        # прочитать g // g[0 ... n - 1][0 ... n - 1] - массив, в котором хранятся веса рёбер, g[i][j] = 2000000000, если ребра между i и j нет

        #      -4-5-8-
        # 1-2-3<        >-9
        #

        # первая вершина-вторая вершина-вес перехода
        # 1-2-5
        # 2-1-5

        #                -(3)-4-(5)-5-(2)-8-(5)-
        # 1-(5)-2-(10)-3<                         >-9
        #                -(3)-6-(6)-7-(8)------

















       #valid = [True] * self.max_id
       #weight = [1000000] * self.max_id
       #weight[start] = 0
       #for i in range(self.max_id):
       #    self.paths[i] = []
       #    min_weight = 1000001
       #    ID_min_weight = -1
       #    for i in range(self.max_id):
       #        if valid[i] and weight[i] < min_weight:
       #            min_weight = weight[i]
       #            ID_min_weight = i

       #    for i in range(self.max_id):
       #        if weight[ID_min_weight] + self.dijkstra_graph[ID_min_weight][i] < weight[i]:
       #            weight[i] = weight[ID_min_weight] + self.dijkstra_graph[ID_min_weight][i]
       #    valid[ID_min_weight] = False
       #if weight[stop]==10000:raise Exception('no path to point')
       #return weight
