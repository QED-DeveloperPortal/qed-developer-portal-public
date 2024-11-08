---
title: "Durable Functions"
author: andrew
categories: Public
classification: Public
tags: [opinion,architecture]
date: 2024-11-07 04:55:26 
updatedBy: andrew
updated: 2024-11-08 00:06:13 
likes: 0
---

Durable Functions are Azure Functions that enable you to run stateful functions in a serverless environment.

**Benefits**

1. Distributed transactions in a cloud environment are efficient and simple rather than being a bottleneck and complex to setup.

**Configuration**

The repo for these is at https://github.com/QED-DeveloperPortal/devportal-functions.

They are deployed from this repo via a GitHub Action in the devportal-functions Function App in the QED Azure Portal.

APIs are exposed via the URI https://devportal-functions.azurewebsites.net

~~~~