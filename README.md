# Kaggle national datascience bowl 2017 2nd place code
This is the source code for my part of the 2nd place solution to the [National Data Science Bowl 2017](https://www.kaggle.com/c/data-science-bowl-2017/) hosted by Kaggle.com. For documenation about the approach go to: http://juliandewit.github.io/kaggle-ndsb2017/

#### Dependencies & data
The solution is built using Keras with a tensorflow backend on windows 64bit.
Next to this I used scikit-learn, pydicom, simpleitk, beatifulsoup, opencv and XgBoost.
All in all it was quite an engineering effort.

#### General
The source contains much dead code. Cleaning up 100% was too risky on such short notice.
The solution relies on manual labels, generated labels and 2 resulting submissions from team member Daniel Hammack. These files are all in this archive and can be put at the location as can be configured in the settings.py. Trained models are also provided through a download url URL
The solution is a combination of nodule detectors/malignancy regressors. My two parts are trained with LUNA16 data with a mix of positive and negative labels + malignancy info from the LIDC dataset. My second part also uses some manual annotations made on the NDSB3 trainset. Predictions are generated from the raw nodule/malignancy predictions combined with the location information and general “mass” information. Masses are no nodules but big suspicious tissues present in the CT-images. De masses are detected with a U-net trained with manual labels.
The 3rd and 4th part come from Daniel’s solution. 
My final solution is a blend of the 4 different part. Blending is done by taking a simple average.

#### Preprocessing
First run step1_preprocess_ndsb.py. This will extract all the ndsb dicom files , scale to 1x1x1 mm, and make a directory containing .png slice images. Lung segmentation mask images are also generated. They will be used later in the process for faster predicting.
Then run step1_preprocess_luna16.py. This will extract all the LUNA source files , scale to 1x1x1 mm, and make a directory containing .png slice images. Lung segmentation mask images are also generated. This step also generates various CSV files for positive and negative examples.
The nodule detectors are trained on positive and negative 3d cubes which must be generated from the LUNA16 and NDSB datasets. step1b_preprocess_make_train_3dimages.py takes the different csv files and cuts out 3d cubes from the patient slices. The cubes are saved in different directories.
step1_preprocess_mass_segmenter.py is to generate the mass u-net trainset. It can be run but the generated resized images + labels is provided in this archive so this step does not need to be run. However, this file can be used to regenerate the traindata.

#### Training neural nets
This step can be skipped if you take the models that are provided the download link: URL
First train the 3D convnets that detect nodules and predict malignancy. This can be done by running 
the step2_train_nodule_detector.py file. This will train various combinations of positive and negative labels. The resulting models (NAMES) are stored in the ./workdir directory.
The mass detector can be trained using step2_train_mass_segmenter.py. It trains 3 folds and models are stored in the ./workdir (names)
Training the 3D convnets will be around 10 hours per piece. The 3 mass detector folds will take around 8 hours in total

#### Predicting neural nets
Once trained or downloaded through the URL the models can be placed in the ./models/ directory.
From there the nodule detector step3_predict_nodules.py  can be run to detect nodules in a 3d grid per patient. The detected nodules and predicted malignancy are stored per patient in a separate directory. 
The masses detector can be run through step2_train_mass_segmenter.py and will write a csv with estimated masses per patient.

#### Training of submissions, combining submissions for final  submission.
Based on the per-patient csv’s the masses.csv and other metadata we will train an xgboost model to generate submissions (step4_train_submissions.py). There are 3 levels of submissions. First the per-model submissions. (level1). Different models are combined in level2, and Daniel’s submissions are added. These level 2 submissions will be combined (averaged) into one final submission.
Below are the different models that will be generated/combined.
Level 1:
Luna16_fs (trained on full luna16 set)
Luna16_ndsbposneg v1 (trained on luna16 + manual pos/neg labels in ndsb)
Luna16_ndsbposneg v2 (trained on luna16 + manual pos/neg labels in ndsb)
2, 3 will be averaged into 1 level 2 model
Level 2.
Luna16_fs
Luna16_ndsbposneg
Daniel model 1
Daniel model 2
These 4 models will be averaged into 1 final_submission.csv
