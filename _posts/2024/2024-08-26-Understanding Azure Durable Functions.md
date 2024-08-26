---
title: Understanding Azure Durable Functions
author: jeny-amatya-qed
categories: [Public]
classification: Unofficial (Everyone)
tags: [azure,opinion]
date: 2024-08-26 05:27:42 
likes: 0
---

# Overview

**Azure Durable Functions** is an extension of Azure Functions that allows you to write stateful functions in a serverless environment. It provides the capability to define workflows using code, handle long-running operations, and manage state across multiple function executions.

## Key Concepts
1. **Orchestrator Function:** This function defines the workflow. It coordinates the execution of other functions (activity functions) in a sequence or pattern like fan-out/fan-in.

2. **Activity Function:** These are the basic units of work and can be executed independently. The orchestrator calls these functions.
 
3. **Durable Timer:** Allows the orchestrator to wait for a certain time without consuming any compute resources.

4. **Client Function:** This function triggers the orchestrator. It can start a new workflow, check the status, or terminate it.

5. **Entity Functions:** Manage and maintain state using durable entities, useful for scenarios requiring fine-grained state management.

## Real-World Scenario: E-commerce Order Processing
