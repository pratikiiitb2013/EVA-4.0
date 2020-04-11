from imports_eva import *


class Net(nn.Module):
    def __init__(self, dropout_value=0.0):
        super(Net, self).__init__()

        # INPUT BLOCK
        self.convblock11 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=(3, 3), padding=1, bias=False),
            nn.BatchNorm2d(32),
            nn.ReLU(),  # 32
            nn.Dropout(dropout_value)
        )

        # CONV BLOCK 1
        self.convblock12 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(3, 3), padding=1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),  # 32
            nn.Dropout(dropout_value)
        )

        self.convblock13 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=(3, 3), padding=1, bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU(),  # 32
            nn.Dropout(dropout_value)
        )

        # TRANSITION BLOCK 1
        self.pool1 = nn.MaxPool2d((2, 2))  # 16
        self.convblock21 = nn.Sequential(
            nn.Conv2d(in_channels=128, out_channels=32, kernel_size=(1, 1), padding=0, bias=False),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.Dropout(dropout_value)
        )  # 16

        # CONV BLOCK 2
        self.depthwise = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=(3, 3), padding=1, groups=32, bias=False),
            # 16*16*32
            # nn.Dropout(0.25),
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(1, 1)),  # 16*16*64
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Dropout(0.2)
        )

        self.convblock23 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=(3, 3), padding=1, bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.Dropout(dropout_value)
        )  # 16

        # TRANSITION BLOCK 2
        self.pool2 = nn.MaxPool2d(2, 2)  # 8
        self.convblock31 = nn.Sequential(
            nn.Conv2d(in_channels=128, out_channels=32, kernel_size=(1, 1), padding=0, bias=False),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.Dropout(dropout_value)
        )  # 8

        # CONV BLOCK 3
        self.convblock32 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(3, 3), padding=1, bias=False, dilation=2),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Dropout(dropout_value)
        )  # 8 6

        self.convblock33 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=(3, 3), padding=1, bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.Dropout(dropout_value)
        )  # 8 6

        # TRANSITION BLOCK 3
        self.pool3 = nn.MaxPool2d(2, 2)  # 4 3
        self.convblock41 = nn.Sequential(
            nn.Conv2d(in_channels=128, out_channels=32, kernel_size=(1, 1), padding=0, bias=False),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.Dropout(dropout_value)
        )  # 4 3

        # CONV BLOCK 4
        self.depthwise2 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=(3, 3), padding=1, groups=32, bias=False),
            # 16*16*32
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(1, 1)),  # 16*16*64
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Dropout(dropout_value)
        )

        self.convblock43 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=90, kernel_size=(3, 3), padding=1, bias=False),
            nn.BatchNorm2d(90)
            # nn.ReLU()
        )  # 4 3

        # OUTPUT BLOCK
        self.gap = nn.Sequential(
            nn.AvgPool2d(kernel_size=3)
        )

        self.linear = nn.Sequential(
            nn.Conv2d(in_channels=90, out_channels=10, kernel_size=(1, 1), padding=0, bias=False),
            # nn.Conv2d(in_channels=50, out_channels=10, kernel_size=(1,1), padding=0, bias=False)
            # nn.Linear(90, 10)
        )

    def forward(self, x):
        x = self.convblock11(x)
        x = self.convblock12(x)
        x = self.convblock13(x)
        x = self.pool1(x)
        x = self.convblock21(x)
        #      x = self.convblock22(x)
        x = self.depthwise(x)
        x = self.convblock23(x)
        x = self.pool2(x)
        x = self.convblock31(x)
        x = self.convblock32(x)
        x = self.convblock33(x)
        x = self.pool3(x)
        x = self.convblock41(x)
        # x = self.convblock42(x)
        x = self.depthwise2(x)
        x = self.convblock43(x)
        x = self.gap(x)
        x = self.linear(x)
        x = x.view(-1, 10)
        return F.log_softmax(x, dim=-1)


def get_model_instance(dp):
    return Net(dropout_value=dp)