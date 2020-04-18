
<h2><i> Assignment B </I></h2>
<hr>

<h3><i> Task to accomplish </I></h3>

```
Assignment B:
1) Download 50 images of dogs. 
2) Use this (Links to an external site.) to annotate bounding boxes around the dogs.
3) Download JSON file. 
4) Describe the contents of this JSON file in FULL details (you don't need to describe all 10 instances, anyone would work). 
5) Refer to this tutorial (Links to an external site.). Find out the best total numbers of clusters. Upload link to your Colab File uploaded to GitHub. 


```

<h3><i>Annotation file explained</I></h3>

```
JSON file - Annotation data for first file

 'images': [{'id': 0,
   'width': 421,
   'height': 499,
   'file_name': 'dog.4001.jpg',
   'license': 1,
   'date_captured': ''},


'annotations': [{'id': 0,
   'image_id': '0',
   'category_id': 1,
   'segmentation': [107, 56, 328, 56, 328, 493, 107, 493],
   'area': 96577,
   'bbox': [107, 56, 221, 437],
   'iscrowd': 0},


Explanation - Important terms -

In 'images' key :
1) width - The actual width of the image on which the annotation is done - 421
2) height - The actual height of the image on which the annotation is done - 499
3) file_name - name of the image as in folder. (dog.4001.jpg)

In 'annotations' key
1) bbox - [107, 56, 221, 437],
   1) 107, 56 - These are the centre coordinates for the bounding box. 107 - x and 56 - y
   2) 221,437 - These are the width and height respective to bbox. Width=221, Height = 437
   
```

<h3><i> Clusters for the data with optimal clusters to be 5 </I></h3>

![img](https://github.com/SID-SURANGE/EVA-4.0/blob/master/Session%2012%20YOLO/Assignment%20B/Cluster.png)
