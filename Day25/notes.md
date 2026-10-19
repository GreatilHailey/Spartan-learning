# 日期：2026-10-15
- 本次手算和 Python 使用教学模数 17，官方代码使用其 `Scalar` 有限域
## 今天的目标：
- 学习多线性扩展 MLE
- 阅读并理解官方源码中求 MLE 过程

## 实际完成：
- 理解 MLE 的原理
- 编写计算基本 MLE 的 py 程序
- 深度理解官方源码中关于 MLE 的部分

## 成果
- 手算了若干 MLE 的简单示例
- 撰写了计算基本 MLE 的 Python 程序，保存到了 `/home/greatil/projects/spartan/Spartan-learning/Day25/mle_basics.py` 中
- 阅读了官方源码 `/home/greatil/projects/spartan/Spartan/src/dense_mlpoly.rs` 中的 MLE 多项式存储结构 `pub struct DensePolynomial` ，构造函数 `pub fn new(Z:` 以及求值函数 `pub fn evaluate(&self, r:` （注意此处源码 236 行的为求值函数，110 行的同名函数用于在稀疏多项式证明时，计算与初始化内存地址有关的求值）

## 对今天的理解：
- 多线性多项式即每个变量在多项式中的次数都不超过 1；次数为 1 对应“线性”，多个变量对应“多”；注意多项式中仍可能出现二次项，例如 $f(x, y) = 1 + x + y + xy$ 仍是多线性多项式
- 今日学习示例中的 MLE 均为由 4 个点定义；有 $\mathscr l$ 个变量的 MLE 核心定义为：给定 $2^\mathscr l$ 个位置（每个坐标均为 0/1）上的值，构造一个多线性多项式，使得其在给定 $2^\mathscr l$ 个位置上的值满足要求，同时可以扩展到其它位置求值，扩展后的多项式记为 $\tilde f$ 
- 多线性扩展的思想类似插值法，对原表位置的每个布尔标签位，标签为 0 时使用因子 $1-r_i$，标签为 1 时使用因子 $r_i$。将各坐标的因子相乘，得到该位置在求值点 $\mathbf r$ 下的权重；再将所有表值与对应权重相乘并求和
- `mle_basics.py` 对 $\tilde f(x, y) = 3(1-x)(1-y) + 5(1-x)y + 7x(1-y) + 11xy$ 的扩展求值进行了编写
- 源码中 `pub struct DensePolynomial` 保存了多项式的原始初始值，其源码如下：
  ```Rust
  pub struct DensePolynomial {
    num_vars: usize, // the number of variables in the multilinear polynomial
    len: usize,
    Z: Vec<Scalar>, // evaluations of the polynomial in all the 2^num_vars Boolean inputs
    }
  ```
  其中 `num_vars` 保存了多线性多项式中的变量数量，`len` 保存了当前有效取值表长度，`Z` 保存了原表给出的取值；在按全部布尔位置写出的 MLE 插值公式中，每个表项均对应一个求和项，包括取值为零的位置，故 `len` 也是按全部布尔位置写出的 MLE 插值公式的项数
- 源码中 `pub fn new(Z: Vec<Scalar>)` 函数用于从取值表长度确定多项式变量数量，其源码如下：
  ```Rust
  pub fn new(Z: Vec<Scalar>) -> Self {
    DensePolynomial {
      num_vars: Z.len().log_2(),
      len: Z.len(),
      Z,
    }
  }
  ```
  其中由于每个坐标均有 0/1 两种可能，故应满足关系 $\|Z\| = 2^{num\_vars}$ ，从而有 `num_vars: Z.len().log_2()` ，同时构造时由取值表长度确定变量数，故有 `len: Z.len()` 
- 源码中 `pub fn evaluate(&self, r: &[Scalar])` 用于生成权重，再与取值表相乘求和，其源码如下：
  ```Rust
  pub fn evaluate(&self, r: &[Scalar]) -> Scalar {
    // r must have a value for each variable
    assert_eq!(r.len(), self.get_num_vars());
    let chis = EqPolynomial::new(r.to_vec()).evals();
    assert_eq!(chis.len(), self.Z.len());
    DotProductProofLog::compute_dotproduct(&self.Z, &chis)
  }
  ```
  其中两个 `assert_eq!` 分别判断输入点坐标 `r` 的维度是否与多项式变量数相同，若不同则无法计算，以及判断权重 `chis` 的个数与 `Z` 所记录的点数是否相同，因为一个点对应一个权重，所以必须相同，否则无法继续；`chis` 的生成逻辑为，先将 `r` 从切片转成向量，然后由其构建 `EqPolynomial` 类型对象，并进行 `.evals()` 方法对每个变量依次迭代得出所有权重值组成的列表；最后用 `DotProductProofLog::compute_dotproduct()` 进行取值和权重的对应相乘后求和得出最后的多项式扩展取值

## 不懂的知识：
- 暂无