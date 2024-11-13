---
title: "AutoImporter"
author: andrew
categories: Public
classification: Public
tags: [opinion,architecture]
date: 2024-11-07 06:49:33 
updatedBy: andrew
updated: 2024-11-13 00:03:22 
likes: 0
---

**Overview**

DevPortal includes functionality to import PDF and Word documents from the department's internal Content Manager system.

This capability also includes the ability to summarise the imported documents via Azure Open AI.

Currently documents that are to be imported are accessed via the Microsoft APIM capability exposed by the EIP/Integration team. 

&nbsp;
**Security**

Ocp-Apim-Subscription-Key is added as a Http Request Header key and is set with the value stored in the Azure Environment variable INTEGRATION_APIM_SUBSCRIPTION_KEY in the swa-developer-portal project.

The Authorisation token for accessing this is stored in the CONTENT_MANAGER_ACCESS_TOKEN Environment variable in the swa-developer-portal project and is added to the Http Request Header Authorization key.

&nbsp;
**Architecture Diagrams**

Details of how the AutoImporter fits into the DevPortal architecture to source documents from Content Manager can be found at [How the portals import generation and transformation services work](https://ambitious-pond-0f5283f00-dev.eastasia.3.azurestaticapps.net/public/How_the_portals_import_generation_and_transformation_services_work/).