def is_inside(point_pos, rectangle_pos):
    if rectangle_pos[0] <= point_pos[0] <= rectangle_pos[0] + rectangle_pos[2] \
    and rectangle_pos[1] <= point_pos[1] <= rectangle_pos[1] + rectangle_pos[3]:
        return True
    else:
        return False




