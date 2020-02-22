<h1><i> Assignment 5</i></h1><hr>
<h4>Assignment Target -</h4>
1) 99.4% (this must be consistently shown in your last few epochs, and not a one-time achievement)<br>
2) Less than or equal to 15 Epochs<br>
3) Less than 10000 Parameters<br>
4) Calculate Receptive Field for each Model(<b>RF Calculations can be viewed in notebooks</b>)
<hr>
<h4><b> Solution </b></h4>
Solution spans over 5 different code files where each new code files improves upon the issues of last file.<br>
<ul>
  <li><b>CODE 1</b> - Base code setup for MNIST dataset</li>
  <li><b>CODE 2</b> - Restructured Architecture definition with proper SEQUENTIAL LAYERS and minimizing parameter count</li>
  <li><b>CODE 3</b> - GAP Instroduced, removing the last layer bulky kernels. Further reduction in parameters over whole architecture</li>
  <li><b>CODE 4</b> - Introducting Batch Normalization to increase efficiency and help model converge faster.  </li>
  <li><b>CODE 5</b> - Tacking problem of Overfitting with Dropout</li>
  <li><b>CODE 6</b> - Introducing StepLR: to increase model efficiency</li>
</ul>

<hr>
<h4> CODE 1 ANALYSIS</H4>

