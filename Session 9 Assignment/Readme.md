<h2><b><i> S9 Assignment</i></b></h2>
<hr>
<h3>Things to accomplish</h3>
<ol>
  <li>Move your last code's transformations to Albumentations. Apply ToTensor, HorizontalFlip, Normalize (at min) + More (for additional points)
</li>
  <li>Please make sure that your test_transforms are simple and only using ToTensor and Normalize
</li>
  <li>Implement GradCam function as a module.Your final code (notebook file) must use imported functions to implement transformations and GradCam functionality
</li>
  <li>Target Accuracy is 87%</li>
</ol>

<HR>

<h3> Final Model metrics</h3>
<ul>
  <li>Epochs - 24</li>
  <li>Test accuracy - 88.97</li>
  <li>Augmentation - Albumentation (Horizontal Flip, Rotate, HueSaturationValue, Cutout)</li>
</ul>


<hr>

<h3>Training Logs</h3>


```
0%|          | 0/391 [00:00<?, ?it/s]EPOCH: 1
Loss=1.3948262929916382 Batch_id=390 Accuracy=38.45: 100%|██████████| 391/391 [00:31<00:00, 12.44it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0106, Accuracy: 5071/10000 (50.71%)


EPOCH: 2
Loss=1.0757333040237427 Batch_id=390 Accuracy=52.93: 100%|██████████| 391/391 [00:31<00:00, 12.40it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0083, Accuracy: 6302/10000 (63.02%)


EPOCH: 3
Loss=0.9199005365371704 Batch_id=390 Accuracy=62.19: 100%|██████████| 391/391 [00:31<00:00, 12.44it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0069, Accuracy: 6898/10000 (68.98%)


EPOCH: 4
Loss=0.849989116191864 Batch_id=390 Accuracy=68.02: 100%|██████████| 391/391 [00:31<00:00, 12.42it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0056, Accuracy: 7507/10000 (75.07%)


EPOCH: 5
Loss=0.7554132342338562 Batch_id=390 Accuracy=72.16: 100%|██████████| 391/391 [00:31<00:00, 12.40it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0056, Accuracy: 7581/10000 (75.81%)


EPOCH: 6
Loss=0.5513595342636108 Batch_id=390 Accuracy=74.73: 100%|██████████| 391/391 [00:31<00:00, 12.42it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0049, Accuracy: 7832/10000 (78.32%)


EPOCH: 7
Loss=0.6458432078361511 Batch_id=390 Accuracy=76.81: 100%|██████████| 391/391 [00:31<00:00, 12.34it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0045, Accuracy: 8040/10000 (80.40%)


EPOCH: 8
Loss=0.5360523462295532 Batch_id=390 Accuracy=78.62: 100%|██████████| 391/391 [00:31<00:00, 12.39it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0042, Accuracy: 8208/10000 (82.08%)


EPOCH: 9
Loss=0.5684243440628052 Batch_id=390 Accuracy=80.21: 100%|██████████| 391/391 [00:31<00:00, 12.40it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0044, Accuracy: 8151/10000 (81.51%)


EPOCH: 10
Loss=0.8166564702987671 Batch_id=390 Accuracy=81.49: 100%|██████████| 391/391 [00:31<00:00, 12.35it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0038, Accuracy: 8404/10000 (84.04%)


EPOCH: 11
Loss=0.4726555347442627 Batch_id=390 Accuracy=82.61: 100%|██████████| 391/391 [00:32<00:00, 12.19it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0037, Accuracy: 8413/10000 (84.13%)


EPOCH: 12
Loss=0.5876569747924805 Batch_id=390 Accuracy=83.62: 100%|██████████| 391/391 [00:32<00:00, 12.22it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0038, Accuracy: 8435/10000 (84.35%)


EPOCH: 13
Loss=0.4808524549007416 Batch_id=390 Accuracy=84.53: 100%|██████████| 391/391 [00:31<00:00, 12.26it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0036, Accuracy: 8487/10000 (84.87%)


EPOCH: 14
Loss=0.453606516122818 Batch_id=390 Accuracy=85.52: 100%|██████████| 391/391 [00:31<00:00, 12.34it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0034, Accuracy: 8622/10000 (86.22%)


EPOCH: 15
Loss=0.3186863660812378 Batch_id=390 Accuracy=86.16: 100%|██████████| 391/391 [00:31<00:00, 12.47it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0034, Accuracy: 8562/10000 (85.62%)


EPOCH: 16
Loss=0.4241381585597992 Batch_id=390 Accuracy=86.98: 100%|██████████| 391/391 [00:31<00:00, 12.44it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0032, Accuracy: 8661/10000 (86.61%)


EPOCH: 17
Loss=0.6950053572654724 Batch_id=390 Accuracy=87.56: 100%|██████████| 391/391 [00:31<00:00, 12.35it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0032, Accuracy: 8701/10000 (87.01%)


EPOCH: 18
Loss=0.4540618062019348 Batch_id=390 Accuracy=90.33: 100%|██████████| 391/391 [00:31<00:00, 12.36it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0029, Accuracy: 8842/10000 (88.42%)


EPOCH: 19
Loss=0.2989608347415924 Batch_id=390 Accuracy=91.09: 100%|██████████| 391/391 [00:31<00:00, 12.36it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0028, Accuracy: 8873/10000 (88.73%)


EPOCH: 20
Loss=0.2554750144481659 Batch_id=390 Accuracy=91.42: 100%|██████████| 391/391 [00:31<00:00, 12.34it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0028, Accuracy: 8877/10000 (88.77%)


EPOCH: 21
Loss=0.21696043014526367 Batch_id=390 Accuracy=91.83: 100%|██████████| 391/391 [00:31<00:00, 12.23it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0028, Accuracy: 8876/10000 (88.76%)


EPOCH: 22
Loss=0.11218075454235077 Batch_id=390 Accuracy=92.25: 100%|██████████| 391/391 [00:31<00:00, 12.35it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0028, Accuracy: 8893/10000 (88.93%)


EPOCH: 23
Loss=0.14965422451496124 Batch_id=390 Accuracy=92.17: 100%|██████████| 391/391 [00:31<00:00, 12.28it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0028, Accuracy: 8897/10000 (88.97%)


EPOCH: 24
Loss=0.31349560618400574 Batch_id=390 Accuracy=92.23: 100%|██████████| 391/391 [00:31<00:00, 12.34it/s]

Test set: Average loss: 0.0028, Accuracy: 8897/10000 (88.97%)
```
<hr>
<h3> Misclassified images</h3>

![IMGAGE](https://github.com/SID-SURANGE/EVA-4.0/blob/master/Session%209%20Assignment/Misclassified_S9.png)

<HR>
Author - Siddharth Surange






