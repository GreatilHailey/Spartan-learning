def check_constraints(witness, inputs, p):
    left_values = [
        ((witness[0] + witness[1]) * inputs[0]) % p,
        ((witness[0] + inputs[1]) * witness[2]) % p,
        (witness[4] * 1) % p,
    ]
    right_values = [
        witness[2] % p,
        witness[3] % p,
        0 % p,
    ]

    checks = []

    for i in range(len(left_values)):
        satisfied = left_values[i] == right_values[i]
        checks.append(satisfied)

        print(
            f"constraint {i}: "
            f"left = {left_values[i]}, "
            f"right = {right_values[i]}, "
            f"satisfied = {satisfied}"
        )

    return all(checks)

p = 17
witness = [3, 4, 14, 10, 0]
inputs = [2, 5]

print("valid case: ")
valid_result = check_constraints(witness, inputs, p)
print("all constraints satisfied: ", valid_result)
assert valid_result

bad_witness = witness.copy()
bad_witness[4] = 1

print("invalid case: ")
bad_witness_result = check_constraints(bad_witness, inputs, p)
print("all constraints satisfied: ", bad_witness_result)
assert not bad_witness_result

bad_inputs = inputs.copy()
bad_inputs[0] = 3

print("invalid public input case: ")
bad_inputs_result = check_constraints(witness, bad_inputs, p)
print("all constraints satisfied: ", bad_inputs_result)
assert not bad_inputs_result