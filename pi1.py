import random

def calculate_pi(n): # im wieksze n tym bardziej dokladny wynik Pi
    num_of_points_circle = 0
    num_of_points_total = 0
    for ele in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2  # sqrt(x^2 + y^2) < 1
        if distance <= 1:
            num_of_points_circle += 1
        num_of_points_total += 1
    return 4 * num_of_points_circle / num_of_points_total   # pole kola/ pole kwadratu =
# num_of_points_in_circle/ num_of_points_total
