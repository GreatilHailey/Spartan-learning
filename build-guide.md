**以下是 D8 首次构建的实际命令**
### 源码
- 官方仓库地址：https://github.com/microsoft/Spartan.git
- 本次使用提交哈希：d62b961f9497e3c07a921b6da1457cad467598d9

### 环境
- 系统：Ubuntu 24.04.3 LTS（VMware 虚拟机）
- Rust 版本：1.98.1
- Cargo 版本：1.98.1

### 依赖与配置
- Cargo.lock 位置：构建使用的位置为：~/Spartan ；保存的备份位置为：~/Spartan-learning/Day08/logs
- rustflags：~/Spartan/.cargo/config
  ```log
  rustflags = [
  "-C", "target-cpu=native",
  ]
  ```

### 操作步骤
```shell
cd Spartan
cargo build --examples --benches --verbose 2>&1 | tee ../Spartan-learning/Day08/logs/build-01.log
build_status=${PIPESTATUS[0]}
printf 'cargo build exit code: %s\n' "$build_status" | tee ../Spartan-learning/Day08/logs/build-01-exit.log
```

### 结果判断
- 输出 `cargo build exit code: 0` 表示构建成功
- 只完成构建，尚未运行测试

**以下是 D12 官方测试记录**

**注**：当前保存的日志对应第二次运行；第一次因未及时捕获退出码而重跑，原日志被覆盖
### 执行位置
- `/home/greatil/Spartan`

### 实际命令
- `cargo test --release --verbose --locked 2>&1 | tee ../Spartan-learning/Day12/logs/test-01.log` 用来构建并运行测试
- `test_status=${PIPESTATUS[0]}` 用来获得测试退出码
- `printf 'cargo test exit code: %s\n' "$test_status" | tee ../Spartan-learning/Day12/logs/test-01-exit.log` 用来显示并保存退出码到日志中

### 再次运行时的注意事项
- 注意先创建日志目录，并且每次运行都要更改日志名
- 在构建并运行 test 后要及时保存退出码

### 已验证的结果
- Day12 的 42 个库测试、3 个文档测试全部通过，退出码为 0 
- 并不等于完整复现