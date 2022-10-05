def calculate_bags(small, big, total):
    max_big_boxes = int(total / 5)
    if max_big_boxes < big:
        big_boxes_we_can_use = max_big_boxes
    else:
        big_boxes_we_can_use = big

    total -= (big_boxes_we_can_use * 5)

    if (small < total):
        return -1

    return int(total)
