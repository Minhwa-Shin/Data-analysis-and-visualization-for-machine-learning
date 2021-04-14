import numpy as np
import pandas as pd

frame = pd.DataFrame(np.arange(9).reshape((3,3)),
                    index=['a','c','d'],
                    columns=['Ohio','Texas','California'])
print('\n',frame)

frame2=frame.reindex(['a','b','c','d'])
print('\n',frame2)

state=['Texas','Utah','California']
frame3=frame.reindex(columns=state)
print('\n',frame3)
