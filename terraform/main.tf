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

#################################
# Azure AD ######################
#################################

data "azuread_client_config" "current" {}

resource "azuread_application" "github_actions" {
  display_name = "github-actions"
  owners       = [data.azuread_client_config.current.object_id]
}

resource "azuread_service_principal" "github_actions_sp" {
  client_id = azuread_application.github_actions.client_id
  app_role_assignment_required = false
  owners = [data.azuread_client_config.current.object_id]
}

resource "azuread_service_principal_password" "github_actions_sp_password" {
  service_principal_id = azuread_service_principal.github_actions_sp.object_id
  end_date             = "2024-12-31T12:00:00Z"
}

resource "azurerm_role_assignment" "github_actions_sp_contributor" {
  principal_id   = azuread_service_principal.github_actions_sp.object_id
  role_definition_name = "Contributor"
  scope          = azurerm_resource_group.conception.id
}


#################################
# GitHub Actions ################
#################################


resource "github_actions_secret" "acr_login_server" {
  repository      = var.github_repository
  secret_name     = "REGISTRY_SERVER"
  plaintext_value = azurerm_container_registry.conception.login_server
}

resource "github_actions_secret" "acr_username" {
  repository      = var.github_repository
  secret_name     = "REGISTRY_USERNAME"
  plaintext_value = azuread_service_principal.github_actions_sp.client_id
}

resource "github_actions_secret" "acr_password" {
  repository      = var.github_repository
  secret_name     = "REGISTRY_PASSWORD"
  plaintext_value = azuread_service_principal_password.github_actions_sp_password.value
}


#################################
# Output variables ##############
#################################

output "service_principal_password" {
  value = azuread_service_principal_password.github_actions_sp_password.value
  sensitive = true
}