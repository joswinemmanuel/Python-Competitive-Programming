def squares(a, b):
    squares = 0
    i = int(math.sqrt(min(a, b)))
    while i*i <= max(a, b):
        if i*i >= min(a, b):
            squares += 1
        i += 1
    return squares
