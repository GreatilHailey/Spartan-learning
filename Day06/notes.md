# 日期：2026-09-19

## 今天的目标：
- 阅读官方源码中构建说明
- 下载安装 Rust 工具链
- 了解创建 Cargo 项目

## 实际完成：
- 阅读了 README.md 中关于安装、编译及运行的部分
- 阅读了 Cargo.toml 中的 edition 及 [dependencies] 
- 安装了 Rust
- 创建了最小 Cargo 项目并对代码进行修改

## 成果
- 安装 Rust 版本为 `rustc 1.98.1 (48a229cea 2026-09-01)` 
- 安装 Cargo 版本为 `cargo 1.98.1 (797e8a9bc 2026-08-05)`  
- 创建了 `Day06/hello_rust` 并成功编译运行
- 修改代码为
  ```rust 
  fn main() {
    println!("The environment of Day06 is set up correctly!");
    } 
  ```
  并成功编译运行
- 在 `.gitignore` 中加入了对 Cargo 项目中的编译产物文件夹 `target/` 的屏蔽

## 对今天的理解：
- 官方源码仓库 `README.md` 中的前两行 `![Rust](...)` 和 `crates.io` 的两个徽章分别显示仓库自动化工作流状态，以及已发布的 Rust 软件包版本并提供链接
- `command -v xxx` 可以查询当前终端能否找到命令 `xxx` 
- 可以通过 `sed -n 'x,yp' name.xxx` 的方式查询文件 `name.xxx` 的第 `x` 到第 `y` 行
- Cargo 创建项目的命令为 `cargo new Day06/hello_rust --bin --vcs none --edition 2021` ，其中 `--bin` 代表创建可运行的程序项目；`--vcs none` 代表不另建 Git 仓库，由现有学习仓库管理；`--edition 2021` 是为了使用与 Spartan 相同的 Rust 语言版次
- 创建好的 Cargo 项目中的 `Cargo.toml` 文件包含项目名称、版本、语言版次和依赖配置；`src/main.rs` 包含程序源码，包含程序入口
- 程序源码中 `fn main()` 为程序入口；`println` 用来输出内容并在末尾换行；`!` 是 Rust 的宏调用标记

## 不懂的知识：
- 对 Rust 语言理解还欠缺，等待后续了解