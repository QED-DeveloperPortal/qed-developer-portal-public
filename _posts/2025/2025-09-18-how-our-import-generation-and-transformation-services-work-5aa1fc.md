---
title: "How our import, generation and transformation services work"
slug: "how-our-import-generation-and-transformation-services-work-5aa1fc"
author: jeny-amatya-qed
owner: jeny-amatya-qed
categories: Public
classification: Public
tags: [auto-import, about]
date: 2025-09-18 00:57:06
likes: 0
imported: True 
import-source: "azure-devops"
import-reference: ""
import-config-id: "c6c31b6c-8b60-4e7f-90c4-e08c5d555ce1"
publishedOn: 2025-09-18 00:57:06
---

The Developer Portal's import, generation and transformation services leverage Azure functions, factories, and GitHub integrations. This system ensures efficient content reception, transformation, validation, and publication across multiple platforms.

### High-level overview
The diagram represents a system architecture involving various services, factories, and integrations. It includes components for content management, transformation, and generation, integrated with external platforms like GitHub, Azure, and a DevOps wiki.

### Key components and interactions

1. **Azure Function and Cosmos DB**
   - **ContentService**: An Azure Function named `ContentService` is configured to interact with Azure Cosmos DB for data storage and retrieval.

2. **Factories**
   - **ContentReceiverFactory**: Creates instances for receiving content.
   - **ContentTransformationFactory**: Creates instances for transforming content.
   - **ContentGenerationFactory**: Creates instances for generating content.

3. **Services**
   - **Content receiver services**:
     - **DevopsWikiReceiverService**: Receives content from a DevOps wiki.
     - **GithubReceiverService**: Receives content from a GitHub repository.
     - **ContentmanagerReceiverService**: Receives content from a Content Manager system.

   - **Content transformation services**:
     - **AISummaryTransformationService**: Transforms content by generating AI summaries.
     - **AIMarkdownTransformationService**: Transforms content into Markdown format using AI.

   - **Content generation services**:
     - **ContentGenerationService**: Generated markdown files that include the transformed content, to be published into Developer Portal.
     - **MarkdownService**: Specifically processes transformed content into markdown file.
     - **ValidationService**: Validates the content, ensuring it meets certain criteria.

4. **GitHub integration**
   - **HttpClientGithubService** and **OctokitGithubService**: These services interact with GitHub repository via GitHub API and Octokit API, to perform a number of operations.
   - **GitHub CI/CD pipelines**: Continuous Integration and Continuous Deployment pipelines validate the structure of Markdown content and the author information before publishing them to the portal website.
   - **GitHub repository**: The storage location for the content being processed and validated.

5. **External content**
   - **DevOps Wiki**: Source of content for the `DevopsWikiReceiverService`.
   - **Content Manager**: System managing the content received by the `ContentmanagerReceiverService`.

6. **Data flow**
   - The `ContentService` function retrieves configurations from Azure Cosmos DB.
   - Factories generate service instances for handling content reception, transformation, and generation.
   - The services interact with various sources like the DevOps wiki, GitHub repo, and content manager.
   - Transformed content goes through CI/CD pipelines for validation before being deployed to the portal website.

### Detailed flow
1. **ContentService** retrieves configurations from Azure Cosmos DB.
2. **ContentReceiverFactory** creates instances of services like `DevopsWikiReceiverService`, `GithubReceiverService`, and `ContentmanagerReceiverService` to receive content from different sources.
3. **ContentTransformationFactory** creates instances of services like `AISummaryTransformationService` and `AIMarkdownTransformationService` to transform the fetched content into Markdown format, using Azure OpenAI.
4. **ContentGenerationFactory** creates instances of services like `ContentGenerationService`, `MarkdownService`, and `ValidationService` to generate and validate the content.
5. Interaction with GitHub repository is done through **HttpClientGithubService** and **OctokitGithubService**.
6. **GitHub CI/CD Pipelines** validate the content structure and author information.
7. Validated content is deployed to the **Developer Portal website**.

![image.png](/.attachments/image-7db7c28f-65ad-4ed5-a5c7-9e76ae3e694c.png)

This system showcases a robust architecture that efficiently handles content from reception to publication. By integrating Azure functions, various service factories, and GitHub automation, the system ensures that content is processed, validated, and published seamlessly. This setup not only maintains content integrity but also optimises the workflow through automation and validation steps.

*This post was written in conjunction with ChatGPT.*