<<<<<<< HEAD
---
title: "LiveDoc generation process"
slug: "product-canvas-guide-fc1ae4"
author: jeny-amatya-qed
categories: Public
classification: Public
tags: [opinion,getting-started]
date: 2025-02-06 06:10:58 
updatedBy: jeny-amatya-qed
updated: 2025-02-10 07:13:27 
likes: 0
---

=======
---
title: "LiveDoc generation process"
slug: "product-canvas-guide-fc1ae4"
author: jeny-amatya-qed
categories: Public
classification: Public
tags: [opinion,getting-started]
date: 2025-02-06 06:10:58 
updatedBy: jeny-amatya-qed
updated: 2025-02-10 07:13:27 
likes: 0
---

>>>>>>> master
# LiveDoc Generation workflow in Developer Portal application

## Overview

One of the crucial feature of the Developer Portal application is to automatically generate LiveDocs, which are dynamic summaries of GitHub repositories. The Developer Portal is built with a C# API backend, hosted as a static web app in Azure, and features a Jekyll-based frontend. The LiveDoc feature extracts relevant data from a given repository, including repository stats, contributor information, and product vision, to create a well-organized Markdown file.

### Key information extracted for LiveDoc:
- **Repository stats**: Primary languages used, file count, lines of code, last updated date.
- **Overview**: Based on the README.md file.
- **Top contributors**: A list of the main contributors to the repository.
- **Product vision statement**: Extracted if the `canvas/vision-canvas*.md` file/s exists in the repository.

## Workflow stages

### Stage 1: Product stakeholder defines vision statement

- The product stakeholder creates a vision statement outlining the product's goals, purpose, and strategic direction.
- This vision statement is saved as a markdown file (e.g., `canvas/vision.md`) and uploaded to their GitHub repository.

### Stage 2: Configuration submission

- The product stakeholder provides the following details to generate the LiveDoc:
  - GitHub repository URL
  - LiveDoc title
  - Author name
  - Token identifier (for accessing the repository)

- This configuration information is then submitted to the Developer Portal team.

### Stage 3: Configuration entry in Developer Portal

- The Developer Portal admin user receives the configuration details from the product stakeholder.
- The admin user creates a new configuration entry in the Developer Portal, using the provided details.
- This configuration is stored in Cosmos DB for future use during the LiveDoc generation process.
- The admin user also stores the token identifier in the Developer Portal key vault.

### Stage 4: LiveDoc generation process

- The Developer Portal admin user triggers the LiveDoc generation process for the specified repository.
- The application performs the following tasks:
  - Scans the repository using the provided token (fine-grained token) and retrieves key details such as:
    - Repository statistics (e.g., primary languages, file count, lines of code, last updated date).
    - Overview section from the `README.md` file.
    - A list of top contributors to the repository.
  - Checks for the presence of the `canvas/vision-canvas.md` file. If found, the product vision statement from the file is included in the LiveDoc.
  - The LiveDoc is generated as a markdown file, containing all the extracted details and formatted accordingly.
  - A pull request (PR) is created in the repository, with the generated LiveDoc awaiting approval.

### Stage 5: Approval & publishing

- The pull request is reviewed and approved before it can be merged and published on the Developer Portal site.
- Once the PR is approved, the Developer Portal admin user publishes the LiveDoc to the portal.
- The admin user then informs the product stakeholder that the LiveDoc has been generated and provides them with a link to the LiveDoc on the portal.

<img src="https://sadevportal3.blob.core.windows.net/root/LiveDoc_Generation.jpg" alt="LiveDoc generation process">

## Conclusion

This workflow describes the steps involved in generating a LiveDoc for a GitHub repository through the Developer Portal. The process ensures that the product vision, repository statistics, overview, and contributor information are all accurately captured and made available to stakeholders in a well-organized format.