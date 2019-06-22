from math import sqrt
class Point(object):

    def __init__(self, x,y):
        self.x= x
        self.y= y
    def __repr__(self):
        return "Point(%d, %d)" % (self.x,self.y)

    def __sub__(self, sec):
        if isinstance(sec,Point):
            return Point(self.x - sec.x, self.y - sec.y)

    def __add__(self,sec):
        if isinstance(sec,Point):
            return Point(self.x + sec.x, self.y + sec.y)
    
    def distance(self, other):
        return sqrt (((self.x-other.x)**2) + ((self.y-other.y)**2))
        
 class Cluster(object):

    def __init__(self, x, y):
        self.center = Point(x, y)
        self.points = []

    def update(self):
    # define initial average coordinates and counter
        xS = 0
        yS = 0
        count = 0
        for p in self.points:
            xS += p.x
            yS += p.y
            count += 1
            self.center = Point(xS/count, yS/count)
            self.points = []


    def add_point(self, point):
        self.points.append(point)
        
def compute_result(points):
    points = [Point(*point) for point in points]
    a = Cluster(1,0)
    b = Cluster(-1,0)
    a_old = []
    for _ in range(10000): # max iterations
        for point in points:
            if point.distance(a.center) < point.distance(b.center):
                # add the right point
                a.add_point(point)
            else:
                # add the right point
                b.add_point(point)
        if a_old == a.points:
            break
        a_old = a.points
        a.update()
        b.update()
    return [(a.center.x, a.center.y), (b.center.x, b.center.y)]
