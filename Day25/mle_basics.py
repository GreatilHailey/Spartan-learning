def mle2(
    values: list[int], 
    x : int, 
    y : int, 
    p: int,
) -> int:
    weights = [
        (1 - x) * (1 - y) % p,
        (1 - x) * y % p,
        x * (1 - y) % p,
        x * y % p,
    ]
    total = 0
    for i in range(4):
        total = (total + values[i] * weights[i]) % p
    return total

p = 17
values = [3, 5, 7, 11]
points = [
    (0, 0),
    (0, 1),
    (1, 0),
    (1, 1),
    (2, 3),
]
for x, y in points:
    result = mle2(values, x, y, p)
    print(f'f_tilde({x}, {y}) = {result}')