import io
import pandas as pd
import requests
from sklearn import datasets
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test



@data_loader
def load_iris(*args, **kwargs):
    """
    Template for loading data from API
    """
    print("yooo")
    iris_data = datasets.load_iris()

    iris_df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    iris_df['target'] = iris_data.target

    print("Hello")
    return iris_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert "target" in output.columns
