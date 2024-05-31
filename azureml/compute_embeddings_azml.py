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

    job_outputs = {
        "word_embeddings": Output(
            type=AssetTypes.URI_FOLDER, path="azureml://datastores/conceptiondatastore/paths/word_embeddings"
        )
    }

    # configure job
    job = command(
        code=".",
        command="poetry run python src/compute_embeddings.py --output-folder ${{outputs.word_embeddings}}",
        outputs=job_outputs,
        # environment=created_environment,
        environment=AZURE_ML_ENVIRONMENT_NAME,
        compute="conceptioncluster",
        display_name="Compute Word Embeddings",
        experiment_name="compute-word-embeddings",
    )

    # connect to workspace and submit job
    returned_job = ml_client.create_or_update(job)
    logging.info(f"Job ID: {returned_job.id}")
    logging.info("Successfully submitted job to Azure ML service.")


if __name__ == "__main__":
    main()
