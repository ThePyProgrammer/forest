# image
from forest._importable import LazyImport


Image = LazyImport("from PIL import Image")
PIL = LazyImport("import PIL")