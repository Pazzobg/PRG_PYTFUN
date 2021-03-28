import sys
import random


def generate_permutations(a, n):
    if n == 0:
        global counter
        global list_random_vals

        if len(list_random_vals) > 0:
            rnd = list_random_vals[0]

            if counter == rnd:
                print(''.join(a))
                list_random_vals.remove(rnd)

        counter += 1
    else:
        for i in range(n):
            generate_permutations(a, n-1)
            j = 0 if n % 2 == 0 else i
            a[j], a[n] = a[n], a[j]
        generate_permutations(a, n-1)


counter = 1

if len(sys.argv) != 2:
    sys.stderr.write("Exactly one argument is required!\n")
    sys.exit(1)

word = sys.argv[1]
print(sys.argv)

# Calculation of total permutations count
permutations_count = 1
p = len(word)
while p > 1:
    permutations_count = permutations_count * p
    p -= 1
print(f"Total possible permutations: {permutations_count}")

# Create a list of ~20 random values within the count of total permutations
list_random_vals = []
for num in range(20):
    random_val = random.randint(1, permutations_count)
    if random_val not in list_random_vals:
        list_random_vals.append(random_val)

list_random_vals.sort()

print(list_random_vals)
generate_permutations(list(word), len(word)-1)

# Execute script with "> python ./tst.py someword" from OS command line
