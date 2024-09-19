---
title: "Use AI to build apps with QED APIs"
author: andrew
categories: public
classification: Unofficial (Everyone)
tags: [ai,api,trending,opinion]
date: 2024-09-03 05:16:52 
updatedBy: jeny-amatya-qed
updated: 2024-09-03 23:22:57 
likes: 0
---

The [DevPortal AI Kit](https://github.com/qed-developerportal/devportal-ai-kit) has been developed to help you start building apps that target publicly available QED APIs, with AI assistance to guide you along the way.

The default configuration allows you to explore the APIs through natural language conversations with a locally installed Large Language Model (LLM), which is set up during the configuration process.

When you make a request to the LLM, Microsoft’s Semantic Kernel interprets it and, if relevant, makes API calls to the DevPortal Semantic Kernel Plugin (source code available in [DevPortalPlugin.cs](https://github.com/QED-DeveloperPortal/DevPortal-AI-Kit/blob/main/Plugins/DevPortalPlugin.cs)). The plugin's descriptions help determine whether an API call should be made.

Responses from the DevPortal Plugin are then passed to the local [LLM](https://llama.meta.com/) (via [Ollama](https://ollama.com)), where they are formatted into a final answer presented to the user.

This setup not only provides you with descriptions of available resources but also includes code examples for using the APIs.

Below is a diagram illustrating how the components are connected.

![DevPortal AI Kit](https://sadevportal3.blob.core.windows.net/root/post/devportal_ai_kit.png)

Stay tuned for future articles on how this capability is being enhanced to better assist you in building outstanding apps for the education sector.