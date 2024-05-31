"""Main script for the Azure ML service."""

import logging
import os
import pathlib

from azure.ai.ml import MLClient, Output, command
from azure.ai.ml.constants import AssetTypes
from azure.ai.ml.entities import AmlCompute, BuildContext, Environment
from azure.identity import DefaultAzureCredential

from constants import AZURE_ML_ENVIRONMENT_NAME

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

    # Create azureml environment
    # created_environment = create_or_update_azureml_environment(ml_client)

    job_outputs = {
        "word_embeddings": Output(
            type=AssetTypes.URI_FOLDER, path="azureml://datastores/conceptiondatastore/paths/word_embeddings"
        )
    }

    # configure job
    job = command(
        code="./src",
        command="poetry run python compute_word_embeddings.py --output-folder ${{outputs.word_embeddings}}",
        outputs=job_outputs,
        # environment=created_environment,
        environment="conception-azureml-env:9",
        compute="conceptioncluster",
        display_name="Compute Word Embeddings",
        experiment_name="compute-word-embeddings",
    )

    # connect to workspace and submit job
    returned_job = ml_client.create_or_update(job)
    logging.info(f"Job ID: {returned_job.id}")
    logging.info("Successfully submitted job to Azure ML service.")


def create_or_update_azureml_environment(ml_client: MLClient) -> Environment:
    """Create or update the AzureML environment by building the local Docker image."""
    environment = Environment(
        build=BuildContext(path=pathlib.Path(__file__).parent),
        name=AZURE_ML_ENVIRONMENT_NAME,
        description="AzureML Environment created for the Conception project",
    )
    created_environment = ml_client.environments.create_or_update(environment)
    return created_environment


if __name__ == "__main__":
    main()
