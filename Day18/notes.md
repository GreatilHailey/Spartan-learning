# 日期：2026-10-01

## 今天的目标：
- 修改一个私有见证值
- 观察约束不满足时程序的行为
- 并准确找到失败的位置

## 实际完成：
- 运行未修改的版本
- 只修改一个私有见证值，先预测结果，再运行
- 对照日志，判断失败发生在满足性检查、证明生成还是证明验证阶段

## 成果
- 在 `Day18/custom_r1cs` 下构建了昨天阅读的示例
- 成功编译并运行了原始版本，并且确认退出码为 0，保存基准日志到 `Day18/logs/custom-valid-01.log` 和 `Day18/logs/custom-valid-exit-01.log` 中
- 修改私有见证 `z4` 从 `Scalar::ZERO` 到 `Scalar::ONE` 后，程序成功通过编译，但满足性检查 `is_sat` 返回 `false`，导致 `src/main.rs` 第 136 行的 `assert_eq!` 断言失败并触发 panic，退出码为 101，保存失败日志到 `Day18/logs/custom-invalid-01.log` 和 `Day18/logs/custom-invalid-exit-01.log` 中
- 保存了成功与失败版本的源码快照 `Day18/custom-valid.rs`、`Day18/custom-invalid.rs`，通过 `diff` 确认仅修改了 `z4` 的赋值和注释

## 对今天的理解：
- 今日只观察证明生成前的检查失败，程序尚未进入证明生成和验证阶段
- 主要了解了 `cargo run` 和 `cargo new` 的几个参数效果
- `cargo new --bin` 创建包含 `src/main.rs` 的可执行程序项目；`--lib` 创建包含 s`rc/lib.rs` 的库项目，默认不创建 `main` 入口。一个项目后续也可以同时包含库和可执行程序；`cargo new` 默认使用 `--bin`
- `--vcs` 是版本控制系统，`--vcs none` 代表创建 Cargo 项目时，不为它单独初始化一个版本控制仓库
- `--release` 代表使用发布配置，默认启用更强的优化，通常编译更慢、程序运行更快；所以简单语法练习可直接使用 `cargo run`；运行 Spartan 的证明计算时使用 `--release`，以减少运行开销；排错时也可以根据需要使用开发配置
- `--offline` 表示不联网，使用本地依赖缓存；`--locked` 表示必须沿用现有 Cargo.lock，需要生成或修改锁文件时就报错；`--verbose` 表示显示更详细的构建过程，便于排错
- `cargo run` 的参数可以按如下场景进行判断：
  ```Bash
  # 简单语法练习
  cargo run
  
  # Spartan 示例，允许按需联网获取依赖
  cargo run --release
  
  # Spartan 示例，依赖已经缓存
  cargo run --release --offline
  
  # 已有成功基准，希望保持依赖版本且不联网
  cargo run --release --offline --locked
  ```

## 不懂的知识：
- 暂无