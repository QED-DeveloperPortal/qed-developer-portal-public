---
title: "Formatting your code for LiveDoc"
author: jeny-amatya-qed
categories: Public
classification: Public
tags: [opinion,getting-started]
date: 2024-11-20 00:58:23 
updatedBy: jeny-amatya-qed
updated: 2024-11-22 01:23:26 
likes: 0
---

## How to format your code for LiveDoc

1. Your repository should be hosted in GitHub.
2. We need a personal access token to access the repository, with read-only privileges.
3. Update the README.md to add section markers that help to extract the relevant text blocks. Please note that you do not include ## Overview in 'Overview' section as it is already included in the LiveDoc template.

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