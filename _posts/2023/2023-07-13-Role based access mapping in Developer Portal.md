---
title: Role based access mapping in Developer Portal
author: jeny-amatya-qed
categories: [Public]
classification: Official
tags: [getting-started,about]
date: 2023-07-13 01:14:37 
updatedBy: jeny-amatya-qed
updated: 2024-08-28 21:57:42 
likes: 1
---

## Overview

In Developer Portal, security and access is managed through Role-Based Access Control (RBAC), where different user roles are assigned specific permissions to various parts of the application. The post will explore how RBAC has been implemented in Developer Portal by mapping different roles to corresponding access levels.

## What is Role-Based Access Control (RBAC)?

Role-Based Access Control (RBAC) is a security paradigm where permissions are assigned to roles rather than individual users. Users are then assigned to these roles, which dictate what actions they can perform in the application

## Custom roles in Developer Portal

Developer Portal implements Role-Based Access Control (RBAC) via custom roles using Azure Active Directory Business-to-Consumer (AAD B2C).

* Administrator: Full access to all features
* Moderator: Can moderate, review and approve content submitted by users
* Internal: Can view and edit content classified as 'Sensitive (Government)'

The following table shows how these roles are mapped to different parts of Developer Portal.

|  |  | Anonymous | Signed in | Internal | Moderator | Administrator |
| :--- | :--- | :--------- | :--- | :--- | :--- | :--- |
| Home |  | ✓ | ✓ | ✓ | ✓ | ✓ |
| Navigation | Home | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | Tags | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | Chat | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | APIs | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | Help | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | Contact us | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | Admin | ✕| ✕| ✕ | ✕ | ✓ |
| Categories | View posts under public | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | View posts under internal | ✕ | ✕ | ✓ | ✓ | ✓ |
|  | Add post for category | ✕ | ✕ | ✓ | ✓ | ✓ |
|  | Update post for category | ✕ | ✕ | ✓ | ✓ | ✓ |
|  | Edit post for category | ✕ | ✕ | ✓ | ✓ | ✓ |
|  | Like post | ✕ | ✓ | ✓ | ✓ | ✓ |
|  | Submit feedback on post | ✕ | ✓ | ✓ | ✓ | ✓ |
| Tags | View all tags | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | Subscribe/unsubscribe to tags | ✕ | ✕ | ✓ | ✓ | ✓ |
| Help | FAQ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Contact us | Send feedback | ✕ | ✓ | ✓ | ✓ | ✓ |
| Admin | View posts pending approval | ✕ | ✕ | ✕ | ✕ | ✓ |
| Profile Summary |  | ✕ | ✓ | ✓ | ✓ | ✓ |
| Manage Profile |  | ✕ | ✓ | ✓ | ✓ | ✓ |

## Further Reading

* [Information security classifications on the Developer Portal](https://developer.qed.qld.gov.au/public/Information-Security-Classifications-and-the-Developer-Portal/)