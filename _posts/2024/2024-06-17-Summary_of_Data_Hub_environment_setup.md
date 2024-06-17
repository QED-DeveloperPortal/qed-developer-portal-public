---
title: "Another Summary of Data Hub environment setup "
author: "jeny-amatya-qed"
categories: [public]
tags: [auto-import, test,word]
date: 2024-06-17 04:36:02
likes: 0
imported: True 
import-source: "GitHub"
import-reference: "4444"
---

# Overview
    The document provides a detailed guide for creating a new Data Hub environment in Zone2, covering the pre-requisites, environment creation steps, utility functions, variable groups, and script executions for setting up the new environment, with a focus on Azure DevOps and Azure components.
    
    ## Key takeaways
    - The pre-requisites for creating a new Data Hub environment in Zone2 involve setting up Resource Groups and a Managed Identity, followed by manual updates and executions. Permissions occur via ServiceNow Universal Request and must be approved by a manager.
    - The Environment Creation Utility assists in replicating and updating various release stages, and the creation of Library Variable Groups for sharing settings among different release definitions.
    - After deployment completion, configuration scripts for the Application Catalogue Database are executed, and specific considerations are highlighted when dealing with the DSB APIM Sync Process, including the need to update scripts for unique identifiers and naming conventions.
    - Various manual scripts are executed to configure the Application Catalogue Database, focusing on creating database users, and updating scripts for unique identifiers and naming conventions.
    
    # Additional Points of Interest
    - Requested Resource Groups should be created before running the release.
    - Managed Identity accounts for Azure Functions are created using a ServiceNow UR, followed by the assignment of Azure Role API Management Service Contributor access and configuring Azure AD ClientId in FuncAppSettings.
    - Environment Creation involves various stages, including manual updates of Variable and Release Variables for Function Apps and APIs, followed by utility-driven executions and configurations.
    - Library Variable Groups house settings partitioned by functional areas and specific environments, such as Zone2Dev, Zone2Test, and Zone2UAT.
    - Manual updates are required for the New Library Variable Groups in the Azure DevOps UI, focusing mainly on monitoring and database variables.
    - Considerations for working with a single APIM instance supporting multiple Data Hub environments, including naming conventions and unique GUID usage, are important.
    - Specific code and script updates are highlighted for GroupId and ApplicationGroupId in the DSB APIM Sync Process for maintaining uniqueness and environment awareness.
    - Multiple scripts are executed to configure the Application Catalogue Database, varying from creating database users to implementing updates catering to unique environment requirements.
