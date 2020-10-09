import sys
sys.path.append('/home/pfa/Documents/Code')
import os
from sort import sort_nicely

os.chdir('/home/datasets/FCCN_Videos')

erros = {'Heniplegic': 'Hemiplegic', 'Neuropatia': 'Neuropathic', 'Parquinson': 'Parkinson'}

# Get list of subjects and sort it
subjects = [sub for sub in os.listdir(os.getcwd())]
sort_nicely(subjects)

for sub in subjects:

    # Get list of sequences of subject and sort it
    subjectPath = os.path.join(os.getcwd(),sub)
    sequences = os.listdir(subjectPath)
    sort_nicely(sequences)

    for sequence in sequences:
        for erro in erros:
            if erro in sequence:
                sequencePath = os.path.join(subjectPath,sequence)
                correctSequencePath = os.path.join(subjectPath,sequence.replace(erro,erros[erro]))
                print('antes: ', sequencePath, 'depois: ', correctSequencePath)
                os.rename(sequencePath, correctSequencePath)
    #print(sequences)


