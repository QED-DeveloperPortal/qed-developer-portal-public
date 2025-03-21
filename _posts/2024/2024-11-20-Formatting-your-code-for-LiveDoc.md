---
title: "Formatting your code for LiveDoc"
slug: "formatting-your-code-for-livedoc-70e820"
author: jeny-amatya-qed
categories: Public
classification: Public
tags: [opinion,getting-started]
date: 2024-11-20 00:58:23 
updatedBy: Joyclyn
updated: 2025-03-21 00:24:09 
likes: 0
---

## How to format your code for LiveDoc

1. For now, your repository must be hosted in **GitHub**. We're working on extending LiveDoc functionality to include code repositories hosted in DevOps, but our initial focus was GitHub.
2. You need to give us a personal access token to access the GitHub repository, with read-only privileges.
3. You need to update your README.md to add section markers that help to extract the relevant text blocks.

Example:

```markdown
<!-- Section: Overview -->
## Overview
Project 'Hello World' is a web-based application... 

<!-- Section: Configuration -->
## Configuration
Clone the repository...

<!-- Section: Installation -->
## Installation
Install the npm packages...
```