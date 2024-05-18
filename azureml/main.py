"""Main script for the Azure ML service."""

import logging
import os

from azure.ai.ml import MLClient, command
from azure.identity import DefaultAzureCredential

# Set up logging
logging.basicConfig(level=logging.INFO)


def main():
    """Main function for the Azure ML service."""
    ml_client = MLClient(
        DefaultAzureCredential(),
        os.environ["SUBSCRIPTION_ID"],
        os.environ["RESOURCE_GROUP"],
        os.environ["WORKSPACE_NAME"],
    )
    # configure job
    job = command(
        code="./src",
        command="python train.py",
        environment="AzureML-sklearn-0.24-ubuntu18.04-py37-cpu@latest",
        compute="conception-cluster",
        experiment_name="train-model",
    )

    # connect to workspace and submit job
    returned_job = ml_client.create_or_update(job)
    logging.info(f"Job ID: {returned_job.id}")
    logging.info("Successfully submitted job to Azure ML service.")


if __name__ == "__main__":
    main()
