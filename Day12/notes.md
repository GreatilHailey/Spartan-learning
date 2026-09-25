# 日期：2026-09-25

## 今天的目标：
- 确认环境
- 运行 Spartan 官方测试
- 保存日志，并判断测试结果

## 实际完成：
- 检查源码、工具链和依赖锁文件
- 按官方配置执行，保存输出和退出码
- 核对测试数量、失败或忽略项

## 成果
- 利用 `rustc --version` 查看了 Rust 编译器版本
- 利用 `sha256sum Cargo.lock /home/greatil/Spartan-learning/Day08/logs/Cargo.lock` 计算官方源码目录中的当前 `Cargo.lock` 与 Day08 保存副本的摘要，确认两者一致
- 利用 `cargo test --release --verbose --locked 2>&1 | tee /home/greatil/Spartan-learning/Day12/logs/test-01.log` 进行构建并运行了官方测试，同时将运行结果保存到了 Day12 的日志中
- 利用 `test_status=${PIPESTATUS[0]}` 保存了测试程序的退出码并且通过 `printf 'cargo test exit code: %s\n' "$test_status" | tee /home/greatil/Spartan-learning/Day12/logs/test-01-exit.log` 将退出码保存到日志中
- 本次实际运行的 45 个测试全部通过，情况如下：

  | 测试部分 | 通过 | 失败 | 忽略 |
  |---|---:|---:|---:|
  | `libspartan` 单元测试 | 42 | 0 | 0 |
  | `nizk` 可执行目标的测试 | 0 | 0 | 0 |
  | `snark` 可执行目标的测试 | 0 | 0 | 0 |
  | 文档示例测试 | 3 | 0 | 0 |
  | **合计** | **45** | **0** | **0** |
- 首次运行未及时捕获退出码，重新运行后覆盖了原日志；当前保存的是第二次运行结果，45 个测试全部通过，退出码为 0

## 对今天的理解：
- `cargo test --release --verbose --locked 2>&1 | tee /home/greatil/Spartan-learning/Day12/logs/test-01.log` 中 `--release` 表示使用发布模式优化； `--verbose` 表示输出详细过程； `--locked` 表示使用现有锁文件，同时如果需要更新锁文件，Cargo 会报错，而不是自动修改它
- 通过 `sha256sum filename` 可以计算文件摘要

## 不懂的知识：
- 暂无