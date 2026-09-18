# 日期：2026-09-18

## 今天的目标：
- 初步了解分支的多种操作

## 实际完成：
- 新建了 practice/day05-git 分支
- 在新分支中对文件内容进行了修改
- 在新分支中完成了提交并且合并到了原分支

## 成果
- \## practice/day05-git

## 对今天的理解：
- 通过 git commit 提交本地，再用 git push -u origin practice/day05-git 将分支送到远程
- -u 代表增加本地分支与远程分支的追踪关系
- origin 为建立 git 仓库时配置的远程地址
- 对于一个分支，首次建立并提交，在送到远程时必须要利用 git push -u 来建立远程追踪关系，后续更改只需用 git push 即可
- 提交后的仓库结构为在 origin 下 practice/day05-git 与 main 分支并列
- 由于创建 practice/day05-git 分支时是从 main 的当前提交出发，故其共享 main 分支中原有的各个文件
- 后续可用 git merge 进行合并

## 不懂的知识：
- 暂无