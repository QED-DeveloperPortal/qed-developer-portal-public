---
title: "Another Summarized guide for Data Hub environment setup "
author: "jeny-amatya-qed"
categories: [public]
tags: [auto-import, test,word]
date: 2024-06-18 00:22:39
likes: 0
imported: True 
import-source: "GitHub"
import-reference: "1222"
---

# Overview
 
This document outlines the process for creating a new Data Hub environment in 'Zone2' from the Azure DevOps perspective. Key components include creating resource groups, managing user identities, environment creation utility, library variable groups, and important considerations for script execution and database configuration.
 
## Key takeaways
 
- Resource Groups:

    - All Resource Groups need to be created by the ITB-ACE team before running the Release. Access permissions are granted by ACE to the Data Hub Service Principal and Integration team's Azure AD group.
- Managed Identity Account:

    - Azure Functions utilize a single Managed User Identity, and specific access and configurations are required before and after creation via ServiceNow UR and scripting.
- Environment Creation:

    - The high-level steps encompass executing the environment creation utility, manual variable updates, stage executions, and database sync configurations with further specifics outlined.
- Library Variable Groups:

    - These are collections of settings shared between release definitions and are partitioned by functional areas and specific environments.
- Manually Updates Post-Deployment:

    - Post-deployment, manual steps need to be undertaken for configuring the Application Catalogue Database, including creation of database users and running specific scripts.
- Important Considerations:

    - Criteria relating to considerations prior to executing database configuration scripts, specifically emphasizing the unique naming conventions and environment-aware configurations for APIM synchronization.

*Notable Highlights*:

- Utilization of a dedicated Environment Creation Utility
- The manual steps required for database user creation and script executions for configuring the Application Catalogue Database
- Key considerations related to the unique naming conventions and environment-aware configurations for APIM synchronization within Zone2's environment.