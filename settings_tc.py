import os
#COMPUTER_NAME = os.environ['hostname']
#print("Computer: ", COMPUTER_NAME)

TARGET_VOXEL_MM = 1.00
MEAN_PIXEL_VALUE_NODULE = 41
LUNA_SUBSET_START_INDEX = 0
SEGMENTER_IMG_SIZE = 320

#BASE_DIR_SSD = "C:/werkdata/kaggle/ndsb3/"
BASE_DIR_SSD = '/home/chicm/ml/kgdata/tianchi/'
#BASE_DIR_SSD = '/home/chicm/ml/kgdata/luna16/'

#BASE_DIR = "D:/werkdata/kaggle/ndsb3/"
BASE_DIR = '/home/chicm/ml/kgdata/tianchi/'
#BASE_DIR = '/home/chicm/ml/kgdata/luna16/'
EXTRA_DATA_DIR = "resources/"
#NDSB3_RAW_SRC_DIR = BASE_DIR + "ndsb_raw/stage12/"
NDSB3_RAW_SRC_DIR = '/home/chicm/ml/kgdata/dsb/stage1/'
LUNA16_RAW_SRC_DIR = BASE_DIR 

#NDSB3_EXTRACTED_IMAGE_DIR = BASE_DIR_SSD + "ndsb3_extracted_images/"
NDSB3_EXTRACTED_IMAGE_DIR = '/home/chicm/ml/kgdata/dsb/ndsb3_extracted_images/'

LUNA16_EXTRACTED_IMAGE_DIR = BASE_DIR_SSD + "extracted_images/"
#NDSB3_NODULE_DETECTION_DIR = BASE_DIR_SSD + "ndsb3_nodule_predictions/"

