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