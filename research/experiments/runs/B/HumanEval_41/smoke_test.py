from solution import car_race_collision

# Basic cases
assert car_race_collision(0) == 0
assert car_race_collision(1) == 1
assert car_race_collision(2) == 4
assert car_race_collision(3) == 9
assert car_race_collision(4) == 16
assert car_race_collision(5) == 25

# Verify the n^2 formula for larger values
for n in range(20):
    assert car_race_collision(n) == n * n
