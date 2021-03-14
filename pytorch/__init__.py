# pytorch
from forest._importable import LazyImport


torch = LazyImport("import torch")

tc = LazyImport("import tensor_comprehensions as tc")

## nnapi
autograd = LazyImport("import torch.autograd as autograd")
Tensor = LazyImport("from torch import Tensor")
nn = LazyImport("import torch.nn as nn")

nnLinear = LazyImport("import torch.nn.Linear as nnLinear")
Conv1d = LazyImport("import torch.nn.Conv1d as Conv1d")
Conv2d = LazyImport("import torch.nn.Conv2d as Conv2d")
Conv3d = LazyImport("import torch.nn.Conv3d as Conv3d")
MaxPool1d = LazyImport("import torch.nn.MaxPool1d as MaxPool1d")
MaxPool2d = LazyImport("import torch.nn.MaxPool2d as MaxPool2d")
MaxPool3d = LazyImport("import torch.nn.MaxPool3d as MaxPool3d")
Dropout = LazyImport("import torch.nn.Dropout as Dropout")
Dropout2d = LazyImport("import torch.nn.Dropout2d as Dropout2d")

functional = LazyImport("import torch.nn.functional as functional")
optim = LazyImport("import torch.optim as optim")
jit = LazyImport("import torch.jit as jit")


## onnx
onnx = LazyImport("import torch.onnx as onnx")


## vision
torchvision = LazyImport("import torchvision")
transforms = LazyImport("import torchvision.transforms as transforms")


## distributed

dist = LazyImport("import torch.distributed as dist ")

