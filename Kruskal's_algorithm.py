"""
My realisation of Kruskal's algorithm during first year of CS degree
Student at Lviv Polytechnic 2021 Yushchak Oleksandr
--------------------------------------------------------------------
Steps:
1) Enter number of edges
2) 1st vertex
3) 2nd vertex
4) Value of path
* 2-3-4 repeat for all edges
"""


class Edge:
    def __init__(self, v1, v2, value):
        self.v1 = v1
        self.v2 = v2
        self.value = value


lst_edges = []
st_edges = []
n_edges = int(input("Enter number of edges:"))
for i in range(0, n_edges):
    v1 = input("Enter first vertex")
    v2 = input("Enter second vertex")
    value = int(input("Enter value of edge"))
    lst_edges.append(Edge(v1, v2, value))

for i in range(0, n_edges):  # сортування списку ребер за вагою/sort list of edges by weight
    index = 0
    for y in range(0, len(lst_edges)):
        last_min = lst_edges[0].value
        if lst_edges[y].value < last_min:
            last_min = lst_edges[y].value
            index = y
    st_edges.append(lst_edges[index])
    # print(lst_edges[index].value) #показує які елементи сортуються/shows what elements are being sorted
    del lst_edges[index]

set_vert = set([])
set_vert.add(st_edges[0].v1)
set_vert.add(st_edges[0].v2)
lst_edges.append(st_edges[0])
branch_count = 0
lst_branch = [[st_edges[0].v1, st_edges[0].v2]]

print(f"Edge #1: {st_edges[0].v1} - {st_edges[0].v2}")
for i in range(1, n_edges):
    indic = False
    indic1 = False
    count = 0

    for c in range(0, len(lst_branch)):
        if st_edges[i].v1 in lst_branch[c] and st_edges[i].v2 in lst_branch[c]:
            indic = True

    for x in range(0, len(lst_branch)):
        if st_edges[i].v1 not in lst_branch[x] and st_edges[i].v2 not in lst_branch[x]:
            count += 1
    if count == len(lst_branch):
        lst_branch.append([st_edges[i].v1, st_edges[i].v2])
        indic1 = True

    if not indic and not indic1:
        arg1 = False
        arg2 = False
        x1 = 0
        x2 = 0
        for t in range(0, len(lst_branch)):
            if st_edges[i].v1 in lst_branch[t]:
                arg1 = True
                x1 = t
        for r in range(0, len(lst_branch)):
            if st_edges[i].v2 in lst_branch[r]:
                arg2 = True
                x2 = r
        if arg1 and arg2:
            union_branch = lst_branch[x1] + lst_branch[x2]  # check
            lst_branch.append(union_branch)  # union

        else:
            if arg1:
                lst_branch[x1].append(st_edges[i].v1)
                lst_branch[x1].append(st_edges[i].v2)
            else:
                lst_branch[x2].append(st_edges[i].v1)
                lst_branch[x2].append(st_edges[i].v2)

    if indic:
        print(f"Edge {st_edges[i].v1} and {st_edges[i].v2} creates cycle! Skipping...")
    else:
        print(f"Edge #{i + 1}: {st_edges[i].v1} - {st_edges[i].v2}")
        set_vert.add(st_edges[i].v1)
        set_vert.add(st_edges[i].v2)
        lst_edges.append(st_edges[i])

print("Final result:")
all_weight = 0
for i in range(0, len(lst_edges)):
    print(f"Edge #{i + 1}: {{{lst_edges[i].v1}, {lst_edges[i].v2}}}   value: {lst_edges[i].value}")
    all_weight += lst_edges[i].value
print(f"Weight of the grapgh: {all_weight}")
