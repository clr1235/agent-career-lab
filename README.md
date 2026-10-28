# agent-career-lab

基于 Python 3.12 和 [uv](https://docs.astral.sh/uv/) 管理的 Python 应用项目。目前项目提供一个命令行入口，运行后会打印欢迎信息；可以在此基础上继续添加课程练习和功能。

## 环境要求

- Python `>=3.12,<3.13`
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

项目通过 `.python-version` 指定 Python 3.12，并在 `pyproject.toml` 中限制兼容版本范围。

## 快速开始

在项目根目录执行：

```bash
# 如本机尚未安装 Python 3.12，可使用 uv 安装
uv python install 3.12

# 根据 uv.lock 创建或同步虚拟环境及依赖
uv sync

# 确认 Python 版本
uv run python --version

# 运行命令行程序
uv run agent-career-lab
```

当前命令行程序会输出：

```text
Hello from agent-career-lab!
```

## 开发命令

项目将 pytest 和 Ruff 配置为开发依赖，可通过 `uv run` 在项目环境中调用：

```bash
# 运行代码检查
uv run ruff check .

# 运行测试（添加测试后使用）
uv run pytest
```

## 项目结构

```text
.
├── README.md
├── pyproject.toml          # 项目元数据、Python 版本和依赖配置
├── uv.lock                 # 锁定依赖版本
├── .python-version         # 指定 Python 3.12
└── src/
    └── agent_career_lab/
        └── __init__.py     # 应用入口 main()
```

命令行入口在 `pyproject.toml` 的 `[project.scripts]` 中声明为 `agent-career-lab`，实现位于 `src/agent_career_lab/__init__.py`。

## 项目配置

- Python 版本范围：`>=3.12,<3.13`
- 运行时依赖：暂无
- 开发依赖：pytest、Ruff
