---
title: "AI Chatbot"
author: andrew
categories: Public
classification: Public
tags: [opinion,architecture,ai]
date: 2024-11-07 06:53:28 
updatedBy: andrew
updated: 2024-11-11 04:01:45 
likes: 0
---

Users are able to have natural language conversations with the DevPortal site, mock QED APIs and site content via an AI Chatbot.

**Semantic Kernel Integration**

Microsoft's Semantic Kernel has been integrated into the AI Chatbot to enable users to interact with the QED APIs through natural language.  The Semantic Kernel capability has been gleaned from the Microsoft Copilot Chat sample at https://github.com/microsoft/chat-copilot.

We use the webapi component of chat-copilot exactly as it is in the sample. It is deployed to oai-sk-webapi in Azure via the Custom Deployment Template https://aka.ms/sk-deploy-existing-azureopenai-portal that is available via the blue "Deploy to Azure" button on the page https://github.com/microsoft/chat-copilot/tree/main/scripts/deploy.

**LiveDoc and Dependency Scanner**

The same Azure Open AI service as used by the Chatbot is also used on occasion by the LiveDoc and Dependency Scanner tools to summarise text contained within the target repos.