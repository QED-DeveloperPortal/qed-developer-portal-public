---
title: "How LiveDoc can help you"
author: matt
categories: [Public]
classification: Public
tags: [ai]
date: 2024-10-22 05:00:10 
updatedBy: Joyclyn
updated: 2024-10-29 22:42:58 
likes: 1
---

# What is LiveDoc and how it can help you

**LiveDoc** is a cloud-hosted tool designed to enhance software documentation through AI-driven analysis of public or private cloud-hosted code repositories. By scanning repositories, LiveDoc generates an AI-assisted summary of the source code, including:

- **Purpose of the software:** A concise overview explaining what the software does.
- **Breakdown of key components:** Detailed analysis of major modules, functions, and patterns in the codebase.
- **Overall summation:** An aggregated view of the codebase structure, with insights into architectural choices.

The generated documentation is saved in **markdown format** and securely stored as a technical article on the **QED Developer Portal**.

LiveDoc can be scheduled to run at regular intervals, ensuring that the documentation stays current. Any changes, whether from updates in coding patterns or new module additions, are automatically captured, providing a constantly refreshed summary of the evolving codebase.

## How LiveDoc works: An overview of Azure Durable Functions

The underlying architecture of LiveDoc leverages **Azure Durable Functions**, a serverless extension that enables orchestration of stateful workflows in Azure Functions. This makes LiveDoc reliable, scalable, and resilient. Here's a high-level breakdown of how it works:

- **Orchestrator Function:** This serves as the central controller, managing the sequence of tasks, error handling, and retries. It directs the flow of data as the code repository is analyzed.
- **Activity Functions:** Each task in LiveDoc—such as fetching repository content, analyzing the code, and generating markdown—runs as a discrete, stateless activity function.
- **Durability and Resilience:** If the process is interrupted, the orchestrator ensures that execution continues from where it left off, allowing LiveDoc to handle large codebases or unexpected failures seamlessly.
- **Timer Triggers:** LiveDoc uses timers to schedule scans at regular intervals, maintaining up-to-date documentation without manual intervention.

## Key features of LiveDoc

1. **Automated Code Analysis:** Quickly generates a comprehensive summary of a code repository.
2. **Markdown Export:** Outputs documentation in markdown format, making it easy to share, edit, and store.
3. **Scheduled Updates:** Runs on a predefined schedule to keep documentation current.
4. **Resilient Architecture:** Built on Azure Durable Functions for reliable and scalable operation.
5. **Integrations:** Works seamlessly with public and private repositories, supporting tools like GitHub, Bitbucket, and Azure Repos.

## How to use LiveDoc - Headless tools

LiveDoc is designed to be used as both a **headless API** and through the **QED Developer Portal UI**. Here’s how to use it via headless tools like **Postman**:

1. **Setup:**
   - Obtain an **API key** from the QED Developer Portal.
   - Configure Postman with the base URL for the LiveDoc API.
2. **API Calls:**
   - Use a `GET` request to initiate a scan on a repository, including the repository URL and API key in the request body.
   - Use a `GET` request to retrieve the generated markdown document or to check the status of a scheduled scan.
3. **Automated Workflow:** 
   - Integrate with CI/CD pipelines to trigger scans after code commits, keeping documentation up-to-date with development changes.

## How to use LiveDoc - Managing config via the UI

LiveDoc’s configuration can be managed directly through the **admin panel** on the QED Developer Portal, allowing users to:

- **Add or remove repositories to scan:** Add new repositories or remove outdated ones from the scanning list.
- **Modify repositories to scan:** Change the configuration values for existing repositories in the list.


## Feature gaps in the existing implementation
The existing implementation of the LiveDoc tool still has some features that have yet to be implemented.
- **Trigger LiveDoc:** Initiate a scan directly from the Admin site on the QED Developer Portal.
- **Set schedules:** Define custom schedules for scanning based on the project’s requirements. Scheduling LiveDoc is an important part of the document generation as it ensures the projects documentation is always current and reflection of the existing state of the project.
- **View Reports:** Access a history of generated markdown documents, with insights into changes made over time.
- **Manage API keys:** Generate and manage API keys to maintain secure access. Whilst this functionality already exists in the Admin site on the QED Developer Portal, the LiveDoc APIs are secured by a different mechanism.

## Links to LiveDoc samples
- To be added in future