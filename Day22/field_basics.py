def add_mod(a, b, p):
    return (a + b) % p 

def mul_mod(a, b, p):
    return (a * b) % p

p = 17

print("20 % 17 =", 20 % p)
print("34 % 17 =", 34 % p)
print("-3 % 17 =", -3 % p)
print("(15 + 5) % 17 =", (15 + 5) % p)
print("(12 * 3) % 17 =", (12 * 3) % p)

print("add_mod(15, 5, p) =", add_mod(15, 5, p))
print("mul_mod(12, 3, p) =", mul_mod(12, 3, p))

assert add_mod(15, 5, p) == 3
assert mul_mod(12, 3, p) == 2

result = mul_mod(add_mod(3, 4, p), 2, p)
print("(3 + 4) * 2 mod 17 =", result)

values = [3, 4, 14, 112, 0]

print("original values: ", values)
print("first value: ", values[0])
print("number of values: ", len(values))

reduced_values = []

for v in values:
    reduced_values.append(v % p)

print("reduced values: ", reduced_values)
print("original values after loop: ", values)

inputs = [2, 5]
left = mul_mod(add_mod(values[0], inputs[1], p), values[2], p)
right = values[3] % p
print("left: ", left)
print("right: ", right)
print("constraint satisfied: ", left == right)