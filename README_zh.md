# Eml Playground

一个交互式数学学习环境，用于通过符号操作和可视化表达式合成探索 `eml(x, y) = e^x - log(y)` 函数。

## 概述

Eml Playground 是一个基于 PyQt6 和 SymPy 构建的桌面应用程序，提供直观的拖放界面用于构建数学表达式。核心焦点是 `eml` 函数（指数减对数），但系统通过 SymPy 的符号代数能力支持广泛的数学运算。

该应用程序设计为一个教育工具，用于通过指导性任务探索函数组合、符号简化和数学发现。

## 功能特性

- **交互式表达式构建**：通过拖放界面从基本组件构建复杂表达式
- **符号计算**：基于 SymPy 提供精确的数学简化和求值
- **任务系统**：渐进式挑战，引导用户进行数学发现
- **表达式库存**：保存和重用已发现的表达式
- **LaTeX 渲染**：实时 LaTeX 渲染，提供优美的数学排版
- **持久化存储**：自动保存进度和库存
- **可扩展架构**：自定义函数定义（eml, sigmoid）并完全集成 SymPy

## 安装

### 前提条件

- Python 3.8 或更高版本
- pip（Python 包管理器）

### 步骤

1. 克隆仓库：
   ```bash
   git clone <仓库地址>
   cd EmlPlayground
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. 运行应用程序：
   ```bash
   python main.py
   ```

## 使用方法

1. **启动应用程序**：运行 `python main.py` 启动 Eml Playground。

2. **理解界面**：
   - **顶部面板**：当前任务和目标表达式
   - **左侧面板**：表达式库存（从此处拖拽）
   - **右侧面板**：合成区域（将表达式拖放到此处）

3. **完成任务**：
   - 从库存拖拽表达式到合成区域
   - 填充表达式槽以构建复合表达式
   - 点击“Synthesize”进行求值并发现新表达式
   - 成功创建的表达式将添加到库存中

4. **逐步挑战**：
   - 任务面板显示当前目标（E, exp(x), log(x) 等）
   - 每个发现的表达式解锁新的数学可能性
   - 系统引导您从基础到高级数学概念

## 项目结构

```
EmlPlayground/
├── main.py                 # 应用程序入口点
├── Eml.py                  # 核心 eml 函数定义
├── EmlPlaygroundWidget.py  # 主应用程序窗口
├── InventoryWidget.py      # 表达式库存面板
├── ExpressionWidget.py     # 交互式表达式部件
├── ExpressionSlotWidget.py # 拖放表达式槽
├── SynthesisWidget.py      # 表达式合成区域
├── TaskWidget.py          # 任务/挑战系统
├── SymbolsWidget.py       # 符号选择面板
├── LatexRenderer.py       # LaTeX 到 pixmap 渲染
├── Sigmoid.py             # Sigmoid 函数定义
├── Archive.py             # 进度保存/加载
├── style.qss              # Qt 样式表
├── requirements.txt       # Python 依赖
└── save.yaml              # 用户进度（自动生成）
```

## 依赖项

- **PyQt6**：GUI 框架
- **SymPy**：符号数学库
- **Matplotlib**：LaTeX 渲染后端
- **PyYAML**：进度序列化

具体版本请参见 `requirements.txt`。

## 开发

### 添加新函数

系统设计为可扩展。要添加新的自定义函数：

1. 按照 `Eml.py` 或 `Sigmoid.py` 的模式创建新文件
2. 定义具有适当求值规则的 SymPy `Function` 子类
3. 在相关部件中导入并注册函数

### 代码风格

- 遵循 PEP 8 约定
- 使用描述性变量名
- 为公共方法添加文档字符串
- 鼓励使用类型提示但不强制要求

### 测试

运行应用程序并验证：
- 表达式拖拽正常工作
- 合成产生数学上正确的结果
- 任务按预期进展
- 进度正确保存和加载

## 许可证

本项目是开源的，采用 MIT 许可证。

## 贡献

欢迎贡献！请随时提交 Pull Request。

1. Fork 本仓库
2. 创建功能分支
3. 进行更改
4. 彻底测试
5. 提交 pull request

## 致谢

- 基于 [SymPy](https://www.sympy.org/) 构建符号数学功能
- GUI 由 [PyQt6](https://www.riverbankcomputing.com/software/pyqt/) 提供支持
- LaTeX 渲染通过 [Matplotlib](https://matplotlib.org/) 实现
- 灵感来源于交互式数学探索工具

## 联系

如有问题或反馈，请在项目仓库中提交 issue。