```
Analysis of CODE1

Target:
Basic code setup with Data Loaders / Sample Architecture / Predictions + Validation
No check of parameters or augumenters taken care at this step

Results:
Epochs - 15
Parameters - 6.3M
Best Train Acc - 99.97(14th epoch)
Best Test Acc - 99.41(11th epoch)
Train/Test Acc last layer - 99.96/99.27 (Difference - 0.70)

Analysis:
Training logs shows sign of overfitting.
The model is large in terms of capacity(parameter count) making it more complex.
Since there are no transforms being done trained model becomes biased to train images which might not be actual representation of true conditions.

```
![image](https://github.com/SID-SURANGE/EVA-4.0/blob/master/Session%205%20Assignment/CODE1%20RF.JPG)
<br>
<h4> CODE 2 ANALYSIS </H4>

```
Analysis of CODE2

Target:
Restructuring the architecture with Conv block and transition blocks.
Make model bit light on trainable parameters as the data is MNIST which is very small.

Results:
Parameters: 54416
Best Train Acc: 99.46
Best Test Acc: 98.99
Difference : 0.47
Epoch - 15

Analysis:
Model still overfits with huge gap. Need to introduce regularization.
The model is less complex with reduction in kernel values.
After reducing the intermediate kernel values, model still is performing good.
```
![Image](https://github.com/SID-SURANGE/EVA-4.0/blob/master/Session%205%20Assignment/CODE2%20RF.JPG)
<br>
<h4> CODE 3 ANALYSIS </H4>

```
Analysis of CODE3

Target:
Training the model under less iterations and restructuring the architecture for less trainiable parameters or complexity.
Removing the large kernel in last layer and replacing it with GAP.

Results:
Parameters: 8710
Best Train Acc: 99.09(15th epoch)
Best Test Acc: 98.90(13th epoch) and 98.74(in 15 th epoch)
Difference : More train accuracy - Small overfit scenario
Epoch - 15

Analysis:
Model looks a bit overfit.
Architecture looks simple overall and can be improved upon to attain good accuracy and prevent overfitting.
```
![Image](https://github.com/SID-SURANGE/EVA-4.0/blob/master/Session%205%20Assignment/CODE3%20RF.JPG)
<br>
<h4> CODE 4 ANALYSIS </H4>

```
Analysis of CODE4

Target:
Introduce Batch Normalization to increase model's efficiency and help it to converge faster. Also it provides some regularization.

Results:
Parameters: 8898
Best Train Acc: 99.64(last epoch)
Best Test Acc: 99.24(last epoch) and 99.30(9th epoch)
Difference : More train accuracy
Epoch - 15

Analysis:
Model stills ovrfits but it doesn't show this trend in overall training
Need to introduce dropout and learn more features.
```
![Image](https://github.com/SID-SURANGE/EVA-4.0/blob/master/Session%205%20Assignment/CODE4%20RF.JPG)
<br>

<h4> CODE 5 ANALYSIS </H4>

```
Analysis of CODE5

Target:
Introduce Dropout to decrease overfitting.
Apply different dropout rates as per kernels in each conv layer.

Results:
Parameters: 8898
Best Train Acc: 99.19
Best Test Acc: 99.26
Difference : More test accuracy
Epoch - 15

Analysis:
Model seams to be stable with no overfitting.
Model accuracy must be tuned by trying different learning rates or changing architecture with more feature extractors.
```

![Image](https://github.com/SID-SURANGE/EVA-4.0/blob/master/Session%205%20Assignment/CODE5%20RF.JPG)
<br>
<h4> CODE 6 ANALYSIS </H4>

```
Analysis of CODE6

Target:
Improve Model accuracy to reach stable test accuracy over 99.4
Use LR Scheduler to add different learning rates to each Epoch.
Change the architecture to make it more efficient.

Results:
Parameters: 8846
Best Train Acc: 99.28(13th Epoch)
Best Test Acc: 99.45(9th epoch) / 99.42(13th epoch)
Difference : No overfitting
Epoch - 13

Analysis:
Model gives a consistent test accuracy above 99.40 which seems to be a good sign.
```
![Image](https://github.com/SID-SURANGE/EVA-4.0/blob/master/Session%205%20Assignment/CODE6%20RF.JPG)

<hr>
<h4> FINAL MODEL(CODE6) TRAIN LOGS</H4>

```
0%|          | 0/938 [00:00<?, ?it/s]EPOCH: 0
Loss=0.006024077534675598 Batch_id=937 Accuracy=94.79: 100%|██████████| 938/938 [00:18<00:00, 51.75it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0489, Accuracy: 9854/10000 (98.54%)


EPOCH: 1
Loss=0.017176061868667603 Batch_id=937 Accuracy=98.00: 100%|██████████| 938/938 [00:18<00:00, 52.07it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0319, Accuracy: 9907/10000 (99.07%)


EPOCH: 2
Loss=0.07757099717855453 Batch_id=937 Accuracy=98.39: 100%|██████████| 938/938 [00:17<00:00, 52.30it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0292, Accuracy: 9910/10000 (99.10%)


EPOCH: 3
Loss=0.023600101470947266 Batch_id=937 Accuracy=98.62: 100%|██████████| 938/938 [00:18<00:00, 51.80it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0289, Accuracy: 9907/10000 (99.07%)


EPOCH: 4
Loss=0.006685391068458557 Batch_id=937 Accuracy=98.74: 100%|██████████| 938/938 [00:18<00:00, 50.60it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0301, Accuracy: 9912/10000 (99.12%)


EPOCH: 5
Loss=0.00912390649318695 Batch_id=937 Accuracy=99.08: 100%|██████████| 938/938 [00:18<00:00, 64.16it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0208, Accuracy: 9935/10000 (99.35%)


EPOCH: 6
Loss=0.015221327543258667 Batch_id=937 Accuracy=99.14: 100%|██████████| 938/938 [00:18<00:00, 50.59it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0199, Accuracy: 9943/10000 (99.43%)


EPOCH: 7
Loss=0.0020703375339508057 Batch_id=937 Accuracy=99.17: 100%|██████████| 938/938 [00:19<00:00, 49.11it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0201, Accuracy: 9942/10000 (99.42%)


EPOCH: 8
Loss=0.005460426211357117 Batch_id=937 Accuracy=99.19: 100%|██████████| 938/938 [00:19<00:00, 48.48it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0203, Accuracy: 9945/10000 (99.45%)


EPOCH: 9
Loss=0.013973012566566467 Batch_id=937 Accuracy=99.22: 100%|██████████| 938/938 [00:18<00:00, 49.49it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0201, Accuracy: 9941/10000 (99.41%)


EPOCH: 10
Loss=0.04891825467348099 Batch_id=937 Accuracy=99.27: 100%|██████████| 938/938 [00:19<00:00, 47.72it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0207, Accuracy: 9942/10000 (99.42%)


EPOCH: 11
Loss=0.01697532832622528 Batch_id=937 Accuracy=99.27: 100%|██████████| 938/938 [00:18<00:00, 49.75it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0199, Accuracy: 9943/10000 (99.43%)


EPOCH: 12
Loss=0.11147846281528473 Batch_id=937 Accuracy=99.28: 100%|██████████| 938/938 [00:18<00:00, 51.78it/s]

Test set: Average loss: 0.0199, Accuracy: 9942/10000 (99.42%)

```
<hr>
<B> Author - Siddharth Surange</b>
