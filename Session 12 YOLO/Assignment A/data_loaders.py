from imports_eva import *
from params import *
from Albumentation_implement import *
from torch.utils.data import Dataset

'''
try:
	with open("params.json") as f:
		params = json.load(f)
except IOError as e:
	raise e
'''

train_transform_list = []
test_transform_list = []

class AddGaussianNoise(object): 
 def __init__(self, mean=0., std=1.): 
      self.std = std 
      self.mean = mean 

 def __call__(self, tensor): 
      return tensor + torch.randn(tensor.size()) * self.std + self.mean 

 def __repr__(self): 
      return self.__class__.__name__ + '(mean={0}, std={1})'.format(self.mean, self.std)

#class train_albumentation:
#  def __init__(self):
#    self.albumentation_transform = A.Compose(train_transform_list)
#
#  def __call__(self, img):
#    img = np.array(img)
#    img = self.albumentation_transform(image=img)
#    return img['image']
#
#class test_albumentation:
#  def __init__(self):
#    self.albumentation_transform = A.Compose(test_transform_list)
#
#  def __call__(self, img):
#    img = np.array(img)
#    img = self.albumentation_transform(image=img)
#    return img['image']
      
class CustomDataset(Dataset):
    def __init__(self, data,labels, transform=None):
        self.data = data
        self.labels = labels
        self.transform = transform
        print("Training Data Shape:{}".format(self.data.shape))
        print("Training Label Shape:{}".format(self.labels.shape))
    
    def __len__(self):
        len_data = self.data.shape[0]
        return len_data
    
    def __getitem__(self, index):
        image = self.data[index]
        #image_tensor = torch.FloatTensor(image)
        # img =torch.from_numpy(image)
        # print("sape of image is:{}".format(img.shape))
        y_label = self.labels[index]
        
        if self.transform:
            image = self.transform(image)
            # print(image) 
        return image, y_label

def train_test_loaders(bs = params["batch_size"], train_dt = None, train_lbls = None, test_dt = None, test_lbls = None):
  transform_names =  [k for k,v in params["transforms"][params["transform_library"]].items() if v is True]
  
  for t in transform_names:
    if params["transform_library"] == "albumentation":
      train_transform_list.append(getattr(A, t)(**params['transform_values'][params["transform_library"]][t]))
    else:
      train_transform_list.append(getattr(transforms, t)(**params['transform_values'][params["transform_library"]][t]))
      
  if params["transform_library"] == "albumentation":
    train_transform_list.append(A.Normalize(**params[params["dataset"] + '_normalize_values']))
    train_transform_list.append(ToTensor())
#    train_transform_list.append(A.GaussNoise(var_limit=1.0))
    test_transform_list.append(A.Normalize(**params[params["dataset"] + '_normalize_values']))
    test_transform_list.append(ToTensor())
    if params["custom_data"]:
        trainset = CustomDataset(train_dt, train_lbls, Albumentation_implement(train_transform_list))
        testset = CustomDataset(test_dt, test_lbls, Albumentation_implement(test_transform_list))
    else:
        trainset = getattr(datasets, params["dataset"])(root='./data', train=True,
                                  download=True, transform=Albumentation_implement(train_transform_list))
        testset = getattr(datasets, params["dataset"])(root='./data', train=False,
                                  download=True, transform=Albumentation_implement(test_transform_list))
    # print('Train Images count', len(trainset))
    # print('Test Images count', len(testset))
  else:
    train_transform_list.append(transforms.ToTensor())
    train_transform_list.append(transforms.Normalize(**params[params["dataset"] + '_normalize_values']))
    train_transform = transforms.Compose(train_transform_list)
    trainset = getattr(datasets, params["dataset"])(root='./data', train=True, 
                                          download=True, transform=train_transform)
    test_transform = transforms.Compose([transforms.ToTensor(), 
                          transforms.Normalize(**params[params["dataset"] + '_normalize_values'])])
    testset = getattr(datasets, params["dataset"])(root='./data', train=False,
                                          download=True, transform=test_transform)



  trainloader = torch.utils.data.DataLoader(trainset, batch_size=bs,
                                            shuffle=True, num_workers=params["n_workers"])
  testloader = torch.utils.data.DataLoader(testset, batch_size=bs,
                                          shuffle=False, num_workers=params["n_workers"])
  return trainloader, testloader