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
- 尚未验证是否可以运行