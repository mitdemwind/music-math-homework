<h1 align=center>《音乐与数学》 实验报告</h1>

**<p align=center>组号：4-25 <br/> 研究题: 机器作曲·遗传算法</p>**
**<p align=center>诸子瑜 孙靖皓 张洋 徐艺宁 陈风凌</p>**

---

## 实验概述

机器作曲是近年来人工智能领域的一个热门研究方向，
其中遗传算法被广泛应用于生成音乐旋律。
本实验旨在通过遗传算法生成音乐旋律，
通过对初始种群的遗传迭代，
探讨适应度函数的选取对最终音乐特性和算法效率的影响。

#### 成员分工

- **代码框架与训练**：陈风凌
- **音乐片段选取**：徐艺宁
- **数据预处理**：孙靖皓
- **适应度函数设计**：诸子瑜
- **代码内容完善**：张洋
- **实验报告**：共同完成

## 实验流程概述

#### 工具与使用方法

我们使用 Python 语言中的 `music21` 第三方库来实现数据与乐谱之间的转换，
并用 `numpy` 库进行数据处理。

首先请确保 Python 版本在 `3.10` 或以上，
在终端输入 `python3 -V` 可以查看 Python 版本。
为安装必要的依赖，打开工作目录在终端执行
``` sh
pip install -r requirements.txt
```

我们使用 `.musicxml` 格式来储存乐谱文件，并使用 MuseScore 软件
查看乐谱和以 midi 形式播放乐谱。可以在其[官网](https://www.musescore.org)下载
安装最新版本的 MuseScore。

#### 遗传算法简述

遗传算法（Genetic Algorithm, GA）是模拟达尔文生物进化论的自然选择
和遗传学机理的生物进化过程的计算模型，
是一种通过模拟自然进化过程搜索最优解的方法。

在模拟种群的迭代中，我们实现了对个体的交叉 (crossover), 变异 (mutation) 等操作。

- **交叉**操作：对于两个乐曲片段，我们随机选取一个截断点 $i$，
  将一个乐曲片段的前 $i$ 小节和另一片段的 $i$ 小节之后进行拼接。

- **变异**操作：包括改变单个音符音高、改变节奏型，以及对旋律进行
  移调 (translation)、倒影 (inversion)、逆行 (retrogration) 变换等。

#### 初始种群选取

我们结合 “从具有相同节拍的若干歌曲、
乐曲中选取十个长度相等的片段” 与 “随机生成” 两种方法产生初始种群。
我们选定节拍为大多数流行歌曲采用的 4/4 拍。为了保证旋律完整性，将长度设置为八小节。
同时为保证调性一致，方便后续处理，将所有乐曲片段都进行了移调处理，
得到 C 大调的初始种群。

在选择歌曲片段方面，主要考虑了节奏和旋律的丰富度，
尽量减少样本内部的旋律重复。
同时，选取了包含古典音乐、流行音乐在内的多种音乐风格，
如《D 大调卡农》、《青花瓷》等，使得初始种群的丰富度提高。

#### 设计适应函数

在遗传算法中，一个核心问题就是适应函数 (fitness function) 的设计。
在进一步学习乐理知识之后，我们设计了如下适应函数。

## 代码实现及各模块说明

我们的代码由 `main.py`, `population.py`, `preprocess.py`,
`constants.py`, `utils.py`, `randmusic.py`, `fitfunction.py` 组成。
其中 `constants.py` 定义了一些全局变量和文件路径，`utils.py` 中实现了
一些简单的帮助函数。

#### 数据处理

该模块主要在文件 `preprocess.py` 中实现。
我们定义了用于转换数据格式的 `Converter` 类。

#### 随机生成旋律

该模块主要在文件 `randmusic.py` 中实现。

#### 遗传算法

该模块主要在文件 `population.py` 中实现。
我们定义了用于模拟个体和种群的 `Individual` 类和 `Population` 类。

- **`Individual`类**

  该类用于模拟遗传算法中的个体，即一个音乐片段。
  每个个体包含一个二维数组 (`melody`），用于表示音符的音高和时值。
  ```py
  class Individual:

      def __init__(self, melody: np.ndarray):
          try:
              self.melody = np.array(melody)
          except Exception as e:
              print("Error when casting melody to numpy array")
             raise e
  ```

- **`Population`类**

  该类用于模拟遗传算法中的种群，它包含一个个体列表以及适应度函数、变异率等属性。
  ```py
  class Population:

    def __init__(self, members: list[Individual],
            fitfunc: callable, mutate_rate: float):
        self._members = members
        self.fitfunc = fitfunc
        self.mutate_rate = mutate_rate
        self._adaptibilty = np.array(list(map(self.fitfunc, self._members)))
  ```

#### 适应度函数

该模块主要在文件 `fitfunction.py` 中实现。
其中适应函数由 `FitFunction` 类的 `__call__` 方法实现。

#### 添加和弦伴奏

该模块主要在文件 `population.py` 中实现。

## 实验结果
