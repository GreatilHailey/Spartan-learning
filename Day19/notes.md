# 日期：2026-10-02

## 今天的目标：
- 修改验证时的公开输入并检查原证明是否仍能通过验证

## 实际完成：
- 准备一个容易手算的正常实例
- 同一份证明先用原公开输入验证，再用修改后的公开输入验证。
- 保存结果，确认失败确实来自验证阶段

## 成果
- 创建了 `Day19/public_input_check` 项目，并且将 `Day18/custom_r1cs` 中的 `main.rs` 复制过来并对 `verify` 过程进行了修改
- `verify` 过程代码如下：
  ```Rust
  //第一次：使用原公开输入验证
  let mut verifier_transcript = Transcript::new(b"snark_example");
  let original_result = proof.verify(
    &comm, &assignment_inputs,
    &mut verifier_transcript, &gens,
  );
  println!("original inputs accepted: {}", original_result.is_ok());
  assert!(original_result.is_ok());

  //仅构造一份修改后的公开输入：I0: 2 -> 3, I1 : 5
  let changed_inputs = InputsAssignment::new(&[
    Scalar::from(3u64).to_bytes(),
    Scalar::from(5u64).to_bytes(),
  ]).unwrap();

  //第二次：使用同一份 proof ，换成修改后的公开输入
  let mut changed_verifier_transcript = Transcript::new(b"snark_example");
  let changed_result = proof.verify(
    &comm, &changed_inputs,
    &mut changed_verifier_transcript, &gens,
  );
  println!("changed input rejected: {}", changed_result.is_err());
  assert!(changed_result.is_err());

  println!("public input comparison completed!");
  ```
- 固定 R1CS 结构、公共参数和同一份证明，原公开输入验证通过；仅将公开输入 `I0` 从 2 改为 3，保持 `I1` = 5，并使用相同初始化标签的新 `transcript` 验证，原证明被拒绝。两个断言均通过，进程退出码为 0
- 最终将运行结果和退出码保存到了 `Day19/logs` 中的日志中；注：由于第一次命令打错成 `run_status=${PIPESTAUTS[0]}` 没有正确获取退出码，故重新运行并保存到了 `02` 日志中

## 对今天的理解：
- 本次实验表明原证明不能直接用于修改后的公开输入

## 不懂的知识：
- 暂无