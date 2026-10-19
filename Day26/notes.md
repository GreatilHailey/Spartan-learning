# 日期：2026-10-16

## 今天的目标：
- 理解基础 sum-check 的流程
- 手算第一轮
- 定位官方代码入口

## 实际完成：
- 根据 D25 实例理解 sum-check 流程
- 延续 D25 的示例，对其背景下的 sum-check 问题进行了计算
- 阅读了源码，明确了 sum-check 代码接口与 R1CS 证明调用接口

## 成果
- 实例计算
- 教学模数：$17$
- 初始目标：$H = 9$
- 第一轮多项式：$g_1(t) = 8 + 10t$
- 一致性检查：$g_1(0) + g_1(1) = 8 + 1 = 9$
- 假设本次挑战 $r_1 = 2$，则下一轮目标为 $g_1(2) = 11$

## 对今天的理解：
- sum-check 用来验证一个多变量多项式在全部布尔位置上的取值之和是否等于证明者声称的 $H$；本次以 MLE 为例，第一轮给出 $g_1(t)=\widetilde f(t,0)+\widetilde f(t,1)$，验证者先检查其次数是否符合约定，以及 $g_1(0)+g_1(1)=H$ 是否成立，随后选择挑战，继续缩小问题，最终还需要核对原多项式的一次求值才算整套证明流程结束
- 官方源码如下：
  ```Rust
  pub struct SumcheckInstanceProof {
    compressed_polys: Vec<CompressedUniPoly>,
  }
  
  impl SumcheckInstanceProof {
    pub fn new(compressed_polys: Vec<CompressedUniPoly>) -> SumcheckInstanceProof {
      SumcheckInstanceProof { compressed_polys }
    }
  
    pub fn verify(
      &self,
      claim: Scalar,
      num_rounds: usize,
      degree_bound: usize,
      transcript: &mut Transcript,
    ) -> Result<(Scalar, Vec<Scalar>), ProofVerifyError> {
      let mut e = claim;
      let mut r: Vec<Scalar> = Vec::new();
  
      // verify that there is a univariate polynomial for each round
      assert_eq!(self.compressed_polys.len(), num_rounds);
      for i in 0..self.compressed_polys.len() {
        let poly = self.compressed_polys[i].decompress(&e);
  
        // verify degree bound
        assert_eq!(poly.degree(), degree_bound);
  
        // check if G_k(0) + G_k(1) = e
        assert_eq!(poly.eval_at_zero() + poly.eval_at_one(), e);
  
        // append the prover's message to the transcript
        poly.append_to_transcript(b"poly", transcript);
  
        //derive the verifier's challenge for the next round
        let r_i = transcript.challenge_scalar(b"challenge_nextround");
  
        r.push(r_i);
  
        // evaluate the claimed degree-ell polynomial at r_i
        e = poly.evaluate(&r_i);
      }
  
      Ok((e, r))
    }
  }
  ```
  其中 `assert_eq!(poly.eval_at_zero() + poly.eval_at_one(), e);` 用来检查 $g_1(0) + g_1(1) \overset?= e$ ，其中 $e$ 保存当前轮的求和目标，初始为 claim，即 $H$，每轮结束后，更新为 $g_i(r_i)$，供下一轮检查使用；本例第一轮开始时 e = 9，结束后变成 11；而 `let r_i = transcript.challenge_scalar(b"challenge_nextround");` 用来使用 `transcript` 生成本轮的挑战点；`e = poly.evaluate(&r_i)` 则是用来计算本轮多项式在挑战点的值，并将其作为下一轮目标值
- 源码整体流程如下：
  - 先用 `decompress(&e)` 来利用当前的目标值恢复本轮中压缩存储的单变量多项式
  - 检查多项式的次数，并且检查在当前多项式在 0, 1 处之和是否等于目标值
  - 将本轮多项式写入 `transcript` 
  - 从更新后的 `transcript` 得到本轮的挑战点 `r_i` 
  - 最后计算本轮多项式在挑战点的值 `poly.evaluate(&r_i)`，并将该值作为下一轮的目标值 
- 通过阅读 R1CS 证明的 sum-check 入口相关源码，发现其在实际应用过程中调用的为 `ZKSumcheckInstanceProof` 接口，即零知识版本，其结构如下：
  ```Rust
  pub struct ZKSumcheckInstanceProof {
    comm_polys: Vec<CompressedGroup>,
    comm_evals: Vec<CompressedGroup>,
    proofs: Vec<DotProductProof>,
  }
  ```
  其中 `comm_polys` 是各轮多项式的承诺，`comm_evals` 是相关求值的承诺，`proofs` 是配套的点积证明

## 不懂的知识：
- `ZKSumcheckInstanceProof` 结构中的 `comm_evals` 和 `proofs` 的具体作用和内容还不是很明白