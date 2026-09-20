# 软件工程实验 1：课程基础与实验环境搭建

本项目是《软件工程》课程实验 1 的提交成果，严格对应实验要求中的工具链配置、GitHub 仓库、Hello World、课程选题和初步实验计划。

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

## 实验计划

`PROJECT_PLAN.md` 包含课程设计流程、个人学习目标和时间分配。实验 1 的要求是这两项内容，不包含另设的“个人职责分配”表。

## GitHub 仓库

项目已发布至：

<https://github.com/Aqua196/software-engineering-experiment-1>

本地仓库已配置同名 `origin` 远程地址。提交或推送时不要把密码、访问令牌等敏感信息写入项目文件。
