---
title: "Role-based access mapping in the Developer Portal"
author: joyclyn
categories: public
classification: Public
tags: [auto-import, getting-started,about]
date: 2025-06-26 13:34:26
likes: 0
imported: True 
import-source: "azure-devops"
import-reference: ""
publishedOn: 2025-06-26 13:34:26
---

| Page ↓ | Role → | Anonymous/Unauthenticated | User/Authenticated | Internal | Moderator | Admin | How we manage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Home |  | ✅ | ✅ | ✅ | ✅ | ✅ | Nil |
| Navigation | Home | ✅ | ✅ | ✅ | ✅ | ✅ | Nil |
|  | Tags | ✅ | ✅ | ✅ | ✅ | ✅ | Nil |
|  | Chat | ✅ | ✅ | ✅ | ✅ | ✅ | Nil |
|  | APIs | ✅ | ✅ | ✅ | ✅ | ✅ | Nil |
|  | Help | ✅ | ✅ | ✅ | ✅ | ✅ | Nil |
|  | Contact us | ✅ | ✅ | ✅ | ✅ | ✅ | Nil |
|  | Admin | ❌ | ❌ | ❌ | ❌ | ✅ | Admin hidden from nav |
| Content classification | View content suitable for general publication | ✅ | ✅ | ✅ | ✅ | ✅ | Nil |
|  | View content suitable for internal use | ❌ | ❌ | ✅ | ✅ | ✅ | *To be decided; possibly hidden* else 403 |
|  | Add new content | ❌ | ✅ | ✅ | ✅ | ✅ | Add post link hidden |
|  | Update content | ❌ | ✅ | ✅ | ✅ | ✅ | Edit link hidden |
|  | Like post | N/A | N/A | N/A | N/A | N/A | Removed - revisit later |
|  | Submit feedback on post | ❌ | ✅ | ✅ | ✅ | ✅ | Feedback box hidden |
| Tags | View all tags | ✅ | ✅ | ✅ | ✅ | ✅ | Nil |
|  | View posts by tag | ✅ | ✅ | ✅ | ✅ | ✅ | Nil |
|  | Un/subscribe to/from tags | ❌ | ❌ | ❌ | ✅ | ✅ | Subscribe button hidden |
| APIs |  | ❌ | ✅ | ✅ | ✅ | ✅ | APIs hidden from nav |
|  | Generate an API key | ❌ | ✅ | ✅ | ✅ | ✅ | Disabled |
| Chat |  | ✅ | ✅ | ✅ | ✅ | ✅ | Responses limited by role |
| Help | FAQ | ✅ | ✅ | ✅ | ✅ | ✅ | Nil |
| Contact us | Send feedback | ❌ | ✅ | ✅ | ✅ | ✅ | Text on screen encourages user to sign in |
| Admin | View posts pending approval | ❌ | ❌ | ❌ | ❌ | ✅ | Admin hidden from nav |
|  | View LiveDoc service | ❌ | ❌ | ❌ | ❌ | ✅ | Nil |
|  | View Members | ❌ | ❌ | ❌ | ❌ | ✅ | Nil |
| Readiness canvas | TBC | ❌ | ✅ | ✅ | ✅ | ✅ | Visible but disabled |
| Profile summary |  | ❌ | ✅ | ✅ | ✅ | ✅ | Profile unavailable |
| Manage profile |  | ❌ | ✅ | ✅ | ✅ | ✅ | Profile unavailable |
| ——— | ——— | ——— | ——— | ——— | ——— | ——— | ——— |
| GitHub public repo | Approve/publish public post | ❌ | Requires invitation as an 'outside collaborator' in GH | Requires GH org membership | Requires GH org membership | Requires GH org membership | GH org membership restrictions |
| GitHub private repo | Approve/publish internal post | ❌ | Requires a paid GH seat | Requires a paid GH seat | Requires a paid GH seat | Requires a paid GH seat | GH membership restrictions |