---
title: "How the portals import generation and transformation services work"
author: Joyclyn
categories: [public]
classification: Unofficial (Everyone)
tags: [auto-import]
date: 2024-08-27 04:20:03
likes: 0
imported: True 
import-source: "Azure Devops"
import-reference: ""
---

The portal's import, generation and transformation services leverage Azure functions, factories, and GitHub integrations. This system ensures efficient content reception, transformation, validation, and publication across multiple platforms.
 
### High-Level Overview
 
The diagram represents a system architecture involving various services, factories, and integrations. It includes components for content management, transformation, and generation, integrated with external platforms like GitHub, Azure, and a DevOps wiki.
 
### Key Components and Interactions
 
1. **Azure Function and Cosmos DB**

    - **ContentService**: An Azure Function named `ContentService` is configured to interact with Azure Cosmos DB for data storage and retrieval.
2. **Factories**

    - **ContentReceiverFactory**: Creates instances for receiving content.
    - **ContentTransformationFactory**: Creates instances for transforming content.
    - **ContentGenerationFactory**: Creates instances for generating content.
3. **Services**

    - **Content Receiver Services**:

        - **DevopsWikiReceiverService**: Receives content from a DevOps wiki.
        - **GithubReceiverService**: Receives content from a GitHub repository.
        - **ContentmanagerReceiverService**: Receives content from a Content Manager system.
    - **Content Transformation Services**:

        - **AISummaryTransformationService**: Transforms content by generating AI summaries.
        - **AIMarkdownTransformationService**: Transforms content into Markdown format using AI.
    - **Content Generation Services**:

        - **ContentGenerationService**: Generated markdown files that includes the transformed content, to be published into Developer Portal
        - **MarkdownService**: Specifically processes transformed content into markdown file.
        - **ValidationService**: Validates the content, ensuring it meets certain criteria.
4. **GitHub Integration**

    - **HttpClientGithubService** and **OctokitGithubService**: These services interact with GitHub repository via GitHub API and Octokit API, to perform a number of operations.
    - **GitHub CI/CD Pipelines**: Continuous Integration and Continuous Deployment pipelines validate the structure of Markdown content and the author information before publishing them to the portal website.
    - **GitHub Repository**: The storage location for the content being processed and validated.
5. **External Content**

    - **DevOps Wiki**: Source of content for the `DevopsWikiReceiverService`.
    - **Content Manager**: System managing the content received by the `ContentmanagerReceiverService`.
6. **Data Flow**

    - The `ContentService` function retrieves configurations from Azure Cosmos DB.
    - Factories generate service instances for handling content reception, transformation, and generation.
    - The services interact with various sources like the DevOps wiki, GitHub repo, and content manager.
    - Transformed content goes through CI/CD pipelines for validation before being deployed to the portal website.

### Detailed Flow

1. **ContentService** retrieves configurations from Azure Cosmos DB.
2. **ContentReceiverFactory** creates instances of services like `DevopsWikiReceiverService`, `GithubReceiverService`, and `ContentmanagerReceiverService` to receive content from different sources.
3. **ContentTransformationFactory** creates instances of services like `AISummaryTransformationService` and `AIMarkdownTransformationService` to transform the fetched content into Markdown format, using Azure OpenAI.
4. **ContentGenerationFactory** creates instances of services like `ContentGenerationService`, `MarkdownService`, and `ValidationService` to generate and validate the content.
5. Interaction with GitHub repository is done through **HttpClientGithubService** and **OctokitGithubService**.
6. **GitHub CI/CD Pipelines** validate the content structure and author information.
7. Validated content is deployed to the **Developer Portal website**.

![image.png](https://sadevportal3.blob.core.windows.net/root/post/import.png)
 
This system showcases a robust architecture that efficiently handles content from reception to publication. By integrating Azure functions, various service factories, and GitHub automation, the system ensures that content is processed, validated, and published seamlessly. This setup not only maintains content integrity but also optimises the workflow through automation and validation steps.
 
*This post was written in conjunction with ChatGPT.*