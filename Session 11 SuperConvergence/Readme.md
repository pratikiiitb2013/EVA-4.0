<h2><b><i> S11 Assignment Superconvergence</i></b></h2>
<hr>
<h3>Things to accomplish</h3>

```
Assignment:

Write a code that draws this curve (without the arrows). In submission, you'll upload your drawn curve and code for that

1. Write a code which uses this new ResNet Architecture for Cifar10:
   1. PrepLayer - Conv 3x3 s1, p1) >> BN >> RELU [64k]
   2. Layer1 -
      1. X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [128k]
      2. R1 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [128k] 
      3. Add(X, R1)
   3. Layer 2 -
      1. Conv 3x3 [256k]
      2. MaxPooling2D
      3. BN
      4. ReLU
   4. Layer 3 -
      1. X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [512k]
      2. R2 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [512k]
      3. Add(X, R2)
   5. MaxPooling with Kernel Size 4
   6. FC Layer 
   7. SoftMax

2. Uses One Cycle Policy such that:
   1. Total Epochs = 24
   2. Max at Epoch = 5
   3. LRMIN = FIND
   4. LRMAX = FIND
   5. NO Annihilation
3. Uses this transform -RandomCrop 32, 32 (after padding of 4) >> FlipLR >> Followed by CutOut(8, 8)
4. Batch size = 512
5. Target Accuracy: 90%. 
6. The lesser the modular your code is (i.e. more the code you have written in your Colab file), less marks you'd get. 

```
<HR>

<h3> Final Model metrics</h3>
<ul>
  <li>Epochs - 24</li>
  <li>Test accuracy - 90.41</li>
  <li>Augmentation - Albumentation (Padding , RandomCrop,Flip, Cutout)</li>
</ul>


<hr>

<h3> Zigzag Cyclic LR pattern </h3>

