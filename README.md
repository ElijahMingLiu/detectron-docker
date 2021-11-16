This is pytorch 1.8 and cuda 10.2 and detectron2
STEPS

1. Install nvidia-docker according to [this link](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#install-guide)

2. Run shell `wget https://dl.fbaipublicfiles.com/detectron2/Misc/cascade_mask_rcnn_R_50_FPN_1x/138602847/model_final_e9d89b.pkl`

3. Run shell `docker build -t detectron-docker .`

4. Run shell `nvidia-docker run -it detectron-docker python run.py`

If no error, you succeed!
