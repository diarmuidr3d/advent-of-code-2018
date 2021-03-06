# input = """1, 1
# 1, 6
# 8, 3
# 3, 4
# 5, 5
# 8, 9"""
input="""353, 177
233, 332
178, 231
351, 221
309, 151
105, 289
91, 236
321, 206
156, 146
94, 82
81, 114
182, 122
81, 153
319, 312
334, 212
275, 93
224, 355
347, 94
209, 65
118, 172
113, 122
182, 320
191, 178
99, 70
260, 184
266, 119
177, 178
313, 209
61, 285
155, 218
354, 198
274, 53
225, 138
228, 342
187, 165
226, 262
143, 150
124, 159
325, 210
163, 176
326, 91
170, 193
84, 265
199, 248
107, 356
45, 340
277, 173
286, 44
242, 150
120, 230"""


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def calculate_closest_point(x, y, points):
    closest = 0
    closest_dist = 10000
    for each in points:
        dist = manhattan_distance(x,y,points[each]["x"],points[each]["y"])
        if dist < closest_dist:
            closest_dist = dist
            closest = each
    return closest

lines = input.split('\n')
points = {}
min_x = 1000
min_y = 1000
max_x = 0
max_y = 0

i = 0
for each in lines:
    coord = each.split(',')
    x = int(coord[0].strip())
    y = int(coord[1].strip())
    points[i] = {"x": x, "y": y, "infinite": False, "area": 0}
    if x > max_x:
        max_x = x + 1
    if x < min_x:
        min_x = x - 1
    if y > max_y:
        max_y = y + 1
    if y < min_y:
        min_y = y - 1
    i = i + 1

x = min_x
while x <= max_x:
    y = min_y
    while y <= max_y:
        closest_point = calculate_closest_point(x, y, points)
        if x == min_x or x == max_x or y == min_y or y == max_y:
            points[closest_point]["infinite"] = True
        else:
            points[closest_point]["area"] = points[closest_point]["area"] + 1
        y = y + 1
    x = x + 1

max_area = 0
for each in points:
    if not points[each]["infinite"] and points[each]["area"] > max_area:
        max_area = points[each]["area"]

print(points)
print(max_area)
