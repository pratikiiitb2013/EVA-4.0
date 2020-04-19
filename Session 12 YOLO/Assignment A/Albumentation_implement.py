from imports_eva import *
from params import *

class Albumentation_implement:
  def __init__(self, transform_list):
    self.transforms = A.Compose(transform_list)

  def __call__(self, img):
    img = np.array(img)
    img = self.transforms(image=img)
    return img['image']