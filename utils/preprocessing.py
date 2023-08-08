# Script to preprocess the data

import pandas as pd

class Preprocessor:
    
    def __init__(self,filepath=None,df=None):
        self.filepath = filepath
        self.df = df
        
    def import_data(self):
        # Import the csv data file
        self.df = pd.read_csv(self.filepath)
        return self.df
    
    def replace_autres_formats(self):
        # Replace "Autres formats" by the right one
        df = self.df
        df['format_panneau'] = [format if format != 'Autres formats' else df['autres_formats'][i] for i,format in enumerate(df['format_panneau'])]
        df.drop(columns=['autres_formats'],inplace = True)
        self.df = df
        return self.df
    
    def put_in_upper(self):
        # Upperize the name of location
        df = self.df
        df['emplacement'] = df['emplacement'].str.upper()
        self.df = df
        return self.df
        
    def apply_steps(self):
        # Import data
        self.import_data()
        # Replace autres formats
        self.replace_autres_formats()
        # Upperize the name of location
        self.put_in_upper()