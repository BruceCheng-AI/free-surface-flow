# 城市水利一维浅水矩形渠道管理仿真平台 V1.0

## 目录

- [城市水利一维浅水矩形渠道管理仿真平台 V1.0](#城市水利一维浅水矩形渠道管理仿真平台-v10)
  - [目录](#目录)
  - [1. 系统概述](#1-系统概述)
  - [2. 命令行使用方法](#2-命令行使用方法)
    - [2.1 模型仿真](#21-模型仿真)
    - [2.2 绘制动态仿真图](#22-绘制动态仿真图)
    - [2.3 打印当前边界数据](#23-打印当前边界数据)
  - [3. 图形界面使用方法](#3-图形界面使用方法)
    - [3.1 计算核心](#31-计算核心)
    - [3.2 流量动画](#32-流量动画)
    - [3.3 水位动画](#33-水位动画)

## 1. 系统概述

本系统旨在为智慧城市水利规划与管理提供详细的水流模拟工具。运河的特性，如固定长度L、规则矩形的横截面、坡度和粗糙度等，都被考虑在内。为了准确捕捉城市运河中的水流动态，本系统引入了基于Saint-Venant的一维流动方程。这些方程的解决依赖于给定的初始条件和两端的边界条件。采用了广泛认可的Preissmann方案进行数值模拟。系统提供双扫描算法和内置的矩阵求逆功能作为求解策略。为满足不同用户需求，平台分为基于python的命令行操作和直观的可视化界面。这不仅助力水文研究者和土木工程师，更有助于城市规划者、洪水管理部门和应急响应团队深入了解和预测城市水流行为，以应对潜在的洪水威胁或其他水相关的安全问题。

![系统启动的可视化界面](images/system_startup_visualization.png)

*图 1: 系统启动的可视化界面*

## 2. 命令行使用方法

### 2.1 模型仿真

运行本仿真平台，请在命令行界面中输入 `python main.py`。一旦平台启动，将会出现提示：“Please type the test number you want. (1~12)”供用户回应。已经预置了11种测试文件，这些文件代表了四种主要的测试情境：静态测试、稳态测试、瞬态测试以及假潮测试。

| 测试种类     | 文件编号        |
| ---------- | -------------- |
| 静态测试     | 1-3            |
| 稳态测试     | 4              |
| 瞬态测试     | 5-10           |
| 假潮测试     | 11             |

用户需选择测试文件后，系统将会进一步询问求解方法：“Now you should choose which method you apply, whether matrix inversion or double sweep. For matrix inversion, type 1; for double sweep, type 2. Please type the number:”。用户需要决定使用哪种求解方法：矩阵求逆（输入1）或双扫描（输入2）。

![模型仿真](images/model_simulation.png)

*图 2: 模型仿真*

### 2.2 绘制动态仿真图

计算完成后，平台会提示：“Now determine whether plot the dynamic graph.”，询问用户是否需要绘制动态仿真图。若选择绘制，用户需指定文件名，绘制的动态仿真图将以.gif格式保存在reports目录下。

![绘制动态仿真图命令](./images/draw_dynamic_simulation.png)

*图 3: 绘制动态仿真图命令*

### 2.3 打印当前边界数据

用户可以选择打印当前的边界条件，以验证模型的计算结果。数据将被保存至reports目录中，供用户进一步分析。

![打印当前边界数据](./images/print_current_boundary_data.png)

*图 4: 打印当前边界数据*

## 3. 图形界面使用方法

### 3.1 计算核心

用户可以在“Dataset”部分选择测试方案，"method"部分选择计算方法。点击“Start Calculation”按钮后，计算结果将实时显示在输出框中。

![计算核心](./images/calculation_core.png)

*图 5: 计算核心*

### 3.2 流量动画

点击“Generate Discharge Animation”按钮后，平台将生成流量变化动态图，描述“Discharge changing with distance”。

![流量动画](./images/discharge_animation.png)

*图 6: 流量动画*

### 3.3 水位动画

点击“Generate Water Level Animation”按钮后，平台将生成水位变化动态图，描述“Water level changing with distance”。

![水位动画](./images/water_level_animation.png)

*图 7: 水位动画*

---

**鹏城实验室**

版本：1.0



日期：2023年

---