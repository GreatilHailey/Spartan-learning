extern crate libspartan;
extern crate merlin;
use libspartan::{Instance, NIZKGens, NIZK};
use merlin::Transcript;
fn main() {
    let num_vars = 1024;
    let num_cons = 1024;
    let num_inputs = 10;

    let gens = NIZKGens::new(
        num_cons, num_vars, num_inputs
    );

    let (inst, vars, inputs) = 
    Instance::produce_synthetic_r1cs(
        num_cons, num_vars, num_inputs
    );

    let mut prover_transcript = 
    Transcript::new(b"nizk_example");
    let proof = NIZK::prove(
        &inst, vars, &inputs, &gens,
        &mut prover_transcript
    );

    let mut verifier_transcript = 
    Transcript::new(b"nizk_example");
    assert!(
        proof.verify(
            &inst, &inputs, 
            &mut verifier_transcript, &gens
        ).is_ok()
    );
    println!("proof verification successful!");
}
