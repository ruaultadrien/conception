"""Training script for a simple random forest classifier on the Iris dataset."""

import logging

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Set up logging
logging.basicConfig(level=logging.INFO)


def main():
    """Main function for the training script."""
    # Load standard dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Evaluate model
    accuracy = model.score(X_test, y_test)
    logging.info(f"Model accuracy: {accuracy}")


if __name__ == "__main__":
    main()
