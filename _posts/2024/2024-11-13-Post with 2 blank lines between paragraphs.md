---
title: "Post with 2 blank lines between paragraphs"
author: Divya28237
categories: Public
classification: Public
tags: [opinion]
date: 2024-11-13 22:39:59 
likes: 0
---

Deployment

It is deployed in Azure as a Web App named dp-mockaco.

<br>
The mock QED APIs that this tool manages are visually displayed to end users via a Microsoft Blazor interface whose code is at https://github.com/QED-DeveloperPortal/mockportal.

Updates to the MockPortal repo are published to Azure inside the apis folder of the qed-developer-portal repo via a Github Action.

External Access

The mocked QED APIs can also be called as APIs via the base URI https://dp-mockaco.azurewebsites.net.

<br>
End users are required to pass an X-Api-Key value as part of the Http Request Header. End users can request an X-Api-Key via the MockPortal part of DevPortal website. This value is stored in Cosmos for each user.