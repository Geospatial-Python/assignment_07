import random
import math
"""
import hates me. Moved imported stuff here so I dont need to fix
also python hates me. nearly gave up so many times.
"""

class Point:

    def __init__(self,x = 0,y = 0,mark = ""):
        self.x = x
        self.y = y
        self.mark = mark

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        direction = ""
        if self.y > other.y:
            direction += "N"
        elif self.y == other.y:
            direction += "-"
        else:
            direction += "S"
        if self.x > other.x:
            direction += "E"
        elif self.x == other.y:
            direction += "-"
        else:
            direction += "W"

        return direction

    def __neg__(self):
        return Point(-self.x,-self.y,self.mark)

    def shift_point(self,x_move,y_move):
        this_point = (self.x,self.y)
        self.x += x_move
        self.y += y_move


class PointPattern:
    def __init__(self):
        origin = Point(0,0,"o")
        self.set_of_points = [origin]

    def avg_nearest_neighbor_dist(self,mark):
        average_nearest_neighbor_distance(self.set_of_points, mark)

    def num_coincident_points(self):
        coincident_points = 0
        len_list = len(self.set_of_points)
        for i in range(len_list):
            if i == len_list-1:
                break
            for j in range(len_list+1):
                if self.set_of_points[i] == self.set_of_points[j]:
                    coincident_points += 1

        return coincident_points

    def list_marks(self):
        mark_list = []
        len_list = len(self.set_of_points)
        for i in range(len_list):
            if not mark_list:
                mark_list.append(self.set_of_points[i].mark)
            elif self.set_of_points[i].mark not in mark_list:
                mark_list.append(self.set_of_points[i].mark)

        return mark_list

    def list_mark_subsets(self):
        mark_list = PointPattern.list_marks(self)
        mark_count = []
        sub_set = []
        for i in range(len(mark_list)):
            sub_set = []
            for j in range(len(self.set_of_points)):
                if mark_list[i] == self.set_of_points[j].mark:
                    sub_set.append(self.set_of_points[j])
            mark_count.append(sub_set)

        return mark_count

    def create_random_points(self):
        return create_random_marked_points(n = len(self.set_of_points),marks = [])

    def k_realizations(self,k = 99):
        return permutations(k,n = 100)

    def critical_points(self,realizations):
        return find_crit_points(realizations)

    def compute_g(self, min_dist):
        gs = 0
        len_list = len(self.set_of_points)
        all_pts_min_dists = []
        for i in range(len_list):
            local_nn = 0
            for j in range(len_list):
                if i != j:
                    new_distance = euclidean_distance(self.set_of_points[i],self.set_of_points[j])
                    if local_nn == 0:
                        local_nn = new_distance
                    elif new_distance < local_nn:
                        local_nn = new_distance

                    all_pts_min_dists.append(local_nn)

        for k in range(len(all_pts_min_dists)):
            if all_pts_min_dists[k]<=min_dist:
                gs += 1

        return gs








def create_random_marked_points(n, marks = []):
    list_of_tuples = [(random.uniform(0,1), random.uniform(0,1)) for i in range(n)]
    list_of_marks = [random.choice(marks) for i in range(n)]
    list_of_points = []
    for j in range(n):
        new_point = Point(list_of_tuples[j][0],list_of_tuples[j][1],list_of_marks[j])
        list_of_points.append(new_point)

    return list_of_points


def euclidean_distance(a, b):
    distance = math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
    return distance


def average_nearest_neighbor_distance(points, mark=""):
    mean_d = 0
    total = 0
    local_nn = 0
    num_of_points = len(points)

    if not mark:
        for i in range(num_of_points):
            local_nn = 0
            for j in range(num_of_points):
                if i != j:
                    new_distance = euclidean_distance(points[i],points[j])
                    if local_nn == 0:
                        local_nn = new_distance
                    elif new_distance < local_nn:
                        local_nn = new_distance

            total += local_nn

    else:
        for i in range(num_of_points):
            local_nn = 0
            for j in range(num_of_points):
                if i != j and points[i].mark == points[j].mark:
                    new_distance = euclidean_distance(points[i],points[j])
                    if local_nn == 0:
                        local_nn = new_distance
                    elif new_distance < local_nn:
                        local_nn = new_distance

            total += local_nn

    mean_d = total/num_of_points

    return mean_d


def permutations(p = 99, n = 100):
    list_means = []

    for i in range(p):
        marks = ["elf", "dwarf", "human", "orc"]
        rand_points = create_random_marked_points(n, marks)
        newMean = average_nearest_neighbor_distance(rand_points)
        list_means.append(newMean)

    return list_means


def find_crit_points(list_means):
    entries = list_means
    maxEntry = 0
    minEntry = 2
    for i in range(len(list_means)):
        if entries[i] > maxEntry:
            maxEntry = entries[i]
        if entries[i] < minEntry:
            minEntry = entries[i]

    return minEntry,maxEntry


def crit_point_check(minEntry, maxEntry, observed):
    if observed < minEntry or observed > maxEntry:
        return True
    else:
        return False
