fn satisfies(a: i64, b: i64, c: i64) -> bool {
    a * b == c
}

#[test]
fn satisfies_case_passes() {
    assert!(satisfies(3, 4, 12));
}

#[test]
fn unsatisfied_case_returns_false() {
    assert!(!satisfies(3, 4, 13));
}