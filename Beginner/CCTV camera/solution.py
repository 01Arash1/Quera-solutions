ax, ay = list(map(int, input().split()))
bx, by = list(map(int, input().split()))
cx, cy = list(map(int, input().split()))
dx, dy = 0, 0

if ax != bx and ax != cx:
    dx = ax
elif bx != ax and bx != cx:
    dx = bx
else:
    dx = cx

if ay != by and ay != cy:
    dy = ay
elif by != ay and by != cy:
    dy = by
else:
    dy = cy

print(dx, dy)