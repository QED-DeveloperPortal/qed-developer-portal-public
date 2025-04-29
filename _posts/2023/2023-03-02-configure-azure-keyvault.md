---
title: "How to create and configure Azure KeyVault for a Static Web App"
slug: "how-to-create-and-configure-azure-keyvault-for-a-static-web-app-be7167"
author: matt
categories: Public
classification: Public
tags: [opinion,technology]
date: 2023-02-03 12:00:00 
updatedBy: Joyclyn
updated: 2025-04-29 04:57:32 
likes: 3
---

## Create the Azure KeyVault

First ensure all sensitive configuration data is identified and added to Azure KeyVault. This is an encrypted store which can be referenced from the Azure Static Web App (SWA) settings.

As well as creating the KeyVault, it will need to have access policies configured so values can be read from the SWA itself.

* Create the Keyvault (use a naming convention appropriate for the application, e.g. 'kv-dev-portal').
* Ensure Region is Australia Southeast, pricing tier is standard.
* Open the KeyVault properties in Azure.
* Under "Settings", click on "Access policies".
* Check "Azure Resource Manager for template deployment".
* Under permission model leave "Vault access policy" as default.

### Add an access policy for the SWA

* Browse to your SWA in the Azure Portal.
* From the left menu, click "Identity".
* Under system-assigned tab, toggle the status field on as shown below. This should show a GUID and button below. Then click the Save button to save the newly generated identity.
* Copy the newly created Object Id.
* Browse back to the Key Vault.
* Click "+ Add Access Policy".
* Search for the Object Id and select it.
* Select Key permissions "Get, List".
* Select Secret permissions "Get, List".
* Save changes.

### Adding secrets to KeyVault

Now you can add the following values to Azure KeyVault:

* On the left-hand menu, click on "Secrets".
* On the top menu, click "Generate/Import".
* Enter the name and value of the secret, click "Create".

Generated secrets/passwords using a Node.js command prompt:
Secrets:
```
node -e "console.log(require('crypto').randomBytes(256).toString('base64'));"
```
Passwords: 
```
node -e "console.log(require('crypto').randomBytes(64).toString('base64'));"
```