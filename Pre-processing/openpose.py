import sys
sys.path.append('/Users/pedroflores/Documents/IST/Tese/Code')
import os
from sort import sort_nicely

pathOut = '../DATASETS/GAIT-IST-2020'
pathologies = {'Diplegic': 'pat1', 'Hemiplegic': 'pat2', 'Neuropathic': 'pat3', 'Normal': 'normal', 'Parkinson': 'pat4'}
cameras = {'Camera 1': 'front_view', 'Camera 3': 'side_view'}
severity2lvl = {'s1': 'lvl1', 's2': 'lvl2', 'Normal': ''}

# Go to directory with video sequences of subjects
subjects_path = '/Users/pedroflores/Documents/IST/Tese/DATASETS/GAIT-IST-subs/'
os.chdir(subjects_path)

# Get list of subjects and sort it
subjects = [sub for sub in os.listdir(subjects_path) if '.DS' not in sub]
sort_nicely(subjects)
#print(subjects)

# Build dict with list of video filenames for each subject
subjects_sequences = {}

for sub in subjects:

    # Get list of sequences of subject and sort it
    sequences = os.listdir(subjects_path + sub)
    sort_nicely(sequences)
    subjects_sequences[sub] = sequences

# Change directory to openpose to run it
os.chdir('/Users/pedroflores/Documents/IST/Tese/openpose')

# Iterate through subjects to run openpose on each of its sequences
for subject in subjects_sequences:

    for sequence in subjects_sequences[subject]:
        pathIn = os.path.join('../DATASETS/GAIT-IST-subs/', subject, sequence)

        for pathology in pathologies:
            if pathology in sequence:
                for camera in cameras:
                    if camera in sequence:
                        for severity in severity2lvl:
                            if severity in sequence:
                                # Final folder name: subXpatYlvlZ_Wdireaction
                                dest_folder_name = sub+pathologies[pathology]+severity2lvl[severity]
                                # pathology/subject/view/subXpatYlvlZ_Wdireaction
                                dest_dir = os.path.join(pathOut,pathology,subject,'pose',cameras[camera],dest_folder_name)

        os.system('./build/examples/openpose/openpose.bin --video ' + pathIn + ' --part_candidates --write_json ' + dest_dir + ' --display 0 --render_pose 0')

# ./build/examples/openpose/openpose.bin --video examples/media/output.mpg --part_candidates --write_json ../DATASETS/GAIT-IST-2020/pose2/ --display 0 --render_pose 0
