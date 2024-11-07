points = [(1, 2), (4, 6), (7, 8), (2, 5), (9, 10)] 

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)): 
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)

print("Hesaplanan mesafeler:", distances)
print("Minimum mesafe:", min_distance)