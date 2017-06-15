import os, glob

DATA_DIR = '/home/chicm/ml/kgdata/tianchi'

ids = []
for i in range(5):
    filenames = glob.glob(DATA_DIR+'/test_subset'+str(i).zfill(2) + '/*.mhd')
    for fn in filenames:
        ids.append(fn.split('/')[-1].split('.')[0])

print(ids)
with open('sample_submission.csv', 'w') as f:
    header = 'seriesuid,coordX,coordY,coordZ,probablity\n'
    f.write(header)
    for seriesuid in ids:
        line = '{},0,0,0,0.5\n'.format(seriesuid)
        f.write(line)