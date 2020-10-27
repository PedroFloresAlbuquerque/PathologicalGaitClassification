import os

pathOut = "/home/datasets/metadata"
pathologies = {'Diplegic': 'pat1', 'Hemiplegic': 'pat2', 'Neuropathic': 'pat3', 'Normal': 'normal', 'Parkinson': 'pat4'}
cameras = {'Camera 1': 'front_view', 'Camera 3': 'side_view'}
subs = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12','s13', 's14', 's15', 's16', 's17', 's18', 's19', 's20', 's21', 's22', 's23']

os.mkdir(pathOut)

# Iterate through pathologies to access each pathology directory
for pathology in pathologies:

    # Create folder path for each pathology in DATASETS directory
    pathology_dir = os.path.join(pathOut, pathology)
    os.mkdir(pathology_dir)

    # Create folder for each subject in each pathology directory
    for sub in subs:
        sub_dir = os.path.join(pathology_dir, sub)
        os.mkdir(sub_dir)

        # Create folder for binary silhouettes
        sub_dir_silhouettes = os.path.join(sub_dir, 'silhouettes')
        os.mkdir(sub_dir_silhouettes)

        # Create folder for each view angle in the subject silhouettes directories
        for view in ['side_view']:
            # Silhouettes
            silhouettes_view_dir = os.path.join(sub_dir_silhouettes, view)
            os.mkdir(silhouettes_view_dir)
    
