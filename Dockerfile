FROM pytorch/pytorch:1.8.1-cuda10.2-cudnn7-devel

RUN apt-get -y update \
    && apt-get install -y git libgl1-mesa-glx libglib2.0-0

# RUN pip install torch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0
RUN pip install 'git+https://github.com/facebookresearch/detectron2.git'
RUN pip install opencv-python


COPY code /workspace