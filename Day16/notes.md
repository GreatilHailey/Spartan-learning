# 日期：2026-09-29

## 今天的目标：
- 阅读对比
- 运行示例
- 整理成果

## 实际完成：
- 找出 NIZK 与 SNARK 参数生成、证明和验证接口的差异
- 使用本地固定版本官方库，保存结果和退出码
- 写接口对比，在 draw.io 图中标出分支

## 成果
- 阅读了官方仓库中 README.md 中的 NIZK 示例代码并进行理解
- 本地创建了 `Day16/nizk_example` ，运行了官方 NIZK 示例，代码如下
  ```Rust
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
  ```
- 首次因变量名拼写错误未成功运行，修正后第二次验证通过，退出码为 0；成功记录对应 `nizk-02.log` 和 `nizk-02-exit.log`
- 将示例复现过程以及成功后的退出码进行了日志保存，保存在了 `Day16/logs/nizk-02.log` 和 `Day16/logs/nizk-02-exit.log` 中
- 最后整理了官方 SNARK 示例代码与官方 NIZK 示例代码各个接口的对应表，保存在了 `Day16/interface-comparison.md` 中

## 对今天的理解：
- NIZK 示例没有像 SNARK 示例那样单独调用 encode，得到并传入 comm 和 decomm，但这不代表 NIZK 内部没有使用承诺机制

## 不懂的知识：
- 暂无