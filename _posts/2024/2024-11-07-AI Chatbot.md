---
title: "AI Chatbot"
author: andrew
categories: Public
classification: Public
tags: [opinion,architecture,ai]
date: 2024-11-07 06:53:28 
updatedBy: andrew
updated: 2024-11-07 20:55:20 
likes: 0
---

Users are able to have a natural language chat with our site and it's content via natural language using AI Chatbot.

We have added Semantic Kernel to enable us to provide capability for users to interact with the QED APIs through natural language.  The Semantic Kernel capability has been gleaned from the Microsoft Copilot Chat sample at https://github.com/microsoft/chat-copilot.

We use the webapi component of chat-copilot. It is deployed to oai-sk-webapi in Azure via the link https://aka.ms/sk-deploy-existing-azureopenai-portal that is on the page https://github.com/microsoft/chat-copilot/tree/main/scripts/deploy.