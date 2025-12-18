---
title: "AI Chatbot"
author: andrew
categories: Public
classification: Public
tags: [opinion,architecture,ai]
date: 2024-11-07 06:53:28 
updatedBy: andrew
updated: 2024-11-13 00:02:22 
likes: 0
publishedOn: 2024-11-13 00:02:22
---

Users are able to have natural language conversations with the DevPortal site, mock QED APIs and site content via an AI Chatbot.

&nbsp;
**Azure Open AI**

A Chat Completions model and an Embeddings model are configured in Azure Open AI Studio. This configuration can be accessed at [https://oai.azure.com/resource/deployments](https://oai.azure.com/resource/deployments).

&nbsp;
**Semantic Kernel Integration**

Microsoft's Semantic Kernel has been integrated into the AI Chatbot to enable users to interact with the QED APIs through natural language.  The Semantic Kernel capability has been gleaned from the Microsoft Copilot Chat sample at [https://github.com/microsoft/chat-copilot](https://github.com/microsoft/chat-copilot).

We use the webapi component of chat-copilot exactly as it is in the sample. It is deployed to oai-sk-webapi in Azure via the Custom Deployment Template [https://aka.ms/sk-deploy-existing-azureopenai-portal](https://aka.ms/sk-deploy-existing-azureopenai-portal) that is available via the blue "Deploy to Azure" button on the page [https://github.com/microsoft/chat-copilot/tree/main/scripts/deploy](https://github.com/microsoft/chat-copilot/tree/main/scripts/deploy).

Semantic Kernel employs the same Chat Completions and Embeddings models from Azure Open AI but adds a layer for coordinating components such as a custom Semantic Kernel Plugin that is exposed to enable interaction with the mocked QED APIs.

Semantic Kernel security is configured with the following Environment variables that can be found in the swa-developer-portal project:

SEMANTIC_KERNEL_BACKEND_CLIENT_ID
SEMANTIC_KERNEL_BACKEND_SECRET
SEMANTIC_KERNEL_BACKEND_TENANT_ID
SEMANTIC_KERNEL_FRONTEND_REDIRECT_URI
SEMANTIC_KERNEL_FRONTEND_SECRET

For Semantic Kernel to work inside Azure, two Entra App Registrations are required. SP-DeveloperportalBE-Dev is the backend App Registration, while SP-DeveloperportalFE-Dev is the frontend App Registration. These are configured as per instructions on the page [https://github.com/microsoft/chat-copilot/tree/main/scripts/deploy](https://github.com/microsoft/chat-copilot/tree/main/scripts/deploy).

&nbsp;
**Live~~~~Doc and Dependency Scanner**

The same Azure Open AI service as used by the Chatbot is also used on occasion by the LiveDoc and Dependency Scanner tools to summarise text contained within the target repos.