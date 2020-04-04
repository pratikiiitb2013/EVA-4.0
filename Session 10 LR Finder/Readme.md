<h2><b><i> S10 Assignment</i></b></h2>
<hr>
<h3>Things to accomplish</h3>

```
1. Pick your last code
2. Make sure  to Add CutOut to your code. It should come from your transformations (albumentations)
   Use this repo: https://github.com/davidtvs/pytorch-lr-finder (Links to an external site.) 
3. Move LR Finder code to your modules. Implement LR Finder (for SGD, not for ADAM)
4. Implement ReduceLROnPlatea: https://pytorch.org/docs/stable/optim.html#torch.optim.lr_scheduler.ReduceLROnPlateau (Links to an      external site.)
5. Find best LR to train your model
6. Use SDG with Momentum
7. Train for 50 Epochs. 
8. Show Training and Test Accuracy curves
9. Target 88% Accuracy.
10 Run GradCAM on the any 25 misclassified images. Make sure you mention what is the prediction and what was the ground truth label.
11 Submit

```
<HR>

<h3> Final Model metrics</h3>
<ul>
  <li>Epochs - 50</li>
  <li>Test accuracy - 91.73</li>
  <li>Augmentation - Albumentation (Horizontal Flip, Rotate, HueSaturationValue, Cutout)</li>
</ul>


<hr>

<h3>Training Logs</h3>


