---
title: "Dependency scan result - Developer Portal"
author: jeny-amatya-qed
categories: [Public]
classification: Sensitive (Government staff)
date: 2024-10-29 00:29:26 
likes: 0
---

# Repository Scanning results
## Configuration
Repository name: qed-developer-portal
Repository url: https://github.com/QED-DeveloperPortal/qed-developer-portal
Source folder ignore list: node_modules, bin, obj
Source file extension white list: .cs
Deprecated packages:
- Microsoft.Azure.Cosmos (3.40.0)
## Results
Scan start: 00:11:08 UTC
Scan completed: 00:14:00 UTC
Total scan time: 00:02:52.5570672
Files scanned: 87
Files affected: 7
### Packages
**Microsoft.Azure.Cosmos**
api/api.csproj
*Deprecated package reference detected in package/project file.*
### Source
**Microsoft.Azure.Cosmos**
api/AzureAIFunction.cs
*Import/using statement detected in source file.*
api/Repositories/Base/Interfaces/IRepositoryBase.cs
*Import/using statement detected in source file.*
api/Repositories/Base/RepositoryBase.cs
*Import/using statement detected in source file.*
api/Repositories/ContentServiceConfigurationRepository.cs
*Import/using statement detected in source file.*
api/Services/GitHubPackageScanningService.cs
*Import/using statement detected in source file.*
api/Utilities.cs
*Import/using statement detected in source file.*

