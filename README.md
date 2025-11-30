# uv项目使用指南

在讲uv前，我们先回顾一下常规的python项目管理是怎样的，拿到一个项目，我们需要用如下命令：

```shell
python -m venv .venv
```

```shell
source .venv/bin/activate
```

```shell
vim pyproject.toml
```

```shell
pip install -e .
```

然而，现在有了uv，都不需要了，只需要一句`uv add ...`或`uv sync`就可以完成。

> `uv` 是近年来新兴的一款 **轻量级、高性能、现代化的 Python 包和虚拟环境管理工具**，它的目标是部分替代 `pip`、`virtualenv`、`pip-tools`、`poetry`、`pipenv` 这类工具，提升开发者的日常体验。
>
> 下面记录一下我 **从零开始** 学习 `uv`，在 Python 项目中进行包管理的体验。

视频：https://www.bilibili.com/video/BV1ajJ7zPEa5/

## 一、uv 是什么？

`uv` 是由 [Astral](https://astral.sh) 团队开发的，用 **Rust 编写**，具有超高的性能。主要功能包括：

- 安装依赖（替代 `pip`）
- 管理虚拟环境（替代 `venv`、`virtualenv`）
- 支持 `pyproject.toml`（兼容 `poetry` 风格）
- 更快的包解析与安装（比 `pip`、`poetry` 更快）
- 支持缓存加速和并发下载

> **一句话总结：uv 是现代 Python 项目的全能包管理工具。**

**竞品比较**：

1. [pip](https://pip.pypa.io/en/stable/)：Python 的官方包管理器，功能全面，但性能较低，且需要开发者手动管理多个步骤。
2. [rye](https://github.com/astral-sh/rye)：全面且现代化的 Python 项目和包管理解决方案，整合了 python 版本管理、自动化依赖管理、python 包管理、自动化虚拟环境管理、项目初始化、python lint 等功能，适合中大型项目或团队使用。
3. [pip-tools](https://github.com/jazzband/pip-tools)：用于管理 Python 项目依赖的工具集，能帮助开发者生成、更新和锁定项目的依赖版本。
4. [pipx](https://github.com/pypa/pipx)：专门用于下载和管理 python 应用程序的工具，能下载并运行各种 Python 应用程序，且不会污染系统或项目的环境。
5. [poetry](https://python-poetry.org/)：主要用于管理 python 项目依赖、打包和发布的工具，旨在简化依赖管理，同时提供一个统一的工作流来创建和分发 Python 包。
6. [pyenv](https://github.com/pyenv/pyenv)：用于管理多个 Python 版本的工具。相较于 `uv`，`pyenv` 最大的不同是以源码编译的方式安装 python。

## 二、uv 的安装

推荐使用 pipx 安装 uv：

```shell
pipx install uv
```

> ⚠️ `pipx` 是安装命令行工具的神器，相当于全局环境下的隔离安装，推荐学习和使用。

![image-20250611202655692](https://cdn.jsdelivr.net/gh/01Petard/imageURL@main/img/202506112026764.png)

检查是否安装成功：

```shell
uv --version
```

![image-20250611202707532](https://cdn.jsdelivr.net/gh/01Petard/imageURL@main/img/202506112027565.png)

好家伙，连Git仓库都帮我们创建好了

![image-20250611202932378](https://cdn.jsdelivr.net/gh/01Petard/imageURL@main/img/202506112029417.png)

## 三、用uv搭建环境

### 查看可用python版本

```shell
uv python list
```

![image-20250611203425157](https://cdn.jsdelivr.net/gh/01Petard/imageURL@main/img/202506112034196.png)

### 安装python

```shell
uv python install [python_version]
```

![image-20250611203433768](https://cdn.jsdelivr.net/gh/01Petard/imageURL@main/img/202506112034797.png)

### 初始化新项目

新项目的目录下会生成 `pyproject.toml`、`.python-version` 文件。

```shell
uv init [项目名]
```

![image-20250611203518214](https://cdn.jsdelivr.net/gh/01Petard/imageURL@main/img/202506112035253.png)

### 同步依赖

根据 `pyproject.toml` 安装或更新依赖

```shell
uv sync
```

![image-20250611204849517](https://cdn.jsdelivr.net/gh/01Petard/imageURL@main/img/202506112048568.png)

### 安装依赖

相比于 `pip install`，`uv add` 提供了更高层次的自动化，能自动管理虚拟环境和更新 `pyproject.toml` 文件。

```shell
uv add [module]
```

![image-20250611203251672](https://cdn.jsdelivr.net/gh/01Petard/imageURL@main/img/202506112032702.png)

### 查看依赖树

相比于 `pip list`提供了更详细的依赖关系信息，且能以树状结构展示。

```shell
uv tree
```

![image-20250611203723249](https://cdn.jsdelivr.net/gh/01Petard/imageURL@main/img/202506112037282.png)

### 移除依赖

相比于 `pip uninstall`更智能，在卸载指定包后，还会检测并删除未使用的依赖项。

```shell
uv remove [module]
```

![image-20250611203939503](https://cdn.jsdelivr.net/gh/01Petard/imageURL@main/img/202506112039541.png)

## 四、用uv运行项目

### 临时运行项目或脚本

可以在不显式激活虚拟环境的情况下，在项目的虚拟环境中执行任何命令或脚本。

```shell
uv run [.py]
```

![image-20250611204650497](https://cdn.jsdelivr.net/gh/01Petard/imageURL@main/img/202506112046549.png)

### 安装/卸载命令行工具

安装后这些工具会被自动放进 `.venv/bin/`（或 Windows 下的 `Scripts/`），可直接用。

安装：

```shell
uv tool instal [...]
```

![image-20250611205101623](https://cdn.jsdelivr.net/gh/01Petard/imageURL@main/img/202506112051651.png)

卸载：

```shell
uv tool uninstall [...]
```

![image-20250611205634844](https://cdn.jsdelivr.net/gh/01Petard/imageURL@main/img/202506112056879.png)

### 创建临时虚拟环境

是 `uv tool run` 的简写，能调用 Python 包中的实用工具，并且不会影响当前项目环境，类似于 `pipx`。

```shell
uvx
```

![image-20250611205738330](https://cdn.jsdelivr.net/gh/01Petard/imageURL@main/img/202506112057376.png)

### 运行临时脚本

```shell
uv init --script [.py]
```

![image-20250611210119114](https://cdn.jsdelivr.net/gh/01Petard/imageURL@main/img/202506112101157.png)

修改文件，添加必需依赖

![image-20250611210136700](https://cdn.jsdelivr.net/gh/01Petard/imageURL@main/img/202506112101723.png)

```shell
uv run [.py]
```

![image-20250611210153367](https://cdn.jsdelivr.net/gh/01Petard/imageURL@main/img/202506112101421.png)

### 将项目的锁文件导出为其他格式

将项目的锁文件导出为其他格式，如 `requirements.txt`。

```shell
uv export
```

![image-20250611204343735](https://cdn.jsdelivr.net/gh/01Petard/imageURL@main/img/202506112043775.png)
