def is_inside(point_pos, rectangle_pos):
    if rectangle_pos[0] <= point_pos[0] <= rectangle_pos[0] + rectangle_pos[2] \
    and rectangle_pos[1] <= point_pos[1] <= rectangle_pos[0] + rectangle_pos[3]:
        return True
    else:
        return False

# Test case

got_inside = is_inside([50, 50], [20, 20, 10, 100])
#should be outside, return false
if got_inside is not True:
    print("Code is correct")
else:
    print("Got bug")

