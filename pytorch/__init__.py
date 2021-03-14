# pytorch
from ._importable import LazyImport, _import_statements


torch = LazyImport("import torch")

tc = LazyImport("import tensor_comprehensions as tc")