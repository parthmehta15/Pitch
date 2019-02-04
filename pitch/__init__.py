import  scipy.io.wavfile  as wav
import matplotlib.pyplot as plt
import numpy as np

def find_pitch(audiofile):
    fs,x = wav.read(audiofile)
    ms20=int((fs/50))
    ms2=int(fs/500)

    x=[i/32767 for i in x]

    y=plt.acorr(x,maxlags=ms20,normed=True)

    y=y[1]
    z=y[round(len(y)/2):]
    z=z[ms2:ms20]
    zmax=max(z)

    index=np.where(z==zmax)
    index=index[0][0]

    pitch=fs/(ms2+index+2)

    return pitch
