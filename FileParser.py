import pandas as pd

class DataFrameLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        return pd.read_csv(self.file_path)


class DataFrameSelector:
    def __init__(self, df, columns):
        self.df = df
        self.columns = columns

    def select(self):
        selected_df = self.df[self.columns]
        selected_df.index = selected_df.index + 1  # Reset the index and start from 1
        return selected_df


class DataFrameWriter:
    def __init__(self, df, file_path):
        self.df = df
        self.file_path = file_path

    def write(self):
        self.df.to_csv(self.file_path, index=False)


class DataFrameFilter:
    def __init__(self, df, column, filter_value):
        self.df = df
        self.column = column
        # self.filter = filter
        self.filter_value = filter_value


    def apply_filter(self):
        return self.df[self.df[self.column].str.contains(self.filter_value)]


loader = DataFrameLoader('./data/file/s&p_500.csv')
df = loader.load()

# Get only the three columns stated.
selector = DataFrameSelector(df, ['Security', 'GICS Sub-Industry', 'Headquarters Location'])
selected_df = selector.select()

writer = DataFrameWriter(selected_df, './data/file/refined_s&p_500.csv')
writer.write()

# Get all the Tech Industry companies into a separate file.
filter = DataFrameFilter(selected_df, 'GICS Sub-Industry', 'IT|Software|IT Services|Internet Services & Infrastructure|'+
                                                                        'Technology Hardware|Storage & Peripherals|Electronic Equipment|Instruments & Components')
it_industries_df = filter.apply_filter()

writer = DataFrameWriter(it_industries_df, './data/file/it_industries.csv')
writer.write()

# Get all the companies that are not Tech Industry compnanies into a separate file.
filter = DataFrameFilter(selected_df, 'GICS Sub-Industry', 'IT|Software|IT Services|Internet Services & Infrastructure|'+
                                                                        'Technology Hardware|Storage & Peripherals|Electronic Equipment|Instruments & Components')
non_it_industries_df = selected_df.drop(it_industries_df.index)

# Add new column 'hiring_software_engineers' with all values set to False
non_it_industries_df = non_it_industries_df.assign(hiring_software_engineers=False)

writer = DataFrameWriter(non_it_industries_df, './data/file/non_it_industries.csv')
writer.write()