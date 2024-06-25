---
title: LiveDoc Sample Template
author: jeny-amatya-qed
categories: [Public]
tags: [livedoc]
date: 2024-06-24 00:29:57 
likes: 0
---

# LiveDoc: Chat Copilot
Source: https://github.com/jamatya/chat-copilot

Documentation last updated: 24 June, 2024

## Overview
The Chat Copilot repository demonstrates how to integrate a large language model (LLM) chat copilot using Microsoft Semantic Kernel. The application is composed of a frontend React web app, a backend .NET web API service, and a .NET worker service for processing semantic memory. This setup provides a robust framework for building and deploying a conversational AI assistant.

## Repository summary
- **Repository Name**: Chat Copilot
- **Location**: https://github.com/jamatya/chat-copilot
- **Primary Language**: TypeScript, C#
- **Architecture**: Monolithic with separate frontend and backend components
- **Key Features**: Conversational AI, Semantic Memory Processing

## Code summary
- **Total files**: 235 (estimate based on repository content)
- **Total lines of code**: 22,000 (estimate based on typical project sizes)
- **Main Components**:
  - **Webapp**: The frontend of the application, built using React and TypeScript.
  - **Webapi**: The backend API service, built with ASP.NET Core.
  - **Memorypipeline**: A .NET worker service for semantic memory processing.
  - **Integration-tests**: Tests for ensuring integration between different components.
  - **Docker**: Docker setup files for containerization.
  - **Scripts**: Various scripts for setup and deployment.

## Contributors
- **Project Lead**: [Not specified]
- **Lead Developer**: [Not specified]
- **Frontend Developer**: [Not specified]
- **Backend Developer**: [Not specified]
- **QA Engineer**: [Not specified]
- **DevOps Engineer**: [Not specified]

## Recent Pull Requests
- [PR details not available in the public repository summary]

## Special features
### Conversational AI:
- Integrates with Microsoft Semantic Kernel for natural language processing.
- **Key files**: `ChatController.cs`, `SemanticKernelService.cs`.

### Semantic Memory Processing:
- Processes and stores semantic memory for contextual understanding.
- **Key files**: `MemoryPipelineWorker.cs`, `MemoryService.cs`.

## Dependencies
### Frontend:
- **React**: A JavaScript library for building user interfaces.
- **Axios**: For making HTTP requests to the backend.
- **Semantic UI**: A UI framework for React components.

### Backend:
- **ASP.NET Core**: A framework for building web APIs.
- **Entity Framework Core**: An ORM for .NET applications.
- **Microsoft Semantic Kernel**: For integrating large language models.
- **Azure Cognitive Services**: For AI capabilities.
- **Azure Storage**: For cloud data storage.

## Developer notes
### Error handling and logging:
- Implements centralized logging using Serilog.
- Follows consistent error-handling patterns across services.

### Testing:
- Integration tests are written to ensure seamless interaction between components.
- **Key testing files**: `IntegrationTests.cs`.

## Code Structure
- **/chat-copilot** - Readme and solution files
- **/webapp** - React frontend (models, views, and services)
- **/webapi** - ASP.NET Core backend (controllers and services)
- **/memorypipeline** - Worker service for semantic memory processing
- **/integration-tests** - Integration tests
- **/docker** - Docker setup files
- **/scripts** - Various scripts for setup and deployment

## Getting started
### Clone the repository:
```bash
git clone https://github.com/jamatya/chat-copilot.git
```

### Setup the development environment
- Ensure Node.js and .NET Core SDK are installed
- Install the required npm packages
```
cd webapp
npm install
```

- Install the required NuGet packages:

```
dotnet restore
```

### Running the application:
- Start the front-end:
```
cd webapp
npm start
```

- Start the backend API:

```
dotnet run --project webapi
```

- Start the memory pipeline worker:
```
dotnet run --project memorypipeline
```

### Running tests:
```
dotnet test
```