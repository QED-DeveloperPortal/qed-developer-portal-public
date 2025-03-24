---
title: "How LiveDoc can help you"
slug: "how-livedoc-can-help-you-1365ba"
author: matt
categories: Public
classification: Public
tags: [opinion,ai]
date: 2024-10-22 05:00:10 
updatedBy: Joyclyn
updated: 2025-03-24 00:35:35 
likes: 1
---

# What LiveDoc does and how it can help you

**LiveDoc** is a cloud-hosted tool designed to enhance software documentation through AI-driven analysis of public or private cloud-hosted code repositories. By scanning repositories, LiveDoc generates an AI-assisted summary of the source code, including:

- **Purpose of the software:** A concise overview explaining what the software does.
- **Breakdown of key components:** Detailed analysis of major modules, functions, and patterns in the codebase.
- **Overall summation:** An aggregated view of the codebase structure, with insights into architectural choices.

The generated documentation is saved in a **Markdown format** and securely stored as a technical article on the **Developer Portal**.

LiveDoc can be scheduled to run at regular intervals, ensuring that the documentation stays current. Any changes, whether from updates in coding patterns or new module additions, are automatically captured, providing a constantly refreshed summary of the evolving codebase.

## How LiveDoc works: An overview of Azure Durable Functions

The underlying architecture of LiveDoc leverages **Azure Durable Functions**, a serverless extension that enables orchestration of stateful workflows in Azure Functions. This makes LiveDoc reliable, scalable, and resilient. Here's a high-level breakdown of how it works:

- **Orchestrator function:** This serves as the central controller, managing the sequence of tasks, error handling, and retries. It directs the flow of data as the code repository is analysed.
- **Activity functions:** Each task in LiveDoc—such as fetching repository content, analysing the code, and generating Markdown—runs as a discrete, stateless activity function.
- **Durability and resilience:** If the process is interrupted, the orchestrator ensures that execution continues from where it left off, allowing LiveDoc to handle large codebases or unexpected failures seamlessly.
- **Timer triggers:** LiveDoc uses timers to schedule scans at regular intervals, maintaining up-to-date documentation without manual intervention.

## Key features of LiveDoc

1. **Automated code analysis:** Quickly generates a comprehensive summary of a code repository.
2. **Markdown export:** Outputs documentation in Markdown format, making it easy to share, edit, and store.
3. **Scheduled updates:** Runs on a predefined schedule to keep documentation current.
4. **Resilient architecture:** Built on Azure Durable Functions for reliable and scalable operation.
5. **Integrations:** Works seamlessly with public and private repositories, supporting tools like GitHub, Bitbucket, and Azure repos.

## How to use LiveDoc - headless tools

LiveDoc is designed to be used as both a **headless API** and through the **QED Developer Portal UI**. Here’s how to use it via headless tools like **Postman**:

1. **Setup:**
   - Obtain an **API key** from the Developer Portal.
   - Configure Postman with the base URL for the LiveDoc API.
2. **API calls:**
   - Use a `GET` request to initiate a scan on a repository, including the repository URL and API key in the request body.
   - Use a `GET` request to retrieve the generated Markdown document or to check the status of a scheduled scan.
3. **Automated workflow:** 
   - Integrate with CI/CD pipelines to trigger scans after code commits, keeping documentation up-to-date with development changes.

## How to use LiveDoc - managing config via the UI

LiveDoc’s configuration can be managed directly through the **admin panel** on the Developer Portal, allowing users to:

- **Add or remove repositories to scan:** Add new repositories or remove outdated ones from the scanning list.
- **Modify repositories to scan:** Change the configuration values for existing repositories in the list.


## Feature gaps in the existing implementation
The existing implementation of the LiveDoc tool still has some features that have yet to be implemented.
- **Trigger LiveDoc:** Initiate a scan directly from the Admin site on the QED Developer Portal.
- **Set schedules:** Define custom schedules for scanning based on the project’s requirements. Scheduling LiveDoc is an important part of the document generation as it ensures the projects documentation is always current and reflection of the existing state of the project.
- **View reports:** Access a history of generated Markdown documents, with insights into changes made over time.
- **Manage API keys:** Generate and manage API keys to maintain secure access. Although this functionality already exists in the Admin site on the Developer Portal, the LiveDoc APIs are secured by a different mechanism.

## Links to LiveDoc samples
- To be added in future