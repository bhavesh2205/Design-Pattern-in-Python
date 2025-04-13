from abc import ABC, abstractmethod
import pandas as pd


class ExploratoryDataAnalysis(ABC):
    """
    The Template class defines a template method that contains a skeleton of some algorithm.
    The algorithm can be varied by overriding the abstract operations.
    """

    def run_pipeline(self, path: str):
        """
        The template method defines the skeleton of an algorithm.
        """
        df = self.load_data(path)
        df = self.handle_missing(df)
        df = self.encode_categoricals(df)
        self.plot(df)
        return df  # Return the processed DataFrame

    @abstractmethod
    def load_data(self):
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
    def encode_categoricals(self, df):
        """
        The abstract method to encode the categorical variables.
        """
        pass

    def plot(self, df):
        """
        The method to plot the data.
        """
        print("Plotting basic distributions")


# A concrete implementation
class ProcessData(ExploratoryDataAnalysis):
    """
    The Concrete class implements the abstract operations.
    """

    def load_data(self, path: str) -> pd.DataFrame:
        """
        The concrete method to load the data.
        """
        df = pd.read_csv(path)
        return df

    def handle_missing(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        The concrete method to handle the missing values.
        """
        df["annual_mileage"] = df["annual_mileage"].fillna(df["annual_mileage"].mean())

        return df

    def encode_categoricals(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        The concrete method to encode the categorical variables.
        """
        df["vehicle_type"] = df["vehicle_type"].map({"sedan": 0, "sports car": 1})
        df["vehicle_year"] = df["vehicle_year"].map({"before 2015": 0, "after 2015": 1})
        return df


# Use it
pipeline = ProcessData()
df_cleaned = pipeline.run_pipeline(path="data/car_insurance.csv")
print(df_cleaned[["vehicle_type", "vehicle_year", "annual_mileage"]].head())
