from math import sqrt

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return sqrt (((self.x-other.x)**2) + ((self.y-other.y)**2))
    
    def __repr__(self):
        return 'Point(%d, %d)' % (self.x, self.y)
