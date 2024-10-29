---
title: "LiveDoc - Code documentation and dependancy reporting features"
author: jeny-amatya-qed
categories: Public
classification: Official (Everyone)
tags: [ai,source-code]
date: 2024-10-29 02:06:52 
likes: 0
---

## Overview
The Developer Portal includes a tool called the **Dependency Scanning Tool**, which allows users to scan source repositories (currently only GitHub is supported) for any references to assemblies that may be deprecated or targeted for removal by a software team.

## Usage

1. **Setup**
   - Obtain an **API key** from the QED Developer Portal..
   - Configure Postman with the base URL for the [Dependency Scanning API](https://devportal-functions.azurewebsites.net/api/DependencyScanningFunction).

2. **Configure Input Parameters**
   - Users can define the configuration/parameters for scanning a repository in the **Admin > Dependency Scanning** section. Here, users can specify details like:
     - Name of the source repository
     - URL of the repository
     - Output report format
     - Name and version of deprecated packages to be scanned
   - These configurations are stored in CosmosDB and can be accessed using a unique repository key.

![Dependency Scanning Configuration](https://sadevportal3.blob.core.windows.net/root/dependency-scanner1.png)

3. **API Call**
   - Send a `GET` request to initiate the scan, including both the repository key and API key in the request headers.
![Dependency Scanning API call](https://sadevportal3.blob.core.windows.net/root/dependency-scanner2.png)

  ![Dependency Scanning API response](https://sadevportal3.blob.core.windows.net/root/dependency-scanner3.png)

4. **Scan Report**
   - The scan results are saved to Azure Blob Storage, with the [location ](https://dpstoragefunctions.blob.core.windows.net/source-scan-reports)specified in the response to the scan request.
