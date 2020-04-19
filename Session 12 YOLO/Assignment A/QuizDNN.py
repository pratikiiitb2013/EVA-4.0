from imports_eva import *
from params import *


class QuizDNN(nn.Module):
    def __init__(self, dropout_value = 0.0):
      super(QuizDNN, self).__init__()
        
      self.convblock1 = nn.Sequential(
          nn.Conv2d(in_channels=3, out_channels=3, kernel_size=(3, 3), padding=1, bias=False),
          nn.BatchNorm2d(3),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )

      self.convblock2 = nn.Sequential(
          nn.Conv2d(in_channels=3, out_channels=3, kernel_size=(3, 3), padding=1, bias=False),
          nn.BatchNorm2d(3),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )

      self.pool1 = nn.MaxPool2d((2, 2))

      self.convblock3 = nn.Sequential(
          nn.Conv2d(in_channels=3, out_channels=3, kernel_size=(3, 3), padding=1, bias=False),
          nn.BatchNorm2d(3),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )
        
      self.convblock4 = nn.Sequential(
          nn.Conv2d(in_channels=3, out_channels=3, kernel_size=(3, 3), padding=1, bias=False),
          nn.BatchNorm2d(3),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )

      self.convblock5 = nn.Sequential(
          nn.Conv2d(in_channels=3, out_channels=3, kernel_size=(3, 3), padding=1, bias=False),
          nn.BatchNorm2d(3),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )

      self.pool2 = nn.MaxPool2d((2, 2))

      self.convblock6 = nn.Sequential(
          nn.Conv2d(in_channels=3, out_channels=3, kernel_size=(3, 3), padding=1, bias=False),
          nn.BatchNorm2d(3),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )
        
      self.convblock7 = nn.Sequential(
          nn.Conv2d(in_channels=3, out_channels=3, kernel_size=(3, 3), padding=1, bias=False),
          nn.BatchNorm2d(3),
          nn.ReLU(),
          nn.Dropout(dropout_value)
      )

      self.convblock8 = nn.Sequential(
          nn.Conv2d(in_channels=3, out_channels=3, kernel_size=(3, 3), padding=1, bias=False),
          # nn.BatchNorm2d(3),
          # nn.ReLU(),
          # nn.Dropout(dropout_value)
      )

      self.gap = nn.Sequential(
          nn.AdaptiveAvgPool2d((1,1))
      ) 

      self.linear1 = nn.Sequential(
          nn.Conv2d(in_channels=3, out_channels=500, kernel_size=(1,1), padding=0, bias=False),
      )

      self.linear2 = nn.Sequential(
          nn.Conv2d(in_channels=500, out_channels=10, kernel_size=(1,1), padding=0, bias=False),
      )

    def forward(self, x):
       x1 = x
       x2 = self.convblock1(x1)
       x3 = self.convblock2(x1 + x2)
       x4 = self.pool1(x1 + x2 + x3)
       x5 = self.convblock3(x4)
       x6 = self.convblock4(x4 + x5)
       x7 = self.convblock5(x4 + x5 + x6)
       x8 = self.pool2(x5 + x6 + x7)
       x9 = self.convblock6(x8)
       x10 = self.convblock7(x8 + x9)
       x11 = self.convblock8(x8 + x9 + x10)
       x12 = self.gap(x11)
       x13 = self.linear1(x12)
       x14 = self.linear2(x13)
       x15 = x14.view(-1, 10)
       return x15
		

		
def get_model_instance(dp):
	return QuizDNN(dropout_value = dp)