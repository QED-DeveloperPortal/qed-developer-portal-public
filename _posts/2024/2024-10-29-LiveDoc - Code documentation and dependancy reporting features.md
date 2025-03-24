---
title: "LiveDoc - Code documentation and dependancy reporting features"
slug: "livedoc-code-documentation-and-dependancy-reporting-features-75465c"
author: jeny-amatya-qed
categories: Public
classification: Public
tags: [opinion,ai,source-code]
date: 2024-10-29 02:06:52 
updatedBy: Joyclyn
updated: 2025-03-24 22:19:45 
likes: 0
---

*Note: Since this post was published, we have combined the dependency scanning tool with our LiveDoc service.*

## Overview
The Developer Portal includes a tool called the **dependency scanning tool**, which allows users to scan source repositories (currently only GitHub is supported) for any references to assemblies that may be deprecated or targeted for removal by a software team.

## Usage

1. **Setup**
   - Obtain an **API key** from the Developer Portal..
   - Configure Postman with the base URL for the [dependency scanning API](https://devportal-functions.azurewebsites.net/api/DependencyScanningFunction).

2. **Configure input parameters**
   - Admin users can define the configuration/parameters for scanning a repository in the **Admin > Dependency scanning** section. Here, we can specify details like:
     - Name of the source repository
     - URL of the repository
     - Output report format
     - Name and version of deprecated packages to be scanned
   - These configurations are stored in CosmosDB and can be accessed using a unique repository key. 
   - ![Dependency scanning configuration](https://sadevportal3.blob.core.windows.net/root/dependency-scanner1.png)

3. **API call**
    - Send a `GET` request to initiate the scan, including both the repository key and API key in the request headers.
    - ![Dependency scanning API call](https://sadevportal3.blob.core.windows.net/root/dependency-scanner2.png)
        
4. **Scan report** 
   - The scan results are saved to Azure blob storage, with the [location ](https://dpstoragefunctions.blob.core.windows.net/source-scan-reports) specified in the response to the scan response.
   -  ![Dependency scanning API response](https://sadevportal3.blob.core.windows.net/root/dependency-scanner3.png)