# 软件工程实验 1：课程基础与实验环境搭建

本项目是《软件工程》课程实验 1 的提交成果，用于验证编程环境、Git 工作流和基础测试流程。

## 环境

- 操作系统：macOS
- Python：3.13.15
- Git：2.50.1
- 编辑器：Visual Studio Code（命令行工具可用）

## 项目结构

```text
.
├── hello.py                 # Hello World 程序
├── tests/test_hello.py      # 自动化测试
├── EXPERIMENT_REPORT.md     # 实验报告
└── PROJECT_PLAN.md          # 课程设计初步计划
```

## 运行

```bash
python3 hello.py
```

预期输出：

```text
Hello, World!
```

## 测试

```bash
python3 -m unittest discover -s tests -v
```

## GitHub 发布

在 GitHub 网页中新建空仓库后执行：

```bash
git remote add origin https://github.com/<你的用户名>/software-engineering-experiment-1.git
git branch -M main
git push -u origin main
```

请将 `<你的用户名>` 替换为自己的 GitHub 用户名。不要把密码或访问令牌写入项目文件。
