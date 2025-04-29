---
title: "Auto importer"
slug: "auto-importer-ab802a"
author: andrew
categories: Public
classification: Public
tags: [architecture]
date: 2024-11-07 06:49:33 
updatedBy: Joyclyn
updated: 2025-04-29 00:42:23 
likes: 0
---

### Overview

The Developer Portal includes functionality to import PDF and Word documents from the department's internal Content Manager system.

This capability also includes the ability to summarise the imported documents via Azure Open AI.

Currently, documents that are to be imported are accessed via the Microsoft APIM capability exposed by the EIP/Integration team. 

### Security

Ocp-Apim-Subscription-Key is added as a Http Request Header key and is set with the value stored in the Azure Environment variable INTEGRATION_APIM_SUBSCRIPTION_KEY in the swa-developer-portal project.

The Authorisation token for accessing this is stored in the CONTENT_MANAGER_ACCESS_TOKEN Environment variable in the swa-developer-portal project and is added to the Http Request Header Authorization key.

### Architecture diagrams

Details of how the auto importer fits into the Developer Portal architecture to source documents from Content Manager can be found at [How the portals import generation and transformation services work](https://ambitious-pond-0f5283f00-dev.eastasia.3.azurestaticapps.net/public/How_the_portals_import_generation_and_transformation_services_work/). Note: You'll need staff credentials to access this link.