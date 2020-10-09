import os, shutil, re

# # Get root directory with files
source_dir = '../DATASETS/GAIT-IST'

# # Define destination directory
dest_dir = '../DATASETS/GAIT-IST-GEIs'
os.mkdir(dest_dir)

classes = {'diplegic' : 0, 'hemiplegic' : 1, 'neuropathic' : 2, 'normal' : 3, 'parkinsonian' : 4}

# Nice funtion to implement natural sort on file names (1 2 .. 10 11 VS 1 10 11 .. 2)
# https://blog.codinghorror.com/sorting-for-humans-natural-sort-order/
def sort_nicely( l ):
    # Sort the given list in the way that humans expect.
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    l.sort( key=alphanum_key )

## Train GEIs directories
for pathology in list(classes.keys()):

    pathology_dir = source_dir + '/{}'.format(pathology)
    dest_pathology_dir = os.path.join(dest_dir, pathology)
    os.mkdir(dest_pathology_dir)

    pathology_subj_folders = [name for name in os.listdir(pathology_dir) if os.path.isdir(os.path.join(pathology_dir, name))]

    # /Pathology/subj{i}/GEIs/subj_{i}-pat_{j}-lvl_{k}-{l}_{direction}
    sort_nicely(pathology_subj_folders)
    for subj_folder in pathology_subj_folders:
        subj_folder_dir = os.path.join(pathology_dir, subj_folder)
        dest_subj_folder_dir = os.path.join(dest_pathology_dir, subj_folder)
        os.mkdir(dest_subj_folder_dir)

        # print(subj_folder_dir)
        subj_GEIs_dir = os.path.join(subj_folder_dir, 'GEIs')
        dest_subj_GEIs_dir = os.path.join(dest_subj_folder_dir, 'GEIs')
        os.mkdir(dest_subj_GEIs_dir)
        # print(subj_GEIs_dir)

        subj_GEIs_folders = [name for name in os.listdir(subj_GEIs_dir) if os.path.isdir(os.path.join(subj_GEIs_dir, name))]
        sort_nicely(subj_GEIs_folders)

        for folder in subj_GEIs_folders:
            # Directory with the GEI images
            subj_pat_lvl_dir = os.path.join(subj_GEIs_dir, folder)
            dest_subj_pat_lvl_dir = os.path.join(dest_subj_GEIs_dir, folder)
            os.mkdir(dest_subj_pat_lvl_dir)
            # print(subj_pat_lvl_dir)
            file_names = os.listdir(subj_pat_lvl_dir)
            sort_nicely(file_names)
            # print(file_names)
            
            # Convert images to numpy arrays, put in batches
            for file_name in file_names:
                file_path = os.path.join(subj_pat_lvl_dir, file_name)

                # Create destination file path
                dest_file_path = os.path.join(dest_subj_pat_lvl_dir, file_name)

                # Copy file from source to destination
                shutil.copyfile(file_path, dest_file_path)