import pandas as pd

from abc import ABC, abstractmethod


# abstract base class for missing value strategies
class MissingValueStrategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.
    The Context uses this interface to call the algorithm defined by Concrete Strategies.
    """
    @abstractmethod
    def handle_missing(self, df: pd.DataFrame, column: str) -> pd.DataFrame:
        """
        The abstract method to handle the missing values.
        
        args:
            df: pandas.DataFrame - dataframe to handle missing values
            column: str - column to handle missing values
        returns:
            pandas.DataFrame - dataframe with missing values handled
        """
        pass

# concrete strategies dropping missing values
class DropStrategy(MissingValueStrategy):
    
    def handle_missing(self, df, column)->pd.DataFrame:
        """
        perform the concrete strategy of dropping missing values.
        
        args:
            df: pandas.DataFrame - dataframe to handle missing values
            column: str - column to handle missing values
        returns:
            pandas.DataFrame - dataframe with missing values handled
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

# context class for missing value strategies
class DataHandlerContext:
    """
    The Context class defines the interface of interest to clients.
    It also maintains a reference to a Concrete Strategy object.
    """
    def __init__(self, strategy: MissingValueStrategy):
        """
        The Context class initializes with a specific strategy.
        
        args:
            strategy: MissingValueStrategy - strategy to handle missing values
        returns:
            None
        """
        self._strategy = strategy
        
    def set_strategy(self, strategy: MissingValueStrategy):
        """
        Set the strategy to handle missing values.
        
        args:
            strategy: MissingValueStrategy - strategy to handle missing values
        returns:
            None
        """
        self._strategy = strategy

    def handle(self, df: pd.DataFrame, column: str) -> pd.DataFrame:
        """
        The Context class delegates the responsibility to the strategy object.
        
        args:
            df: pandas.DataFrame - dataframe to handle missing values
            column: str - column to handle missing values
        returns:
            pandas.DataFrame - dataframe with missing values handled
        """
        return self._strategy.handle_missing(df, column)

# usage
if __name__ == "__main__":
    # load the data
    df = pd.read_csv('data/car_insurance.csv')

    # create a context using the MedianStrategy
    data_handler = DataHandlerContext(MedianStrategy())

    # handle the missing values
    df_cleaned = data_handler.handle(df.copy(), 'credit_score')
    #print the cleaned column
    print(df_cleaned['credit_score'])

