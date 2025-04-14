import pandas as pd
from abc import ABC, abstractmethod


# base strategy interface
class MissingValueStrategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.
    The Context uses this interface to call the algorithm defined by Concrete Strategies.
    """

    @abstractmethod
    def handle_missing(self, df, column):
        """
        The abstract method to handle the missing values.
        """
        pass


# strategy 1: drop
class DropStrategy(MissingValueStrategy):
    """
    The Concrete Strategy implements the algorithm while following the base Strategy interface.
    """

    def handle_missing(
        self, df: pd.DataFrame, column: str) -> pd.DataFrame:  # public method
        """
        The concrete method to handle the missing values.
        
        args:
            df: pandas.DataFrame
            column: str
        returns:
            pandas.DataFrame
        """
        if self._column_has_missing_values(df, column):
            return df.drop(columns=[column])
        else:
            return df

    def _column_has_missing_values(self, df: pd.DataFrame, column: str) -> bool:
        """
        The private method to check if the column has missing values.
        
        args:
            df: pandas.DataFrame - dataframe to check for missing values
            column: str - column to check for missing values
        returns:
            bool - True if the column has missing values, False otherwise
        """
        return df[column].isnull().any()


# strategy 2: mean imputation
class MeanStrategy(MissingValueStrategy):
    def handle_missing(self, df: pd.DataFrame, column: str) -> pd.DataFrame:  # public
        """
        The concrete method to handle the missing values using mean imputation.
        args:
            df: pandas.DataFrame
            column: str
        returns:
            pandas.DataFrame
        """
        mean_value = self._calculate_mean(df, column)
        df[column] = df[column].fillna(mean_value)
        return df

    def _calculate_mean(self, df: pd.DataFrame, column: str) -> float:
        """
        The private method to calculate the mean of the column.
        args:
            df: pandas.DataFrame - dataframe to calculate the mean of the column
            column: str - column to calculate the mean of the column
        returns:
            float - mean of the column
        """
        return df[column].mean()


# strategy 3: custom imputation
class CustomStrategy(MissingValueStrategy):
    def handle_missing(self, df: pd.DataFrame, column: str) -> pd.DataFrame:
        """
        The public method to handle the missing values using custom imputation.
        args:
            df: pandas.DataFrame
            column: str
        returns:
            pandas.DataFrame
        """
        if self._too_many_nulls(df, column):
            return df.drop(columns=[column])
        else:
            return df.fillna({column: self._get_default_value()})

    def _too_many_nulls(self, df: pd.DataFrame, column: str) -> bool:
        """
        The private method to check if the column has too many nulls.

        args:
            df: pandas.DataFrame - dataframe to check for too many nulls
            column: str - column to check for too many nulls
        returns:
            bool - True if the column has too many nulls, False otherwise
        """
        return df[column].isnull().mean() > 0.6

    def _get_default_value(self) -> int:
        """
        The private method to get the default value.
        args:
            None
        returns:
            int - default value
        """
        return -1


# usage
if __name__ == "__main__":
    df = pd.read_csv("data/car_insurance.csv")

    # create a context using DropStrategy directly
    context = DropStrategy()

    # handle the missing values
    df_cleaned = context.handle_missing(df, "annual_mileage")

    # print the cleaned dataframe
    print(df_cleaned.columns)
