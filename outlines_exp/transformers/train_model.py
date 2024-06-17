if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import sklearn.neural_network

@transformer
def transform(data, *args, **kwargs):
    """
    Train the model
    """
    print(data[0])
    train_df = data[0]
    model = sklearn.neural_network.MLPClassifier(
        hidden_layer_sizes=kwargs['HIDDEN_LAYER_SIZES'], 
        max_iter=500)
    y = train_df["target"]
    X = train_df.drop(columns="target")
    model.fit(X, y)
    # Specify your transformation logic here

    return model


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
