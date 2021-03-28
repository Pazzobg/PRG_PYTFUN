counter = 0
for c in range(1, 48):
    for b in range(1, c):
        for a in range(1, b):
            if a**2 + b**2 == c**2:
                print("{:3d}, {:3d}, {:3d}".format(a, b, c))
                # print(f"{a}**2 + {b}**2 == {c}**2: {a ** 2} + {b ** 2} = {c ** 2}")

                counter += 1

print(f"Total number of Pythagorean triples for range 1-48: {counter}")
