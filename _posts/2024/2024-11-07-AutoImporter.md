---
title: "AutoImporter"
author: andrew
categories: Public
classification: Public
tags: [opinion,architecture]
date: 2024-11-07 06:49:33 
updatedBy: andrew
updated: 2024-11-11 22:49:32 
likes: 0
---

DevPortal includes functionality to import PDF and Word documents from the department's internal Content Manager system.

This capability also includes the ability to summarise the imported documents via Azure Open AI.

Currently documents that are to be imported are accessed via the Microsoft APIM capability exposed by the EIP/Integration team. The Authorisation token for accessing this is stored in the CONTENT_MANAGER_ACCESS_TOKEN Environment variable in the swa-developer-portal project.

Details of how the AutoImporter fits into the DevPortal architecture can be found at https://ambitious-pond-0f5283f00-dev.eastasia.3.azurestaticapps.net/public/How_the_portals_import_generation_and_transformation_services_work/.