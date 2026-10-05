# 日期：2026-10-03

## 今天的目标：
- 重跑正反例
- 整理重跑记录
- 独立讲述流程

## 实际完成：
- 重跑 D19 的正反对照
- 自己讲一遍流程

## 成果
- 将公开输入源码保存在为 `Day20/public-input-source.rs` 
- 重跑输出仍然通过，并且退出码为 `0` ，结论正确
- 将重跑对照的输出日志保存到了 `Day20/logs/public-input-01.log` ，并且保存了退出码到 `Day20/logs/public-input-01-exit.log` 

## 对今天的理解：
- `inst` 提供 R1CS 约束结构， 私有见证提供约束中的私有见证值，即 `z_i` 的值，公开输入提供约束中公开输入的值，即 `I_i` 的值 
- `new` 生成了 SNARK 的公共参数 `gens` ,然后利用 `encode` 生成承诺 `comm` 和承诺配套信息 `decomm` ，其中 `decomm` 供证明生成使用，然后利用 `prove` 配合 prover 的 transcript 生成了证明，最后利用 `proof.verify()` 配合 verifier 的 transcript 进行了验证 
- D18 的负例停在了满足性后的断言处，整体位于 R1CS 示例构建内，所以无法正常退出；但 D19 专门利用 `.is_err()` 来检测是否拒绝，此处拒绝反而满足断言，故可以返回 `0`

## 不懂的知识：
- 暂无