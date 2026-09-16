# 日期：2026-09-16

## 今天的目标：
- 初步学习如何保存日志

## 实际完成：
- 学会了简单利用 Shell 命令行结合管道和重定向对程序记录日志
- 学会基本管道用法
- 学会了重定向的基本用法
- 学会了基本文件描述符重定向用法

## 成果
- 对 Day01/practice.py 利用 Shell 命令行 (例如 ```printf '3\n4\n12\n' | python3 Day01/practice.py > Day03/logs/check-valid-01.log 2>&1```)进行了不同组输入并记录了日志结果：
- 输入 '3\n4\n12\n' 并利用重定向将输出结果记录到了 Day03/logs/check-valid-01.log 中
- 输入 'abc\n4\n12\n' 并利用文件描述符重定向将 stderr 一并输入到了 Day03/logs/check-error-02.log 中
- 输入 '3\n4\n13\n' 并利用重定向将输出结果记录到了 Day03/logs/check-unsatisfied-01.log 中

## 对今天的理解：
- 学会了利用 Shell 命令行运行程序
-  | 是管道，其作用为将左侧命令的标准输出传给右侧命令的标准输入，在此处是将左侧 printf 命令输出的字符串传到 Day01/practice.py 的输入中
-  \> 是输出重定向，其作用是将 Python 程序的 stdout 写入文件，在此处是将 Day01/practice.py 的 stdout 放入 Day03/logs/check-xxx-xx.log 中
-  2>&1 是文件描述符重定向，其作用是将 2 代表的 stderr 重定向指到 &1 代表的 stdout 的位置 ，在此处是将 Day01/practice.py 的 stderr 也一并写进 log 中，注意此处由于 2 在文件描述符重定向 \> 之前，故 Shell 会默认 2 是文件描述符，所以不用加 & 来代表 2 是文件描述符；而 1 由于在 \> 之后，故必须加上 &1 表示 stdout 文件描述符而不是一个名为 1 的文件

## 不懂的知识：
- 暂无，该日内容量较少