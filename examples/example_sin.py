import numpy as np
import pandas as pd
from faerun import Faerun


faerun = Faerun(view='free', shader='circle')

t = np.linspace(0, 12.0, 326)
s = np.sin(np.pi * t)
c = np.cos(np.pi * t)
 
data = {
    'x': t,
    'y': s,
    'z': c,
    'c': t / max(t)
}

df = pd.DataFrame.from_dict(data)
faerun.plot(df)
