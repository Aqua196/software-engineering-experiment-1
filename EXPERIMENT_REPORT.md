# 实验 1：课程基础与实验环境搭建

## 一、实验目的

熟悉工具链，理解实验体系与软件工程流程。

## 二、核心内容与完成情况

### 1. 安装配置相关工具

已检查 Python、Git、Visual Studio Code、Python `unittest` 以及 Markdown/Mermaid 文档工具，均可用于本实验。

### 2. 注册 GitHub 账号并创建实验仓库

已使用 GitHub 账号 Aqua196 创建公开实验仓库：

<https://github.com/Aqua196/software-engineering-experiment-1>

### 3. 编写并提交 Hello World 程序

在 `hello.py` 中实现 `greeting()` 和 `main()`，运行结果为 `Hello, World!`；程序和测试文件已提交到本地 Git 仓库及 GitHub 仓库。

### 4. 阅读课程第一章节并自主选题

结合软件工程课程第一章节关于软件过程和质量保证的内容，确定课程设计主题为“个人任务管理系统”。详细主题说明见 `PROJECT_PLAN.md`。

### 5. 安排课程设计流程并撰写初步计划

`PROJECT_PLAN.md` 已列出课程设计流程、个人学习目标和 8 周时间分配，总投入约 40 小时。

## 三、实验环境与工具验证

| 类别 | 工具与版本 | 用途 | 验证结果 |
|---|---|---|---|
| 编程语言 | Python 3.13.15 | 编写和运行程序 | 正常 |
| 版本控制 | Git 2.50.1 | 记录代码变更 | 正常 |
| IDE | Visual Studio Code | 代码编辑与调试 | 命令行入口可用 |
| 测试工具 | unittest（Python 标准库） | 自动化测试 | 2 项测试通过 |
| 建模方式 | Mermaid / Markdown | 后续绘制流程图与结构图 | 无需额外安装 |

## 四、运行与提交验证

### 1. 运行 Hello World

运行命令：

```bash
python3 hello.py
```

实际输出：

```text
Hello, World!
```

### 2. 编写并运行测试

测试覆盖两类行为：

- `greeting()` 的返回值必须为 `Hello, World!`；
- 从命令行运行程序时，标准输出必须为 `Hello, World!` 并正常退出。

执行命令：

```bash
python3 -m unittest discover -s tests -v
```

测试结果：

```text
Ran 2 tests
OK
```

### 3. 使用 Git 记录实验过程

实验按“仓库初始化—功能实现—文档与计划—GitHub 发布记录”拆分提交，使每次提交目标单一、历史清晰。可通过以下命令查看：

```bash
git log --oneline --decorate
```

提交记录如下：

```text
638bd22 chore: initialize experiment repository
a4b11ca feat: add tested Hello World program
49f320d docs: add experiment report and project plan
151ce6d docs: record GitHub publication
```

## 五、实验要求核对

| Word 文档中的实验要求 | 核对结果 |
|---|---|
| 工具能正常运行，仓库提交记录完整 | Python、Git、IDE 和测试均已验证；本地与 GitHub 仓库均有分阶段提交记录 |
| 实验计划包含个人学习目标与时间分配 | `PROJECT_PLAN.md` 已列出 5 项个人学习目标和 8 周/40 小时初步时间分配 |

## 六、实验结果

| 检查项 | 结果 |
|---|---|
| Python 程序可运行 | 通过 |
| 输出符合预期 | 通过 |
| 自动化测试 | 2/2 通过 |
| 本地 Git 仓库 | 已建立 |
| 提交记录 | 按阶段保存 |
| GitHub 公开仓库 | 已创建并上传实验文件 |
| 课程设计选题 | 已确定 |
| 个人学习目标 | 已列出 |
| 时间分配 | 已完成 |

## 七、问题与解决办法

1. 当前环境未安装 GitHub CLI，因此先完成本地仓库和全部提交，再通过 GitHub 网页创建公开仓库并上传实验成果。
2. 为避免引入环境差异，Hello World 与测试只使用 Python 标准库，不依赖第三方包。

## 八、实验总结

本次实验按 Word 文档列出的五项任务完成了工具配置、GitHub 仓库、Hello World、课程选题和初步实验计划。报告中的计划明确包含个人学习目标和时间分配，实验结果可由程序运行、自动化测试和 Git 提交记录复核，并为后续个人任务管理系统的需求分析建立基础。
