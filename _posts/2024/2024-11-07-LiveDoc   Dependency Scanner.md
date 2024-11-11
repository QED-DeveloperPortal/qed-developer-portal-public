---
title: "LiveDoc / Dependency Scanner"
author: andrew
categories: Public
classification: Public
tags: [opinion,architecture]
date: 2024-11-07 06:47:56 
updatedBy: andrew
updated: 2024-11-11 23:28:53 
likes: 0
---

**Dependency Scanner**

Dependency Scanner is a tool for internal QED use.

It is used to create a report of dependencies for internally developed source code.

**Dependency Scanner Authentication**

In order to generate a Dependency Scanner report for a repo one must have an access token that is approved by that repo.

**LiveDoc**

Starts by creating Cosmos Database if it doesn't already exist.

Generates a summary of the README.md file to give an overview of the project. Otherwise, if a markdown tag of #Overview# is present it uses that section.

Generates configuration notes from the README.md file, or uses the #Configuration# section of the same file if that is present.

Generates installation notes from the README.md file, or uses the #Installation# section of the same file if that is present.

LiveDoc also attempts extract developer notes from code comments and the README.md file.

Generates list of project contributors by parsing the root README.md files and pull requests in a project.

**LiveDoc Authentication**

In order to generate a LiveDoc report for a repo one must have an access token that is approved by that repo.

**DevPortal Permissions**

LiveDoc and Dependency Scanner are only available via the Admin menu in DevPortal which is only available to users who have been granted the Admin role.