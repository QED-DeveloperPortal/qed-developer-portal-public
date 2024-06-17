---
title: "Another Data Hub environment setup summary "
author: "jeny-amatya-qed"
categories: [public]
tags: [auto-import, test,word]
date: 2024-06-17 14:58:02
likes: 0
imported: True 
import-source: "GitHub"
import-reference: "4444"
---

# Summary
 
The document outlines the process of creating a new Data Hub environment in Zone2. It details the prerequisites, steps involved in the new environment creation, the Environment Creation Utility, handling the Library Variable Groups, executing scripts to configure the Application Catalogue Database, and important considerations for the process.
 
## Key takeaways
 
- Prerequisites involve creating new Resource Groups and a Managed Identity, which require approval from the Manager - Integration.
- Execution of the environment creation utility involves manually updating Variable Groups, Release Variables for Function Apps and APIs, and executing the appropriate stages for Release Pipelines as per deployment dependency order.
- Library variable groups are instrumental in sharing settings between release definitions and for specific environments.
- Manually running scripts and considering various factors are crucial steps in configuring the Application Catalogue Database.
- The DSB APIM Sync Process and its usage of GUIDs for syncing, particularly GroupId and ApplicationGroupId, need modifications to ensure uniqueness for different environments.
- Executing scripts and maintenance tasks as described in the App Catalogue Deployment Guide is essential for the process to be completed accurately.