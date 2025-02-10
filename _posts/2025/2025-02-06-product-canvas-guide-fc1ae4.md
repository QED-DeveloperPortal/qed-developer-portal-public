---
title: "Product canvas guide"
slug: "product-canvas-guide-fc1ae4"
author: jeny-amatya-qed
categories: Public
classification: Public
tags: [opinion,getting-started]
date: 2025-02-06 06:10:58 
updatedBy: jeny-amatya-qed
updated: 2025-02-10 04:49:21 
likes: 0
---

# LiveDoc Generation Process Workflow in Developer Portal Application

## Overview

The Developer Portal Application is designed to automatically generate LiveDocs, which are dynamic summaries of GitHub repositories. The portal is built with a C# API backend, hosted as a static web app in Azure, and features a Jekyll-based frontend. The LiveDoc feature extracts relevant data from a given repository, including repository stats, contributor information, and product vision, to create a well-organized Markdown file.

### Key Information Extracted for LiveDoc:
- **Repository stats**: Primary languages used, file count, lines of code, last updated date.
- **Overview**: Based on the README.md file.
- **Top contributors**: A list of the main contributors to the repository.
- **Product vision statement**: Extracted if the `canvas/vision.md` file exists in the repository.

## Workflow Stages

### Stage 1: Product Stakeholder Defines Vision Statement

- The Product Stakeholder creates a vision statement outlining the product's goals, purpose, and strategic direction.
- This vision statement is saved as a Markdown file (e.g., `canvas/vision.md`) and uploaded to their GitHub repository.

### Stage 2: Configuration Submission

- The Product Stakeholder provides the following details to generate the LiveDoc:
  - GitHub repository URL
  - LiveDoc title
  - Author name
  - Token identifier (for accessing the repository)

- This configuration information is then submitted to the Dev Portal Admin.

### Stage 3: Configuration Entry in Developer Portal

- The Dev Portal Admin receives the configuration details from the product stakeholder.
- The Admin creates a new configuration entry in the Developer Portal, using the provided details.
- This configuration is stored in Cosmos DB for future use during the LiveDoc generation process.

### Stage 4: LiveDoc Generation Process

- The Dev Portal Admin triggers the LiveDoc generation process for the specified repository.
- The application performs the following tasks:
  - Scans the repository using the provided token and retrieves key details such as:
    - Repository statistics (e.g., primary languages, file count, lines of code, last updated date).
    - Overview section from the `README.md` file.
    - A list of top contributors to the repository.
  - Checks for the presence of the `canvas/vision.md` file. If found, the product vision statement from the file is included in the LiveDoc.
  - The LiveDoc is generated as a Markdown file, containing all the extracted details and formatted accordingly.
  - A Pull Request (PR) is created in the repository, with the generated LiveDoc awaiting approval.

### Stage 5: Approval & Publishing

- The Pull Request is reviewed and approved before it can be merged and published on the Developer Portal site.
- Once the PR is approved, the Dev Portal Admin publishes the LiveDoc to the portal.
- The Dev Portal Admin then informs the Product Stakeholder that the LiveDoc has been generated and provides them with a link to the LiveDoc on the portal.

## Conclusion

This workflow describes the steps involved in generating a LiveDoc for a GitHub repository through the Developer Portal Application. The process ensures that the product vision, repository statistics, overview, and contributor information are all accurately captured and made available to stakeholders in a well-organized format.
