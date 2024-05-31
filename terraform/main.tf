# main.tf


#################################
# Configure the Azure providers #
#################################

terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "azurerm" {
  features {}
}

provider "azuread" {
  tenant_id = var.tenant_id
}


provider "github" {
  token = var.github_token
  owner = var.github_owner
}


####################
# Azure Resources ##
####################

data "azurerm_client_config" "current" {}

# Create a resource group
resource "azurerm_resource_group" "conception" {
  name     = "conception"
  location = "West Europe"
}

# Create an Azure Container Registry
resource "azurerm_container_registry" "conception" {
  name                = "conceptionacr"
  resource_group_name = azurerm_resource_group.conception.name
  location            = azurerm_resource_group.conception.location
  sku                 = "Basic"
  admin_enabled       = true
}

resource "azurerm_application_insights" "conception" {
  name                = "conception-insights"
  location            = azurerm_resource_group.conception.location
  resource_group_name = azurerm_resource_group.conception.name
  application_type    = "web"
}

resource "azurerm_key_vault" "conception" {
  name                = "conceptionkeyvault"
  location            = azurerm_resource_group.conception.location
  resource_group_name = azurerm_resource_group.conception.name
  tenant_id           = data.azurerm_client_config.current.tenant_id
  sku_name            = "standard"
}

resource "azurerm_storage_account" "conception" {
  name                     = "conceptionstorageaccount"
  location                 = azurerm_resource_group.conception.location
  resource_group_name      = azurerm_resource_group.conception.name
  account_tier             = "Standard"
  account_replication_type = "GRS"
}

resource "azurerm_machine_learning_workspace" "conception" {
  name                    = "conceptionworkspace"
  location                = azurerm_resource_group.conception.location
  resource_group_name     = azurerm_resource_group.conception.name
  application_insights_id = azurerm_application_insights.conception.id
  key_vault_id            = azurerm_key_vault.conception.id
  storage_account_id      = azurerm_storage_account.conception.id
  container_registry_id   = azurerm_container_registry.conception.id
  public_network_access_enabled = true

  identity {
    type = "SystemAssigned"
  }
}

resource "azurerm_machine_learning_compute_cluster" "conception" {
  name                   = "conceptioncluster"
  machine_learning_workspace_id = azurerm_machine_learning_workspace.conception.id
  location               = azurerm_resource_group.conception.location
  vm_priority = "Dedicated"
  vm_size = "Standard_DS2_v2"
  scale_settings {
    min_node_count                       = 0
    max_node_count                       = 1
    scale_down_nodes_after_idle_duration = "PT30S" # 30 seconds
  }
  identity {
    type = "SystemAssigned"
  }
}

resource "azurerm_storage_container" "conception" {
  name                  = "conception-storage-container"
  storage_account_name  = azurerm_storage_account.conception.name
  container_access_type = "private"
}

resource "azurerm_machine_learning_datastore_datalake_gen2" "conception" {
  name                 = "conceptiondatastore"
  workspace_id         = azurerm_machine_learning_workspace.conception.id
  storage_container_id = azurerm_storage_container.conception.resource_manager_id
}

resource "azurerm_role_assignment" "cluster_to_access_storage" {
  principal_id   = azurerm_machine_learning_compute_cluster.conception.identity[0].principal_id
  role_definition_name = "Storage Blob Data Contributor"
  scope          = azurerm_storage_account.conception.id  
}
#################################
# Azure AD ######################
#################################

data "azuread_client_config" "current" {}


resource "azuread_application_registration" "github_actions_app" {
  display_name = "github-actions-conception"
}

resource "azuread_service_principal" "github_actions_sp" {
  client_id = azuread_application_registration.github_actions_app.client_id
  app_role_assignment_required = false
  owners = [data.azuread_client_config.current.object_id]
}

resource "azurerm_role_assignment" "github_actions_sp_contributor" {
  principal_id   = azuread_service_principal.github_actions_sp.object_id
  role_definition_name = "Contributor"
  scope          = azurerm_resource_group.conception.id
}



resource "azuread_application_federated_identity_credential" "openid_connect_github_main" {
  display_name = "github-main-branch"
  audiences = ["api://AzureADTokenExchange"]
  issuer = "https://token.actions.githubusercontent.com"
  application_id = azuread_application_registration.github_actions_app.id
  subject = "repo:ruaultadrien/conception:ref:refs/heads/main"
}

resource "azuread_application_federated_identity_credential" "openid_connect_github_pull_request" {
  display_name = "github-pull-request"
  audiences = ["api://AzureADTokenExchange"]
  issuer = "https://token.actions.githubusercontent.com"
  application_id = azuread_application_registration.github_actions_app.id
  subject = "repo:ruaultadrien/conception:pull_request"
}
#################################
# GitHub Actions ################
#################################


resource "github_actions_secret" "acr_login_server" {
  repository      = var.github_repository
  secret_name     = "REGISTRY_SERVER" # pragma: allowlist secret
  plaintext_value = azurerm_container_registry.conception.login_server
}

resource "github_actions_secret" "acr_username" {
  repository      = var.github_repository
  secret_name     = "SP_USERNAME" # pragma: allowlist secret
  plaintext_value = azuread_service_principal.github_actions_sp.client_id
}

resource "github_actions_secret" "client_id" {
  repository      = var.github_repository
  secret_name     = "CLIENT_ID" # pragma: allowlist secret
  plaintext_value = azuread_service_principal.github_actions_sp.client_id
}

resource "github_actions_secret" "tenant_id" {
  repository      = var.github_repository
  secret_name     = "TENANT_ID" # pragma: allowlist secret
  plaintext_value = var.tenant_id
}

resource "github_actions_secret" "subscription_id" {
  repository      = var.github_repository
  secret_name     = "SUBSCRIPTION_ID" # pragma: allowlist secret
  plaintext_value = data.azurerm_client_config.current.subscription_id
}

resource "github_actions_secret" "resource_group" {
  repository      = var.github_repository
  secret_name     = "RESOURCE_GROUP" # pragma: allowlist secret
  plaintext_value = azurerm_resource_group.conception.name
}

resource "github_actions_secret" "workspace_name" {
  repository      = var.github_repository
  secret_name     = "WORKSPACE_NAME" # pragma: allowlist secret
  plaintext_value = azurerm_machine_learning_workspace.conception.name
}
