---
title: "AI chatbot"
slug: "ai-chatbot-bc6cd4"
author: andrew
categories: Public
classification: Public
tags: [architecture,ai]
date: 2024-11-07 06:53:28 
updatedBy: Joyclyn
updated: 2025-04-29 00:38:15 
likes: 0
publishedOn: 2025-04-29 00:38:15
---

Users are able to have natural language conversations with the Developer Portal site, mock APIs and site content via an AI chatbot.

### Azure Open AI

A chat completions model and an embeddings model are configured in Azure Open AI Studio. You can access this configuration at [https://oai.azure.com/resource/deployments](https://oai.azure.com/resource/deployments).

###Semantic Kernel integration

We have integrated Microsoft's Semantic Kernel into the AI chatbot to enable users to interact with the APIs through natural language.  The Semantic Kernel capability has been gleaned from the Microsoft Copilot Chat sample at [https://github.com/microsoft/chat-copilot](https://github.com/microsoft/chat-copilot).

We use the webapi component of chat-copilot exactly as it is in the sample. It is deployed to oai-sk-webapi in Azure via the custom deployment template [https://aka.ms/sk-deploy-existing-azureopenai-portal](https://aka.ms/sk-deploy-existing-azureopenai-portal) that is available via the blue "Deploy to Azure" button on the page [https://github.com/microsoft/chat-copilot/tree/main/scripts/deploy](https://github.com/microsoft/chat-copilot/tree/main/scripts/deploy).

Semantic Kernel employs the same chat completions and embeddings models from Azure Open AI but adds a layer for coordinating components such as a custom Semantic Kernel plugin that is exposed to enable interaction with the mocked APIs.

Semantic Kernel security is configured with the following environment variables that can be found in the swa-developer-portal project:

SEMANTIC_KERNEL_BACKEND_CLIENT_ID
SEMANTIC_KERNEL_BACKEND_SECRET
SEMANTIC_KERNEL_BACKEND_TENANT_ID
SEMANTIC_KERNEL_FRONTEND_REDIRECT_URI
SEMANTIC_KERNEL_FRONTEND_SECRET

For Semantic Kernel to work inside Azure, two Entra App Registrations are required. SP-DeveloperportalBE-Dev is the backend App Registration, while SP-DeveloperportalFE-Dev is the frontend App Registration. These are configured as per instructions on the page [https://github.com/microsoft/chat-copilot/tree/main/scripts/deploy](https://github.com/microsoft/chat-copilot/tree/main/scripts/deploy).

### LiveDoc

We use the same Azure Open AI service used by the chatbot for our LiveDoc service to summarise text contained within the target repos.