![img](https://github.com/SID-SURANGE/EVA-4.0/blob/master/Session%2011%20SuperConvergence/Zigzag_S11.png)

<hr>

<h3>Training Logs</h3>


```
 0%|          | 0/98 [00:00<?, ?it/s]EPOCH: 1
LR: [0.0157], M : [0.9500000000000001]
Loss=2.583657741546631 Batch_id=97 Accuracy=12.60: 100%|██████████| 98/98 [00:24<00:00,  4.02it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0044, Accuracy: 1583/10000 (15.83%)


EPOCH: 2
LR: [0.051025], M : [0.9125]
Loss=4.166126728057861 Batch_id=97 Accuracy=22.27: 100%|██████████| 98/98 [00:24<00:00,  3.99it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0039, Accuracy: 2666/10000 (26.66%)


EPOCH: 3
LR: [0.08635000000000001], M : [0.875]
Loss=2.6135990619659424 Batch_id=97 Accuracy=27.16: 100%|██████████| 98/98 [00:24<00:00,  3.96it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0039, Accuracy: 3393/10000 (33.93%)


EPOCH: 4
LR: [0.121675], M : [0.8375]
Loss=1.712868332862854 Batch_id=97 Accuracy=35.69: 100%|██████████| 98/98 [00:24<00:00,  3.94it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0030, Accuracy: 4419/10000 (44.19%)


EPOCH: 5
LR: [0.157], M : [0.8]
Loss=1.4527246952056885 Batch_id=97 Accuracy=44.58: 100%|██████████| 98/98 [00:24<00:00,  3.95it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0024, Accuracy: 5630/10000 (56.30%)


EPOCH: 6
LR: [0.14956315789473684], M : [0.8078947368421053]
Loss=1.276489496231079 Batch_id=97 Accuracy=53.75: 100%|██████████| 98/98 [00:24<00:00,  3.95it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0021, Accuracy: 6197/10000 (61.97%)


EPOCH: 7
LR: [0.14212631578947368], M : [0.8157894736842105]
Loss=1.0108896493911743 Batch_id=97 Accuracy=61.38: 100%|██████████| 98/98 [00:24<00:00,  3.96it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0019, Accuracy: 6548/10000 (65.48%)


EPOCH: 8
LR: [0.13468947368421053], M : [0.8236842105263158]
Loss=0.8660224676132202 Batch_id=97 Accuracy=66.86: 100%|██████████| 98/98 [00:24<00:00,  3.95it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0015, Accuracy: 7227/10000 (72.27%)


EPOCH: 9
LR: [0.12725263157894737], M : [0.8315789473684211]
Loss=0.7476513981819153 Batch_id=97 Accuracy=71.11: 100%|██████████| 98/98 [00:24<00:00,  3.94it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0014, Accuracy: 7593/10000 (75.93%)


EPOCH: 10
LR: [0.11981578947368421], M : [0.8394736842105264]
Loss=0.806189775466919 Batch_id=97 Accuracy=74.17: 100%|██████████| 98/98 [00:24<00:00,  3.94it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0013, Accuracy: 7732/10000 (77.32%)


EPOCH: 11
LR: [0.11237894736842105], M : [0.8473684210526315]
Loss=0.6486853361129761 Batch_id=97 Accuracy=76.55: 100%|██████████| 98/98 [00:24<00:00,  3.93it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0011, Accuracy: 8141/10000 (81.41%)


EPOCH: 12
LR: [0.10494210526315789], M : [0.8552631578947368]
Loss=0.7142148613929749 Batch_id=97 Accuracy=78.14: 100%|██████████| 98/98 [00:24<00:00,  3.93it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0011, Accuracy: 8104/10000 (81.04%)


EPOCH: 13
LR: [0.09750526315789473], M : [0.8631578947368421]
Loss=0.51921147108078 Batch_id=97 Accuracy=80.41: 100%|██████████| 98/98 [00:24<00:00,  3.93it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0010, Accuracy: 8224/10000 (82.24%)


EPOCH: 14
LR: [0.09006842105263158], M : [0.8710526315789474]
Loss=0.4945242404937744 Batch_id=97 Accuracy=81.37: 100%|██████████| 98/98 [00:24<00:00,  3.93it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0009, Accuracy: 8489/10000 (84.89%)


EPOCH: 15
LR: [0.08263157894736842], M : [0.8789473684210526]
Loss=0.4414375424385071 Batch_id=97 Accuracy=82.73: 100%|██████████| 98/98 [00:24<00:00,  3.95it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0009, Accuracy: 8370/10000 (83.70%)


EPOCH: 16
LR: [0.07519473684210526], M : [0.8868421052631579]
Loss=0.4413408637046814 Batch_id=97 Accuracy=83.48: 100%|██████████| 98/98 [00:24<00:00,  3.93it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0008, Accuracy: 8652/10000 (86.52%)


EPOCH: 17
LR: [0.0677578947368421], M : [0.8947368421052632]
Loss=0.48129358887672424 Batch_id=97 Accuracy=84.96: 100%|██████████| 98/98 [00:24<00:00,  3.93it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0008, Accuracy: 8673/10000 (86.73%)


EPOCH: 18
LR: [0.06032105263157894], M : [0.9026315789473686]
Loss=0.39693573117256165 Batch_id=97 Accuracy=85.63: 100%|██████████| 98/98 [00:24<00:00,  3.94it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0007, Accuracy: 8719/10000 (87.19%)


EPOCH: 19
LR: [0.052884210526315784], M : [0.9105263157894736]
Loss=0.4074959456920624 Batch_id=97 Accuracy=86.24: 100%|██████████| 98/98 [00:24<00:00,  3.93it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0007, Accuracy: 8812/10000 (88.12%)


EPOCH: 20
LR: [0.045447368421052625], M : [0.9184210526315789]
Loss=0.39281949400901794 Batch_id=97 Accuracy=87.12: 100%|██████████| 98/98 [00:24<00:00,  3.94it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0007, Accuracy: 8753/10000 (87.53%)


EPOCH: 21
LR: [0.03801052631578947], M : [0.9263157894736842]
Loss=0.33538058400154114 Batch_id=97 Accuracy=87.74: 100%|██████████| 98/98 [00:24<00:00,  3.95it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0006, Accuracy: 8897/10000 (88.97%)


EPOCH: 22
LR: [0.03057368421052631], M : [0.9342105263157895]
Loss=0.27865177392959595 Batch_id=97 Accuracy=88.33: 100%|██████████| 98/98 [00:24<00:00,  3.95it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0006, Accuracy: 9004/10000 (90.04%)


EPOCH: 23
LR: [0.02313684210526315], M : [0.9421052631578948]
Loss=0.2939189374446869 Batch_id=97 Accuracy=89.59: 100%|██████████| 98/98 [00:24<00:00,  3.95it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0006, Accuracy: 9012/10000 (90.12%)


EPOCH: 24
LR: [0.0157], M : [0.9500000000000001]
Loss=0.27296972274780273 Batch_id=97 Accuracy=90.35: 100%|██████████| 98/98 [00:24<00:00,  3.94it/s]

Test set: Average loss: 0.0006, Accuracy: 9041/10000 (90.41%)

```
<hr>
<h3> Misclassified images</h3>

![IMGAGE](https://github.com/SID-SURANGE/EVA-4.0/blob/master/Session%2010%20LR%20Finder/S10_Misclassified.png)

<HR>
Author - Siddharth Surange



