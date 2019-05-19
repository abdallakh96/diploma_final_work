import os

path = "gdrive/My Drive/checkset_descriptors"

uno = "/unopictures/best"
stereoscopic = "/stereoscopic/best"
epsilon = 0.2


list = os.listdir(path + uno)
for l in list:
    N_correct_uno = 0
    N_correct_stereo = 0
    files = os.listdir(path + uno +"/"+ l)
    arrays_uno = {}
    arrays_stereo = {}
    i = 0
    for element in files:
        arrays_uno[i] = np.load(path +"/"+ uno +"/"+ l + "/" + element)
        arrays_stereo[i] = np.load(path +"/"+ stereo +"/"+ l + "/" + element)
        i = i + 1
    for i in range(500):
        break
        for j in range(500):
            if distance(arrays_uno[i],arrays_uno[j])<epsilon:
                N_correct_uno  = N_correct_uno+1
            if distance(arrays_stereo[i],arrays_stereo[j])<epsilon:
                N_correct_stereo  = N_correct_stereo + 1

    print("Folder: " + l)            
    print("correct uno: " + str(N_correct_uno) +" is percent " + str(N_correct_uno/(500*500)))
    print("correct stereo: " + str(N_correct_stereo) +" is percent " + str(N_correct_stereo/(500*500)))