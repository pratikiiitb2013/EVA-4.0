params  = {
  "transform_library" : "albumentation", ## use "torch" or "albumentation"
  "model": "resnet18",
  "dataset": "CIFAR10",
  "CIFAR10_normalize_values": {"mean" : (0.5, 0.5, 0.5), "std" : (0.5, 0.5, 0.5)},
  "MNIST_normalize_values": {"mean" : (0.1307,), "std" : (0.3081,)},
  "batch_size" : 512,
  "transforms" : { "torch" : {
                              "RandomHorizontalFlip" : True, 
                              "RandomRotation" : True,
                              "ColorJitter" : True,
                              "Cutout" : False
                  },
                  "albumentation" : {
                              "PadIfNeeded" : True,
                              "RandomCrop" : True,
                              "HorizontalFlip" : True, 
                              "Rotate" : False,
                              "HueSaturationValue" : False,
                              "Cutout" : True
                  }
				},
  "transform_values" : { "torch" : {
                                      "RandomHorizontalFlip" : {"p" :0.5},
                                      "RandomRotation" : {"degrees" : 5},
                                      "ColorJitter" : {"hue" : 0.05, "saturation" : 0.05}
                          },
                          "albumentation" : {
                                      "PadIfNeeded" : {"min_height" : 40, "min_width" : 40, "border_mode" : 1, "always_apply" : True},
                                      "RandomCrop" : {"height" : 32, "width" : 32, "always_apply" : True},
                                      "HorizontalFlip" : {"p" :0.5},
                                      "Rotate" : {"limit" : 5},
                                      "HueSaturationValue" : {"hue_shift_limit" : 0.05, "sat_shift_limit" : 0.05},
                                      "Cutout" : {"max_h_size" : 8, "max_w_size" : 8, "num_holes" : 1, "always_apply" : True}
                              
                          }
						},
  "n_workers" : 2,
  "dropout" : 0.0
}