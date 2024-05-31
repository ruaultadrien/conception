# AzureML Service

## Run embedding computation

#### On AzureML
```bash
poetry install
poetry shell
source .env
python compute_embeddings_azml.py
```

#### Locally
```bash
poetry install
poetry shell
python src/compute_embeddings.py --output-folder data/compute_embeddings
```

### Deploy a compute cluster in Azure ML
az ml compute create --file compute.yml --resource-group $RESOURCE_GROUP --workspace-name $WORKSPACE_NAME