# 日期：2026-9-23

## 今天的目标：
- 学习读 Spartan 代码所需的最小 Rust 基础

## 实际完成：
- 学习基本函数创建方法
- 学习基本 `Vec` 用法
- 学习引用
- 学习切片

## 成果
- 完成了一个基本程序，代码如下
  ``` Rust
  fn first_product(values: &[i64]) -> i64 {
    values[0] * values[1]
  }

  fn satisfies(a: i64, b: i64, c:i64) -> bool {
      a * b == c
  }

  fn main() {
      let values: Vec<i64> = vec![3, 4, 12, 13];
      println!("values: {:?}", values);
      println!("case 1: a = {}, b = {}, c = {}: {}", values[0], values[1], values[2], satisfies(values[0], values[1], values[2]));
      println!("case 2: a = {}, b = {}, c = {}: {}", values[0], values[1], values[3], satisfies(values[0], values[1], values[3]));
      println!("first product: {}", first_product(&values));
      println!("values after call: {:?}", values);
  }
  ```

## 对今天的理解：
- Rust 函数创建方法类似 Python，其中 `fn` 对应 `def` ，函数体末尾不带分号的表达式，其值可以作为函数返回值；`-> type` 声明返回类型，格式如下：
  ```Rust
  fn fun(input: type) -> type {
     Operation;
     returnValue
  }
  ```
- Rust 的 `Vec` 类似 Python 的 `list[]` ，但同一个 Vec 的元素类型必须一致；通过语句 `let vecName: Vec<type> = vec![]` 创建，支持下标访问，同时可以用 `vecName[startIndex..endIndex]` 的形式切片，区间为左闭右开；可以用 `println!("{:?}", vecName)` 的形式用调试格式打印整个向量
- 通过在函数参数类型前加 `&` 表示共享引用，类似 C++ ，作用为令函数参数通过共享引用读取传入数据，但不能通过它直接修改今天使用的整数或向量元素，在传入时也要用 `fun(&input)` 的形式传入
- Rust 可以把一个向量在合适的地方自动转换成覆盖整个向量的切片进行引用，即对输入类型为 `fn fun(input: &[type])` 切片引用的函数，输入的 `fun(&vec)` Rust 会自动转化为 `fun(&vec[..])` 

## 不懂的知识：
- 可变引用