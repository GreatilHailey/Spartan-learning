# 日期：2026-09-28

## 今天的目标：
- 阅读示例
- 运行示例
- 整理对应表

## 实际完成：
- 找到参数生成、承诺、证明和验证的调用
- 使用固定版本官方库，保存运行结果
- 记录入口、输入输出及自己的理解

## 成果
- 阅读了官方仓库中 README.md 中的 SNARK 示例代码并进行理解
- 本地创建了 `Day15/snark_example` ，运行了官方 SNARK 示例，代码如下
  ```Rust
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
  ```
- 最终验证断言通过，进程退出码为 0
- 将示例复现过程以及成功后的退出码进行了日志保存，保存在了 `Day15/logs/snark-01.log` 和 `Day15/logs/snark-01-exit.log` 中
- 最后整理了官方示例代码与各部分概念功能的对应表，保存在了 `Day15/concept-code-map.md` 中

## 对今天的理解：
-  Rust 利用 `extern crate 库名称;` 导入外部库，利用 `use 库名称::{名称1, 名称2, ...};` 将类型、函数等名称引入当前作用域，方便后续使用短名称
-  Rust 利用 `let 变量名 = 赋值;` 进行声明并初始化变量并且默认不可变，并且支持类似 Python 的 `let (a, b, c) = 返回元组的函数;` 元组解构
-  Rust 通过 `let mut 变量名 = 赋值;` 进行可变变量的声明和初始化，并且通过 `&mut 变量` 进行可变引用
- 整个示例的流程为：
  ```mermaid
  block-beta
    columns 5

    A["设置规模"] space B["生成公共参数"] space C["准备 R1CS 和赋值"]

    space:5

    D["对 R1CS 作承诺"] space E["生成证明"] space F["验证证明"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
  ```
- 官方示例中 `decomm` 是计算结构承诺的配套辅助数据，供证明者生成与该承诺一致的矩阵多项式求值证明
-  `transcript` 是维护协议消息历史的状态对象；证明者与验证者按相同规则处理相同的公开协议消息，分别导出一致的挑战，从而无需在线交互发送挑战
- `Transcript::new(b"name")` 中的 `b"name"` 为该 `Transcript` 的初始化标签，也称为域分离标签，用于区分不同应用或协议上下文；同一份证明的生成和验证使用相同标签

## 不懂的知识：
- 矩阵构造的具体内容待后续学习
-  `decomm` 的具体数学原理待学习