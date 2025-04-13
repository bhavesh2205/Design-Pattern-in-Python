import pandas as pd
from abc import ABC, abstractmethod

# Context class
class DataHandlerContext:
    """
    The Context class defines the interface of interest to clients.
    It also maintains a reference to a Concrete Strategy object.
    """
    def __init__(self, strategy):
        """
        The Context class initializes with a specific strategy.
        """
        self.strategy = strategy

    def handle(self, df, column):
        """
        The Context class delegates the responsibility to the strategy object.
        """
        return self.strategy.handle_missing(df, column)

# Strategy Interface
class MissingValueStrategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.
    The Context uses this interface to call the algorithm defined by Concrete Strategies.
    """
    @abstractmethod
    def handle_missing(self, df, column):
        
        pass

# Concrete strategies
class DropStrategy(MissingValueStrategy):
    
    def handle_missing(self, df, column)->pd.DataFrame:
        """
        Concrete Strategies implement the algorithm while following the base Strategy interface.
        
        args:
            df: pandas.DataFrame
            column: str
        returns:
            pandas.DataFrame
        """
        return df.dropna(subset=[column])

class MeanStrategy(MissingValueStrategy):
    
    def handle_missing(self, df, column)->pd.DataFrame:
        """
        Concrete Strategies implement the algorithm while following the base Strategy interface.
        
        args:
            df: pandas.DataFrame
            column: str
        returns:
            pandas.DataFrame
        """
        df[column] = df[column].fillna(df[column].mean())
        return df

class MedianStrategy(MissingValueStrategy):
    
    def handle_missing(self, df, column)->pd.DataFrame:
        """
        Concrete Strategies implement the algorithm while following the base Strategy interface.
        
        args:
            df: pandas.DataFrame
            column: str
        returns:
            pandas.DataFrame
        """
        df[column] = df[column].fillna(df[column].median())
        return df

# usage
df = pd.read_csv('data/car_insurance.csv')

context = DataHandlerContext(MeanStrategy())
df_cleaned = context.handle(df.copy(), 'credit_score')

print(df_cleaned['credit_score'])

