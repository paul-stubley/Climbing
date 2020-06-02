from Constants import *


class Route():
    '''This class covers *route* objects, the individual routes at each crag.
    Attributes:
        name   (str)
        crag   (Crag)  - Note, this is a crag object, not a string
        height (float) - height of route in metres
        grade  (str)
        bolts  (int)   - Number of bolts on the route
        notes  (str)   - Optional free text description of route
    Methods:
        add_to_crag()  - Appends this route to the crag
        
    TODO: Data validation to check if grade is in accepted list
    '''
    def __init__(self, name, crag, height, grade, bolts='Unknown', notes=''):
        '''Initialise route and add to crag, iff crag doesn't exist - create it'''
        self.name = name
        self.crag = crag
        self.height = height
        self.grade = grade
        self.bolts = bolts
        self.notes = notes
        self._add_to_crag() # Add this new route the associated crag
        
    def _add_to_crag(self):
        '''Adds this route to the associated crag object
        Args:
            None
        Returns:
            None
        '''
        self.crag.route_dict[self.name]=self
        
    def __repr__(self):
        '''This magic method defines how Route objects present themselves'''
        return 'Name: {} | Grade: {}'.format(self.name,self.grade)
            
            