from math import sqrt

numPoints = int(input("Enter number of points: "))
points = []
distances = []
i = 0

countX = 0
countY = 0

while i < numPoints:
    inpLst = input("Please enter " + str(i) + "th coordinates seperated with space: ").split(" ")
    if len(inpLst) != 2:
        print("Please enter a valid point.", end=" ")
        continue
    coords = tuple(float(coord) for coord in inpLst)
    i += 1
    countX += coords[0]
    countY += coords[1]
    points.append(coords)

coMass = (countX/numPoints, countY/numPoints)
print("Center of mass:", coMass)

i = 0
while i < numPoints:
    rnge = sqrt(((coMass[0]-points[i][0]) ** 2 + (coMass[1] - points[i][1]) ** 2))
    distances.append((rnge, i))
    i += 1

if distances:
    closestPoint = distances[0]
    furthestPoint = distances[0]

for i in range(len(distances)):
    if distances[i][0] < closestPoint[0]:
        closestPoint = (distances[i][0], distances[i][1])
    if distances[i][0] > furthestPoint[0]:
        furthestPoint = (distances[i][0], distances[i][1])

print("Closest point is:", points[closestPoint[1]], end=" ")
print("and has distance:", closestPoint[0])
print("Closest point is:", points[furthestPoint[1]], end=" ")
print("and has distance:", furthestPoint[0])

