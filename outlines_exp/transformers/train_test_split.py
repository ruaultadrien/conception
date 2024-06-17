if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from sklearn.model_selection import train_test_split
@transformer
def transform(data, *args, **kwargs):
    
    train_df, test_df = train_test_split(data, test_size=kwargs["TEST_RATIO"], random_state=kwargs["SEED"])

    return train_df, test_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
