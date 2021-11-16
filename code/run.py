from predictor import VisualizationDemo
from detectron2.config import get_cfg
import cv2

def setup_cfg(config_file):
    cfg = get_cfg()
    cfg.merge_from_file(config_file)
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
    cfg.freeze()
    return cfg

if __name__ == '__main__':
    path = './configs/cascade_mask_rcnn_R_50_FPN_1x.yaml'
    pic = './img/input.jpg'
    output = './img/output.jpg'
    
    cfg = setup_cfg(path)
    demo = VisualizationDemo(cfg)
    
    pic_image = cv2.imread(pic)
    
    detect_res = demo.run_on_image(pic_image)
    
    cv2.imwrite(output, detect_res[1].img)
