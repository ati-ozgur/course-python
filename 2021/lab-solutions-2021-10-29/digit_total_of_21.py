for d1 in range(1, 10):
    for d2 in range(1, 10):
        if d2 == d1:
            continue
        for d3 in range(1, 10):
            if d3 == d1:
                continue
            if d3 == d2:
                continue
            
            total = d1 + d2 + d3
            print("digits:",d1,d2,d3,"total:",total)
            
