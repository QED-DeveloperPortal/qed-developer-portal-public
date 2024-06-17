---
title: "Another Data Hub environment setup summarized "
author: "jeny-amatya-qed"
categories: [public]
tags: [auto-import, test,word]
date: 2024-06-17 16:06:41
likes: 0
imported: True 
import-source: "GitHub"
import-reference: "1452"
---

# Summary
 
The document outlines the process for creating a new data hub environment in Zone2, with a focus on pre-requisites, managed identity accounts, environment creation, library variable groups, and important considerations. It provides details on creating resource groups, managed user identity, and executing environment creation utilities. In addition, it highlights the requirement to manually update variable groups and release variables, and run scripts to configure the application catalogue database. Important considerations around database configuration and syncing with APIM in Zone2 are also detailed.
 
# Key takeaways
 
- **Resource Groups:**

    - All Resource Groups need to be created by ITB - ACE team before the release.
    - Permissions need to be granted to the Resource Group to the Data Hub Service Principal and the Integration teams Azure AD group.
    - Request for creation of resource groups is performed via a ServiceNow Universal Request and requires manager approval.
- **Managed Identity Account:**

    - All Azure Functions are run using the same Managed User Identity with specific access requirements.
    - Creation and configuration of Managed User Identity is initiated via a ServiceNow UR request.
- **New Environment Creation:**

    - Involves executing environment creation utility, manually updating variable groups and release variables, and configuring the App Catalog Database.
- **Library Variable Groups:**

    - Collection of settings shared between release definitions, partitioned by functional areas and specific environments.
- **Important Considerations:**

    - Unique naming and GUID considerations for sync process between the App Catalog Database and APIM artifacts, involving updates to SQL scripts.
- **Database Configuration:**

    - Need to run scripts to configure the Application Catalogue Database, involving creating database users and ensuring unique identifiers for syncing with APIM.

The guide presents a comprehensive and detailed process for setting up a new data hub environment in Zone2, outlining specific steps and considerations for accurate deployment and configuration.