class RectangularGrid:
    def countRectangles(self, width, height):
        cnt = 0
        for i in xrange(1, height+1):
            for j in xrange(1, width+1):
                h, w = (height-i+1), (width-j+1)
                cnt += h*w - min(h,w)
        return cnt

print(RectangularGrid().countRectangles(592, 964))