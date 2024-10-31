---
title: Role based access mapping in Developer Portal
author: jeny-amatya-qed
categories: [Public]
classification: Public
tags: [getting-started,about]
date: 2023-07-13 01:14:37 
updatedBy: jeny-amatya-qed
updated: 2024-09-02 00:37:12 
likes: 1
---

## Overview

In Developer Portal, security and access is managed through Role-Based Access Control (RBAC), where different user roles are assigned specific permissions to various parts of the application. This post will explore how RBAC has been implemented in Developer Portal by mapping different roles to corresponding access levels.

## What is Role-Based Access Control (RBAC)?

Role-Based Access Control (RBAC) is a security paradigm where permissions are assigned to roles rather than individual users. Users are then assigned to these roles, which dictate what actions they can perform in the application

## Custom roles in Developer Portal

Developer Portal implements Role-Based Access Control (RBAC) via custom roles using [Azure Active Directory Business-to-Consumer (AAD B2C)](https://learn.microsoft.com/en-us/azure/active-directory-b2c/overview).

* Administrator: Full access to all features
* Moderator: Can moderate, review and approve content submitted by users
* Internal: Can view and edit content classified as 'Sensitive (Government)'

The following table shows how these roles are mapped to different parts of Developer Portal.


| Navigation |  User Roles  | Anonymous (user has not logged in) |Authenticated (logged in user with no roles) | Internal (has access to non-public content)| Moderator (has access to review and moderate content) | Administrator |
| :--- | :--- | :--------- | :--- | :--- | :--- | :--- |
| | Home | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | Tags | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | Chat | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | APIs | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | Help | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | Contact us | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | Admin | ✕| ✕| ✕ | ✕ | ✓ |
|  | View public content | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | View non-public content  | ✕ | ✕ | ✓ | ✓ | ✓ |
|  | Add/edit public content | ✕ | ✕ | ✓ | ✓ | ✓ |
|  | Add/edit non-public content | ✕ | ✕ | ✓ | ✓ | ✓ |
|  | Moderate/review content | ✕ | ✕ | ✕ | ✓ | ✕ |
|  | Like post | ✕ | ✓ | ✓ | ✓ | ✓ |
|  | Submit feedback on post | ✕ | ✓ | ✓ | ✓ | ✓ |
| Tags | View all tags | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | Subscribe/unsubscribe to tags | ✕ | ✕ | ✕  | ✓ | ✓ |
| Help | FAQ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Contact us | Send feedback | ✕ | ✓ | ✓ | ✓ | ✓ |
| Admin | View posts pending approval | ✕ | ✕ | ✕ | ✕ | ✓ |
| Profile Summary |  | ✕ | ✓ | ✓ | ✓ | ✓ |
| Manage Profile |  | ✕ | ✓ | ✓ | ✓ | ✓ |

