fn first_product(values: &[i64]) -> i64 {
    values[0] * values[1]
}

fn satisfies(a: i64, b: i64, c:i64) -> bool {
    a * b == c
}

fn main() {
    let values: Vec<i64> = vec![3, 4, 12, 13];
    println!("values: {:?}", values);
    println!("case 1: a = {}, b = {}, c = {}: {}", values[0], values[1], values[2], satisfies(values[0], values[1], values[2]));
    println!("case 2: a = {}, b = {}, c = {}: {}", values[0], values[1], values[3], satisfies(values[0], values[1], values[3]));
    println!("first product: {}", first_product(&values));
    println!("values after call: {:?}", values);
}
