import numpy as np
import pandas as pd
import os
import SimpleITK
import settings_tc

# df_result = pd.DataFrame(result, columns=['seriesuid','coordX', 'coordY', 'coordZ', 'probability'])

MHD_BASE_DIR = settings_tc.BASE_DIR_SSD

num_test_subset = 5

pixel_submission_file = '/home/chicm/ml/tianchi/kaggle_ndsb2017/submission1.csv'

target_csv_file = '/home/chicm/ml/tianchi/kaggle_ndsb2017/sub_mm.csv'

def find_mhd_file(seriesuid):
    for i in range(num_test_subset):
        filename = MHD_BASE_DIR + 'test_subset' + str(i).zfill(2) + '/' + seriesuid + '.mhd'
        if os.path.exists(filename):
            return filename
    print('can not find mhd file: {}'.format(seriesuid))

param_dict = {}

def get_origin_spacing(seriesuid):
    
    if seriesuid in param_dict:
        return param_dict[seriesuid]

    #print(seriesuid)

    src_path = find_mhd_file(seriesuid)

    itk_img = SimpleITK.ReadImage(src_path)
    img_array = SimpleITK.GetArrayFromImage(itk_img)
    #print("Img array: ", img_array.shape)

    origin = np.array(itk_img.GetOrigin())      # x,y,z  Origin in world coordinates (mm)
    #print("Origin (x,y,z): ", origin)

    #direction = np.array(itk_img.GetDirection())      # x,y,z  Origin in world coordinates (mm)
    #print("Direction: ", direction)


    spacing = np.array(itk_img.GetSpacing())    # spacing of voxels in world coor. (mm)
    print("Spacing (x,y,z): ", spacing)
    #rescale = spacing / settings_tc.TARGET_VOXEL_MM
    #print("Rescale: ", rescale)

    param_dict[seriesuid] = (origin, spacing)
    return origin, spacing

def convert():

    df = pd.read_csv(pixel_submission_file)
    #converted = np.zeros(df.values.shape)
    for i, row in enumerate(df.values):
        uid = row[0]
        x, y, z = row[1], row[2], row[3]
        prob = row[4]
        origin, spacing = get_origin_spacing(uid)
        coords = np.array([x, y, z]) * spacing + origin
        df.ix[i, 'coordX'] = coords[0]
        df.ix[i, 'coordY'] = coords[1]
        df.ix[i, 'coordZ'] = coords[2]
        print([x,y,z])
        print('spacing:{}'.format(spacing))
        print('origin:{}'.format(origin))
        print('cords:{}'.format(coords))
    print(df.head(10))

    df.to_csv(target_csv_file, index=False)

convert()