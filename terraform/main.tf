# main.tf

# Configure the Azure provider
provider "azurerm" {
  features {}
}

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
  sku                 = "Standard"
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
  sku_name            = "premium"
}

resource "azurerm_storage_account" "conception" {
  name                     = "conceptionstorageaccount"
  location                 = azurerm_resource_group.conception.location
  resource_group_name      = azurerm_resource_group.conception.name
  account_tier             = "Standard"
  account_replication_type = "GRS"
}

resource "azurerm_machine_learning_workspace" "conception" {
  name                    = "conception-workspace"
  location                = azurerm_resource_group.conception.location
  resource_group_name     = azurerm_resource_group.conception.name
  application_insights_id = azurerm_application_insights.conception.id
  key_vault_id            = azurerm_key_vault.conception.id
  storage_account_id      = azurerm_storage_account.conception.id

  identity {
    type = "SystemAssigned"
  }
}