import pandas as pd
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod


class DataPreprocessing(ABC):
    """
    The DataPreprocessing class defines the template method that contains a skeleton of some algorithm.
    The algorithm can be varied by overriding the abstract operations.
    """

    def run_pipeline(self, path: str):  # public method
        df = self._load_data(path)  # private
        df = self.handle_missing(df)  # public
        df = self.change_datatype(df, "outcome")  # public
        self._plot_basic_distributions(df, "credit_score")
        return df

    @abstractmethod
    def _load_data(self, path):
        """
        The abstract method to load the data.
        """
        pass

    @abstractmethod
    def handle_missing(self, df):
        """
        The abstract method to handle the missing values.
        """
        pass

    @abstractmethod
    def change_datatype(self, df, column):
        """
        The abstract method to encode the categoricals.
        """
        pass

    def _plot_basic_distributions(self, df, column):
        """
        The private method to plot the basic distributions.
        """
        print("Plotting histogram and boxplot (default logic)")


# concrete class
class ProcessData(DataPreprocessing):
    def _load_data(self, path: str) -> pd.DataFrame:
        """
        The concrete method to load the data.

        args:
            path: str
        returns:
            pandas.DataFrame
        """
        df = pd.read_csv(path)
        return df

    def handle_missing(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        The concrete method to handle the missing values.

        args:
            df: pandas.DataFrame
        returns:
            pandas.DataFrame
        """
        df = df.dropna()
        return df

    def change_datatype(self, df: pd.DataFrame, column: str) -> pd.DataFrame:
        """
        The concrete method to encode the categoricals.

        args:
            df: pandas.DataFrame
            column: str
        returns:
            pandas.DataFrame
        """
        df[column] = df[column].astype(str)
        return df

    def _plot_basic_distributions(self, df: pd.DataFrame, column: str) -> None:
        """
        The private method to plot the basic distributions.

        args:
            df: pandas.DataFrame
            column: str
        returns:
            None
        """
        df[column].hist()
        df[column].plot(kind="box")
        plt.show()


# usage
process_data = ProcessData()
df = process_data.run_pipeline(path="data/car_insurance.csv")
print(df.head())
