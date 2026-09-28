extern crate libspartan;
extern crate merlin;
use libspartan::{Instance, SNARKGens, SNARK};
use merlin::Transcript;
fn main() {
    let num_vars = 1024;
    let num_cons = 1024;
    let num_inputs = 10;
    let num_non_zero_entries = 1024;

    let gens = 
    SNARKGens::new(
        num_cons, num_vars, 
        num_inputs, num_non_zero_entries
    );

    let (inst, vars, inputs) = 
    Instance::produce_synthetic_r1cs(
        num_cons, num_vars, num_inputs
    );

    let (comm, decomm) =
    SNARK::encode(
        &inst, &gens
    );

    let mut prover_transcript = 
    Transcript::new(b"snark_example");
    let proof = SNARK::prove(
        &inst, &comm, &decomm, vars,
        &inputs, &gens, 
        &mut prover_transcript
    );

    let mut verifier_transcript =
    Transcript::new(b"snark_example");
    assert!(
        proof.verify(
            &comm, &inputs,
            &mut verifier_transcript, &gens
        ).is_ok()
    );
    println!("proof verification successful");
}