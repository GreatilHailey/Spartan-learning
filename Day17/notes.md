# 日期：2026-09-30

## 今天的目标：
- 阅读官方自定义 R1CS 示例
- 理解约束结构、私有见证和公开输入在代码中的表示
- 手算一条约束，并逐段理解示例代码

## 实际完成：
- 阅读了官方 README.md 中的自定义 R1CS 示例，源码如下：
  ```Rust
  #![allow(non_snake_case)]
  extern crate curve25519_dalek;
  extern crate libspartan;
  extern crate merlin;
  use curve25519_dalek::scalar::Scalar;
  use libspartan::{InputsAssignment, Instance, SNARKGens, VarsAssignment,   SNARK};
  use merlin::Transcript;
  use rand::rngs::OsRng;
  
  fn main() {
    // produce a tiny instance
    let (
      num_cons,
      num_vars,
      num_inputs,
      num_non_zero_entries,
      inst,
      assignment_vars,
      assignment_inputs,
    ) = produce_tiny_r1cs();
  
    // produce public parameters
  let gens = SNARKGens::new(num_cons, num_vars, num_inputs,   num_non_zero_entries);
  
  // create a commitment to the R1CS   instance
  let (comm, decomm) = SNARK::encode(&  inst, &gens);
  
    // produce a proof of satisfiability
  let mut prover_transcript =   Transcript::new(b"snark_example");
    let proof = SNARK::prove(
      &inst,
      &comm,
      &decomm,
      assignment_vars,
      &assignment_inputs,
      &gens,
      &mut prover_transcript,
    );
  
    // verify the proof of satisfiability
  let mut verifier_transcript =   Transcript::new(b"snark_example");
    assert!(proof
    .verify(&comm, &assignment_inputs, &  mut verifier_transcript, &gens)
      .is_ok());
  println!("proof verification   successful!");
  }
  
  fn produce_tiny_r1cs() -> (
   usize,
   usize,
   usize,
   usize,
   Instance,
   VarsAssignment,
   InputsAssignment,
  ) {
  // We will use the following example, but one could construct any R1CS   instance.
  // Our R1CS instance is three constraints over five variables and two   public inputs
    // (Z0 + Z1) * I0 - Z2 = 0
    // (Z0 + I1) * Z2 - Z3 = 0
    // Z4 * 1 - 0 = 0
  
  // parameters of the R1CS instance   rounded to the nearest power of two
    let num_cons = 4;
    let num_vars = 5;
    let num_inputs = 2;
    let num_non_zero_entries = 5;
  
  // We will encode the above constraints   into three matrices, where
  // the coefficients in the matrix are   in the little-endian byte order
  let mut A: Vec<(usize, usize, [u8; 32])  > = Vec::new();
  let mut B: Vec<(usize, usize, [u8; 32])  > = Vec::new();
  let mut C: Vec<(usize, usize, [u8; 32])  > = Vec::new();
  
  // The constraint system is defined over a finite field, which in our case   is
  // the scalar field of ristreeto255/curve25519 i.e., p =  2^{252}  +27742317777372353535851937790883648493
  // To construct these matrices, we will use `curve25519-dalek` but one can use   any other method.
  
  // a variable that holds a byte   representation of 1
    let one = Scalar::ONE.to_bytes();
  
  // R1CS is a set of three sparse   matrices A B C, where is a row for every
  // constraint and a column for every   entry in z = (vars, 1, inputs)
    // An R1CS instance is satisfiable iff:
  // Az \circ Bz = Cz, where z = (vars,   1, inputs)
  
    // constraint 0 entries in (A,B,C)
  // constraint 0 is (Z0 + Z1) * I0 - Z2   = 0.
  // We set 1 in matrix A for columns   that correspond to Z0 and Z1
  // We set 1 in matrix B for column that   corresponds to I0
  // We set 1 in matrix C for column that   corresponds to Z2
    A.push((0, 0, one));
    A.push((0, 1, one));
    B.push((0, num_vars + 1, one));
    C.push((0, 2, one));
  
    // constraint 1 entries in (A,B,C)
    A.push((1, 0, one));
    A.push((1, num_vars + 2, one));
    B.push((1, 2, one));
    C.push((1, 3, one));
  
    // constraint 3 entries in (A,B,C)
    A.push((2, 4, one));
    B.push((2, num_vars, one));
  
  let inst = Instance::new(num_cons, num_vars, num_inputs, &A, &B, &C).unwrap  ();
  
    // compute a satisfying assignment
    let mut csprng: OsRng = OsRng;
    let i0 = Scalar::random(&mut csprng);
    let i1 = Scalar::random(&mut csprng);
    let z0 = Scalar::random(&mut csprng);
    let z1 = Scalar::random(&mut csprng);
    let z2 = (z0 + z1) * i0; // constraint 0
    let z3 = (z0 + i1) * z2; // constraint 1
    let z4 = Scalar::ZERO; //constraint 2
  
    // create a VarsAssignment
  let mut vars = vec![Scalar::ZERO.  to_bytes(); num_vars];
    vars[0] = z0.to_bytes();
    vars[1] = z1.to_bytes();
    vars[2] = z2.to_bytes();
    vars[3] = z3.to_bytes();
    vars[4] = z4.to_bytes();
  let assignment_vars =   VarsAssignment::new(&vars).unwrap();
  
    // create an InputsAssignment
  let mut inputs = vec![Scalar::ZERO.  to_bytes(); num_inputs];
    inputs[0] = i0.to_bytes();
    inputs[1] = i1.to_bytes();
  let assignment_inputs =   InputsAssignment::new(&inputs).unwrap();
  
  // check if the instance we created is   satisfiable
  let res = inst.is_sat(&  assignment_vars, &assignment_inputs);
    assert_eq!(res.unwrap(), true);
  
    (
      num_cons,
      num_vars,
      num_inputs,
      num_non_zero_entries,
      inst,
      assignment_vars,
      assignment_inputs,
    )
   }
  ```
