def play(left, right):
    """Play a game of Black Jack

    Args:
        left (int): left hand sum value
        right (int): right hand sum value

    Returns:
        int: winning hand value
    """
    ln = left
    rn = right
    if(ln > 21):
        ln = 0
    if(rn > 21):
        rn = 0
    if(ln > rn):
        return ln
    else:
        return rn
