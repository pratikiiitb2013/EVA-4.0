<h2><i> Assignment 4 </i></h2>
<hr>

**ASSIGNMENT - Create an architecture using below conditions**<br>
<ul>
  <li>99.4% validation accuracy</li>
  <li>Less than 20k Parameters</li>
  <li>Less than 20 Epochs</li>
  <li>No fully connected layer</li>
</ul>

**Model Details**<br>
<ul>
  <li><B>EPOCHS</B> - 15</li>
  <li><B>PARAMETERS</B> - 19736</li>
  <li><B>TEST ACCURACY</B> - 99.52</li>
  <li><B> DROPOUT RANGE</B> - (0.05-0.1)</li>
</UL>

**Architecture**<BR>
  
<B><I> (CONV2D+CONV2D) + POOLING + (CONV2D(1*1) + CONV2D + CONV2D) + POOLING + (CONV2D+CONV2D) + GAP + LOG_SOFTMAX</I></B>

```
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 16, 28, 28]             144
       BatchNorm2d-2           [-1, 16, 28, 28]              32
            Conv2d-3           [-1, 24, 28, 28]           3,456
       BatchNorm2d-4           [-1, 24, 28, 28]              48
         Dropout2d-5           [-1, 24, 28, 28]               0
         MaxPool2d-6           [-1, 24, 14, 14]               0
            Conv2d-7           [-1, 16, 14, 14]             384
       BatchNorm2d-8           [-1, 16, 14, 14]              32
            Conv2d-9           [-1, 20, 14, 14]           2,880
      BatchNorm2d-10           [-1, 20, 14, 14]              40
        Dropout2d-11           [-1, 20, 14, 14]               0
           Conv2d-12           [-1, 30, 12, 12]           5,400
      BatchNorm2d-13           [-1, 30, 12, 12]              60
        Dropout2d-14           [-1, 30, 12, 12]               0
        MaxPool2d-15             [-1, 30, 6, 6]               0
           Conv2d-16             [-1, 20, 6, 6]           5,420
      BatchNorm2d-17             [-1, 20, 6, 6]              40
           Conv2d-18             [-1, 10, 4, 4]           1,800
AdaptiveAvgPool2d-19             [-1, 10, 1, 1]               0
================================================================
Total params: 19,736
Trainable params: 19,736
```

**TRAIN LOG**<BR>
```
   0%|          | 0/938 [00:00<?, ?it/s]EPOCH:  0
/usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py:49: UserWarning: Implicit dimension choice for log_softmax has been deprecated. Change the call to include dim=X as an argument.
loss=0.13038276135921478 batch_id=937: 100%|██████████| 938/938 [00:17<00:00, 52.60it/s]
Train set: Average loss: 0.2200, Accuracy: 56111/60000 (93.52%)


  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0361, Accuracy: 9883/10000 (98.83%)

EPOCH:  1
loss=0.06227730214595795 batch_id=937: 100%|██████████| 938/938 [00:17<00:00, 54.99it/s]

Train set: Average loss: 0.0589, Accuracy: 58906/60000 (98.18%)

  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0347, Accuracy: 9888/10000 (98.88%)

EPOCH:  2
loss=0.09297902882099152 batch_id=937: 100%|██████████| 938/938 [00:17<00:00, 53.45it/s]
Train set: Average loss: 0.0445, Accuracy: 59167/60000 (98.61%)


  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0245, Accuracy: 9911/10000 (99.11%)

EPOCH:  3
loss=0.01097095012664795 batch_id=937: 100%|██████████| 938/938 [00:16<00:00, 55.44it/s]
Train set: Average loss: 0.0380, Accuracy: 59263/60000 (98.77%)


  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0280, Accuracy: 9903/10000 (99.03%)

EPOCH:  4
loss=0.07539321482181549 batch_id=937: 100%|██████████| 938/938 [00:17<00:00, 54.99it/s]
Train set: Average loss: 0.0331, Accuracy: 59386/60000 (98.98%)


  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0195, Accuracy: 9935/10000 (99.35%)

EPOCH:  5
loss=0.005106285214424133 batch_id=937: 100%|██████████| 938/938 [00:17<00:00, 54.35it/s]
Train set: Average loss: 0.0294, Accuracy: 59451/60000 (99.08%)


  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0212, Accuracy: 9935/10000 (99.35%)

EPOCH:  6
loss=0.010791778564453125 batch_id=937: 100%|██████████| 938/938 [00:17<00:00, 54.33it/s]

Train set: Average loss: 0.0273, Accuracy: 59484/60000 (99.14%)

  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0229, Accuracy: 9925/10000 (99.25%)

EPOCH:  7
loss=0.009787648916244507 batch_id=937: 100%|██████████| 938/938 [00:16<00:00, 55.62it/s]

Train set: Average loss: 0.0271, Accuracy: 59485/60000 (99.14%)

  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0189, Accuracy: 9930/10000 (99.30%)

EPOCH:  8
loss=0.005941823124885559 batch_id=937: 100%|██████████| 938/938 [00:16<00:00, 56.04it/s]
Train set: Average loss: 0.0228, Accuracy: 59557/60000 (99.26%)


  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0182, Accuracy: 9939/10000 (99.39%)

EPOCH:  9
loss=0.0019976645708084106 batch_id=937: 100%|██████████| 938/938 [00:17<00:00, 54.82it/s]
Train set: Average loss: 0.0222, Accuracy: 59579/60000 (99.30%)


  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0180, Accuracy: 9937/10000 (99.37%)

EPOCH:  10
loss=0.08006562292575836 batch_id=937: 100%|██████████| 938/938 [00:17<00:00, 54.10it/s]
Train set: Average loss: 0.0207, Accuracy: 59589/60000 (99.31%)


  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0188, Accuracy: 9937/10000 (99.37%)

EPOCH:  11
loss=0.018970996141433716 batch_id=937: 100%|██████████| 938/938 [00:16<00:00, 56.22it/s]

Train set: Average loss: 0.0200, Accuracy: 59615/60000 (99.36%)

  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0186, Accuracy: 9940/10000 (99.40%)

EPOCH:  12
loss=0.003424808382987976 batch_id=937: 100%|██████████| 938/938 [00:17<00:00, 53.68it/s]
Train set: Average loss: 0.0189, Accuracy: 59643/60000 (99.41%)


  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0204, Accuracy: 9938/10000 (99.38%)

EPOCH:  13
loss=0.42028385400772095 batch_id=937: 100%|██████████| 938/938 [00:16<00:00, 55.69it/s]
Train set: Average loss: 0.0178, Accuracy: 59658/60000 (99.43%)


  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0159, Accuracy: 9948/10000 (99.48%)

EPOCH:  14
loss=0.0028793364763259888 batch_id=937: 100%|██████████| 938/938 [00:17<00:00, 54.53it/s]
Train set: Average loss: 0.0168, Accuracy: 59686/60000 (99.48%)



Test set: Average loss: 0.0148, Accuracy: 9952/10000 (99.52%)
```

Colab file link - https://colab.research.google.com/drive/1_pENU66CEmxaISSRIWIsQIkpcpjs71g2<br>
Author - Siddharth Surange