- 逐段理解了库导入、参数生成、承诺、证明和验证的调用
- 阅读了 `produce_tiny_r1cs()` 中约束结构与赋值的构造过程
- 手算了第一条约束，区分了满足和不满足的情况
- 今天完成的是代码阅读与手算，尚未运行这个自定义示例

## 成果
- 本次阅读的官方源码提交为 `d62b961f9497e3c07a921b6da1457cad467598d9`
- 示例规模为：
  - 约束行数 `num_cons = 4`，其中 3 条显式约束、1 条零约束
  - 私有变量数量 `num_vars = 5`
  - 公开输入数量 `num_inputs = 2`
  - 矩阵非零项规模上限 `num_non_zero_entries = 5`
- 三条显式约束为：
  ```text
  (Z0 + Z1) * I0 = Z2
  (Z0 + I1) * Z2 = Z3
  Z4 * 1 = 0
  ```
- 第一条约束的手算：
  - 令 `Z0 = 3`、`Z1 = 4`、`I0 = 2`，则 `Z2 = 14`
  - 左边 `(3 + 4) * 2 = 14`，右边为 `14`，约束满足
  - 如果只把 `Z2` 改成 `15`，则约束不满足
- 记录了当前版本 README.md 中的主要代码位置：

  | 内容 | 代码入口 | 行号 |
  |---|---|---|
  | 约束的非零系数记录 | `A.push(...)`、`B.push(...)`、`C.push(...)` | 202～215 |
  | 构造 R1CS 实例 | `Instance::new(...)` | 217 |
  | 生成满足约束的具体赋值 | 随机生成部分值，再计算 `z2`、`z3`、`z4` | 220～227 |
  | 整理并构造私有变量赋值 | `VarsAssignment::new(&vars)` | 230～236 |
  | 整理并构造公开输入赋值 | `InputsAssignment::new(&inputs)` | 239～242 |
  | 直接检查约束满足性 | `inst.is_sat(...)` | 245～246 |

