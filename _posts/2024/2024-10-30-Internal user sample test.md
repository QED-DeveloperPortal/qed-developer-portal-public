---
title: "Internal user sample test"
author: divya-gh
categories: Public
classification: Public
tags: [opinion,tutorials,accessibility,agile]
date: 2024-10-30 04:44:11 
likes: 0
---

# The Developer Portal includes a tool called the Dependency Scanning Tool, which allows users to scan source repositories (currently only GitHub is supported) for any references to assemblies that may be deprecated or targeted for removal by a software team.

Usage
Setup

*Obtain an API key from the QED Developer Portal..*

<span style="color: #7cafc2">Configure Postman with the base URL for the Dependency Scanning API.</span>

~~Configure Input Parameters~~


***


> Name of the source repository

* URL of the repository

1. Output report format

* [ ] Name and version of deprecated packages to be scanned

These configurations are stored in CosmosDB and can be accessed using a unique repository [key](https://ambitious-pond-0f5283f00-test.eastasia.3.azurestaticapps.net/).

Dependency Scanning Configuration

`API Call`

```
Send a GET request to initiate the scan, including both the repository key and API key in the request headers.
```

Dependency Scanning API call

Scan Report

The scan results are saved to Azure Blob Storage, with the location specified in the response to the scan response.

Dependency Scanning API response