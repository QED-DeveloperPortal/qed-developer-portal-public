---
title: "Why and how we use role-based access control"
slug: "why-and-how-we-use-role-based-access-control-c7f576"
author: Joyclyn
owner: Joyclyn
categories: Public
classification: Public
tags: [auto-import, about, getting-started]
date: 2025-08-28 05:30:21
likes: 0
imported: True 
import-source: "azure-devops"
import-reference: ""
---

Role-based access control (RBAC) is a security method that helps manage users’ access to systems and resources based on an assigned role. We use RBAC in the Developer Portal for a few purposes.

## Why we use RBAC

By using RBAC we can manage users’ access levels quickly and easily. We assign each user with a role that has certain pre-defined permissions attached. Then, if we need to adjust access to certain information or functionality, we only need to edit the role’s access rather than each user’s individual access. The changes we make to the role are then automatically applied to the users with that role assigned.

In short, we use RBAC to manage user access because it is:

- efficient
- cost effective
- more secure
- easy to audit.

By attending to the access needs of each role, we can easily manage the access needs of our growing user base.

## How we use RBAC

We manage roles using Azure Active Directory Business-to-Consumer and grant access to a range of users from unauthenticated users to administrators. Most of the information available on our portal is available for all users to view but occasionally, some information is reserved for employees or contractors of the department, by using the ‘internal’ role.

We also use RBAC to nudge any casual, unauthenticated users to sign up and authenticate because, when they do, their access to the site opens right up! Unauthenticated users can only view information. Authenticated users can browse and interact with the information and resources on the site, create API keys and more. If you’re reading this as an unauthenticated user, please consider signing up to join us. We’d love to welcome you to the Developer Portal!

## Our RBAC schedule

Here's how we break down roles in the Developer Portal:

- **Unauthenticated users**: Users with this role can see most of the information on the Developer Portal but they cannot interact with content or offer contributions.
- **Authenticated users**: Users with this role can see most of the information offered on the Developer Portal. They can interact with that content and offer contributions.
- **Internal users**: We use this role for authenticated users who are also employed or contracted to the department. Users with this role can see information on the portal that has a higher classification assigned. They can also interact with all content and offer contributions.
- **Moderators**: We use this role for authenticated users who are employed or contracted to the department *and* who are authorised to moderate user contributions to the portal. Users with this role—in combination with a paid GitHub Enterprise licence—can review and approve user contributions. They can also see information on the portal that has a higher classification assigned, interact with all content and offer their own contributions.
- **Administrators**: We use this role for authenticated users who are employed or contracted to the department *and* who are authorised as a site administrator. Users with this role can access the admin tools and view additional information such as post pending approval. They can also see information on the portal that has a higher classification assigned, interact with all content and offer their own contributions.

If you’d like to see even more detail of our RBAC schedule, visit our post called, [Role-based access mapping in the Developer Portal](/public/Role-based_access_mapping_in_the_Developer_Portal/).

And if you’re curious to know what role(s) you have and you’re signed into the site, you can see your role(s) in your profile summary. If you have any questions or want to request a change, please email us at [developerportal@qed.qld.gov.au](mailto:developerportal@qed.qld.gov.au).