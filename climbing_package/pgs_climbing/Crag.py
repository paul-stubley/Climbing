import pandas as pd
import matplotlib.pyplot as plt
from Constants import *

class Crag():
    '''This class covers *crag* objects, the cliff which houses the routes.
    
    Attributes:
        name
        latitude
        longitude
        rock_type
        route_list  - Adjusted automatically by creating a new route.
        route_count - Adjusted automatically by creating a new route.
    Methods:
        plot_crag_summary
        
        
    TODO:
        Simplify plot into number-grades
    '''
    def __init__(self, name, lat='Unknown', long='Unknown', rock_type='Unknown'):
        '''Initialise the object'''
        self.name = name
        self.lat  = lat
        self.long = long
        self.rock_type = rock_type
        self.route_dict = {}
        self.route_count = 0
        
    def plot_crag_summary(self):
        '''This creates a histogram of the grades at this crag and plots it
        
        Args:
            None
        Returns:
            None
        '''
        # Create df from GRADE_LIST
        grade_df = pd.DataFrame(GRADES_LIST).set_index(0)
        grade_df['count']=0

        # Add counts into it
        grade_counts = pd.Series(item[1].grade for item in self.route_dict.items()).value_counts()

        for i in grade_counts.items():
            grade_df.loc[i[0],'count']=i[1]

        # Plot
        fig,ax = plt.subplots(1,1)
        grade_df.plot(kind='bar', color=GRADES_COLORS, ax=ax, width = 1)
        
        # Formatting
        ax.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')
        ax.legend().set_visible(False)
        ax.set_yticks([])
        ax.set_xlabel('')
        plt.tick_params(axis='x', top=False) 
        plt.box(on=None)
        
    def __repr__(self):
        '''This magic method defines how Crag objects present themselves'''
        return 'Name: {} | Location: {},{}'.format(self.name,self.lat,self.long)
    
        