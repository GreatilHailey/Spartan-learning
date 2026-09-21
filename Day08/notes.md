# 日期：2026-09-21

## 今天的目标：
- 确认源码版本和官方构建配置
- 首次构建并保存日志

## 实际完成：
- 查询了 Rust 及其编译器的版本
- 查询了 Cargo 的配置
- 查看了官方仓库的工作流程配置
- 保存了以上版本信息日志
- 按官方自动化配置进行了构建
- 保存了构建过程日志
- 查询了构建过程中的 Warning 内容
- 保存了官方源码的依赖版本

## 成果
- 利用 `rustup show` 命令查询了已安装及当前启用的 Rust 工具链；利用 `rustc -Vv` 查询了 Rust 编译器版本
- 利用 `cargo --version` 查询了 Cargo 版本；利用 `cat .cargo/config` 查询了 Cargo 配置
- 利用 `sed -n '1,220p' .github/workflows/rust.yml` 查询了官方工作流程配置
- 利用了文件描述符重定向进行了日志保存
- 利用 
  ```Shell
  cargo build --examples --benches --verbose 2>&1 | tee /home/greatil/Spartan-learning/Day08/logs/build-01.log
  build_status=${PIPESTATUS[0]}
  printf 'cargo build exit code: %s\n' "$build_status" | tee /home/greatil/Spartan-learning/Day08/logs/build-01-exit.log
  ```
  在本地按官方自动化配置中的构建命令完成编译，并进行了构建日志保存
- 本次开发模式构建成功，退出码为 0；日志中有警告，但没有阻止构建；尚未运行测试和性能实验
- 利用 `grep -n -A 8 '^warning:' ../Spartan-learning/Day08/logs/build-01.log` 进行了日志 Warning 查询
- 利用 `cp Cargo.lock ../Spartan-learning/Day08/logs/Cargo.lock` 进行了依赖版本保存

## 对今天的理解：
- `cargo build` 命令中 `--examples --benches` 表示编译示例和性能测试程序
- `tee` 跟在管道后面可以让传输的文本既在终端中显示又写入后续指定文件中；此次构建过程用管道来保存日志就是为了加上 `tee` 能够在终端看到构建进度，如果只用重定向的话就无法在终端显示，从保存日志角度来说二者是一样的
- `grep` 命令中 `-n` 表示显示行号，`-A 8` 表示每个匹配行的后面8行，`^` 表示行首符号
- `Cargo.toml` 记录的是项目需要的依赖要求；而此次保存的 `Cargo.lock` 记录的是此次构建实际应用的具体依赖本配置

## 不懂的知识：
- 暂无