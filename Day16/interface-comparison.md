| 比较项 | SNARK | NIZK |
|---|---|---|
| 参数生成入口及规模参数 | `SNARKGens::new(num_cons, num_vars, num_inputs, num_non_zero_entries);` | `NIZKGens::new(num_cons, num_vars, num_inputs);` |
| 是否单独调用计算结构承诺 `encode` | 是 | 否 |
| `prove` 使用的主要数据 | `R1CS约束结构`, `承诺`, `承诺配套信息`, `私有见证值`, `公开输入值`, `公共参数 gens`, `证明者 transcript` | `R1CS约束结构`, `私有见证值`, `公开输入值`, `公共参数 gens`, `证明者 transcript` |
| `verify` 使用的主要数据，包括证明本身 | `proof 本身`, `承诺`, `公开输入值`, `验证者 transcript`, `公共参数 gens` | `proof 本身`, `R1CS约束结构`, `公开输入值`, `验证者 transcript`, `公共参数 gens` |