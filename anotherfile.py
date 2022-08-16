def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(len([x for x in apples if s <= x+a <= t]), len([x for x in oranges if s <= x+b <= t]))