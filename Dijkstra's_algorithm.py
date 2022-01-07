"""
My realisation of Dijkstra's algorithm during first year of CS degree
Student at Lviv Polytechnic 2021 Yushchak Oleksandr
---------------------------------------------------------------------
Steps:
1) Enter number of vertexes and edges
2) Then enter pair of vertexes and value of route
3) Starting and end point
"""


class Vertex():
    def __init__(self, name):
        self.name = name
        self.v_value = 0
        self.used_v = False
        self.parent = None


class Edge():
    def __init__(self, v1, v2, value):
        self.vert_lst = [v1, v2]
        self.e_value = value
        self.used_e = False


def find_avail_routes(vert, num_e, num_v):
    for i in range(0, num_e):
        if vert in e_lst[i].vert_lst:  # search for incident edges
            if not e_lst[i].used_e:  # check whether edge wasn't used

                if e_lst[i].vert_lst[0] == vert:  # find second vertex
                    sec_v = e_lst[i].vert_lst[1]
                else:
                    sec_v = e_lst[i].vert_lst[0]
                first_v = None
                for y in range(0, num_v):  # check whether 2nd vertex wasn't used before
                    if v_lst[y].name == sec_v:
                        if not v_lst[y].used_v:
                            for z in range(0, num_v):
                                if v_lst[z].name == vert:
                                    first_v = v_lst[z]

                            if e_lst[i] not in avail_route:
                                e_lst[i].e_value = e_lst[
                                                       i].e_value + first_v.v_value  # add to availible route value before
                                avail_route.append(e_lst[i])
                            else:
                                print(f"This vertex was already used {e_lst[i].vert_lst}")


v_lst = []
e_lst = []

avail_route = []

n = int(input("Enter number of vertexes:"))
for i in range(1, n + 1):
    v_lst.append(Vertex(i))
x = int(input("Enter number of edges"))
for i in range(0, x):
    e_lst.append(Edge(int(input("Enter v1:")), int(input("Enter v2:")), int(input("Enter value:"))))

'''
print("Graph consists of this vertexes:") #print log 5
for i in range(0, n):
    print(v_lst[i].name)
print("Graph consists of this edges:")
for i in range(0, x):
    print(e_lst[i].vert_lst)
'''
strt_v = int(input("Enter starting point:"))
strt_v_const = strt_v
end_v = int(input("Enter ending point:"))
end_v_const = end_v

while True:
    find_avail_routes(strt_v, x, n)
    '''
    print("All available routes:")  # To show log 1
    for i in range(0, len(avail_route)):
        print(f"{avail_route[i].vert_lst} value: {avail_route[i].e_value}")  # To show log 2
    '''
    last_min_val = 9999
    index = None
    for i in range(0, len(avail_route)):  # find shortest path from list of all availible
        if avail_route[i].e_value < last_min_val:

            first_vertex, second_vertex = None, None  # check whether this 2 vert weren't used before
            for p in range(0, n):
                if avail_route[i].vert_lst[0] == v_lst[p].name:
                    first_vertex = v_lst[p]
            for y in range(0, n):
                if avail_route[i].vert_lst[1] == v_lst[y].name:
                    second_vertex = v_lst[y]
            if first_vertex.used_v and second_vertex.used_v:
                # print(f"This route is impossible, skipping ... {avail_route[i].vert_lst}") #To show log 3
                continue

            else:

                last_min_val = avail_route[i].e_value
                index = i
    print(f"Shortest path is: {avail_route[index].vert_lst}")  # {avail_route[index].e_value}

    for i in range(0, x):  # mark used edge in general list
        if avail_route[index] == e_lst[i]:
            e_lst[i].used_e = True

    index3 = None
    for i in range(0, n):  #
        if avail_route[index].vert_lst[0] == v_lst[i].name and not v_lst[i].used_v:
            sec_vertex = v_lst[i]
            index3 = 1
    for i in range(0, n):  #
        if avail_route[index].vert_lst[1] == v_lst[i].name and not v_lst[i].used_v:
            sec_vertex = v_lst[i]
            index3 = 0

    fir_vertex = avail_route[index].vert_lst[index3]  # find real first vertex that was used before

    for i in range(0, n):  # mark used vertex 1
        if avail_route[index].vert_lst[0] == v_lst[i].name:
            v_lst[i].used_v = True
    for i in range(0, n):  # mark used vertex 2
        if avail_route[index].vert_lst[1] == v_lst[i].name:
            v_lst[i].used_v = True

    for i in range(0, n):  # add to new starting point value of previous route
        if v_lst[i].name == sec_vertex.name:
            v_lst[i].v_value += avail_route[index].e_value
            v_lst[i].parent = fir_vertex  # add parent vertex/ to make chain
            index2 = i

    strt_v = sec_vertex.name

    del avail_route[index]

    if strt_v == end_v:
        print("The end of sequence was reached!")
        print(f"The value is {v_lst[index2].v_value}")

        lst_chain = []
        parent = None
        lst_chain.append(end_v_const)
        indic1 = False
        while True:
            for i in range(0, n):
                if v_lst[i].name == end_v:
                    parent = v_lst[i].parent
                    lst_chain.append(parent)
                    end_v = v_lst[i].parent
                    if end_v == strt_v_const:
                        indic1 = True
                        break
            if indic1:
                break

        print(f"Path from v{strt_v_const} to v{end_v_const}:")
        print(lst_chain[::-1])
        break
