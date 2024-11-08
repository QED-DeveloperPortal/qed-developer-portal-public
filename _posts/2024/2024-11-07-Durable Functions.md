---
title: "Durable Functions"
author: andrew
categories: Public
classification: Public
tags: [opinion,architecture]
date: 2024-11-07 04:55:26 
updatedBy: andrew
updated: 2024-11-08 00:53:06 
likes: 0
---

Durable Functions are Azure Functions that enable you to run stateful functions in a serverless environment without extra configuration cognitive overhead for the developer.

**Benefits**

1. Distributed transactions in a cloud environment are efficient and simple rather than being a bottleneck and complex to setup.
2. Significantly lower cost than using Azure Web Apps.

**Technology**

Durable Functions are built on top of the Durable Tasks Framework which enables the creation of long running workflows (known as orchestrations). The Durable Task Framework source code is available at https://github.com/Azure/durabletask.

**Configuration**

The repo for these is at https://github.com/QED-DeveloperPortal/devportal-functions.

They are deployed from this repo via a GitHub Action in the devportal-functions Function App in the QED Azure Portal.

APIs are exposed via the URI https://devportal-functions.azurewebsites.net

**Security**

TBD

~~~~