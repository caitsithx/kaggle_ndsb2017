import pandas as pd
import numpy as np
import os, glob

PRED_DIR = '/home/chicm/ml/kgdata/tianchi/predictions/predictions10_luna16_fs'

def create_submission(filepath, tgt_csv_file):
    result = None
    old_dir = os.getcwd()
    os.chdir(filepath)
    files = glob.glob('*.csv')
    for fn in files:
        full_fname = os.path.join(filepath, fn)
        patient_id = fn.split('.')[0]
        df = pd.read_csv(full_fname)
        preds = df.loc[df['diameter_mm'] > 3, ['abs_x', 'abs_y', 'abs_z', 'nodule_chance']].values
        num = preds.shape[0]
        ids = np.array([patient_id]*num).reshape(num, 1)
        res = np.hstack((ids,preds))
        
        if result is None:
            result = res
        else:
            result = np.vstack((result,res))
    df_result = pd.DataFrame(result, columns=['seriesuid','coordX', 'coordY', 'coordZ', 'probability'])
    os.chdir(old_dir)
    df_result.to_csv(tgt_csv_file, index=False)

create_submission(PRED_DIR, './submission1.csv')

