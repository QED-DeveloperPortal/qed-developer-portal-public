---
title: "The LiveDoc report generation process"
slug: "product-canvas-guide-fc1ae4"
author: jeny-amatya-qed
categories: Public
classification: Public
tags: [opinion,getting-started]
date: 2025-02-06 06:10:58 
updatedBy: Joyclyn
updated: 2025-03-20 05:40:17 
likes: 0
---

# LiveDoc report generation process

## Overview

The LiveDoc feature of the Developer Portal allows you to have a dynamically generated report that summarises your GitHub code repository (DevOps service coming soon!). 

We built the LiveDoc service with a C# API backend, hosted as a static web app in Azure, and featuring a Jekyll-based frontend. The LiveDoc feature extracts relevant data from a given repository, including repository stats, contributor information, and product vision, to create a well-organised Markdown file.

### Key information extracted for LiveDoc:
- **Repository stats**: Primary languages used, file count, lines of code, last updated date.
- **Overview**: Based on the README.md file.
- **Top contributors**: A list of the main contributors to the repository.
- **Product vision statement**: Extracted if the `canvas/vision-canvas*.md` file/s exists in the repository.

## Workflow stages

### Stage 1: Product stakeholder defines vision statement

- The product stakeholder creates a vision statement outlining the product's goals, purpose, and strategic direction.
- They save this statement as a Markdown file (e.g., `canvas/vision.md`) and upload the file to their GitHub code repository.

### Stage 2: Configuration submission

- The product stakeholder provides the following details to generate the LiveDoc:
  - GitHub repository URL
  - LiveDoc title
  - Author name
  - Token identifier (for accessing the repository)

- Then they provide this configuration information to us to process.

### Stage 3: Configuration entry in Developer Portal

- An admin user from our team receives the configuration details from the product stakeholder and creates a new configuration entry, using the provided details.
- This configuration is stored in Cosmos DB for future use during the LiveDoc report generation process.
- We also store the token identifier in the Developer Portal key vault.

### Stage 4: LiveDoc report generation process

- The admin user triggers the LiveDoc report generation process for the specified repository.
- The application performs the following tasks:
  - Scans the repository using the provided token (fine-grained token) and retrieves key details such as:
    - Repository statistics (e.g., primary languages, file count, lines of code, last updated date).
    - Overview section from the `README.md` file.
    - A list of top contributors to the repository.
  - Checks for the presence of the `canvas/vision-canvas.md` file. If found, the product vision statement from the file is included in the LiveDoc report.
  - The LiveDoc report is generated as a Markdown file, containing all the extracted details and formatted accordingly.
  - A pull request (PR) is created in the repository for the generated LiveDoc report which is awaiting approval.

### Stage 5: Approval and publishing

- The PR is reviewed and approved in GitHub before being merged and published on the Developer Portal site.
- Once the PR is approved, the Developer Portal admin user publishes the LiveDoc report to the portal.
- The admin user then informs the product stakeholder that the LiveDoc report has been generated and provides them with a link to the report.

<img src="https://sadevportal3.blob.core.windows.net/root/LiveDoc_Generation.jpg" alt="LiveDoc generation process">

## Conclusion

This workflow describes the steps involved in generating a LiveDoc report for a GitHub repository through the Developer Portal. The process ensures that the product vision, repository statistics, overview, and contributor information are all accurately captured and made available to stakeholders in a well-organised format.