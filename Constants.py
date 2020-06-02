import numpy as np

# Create the possible sports grade list
GRADES_LIST = [['4'],['4+'],['5'],['5+']]+[[i+l,i+l+'+'] for i in ['6','7'] for l in ['a','b','c']]
GRADES_LIST = [val for sublist in GRADES_LIST for val in sublist]
GRADES_COLORS = [np.array(['g']*4+['orange']*4+['r']*4+['k']*(len(GRADES_LIST)-12))]  # Format needed to use as color list in pandas 
