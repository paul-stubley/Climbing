from dateutil.relativedelta import relativedelta
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
from Constants import *


class Climber():
    '''This class covers the *climber* objects
    Attributes:
        name (str)
        climb_list (dict)
        personal_best (str)
        dob (date)            - Date of birth input Format 'DD/MM/YYYY'
    Methods:
        add_climb(Route)
        get_age()
        plot_progress()
        
    TODO: 
        Data validation on DOB input
        Data validation on attempt_type for add_climb()
        Sort overlapping points in plot_progress chart
        Sort colour of points in plot_progress chart
    '''
    
    def __init__(self, name, dob):
        self.name = name
        self.dob = date(*list(map(int,dob.split('/')))[::-1]) # Split DOB, map to ints, and unpack into date function
        self.climb_list = {}
        
    def get_age(self):
        '''Calculates the climbers age from todays date and their DOB
        Args:
            None
        Returns:
            Int - Age in years
        '''
        return relativedelta(date.today(), self.dob).years
    
    def add_climb(self, route, attempt_date, best_attempt_type):
        '''Adds certain route to a climbers list of routes, including the attempt type
        Args:
            route - Route object that was attempted
            attempt_date - Date attempted
            best_attempt_type - One of 'Flash', 'Top', 'Dogged', 'Attempt'
        Return:
            None
        '''
        self.climb_list[route.name+"|"+attempt_date] = [route, date(*list(map(int,attempt_date.split('/')))[::-1]), best_attempt_type]
        
    def plot_progress(self):
        '''This plots the route attempts through time
        Args:
            None
        Return:
            None
        '''
        # Get climbs in suitable format
        df = pd.DataFrame.from_dict(self.climb_list, orient='index', columns=['route_object','date','attempt_type'])
        df['grade'] = df.apply(lambda x: x.route_object.grade, axis=1)
        
        # Create gradescale to translate grade to axis position
        grades_to_scale = {g:i for i,g in enumerate(GRADES_LIST)}
        scale_to_grades = {i:g for i,g in enumerate(GRADES_LIST)}
        attempt_type_styles = {'Flash':'*','Top':'d','Dogged':'o','Attempt':'x'}

        # Plot
        fig,ax = plt.subplots(1,1)
        for at in ['Flash','Top','Dogged','Attempt']:
            df_temp = df[df.attempt_type == at]
            sct = ax.scatter(df_temp.date
                       , df_temp.apply(lambda x: grades_to_scale[x.grade], axis=1)
                       , marker=attempt_type_styles[at]
                       , s = 60
                       , c='g')
            sct.set_label(at)

        # Format
        plt.gcf().autofmt_xdate() # Prettify the x-labels
        ax.set_xlabel('')
        ax.legend(bbox_to_anchor=(1.28, 1))
        # Relabel yticks, blank string if not visible on axis
        y0, y1 = ax.get_ylim()
        ytick_labels = [scale_to_grades[t] if (t>=y0 and t<=y1) else '' for t in ax.get_yticks()]
        ax.set_yticklabels(ytick_labels);
     
    def __repr__(self):
        '''This magic method defines how Route objects present themselves'''
        return "Name: {}, Climbs: {}".format(self.name, len(self.climb_list))