
def brensenham_line(x,y,x2,y2):
    """
    Brensenham line algorithm
    """
    return_list = __brensenham_line(x, y, x2, y2)
    if return_list and return_list[0][0] != x or return_list[0][1] != y:
        # Reverse list if the brensenham algo
        # drew in the reverse order!
        return_list = return_list[::-1]
    return return_list


def __brensenham_line(x,y,x2,y2):
    """
    Brensenham line algorithm
    """
    steep = 0
    coords = []
    dx = abs(x2 - x)
    
    if (x2 - x) > 0: 
        sx = 1
    else: 
        sx = -1
    
    dy = abs(y2 - y)
    if (y2 - y) > 0: 
        sy = 1
    else: 
        sy = -1
    
    if dy > dx:
        steep = 1
        x,y = y,x
        dx,dy = dy,dx
        sx,sy = sy,sx
    
    d = (2 * dy) - dx
    for i in range(0,dx):
        if steep: 
            coords.append((y,x))
        else: 
            coords.append((x,y))
        
        while d >= 0:
            y = y + sy
            d = d - (2 * dx)
        
        x = x + sx
        d = d + (2 * dy)
    
    coords.append((x2,y2))
    return coords