```
0%|          | 0/391 [00:00<?, ?it/s]EPOCH: 1
Loss=1.4710098505020142 Batch_id=390 Accuracy=35.55: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0112, Accuracy: 4580/10000 (45.80%)


EPOCH: 2
Loss=1.0532110929489136 Batch_id=390 Accuracy=51.69: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0084, Accuracy: 6216/10000 (62.16%)


EPOCH: 3
Loss=0.8741633296012878 Batch_id=390 Accuracy=62.06: 100%|██████████| 391/391 [03:12<00:00,  2.04it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0070, Accuracy: 6851/10000 (68.51%)


EPOCH: 4
Loss=0.7611417770385742 Batch_id=390 Accuracy=68.73: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0066, Accuracy: 7198/10000 (71.98%)


EPOCH: 5
Loss=0.8179715871810913 Batch_id=390 Accuracy=72.85: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0057, Accuracy: 7554/10000 (75.54%)


EPOCH: 6
Loss=1.0033676624298096 Batch_id=390 Accuracy=75.75: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0053, Accuracy: 7708/10000 (77.08%)


EPOCH: 7
Loss=0.6342872381210327 Batch_id=390 Accuracy=77.69: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0046, Accuracy: 7983/10000 (79.83%)


EPOCH: 8
Loss=0.5909603834152222 Batch_id=390 Accuracy=79.21: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0046, Accuracy: 7976/10000 (79.76%)


EPOCH: 9
Loss=0.5077040791511536 Batch_id=390 Accuracy=79.76: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0046, Accuracy: 8024/10000 (80.24%)


EPOCH: 10
Loss=0.6347154378890991 Batch_id=390 Accuracy=80.68: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0043, Accuracy: 8155/10000 (81.55%)


EPOCH: 11
Loss=0.5697492361068726 Batch_id=390 Accuracy=81.05: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0040, Accuracy: 8255/10000 (82.55%)


EPOCH: 12
Loss=0.6580222845077515 Batch_id=390 Accuracy=81.24: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0047, Accuracy: 7954/10000 (79.54%)


EPOCH: 13
Loss=0.4848906099796295 Batch_id=390 Accuracy=82.01: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0040, Accuracy: 8258/10000 (82.58%)


EPOCH: 14
Loss=0.5194594264030457 Batch_id=390 Accuracy=82.22: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0048, Accuracy: 7922/10000 (79.22%)


EPOCH: 15
Loss=0.4080556035041809 Batch_id=390 Accuracy=82.59: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0045, Accuracy: 8059/10000 (80.59%)


EPOCH: 16
Loss=0.5881493091583252 Batch_id=390 Accuracy=82.91: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0041, Accuracy: 8326/10000 (83.26%)


EPOCH: 17
Loss=0.6342006325721741 Batch_id=390 Accuracy=83.12: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0039, Accuracy: 8310/10000 (83.10%)


EPOCH: 18
Loss=0.3957323133945465 Batch_id=390 Accuracy=83.72: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0047, Accuracy: 8054/10000 (80.54%)


EPOCH: 19
Loss=0.4515492022037506 Batch_id=390 Accuracy=83.51: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0044, Accuracy: 8042/10000 (80.42%)


EPOCH: 20
Loss=0.6245758533477783 Batch_id=390 Accuracy=83.86: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0038, Accuracy: 8359/10000 (83.59%)


EPOCH: 21
Loss=0.4051142632961273 Batch_id=390 Accuracy=84.00: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0039, Accuracy: 8334/10000 (83.34%)


EPOCH: 22
Loss=0.449084609746933 Batch_id=390 Accuracy=84.05: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0041, Accuracy: 8288/10000 (82.88%)


EPOCH: 23
Loss=0.4296044707298279 Batch_id=390 Accuracy=84.11: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0035, Accuracy: 8473/10000 (84.73%)


EPOCH: 24
Loss=0.3846204876899719 Batch_id=390 Accuracy=84.50: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0036, Accuracy: 8515/10000 (85.15%)


EPOCH: 25
Loss=0.47053462266921997 Batch_id=390 Accuracy=84.53: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0037, Accuracy: 8426/10000 (84.26%)


EPOCH: 26
Loss=0.3823392987251282 Batch_id=390 Accuracy=84.67: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0042, Accuracy: 8297/10000 (82.97%)


EPOCH: 27
Loss=0.49862536787986755 Batch_id=390 Accuracy=84.79: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0040, Accuracy: 8298/10000 (82.98%)

Epoch    27: reducing learning rate of group 0 to 5.0000e-03.

EPOCH: 28
Loss=0.288582980632782 Batch_id=390 Accuracy=90.49: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0024, Accuracy: 8952/10000 (89.52%)


EPOCH: 29
Loss=0.23396353423595428 Batch_id=390 Accuracy=92.37: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0023, Accuracy: 9022/10000 (90.22%)


EPOCH: 30
Loss=0.14803357422351837 Batch_id=390 Accuracy=93.40: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0022, Accuracy: 9058/10000 (90.58%)


EPOCH: 31
Loss=0.14116156101226807 Batch_id=390 Accuracy=94.23: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0022, Accuracy: 9090/10000 (90.90%)


EPOCH: 32
Loss=0.18833670020103455 Batch_id=390 Accuracy=94.79: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0022, Accuracy: 9098/10000 (90.98%)


EPOCH: 33
Loss=0.08818966150283813 Batch_id=390 Accuracy=95.08: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0022, Accuracy: 9114/10000 (91.14%)


EPOCH: 34
Loss=0.09731098264455795 Batch_id=390 Accuracy=95.72: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0023, Accuracy: 9078/10000 (90.78%)


EPOCH: 35
Loss=0.10328035056591034 Batch_id=390 Accuracy=96.03: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0023, Accuracy: 9077/10000 (90.77%)


EPOCH: 36
Loss=0.14085035026073456 Batch_id=390 Accuracy=96.12: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0022, Accuracy: 9092/10000 (90.92%)


EPOCH: 37
Loss=0.053936075419187546 Batch_id=390 Accuracy=96.69: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0023, Accuracy: 9111/10000 (91.11%)

Epoch    37: reducing learning rate of group 0 to 5.0000e-04.

EPOCH: 38
Loss=0.07508673518896103 Batch_id=390 Accuracy=97.27: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0022, Accuracy: 9163/10000 (91.63%)


EPOCH: 39
Loss=0.020127039402723312 Batch_id=390 Accuracy=97.48: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0022, Accuracy: 9161/10000 (91.61%)


EPOCH: 40
Loss=0.08531539142131805 Batch_id=390 Accuracy=97.56: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0022, Accuracy: 9160/10000 (91.60%)


EPOCH: 41
Loss=0.0777452141046524 Batch_id=390 Accuracy=97.73: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0022, Accuracy: 9162/10000 (91.62%)


EPOCH: 42
Loss=0.12208326905965805 Batch_id=390 Accuracy=97.84: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0022, Accuracy: 9155/10000 (91.55%)


EPOCH: 43
Loss=0.06228365749120712 Batch_id=390 Accuracy=97.81: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0021, Accuracy: 9158/10000 (91.58%)


EPOCH: 44
Loss=0.040064163506031036 Batch_id=390 Accuracy=97.99: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0021, Accuracy: 9158/10000 (91.58%)


EPOCH: 45
Loss=0.056654222309589386 Batch_id=390 Accuracy=98.02: 100%|██████████| 391/391 [03:13<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0021, Accuracy: 9177/10000 (91.77%)


EPOCH: 46
Loss=0.032201316207647324 Batch_id=390 Accuracy=98.00: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0022, Accuracy: 9159/10000 (91.59%)


EPOCH: 47
Loss=0.10584596544504166 Batch_id=390 Accuracy=98.14: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0021, Accuracy: 9158/10000 (91.58%)


EPOCH: 48
Loss=0.13258156180381775 Batch_id=390 Accuracy=98.09: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0022, Accuracy: 9163/10000 (91.63%)


EPOCH: 49
Loss=0.1228618398308754 Batch_id=390 Accuracy=98.14: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0021, Accuracy: 9160/10000 (91.60%)

Epoch    49: reducing learning rate of group 0 to 5.0000e-05.

EPOCH: 50
Loss=0.05144214630126953 Batch_id=390 Accuracy=98.32: 100%|██████████| 391/391 [03:12<00:00,  2.03it/s]

Test set: Average loss: 0.0021, Accuracy: 9173/10000 (91.73%)
```
<hr>
<h3> Misclassified images</h3>

![IMGAGE](https://github.com/SID-SURANGE/EVA-4.0/blob/master/Session%2010%20LR%20Finder/S10_Misclassified.png)

<HR>
Author - Siddharth Surange


