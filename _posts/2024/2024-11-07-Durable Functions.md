---
title: "Durable Functions"
slug: "durable-functions-e9d68d"
author: andrew
categories: Public
classification: Public
tags: [architecture]
date: 2024-11-07 04:55:26 
updatedBy: Joyclyn
updated: 2025-04-29 00:49:27 
likes: 0
---

### Overview

Durable Functions are Azure Functions that enable you to run stateful functions in a serverless environment without extra configuration cognitive overhead for the developer.

Durable Functions are significant easier to setup and run at a much lower cost compared to Azure Web Apps.

### Technology

Durable Functions are built on top of the Durable Tasks Framework which enables the creation of long running workflows (known as orchestrations). The Durable Task Framework source code is available at [https://github.com/Azure/durabletask](https://github.com/Azure/durabletask).

### Configuration

The repo for these is at [https://github.com/QED-DeveloperPortal/devportal-functions](https://github.com/QED-DeveloperPortal/devportal-functions).

They are deployed from this repo via a GitHub Action in the devportal-functions Function App in the QED Azure Portal.

APIs are exposed via the URI [https://devportal-functions.azurewebsites.net](https://devportal-functions.azurewebsites.net)

### Security

APIs are secured by the same Microsoft Entra/AAD B2C configuration as used for the main Developer Portal website.