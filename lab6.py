fuzzy_sets = {
    "water": {
        "none": [(1.0, 0.0), (0.75, 0.1), (0.5, 0.2), (0.25, 0.3), (0.0, 0.4)],
        "bottle": [(0.0, 0.2), (0.5, 0.5), (1.0, 1.0), (0.5, 1.5), (0.0, 2.0)],
        "alot": [(0.0, 1.0), (0.25, 1.25), (0.5, 1.5), (0.75, 1.75), (1.0, 2.0)]
    },
    "temperature": {
        "moderate": [(1.0, 32), (0.75, 50), (0.5, 68), (0.25, 85), (0.0, 100)],
        "hot": [(0.0, 70), (0.25, 80), (0.5, 90), (0.75, 100), (1.0, 110)]
    },
    "distance": {
        "short": [(1.0, 0.25), (0.75, 1), (0.5, 2), (0.25, 3), (0.0, 4)],
        "medium": [(0.0, 2), (0.5, 5), (1.0, 10), (0.5, 15), (0.0, 18)],
        "long": [(0.0, 5), (0.25, 10), (0.5, 15), (0.75, 18), (1.0, 20)]
    }
}


def membership(crisp_value, fuzzy_set):
    min_dist = float('inf')
    closest_val = 0.0
    for fuzzy_val, crisp in fuzzy_set:
        if crisp == crisp_value:
            return fuzzy_val
        dist = abs(crisp - crisp_value)
        if dist < min_dist:
            min_dist = dist
            closest_val = fuzzy_val
    return closest_val

def inverse_membership(fuzzy_value, fuzzy_set):
    min_dist = float('inf')
    closest_crisp = 0.0
    for fuzzy_val, crisp in fuzzy_set:
        dist = abs(fuzzy_val - fuzzy_value)
        if dist < min_dist:
            min_dist = dist
            closest_crisp = crisp
    return closest_crisp


def infer_water_amount(distance_km, temperature_f):
    fuzzy_dist = membership(distance_km, fuzzy_sets["distance"]["long"])
    fuzzy_temp = membership(temperature_f, fuzzy_sets["temperature"]["hot"])
    premise = max(fuzzy_dist, fuzzy_temp)  
    return inverse_membership(premise, fuzzy_sets["water"]["alot"])


def run_tests():
    print("Testing membership()")
    print(membership(-3, fuzzy_sets["water"]["bottle"]))         
    print(membership(1.0, fuzzy_sets["water"]["bottle"]))        
    print(membership(0.3, fuzzy_sets["water"]["bottle"]))       
    print(membership(0.712321345, fuzzy_sets["water"]["bottle"]))
    print(membership(10000, fuzzy_sets["water"]["bottle"]))      

    print("\nTesting inverse_membership()")
    print(inverse_membership(0.0, fuzzy_sets["water"]["bottle"]))   
    print(inverse_membership(0.2, fuzzy_sets["water"]["bottle"]))   
    print(inverse_membership(0.5, fuzzy_sets["water"]["bottle"]))   
    print(inverse_membership(0.8, fuzzy_sets["water"]["bottle"]))
    print(inverse_membership(1.0, fuzzy_sets["water"]["bottle"]))

    print("\nTesting inference")
    km = 3
    temp = 80
    recommended = infer_water_amount(km, temp)
    print(f"The user walked {km} km and it is {temp}°F. Recommended water: {recommended:.2f} L")

if __name__ == "__main__":
    run_tests()

