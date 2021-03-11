#fabricYards(inches)
def fabricYards(inches):
  yards=0
  yards=inches//36
  if inches%36 > 0:
    return(yards+1)
  elif inches%36==0:
    return(yards)

#fabricExcess(inches)
def fabricExcess(inches):
    if inches%36==0:
        return(0)
    elif inches%36>0:
        return(inches-(fabricYards(inches)-1)*36)

#nearestBusStop(street)
def nearestBusStop(street):
    if street%8==0:
        return(street)
    elif street%8!=0:
        return(street//8*8+8)

#numberOfPoolBalls(rows)
def numberOfPoolBalls(rows):
    n=rows
    return((n+1)*n/2)

#numberOfPoolBallRows(balls)
def numberOfPoolBallRows(balls):
    rows=0
    while (numberOfPoolBalls(rows)<balls):
        rows += 1
    return(rows)

#rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2)
def rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2):
    if left2>left1+width1:
        return(False)
    elif top2<top1-height1:
        return(False)
    elif left2+width2<left1:
        return(False)
    elif top2-height2>top1:
        return(False)
    else:
        return(True)

#threeLinesArea(m1, b1, m2, b2, m3, b3)
import math
def threeLinesArea(m1, b1, m2, b2, m3, b3):
    if m1==m2 or m2==m3 or m3==m1:
        return(0)
    else:
        pointA = intersectionPoints(m1, b1, m2, b2)
        pointB = intersectionPoints(m1, b1, m3, b3)
        pointC = intersectionPoints(m2, b2, m3, b3)
        lengthAB = lengthOfSides(pointA, pointB)
        lengthAC = lengthOfSides(pointA, pointC)
        lengthBC = lengthOfSides(pointB, pointC)
        return (areaOfTriangle(lengthAB, lengthAC, lengthBC))

def intersectionPoints(m1, b1, m2, b2):
    x=(b2-b1)/(m1-m2)
    y=(m1*b2-m2*b1)/(m1-m2)
    return(x,y)

def lengthOfSides(a, b):
    return(math.sqrt((a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1])))

def areaOfTriangle(ab, ac, bc):
    s=(ab+ac+bc)/2
    return(math.sqrt(s*(s-ab)*(s-ac)*(s-bc)))
