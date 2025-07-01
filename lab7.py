def membership(x, fuzzy_set):
    closest_y = 0.0
    min_distance = float('inf')
    for y, crisp in fuzzy_set:
        distance = abs(x - crisp)
        if distance < min_distance:
            min_distance = distance
            closest_y = y
    return closest_y

none = [ (1.0, 0.0), (0.5, 0.05), (0.0, 0.1) ]
bottle = [ (0.0, 0.1), (0.4, 0.4), (1.0, 0.8), (0.4, 1.2), (0.0, 1.6) ]
alot = [ (0.0, 0.8), (0.5, 1.2), (0.8, 1.6), (1.0, 2.0) ]

moderate = [ (1.0, 40), (0.6, 55), (0.3, 65), (0.0, 70), (0.3, 75), (0.6, 80), (1.0, 85) ]
hot = [ (0.0, 70), (0.3, 75), (0.6, 80), (1.0, 90) ]

short = [ (1.0, 0.1), (0.5, 0.5), (0.0, 1.5) ]
medium = [ (0.0, 1.0), (0.5, 3.0), (1.0, 5.0), (0.5, 7.0), (0.0, 10.0) ]
long = [ (0.0, 4.0), (0.4, 7.0), (0.8, 10.0), (1.0, 15.0) ]

def mamdani_inference(L, T):
    rule1ant = membership(L, short)
    rule2ant = min(membership(L, medium), membership(T, moderate))
    rule3ant = max(membership(L, long), membership(T, hot))
    numerator = 0.0
    denominator = 0.0
    step = 0.01
    x = 0.0
    while x <= 2.0:
        u1 = rule1ant * membership(x, none)
        u2 = rule2ant * membership(x, bottle)
        u3 = rule3ant * membership(x, alot)
        u = max(u1, u2, u3)
        numerator += u * x
        denominator += u
        x += step
    if denominator == 0:
        return 0.0
    return numerator / denominator

def run_test():
    T = 85
    L = 1.5
    result = mamdani_inference(L, T)
    print(f"Temperature: {T}°F, Distance: {L} km Recommended Water: {result:.2f} L")

if __name__ == "__main__":
    run_test()

