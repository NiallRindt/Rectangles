points = [[1,2],[3,2],[3,3],[1,3],[1,4],[3,4],[9,4],[9,2],[8,4],[8,2]]
lines = []
totallines = []
numberlines = []
def point_above(points):
    for i in range(len(points)):
        for j in range(len(points)-1):
            if points[i][0] == points[j][0] and points[i][1] != points[j][1] and [points[i],points[j]] not in lines and [points[j],points[i]] not in lines and j!=i:
                lines.append([points[i],points[j]])
def check_level(lines,numberlines):
    for i in range(len(lines)):
        print(i)
        for j in range(len(lines)-1):
            print("before")
            print(j)
            if ((lines[i][0][1] == lines[j+1][0][1]) or (lines[i][0][1] == lines[j+1][1][1])) and ((lines[i][1][1] == lines[j][1][1]) or (lines[i][1][1] == lines[j][0][1])) and (lines[i][0][0] != lines[j][0][0]) and ((lines[i],lines[j]) not in numberlines):
                numberlines.append([lines[i],lines[j]])
            print("after")
            print(j)
        totallines.append(len(numberlines))
        numberlines = []
def tallyrects(totallines,rects):
    for i in range(len(totallines)):
        rects += totallines[i]*(totallines[i]-1)/2
    print(rects)

def calculate_rects(points):
    point_above(points)
    check_level(lines,1)
    tallyrects(totallines,0)

calculate_rects(points)