## 对今天的理解：
- `extern crate` 用于声明使用外部库，`use` 用于引入名称，方便后续使用短名称；它们不会安装库，依赖由 `Cargo.toml` 配置。Rust 2021 中通常不需要显式写 `extern crate`
- `#![allow(non_snake_case)]` 允许示例使用 `A`、`B`、`C` 等不符合下划线命名习惯的名称，不改变计算结果
- `produce_tiny_r1cs()` 只调用一次，返回包含七项内容的元组，再由 `main()` 按位置解构；对应关系取决于位置，不取决于变量名
- `usize` 常用于表示数量、长度和下标；函数末尾不加分号的元组表达式可以作为返回值

- A、B、C 使用稀疏方式保存，只记录非零系数：
  ```rust
  let mut A: Vec<(usize, usize, [u8; 32])> = Vec::new();
  ```
  每个元素表示 `(行下标, 列下标, 系数的字节表示)`；`Vec::new()` 创建空向量，`push` 添加记录
- `[u8; 32]` 表示 32 字节数组，共 256 位存储空间，用来保存一个系数的编码，不是 32 个系数
- `Scalar::ONE.to_bytes()` 表示把有限域中的 1 转换为字节编码；`Scalar::ZERO` 表示有限域中的 0
- 本示例提交给构造接口的矩阵列排列为：
  ```text
  列下标： 0   1   2   3   4   5   6   7
  对应值：Z0  Z1  Z2  Z3  Z4   1  I0  I1
  ```
- 每一行约束要求：A 这一行根据赋值算出的值，乘以 B 这一行算出的值，等于 C 这一行算出的值
- C 的某一行没有非零记录，表示右侧值为 0，不表示这条约束不用检查
- A、B、C 分别有 5、3、2 个非零元素，因此非零项规模上限取 `max(5, 3, 2) = 5`。这个参数用于生成公共参数，不控制 A 向量能否添加元素，也不是私有变量数量或三个矩阵非零项的总数

- `Instance::new(...)` 根据规模和矩阵记录构造约束实例，此时还没有代入具体赋值，因此构造成功不等于赋值满足约束
- `OsRng` 使用操作系统随机源；每次调用 `Scalar::random(&mut csprng)` 都会生成一个随机有限域元素，但结果不保证彼此不同。可变借用是传参方式，不是随机值不同的原因
- 示例先随机生成 `i0`、`i1`、`z0`、`z1`，再按照约束计算：
  ```rust
  let z2 = (z0 + z1) * i0;
  let z3 = (z0 + i1) * z2;
  let z4 = Scalar::ZERO;
  ```
  这是示例作者主动构造满足约束的赋值，不是 Spartan 自动求解方程
- `vec![初始值; 数量]` 创建指定数量的元素；`vars` 保存五个私有变量值的编码，`inputs` 保存两个公开输入值的编码
- `inputs[0]` 对应 `I0`，但 `I0` 在矩阵中的列下标为 6，因为矩阵列还包含前面的五个私有变量和常数 1
- `VarsAssignment::new(...)` 和 `InputsAssignment::new(...)` 构造赋值对象；赋值对象构造成功，也不代表已经满足约束

- `inst.is_sat(...)` 接收私有见证和公开输入，直接检查赋值是否满足约束；`proof.verify(...)` 使用证明及相应公开数据进行验证，不接收私有见证
- `.unwrap()` 在 `Result` 为 `Ok(...)` 时取出里面的值，为 `Err(...)` 时触发 panic；`.is_ok()` 只返回表示是否成功的布尔值
- `assert!(条件)` 要求条件为真；`assert_eq!(a, b)` 要求两者相等。当前示例中断言失败会触发 panic，后面的成功提示不会执行
- 当前 `assignment_vars` 按值传入 `prove` 会转移所有权，之后不能继续使用原变量；`&` 是共享借用，`&mut` 是可变借用。`i64` 等支持 `Copy` 的类型按值传入时会复制，原变量仍可使用
- 证明者和验证者分别创建 transcript，使用相同的初始化标签；验证者需要从初始状态开始，不能直接复用证明结束后的 transcript

## 不懂的知识：
- 有限域运算的具体规则待后续学习
- 库内部对变量数量和矩阵的补齐方式待后续学习
- Rust 所有权目前理解了本例中的传值与借用区别，其他规则按需继续学习