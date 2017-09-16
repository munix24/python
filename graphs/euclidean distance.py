import cProfile
import os
import sys
##from scipy.spatial import distance
##a = (1,2,3)
##b = (4,5,6)
##dst = distance.euclidean(a,b)
##print(dst)

rnd = 3

def distance(point1, point2):
    """calculates distance between points in 2d space"""
    return round(((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** .5, rnd)

def distance_3d(point1, point2):
    """calculates distance between points in 3d space"""
    return round(((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2) ** .5, rnd)

def distance_nd(point1, point2):
    """calculates distance between points in nd space"""
    if len(point1) != len(point2):
        return -1
    return round(sum([(point2[x] - point1[x]) ** 2 for x in range(len(point1))]) ** .5, rnd)

def calc_list_distance2(points):
    """calculates distance between a list of points in nd space"""
    dict = {}

    for i in range(len(points)):
        dict[i] = {}
        for n in range(i + 1, len(points)):
            dict[i][n] = distance_nd(points[i], points[n])

    return dict

##points = [[2,4],[3,2],[1,1],[4,3],[1,6],[5,3],[4,2]]
points = [[1, 1], [2, 2], [4, 5], [6, 3], [5, 4], [2, 4]]
##points = ((1,1,1),(2,2,1))
##points = ((1,1,1,1),(2,2,1,1))

##print(calc_list_distance(points))
##print(distance(points[0], points[1]))
##print(distance_3d(points[0], points[1]))
##print(distance_nd(points[0], points[1]))
