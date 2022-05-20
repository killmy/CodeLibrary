### 简介 
一些深度学习的库，记录一些容易遗忘的东西，不一定有用，但是无聊时候的记录,多记录

### Basic
一些可能会用到的东西
#### check
1. ParamsFlops()
   ```python
   __init__(self,,model,input)->None
   计算模型的参数量和浮点数运算量
   params()->float
   flops()->float
   paramsflops->tuple
   getmodel()->dict
   getinput()->tensor
   ```
2. ModelConstruction(model,input,mod)
   生成模型结构图，mod选择生成的方式
#### lrfunction
各种学习率函数+优化器

#### evaluatefunction
各种评估指标函数

#### savesomething
各种东西的保存函数

### Dataset
只读取最原始的数据集

#### ObjectDetectionDataset
目标检测的几种数据集读取方式

#### ClassficationDataset
分类数据集的读取方式

#### TrackDataser
跟踪数据集的读取方式

### Temple
#### train
训练的模板

### 变成技巧
#### class 
class中函数名function不能与返回的变量一样self.function``` 这时候self.function 就是代表function函数```