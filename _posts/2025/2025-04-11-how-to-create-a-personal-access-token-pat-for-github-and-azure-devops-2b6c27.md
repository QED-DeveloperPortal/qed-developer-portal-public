---
title: "How to Create a Personal Access Token (PAT) for GitHub and Azure DevOps"
slug: "how-to-create-a-personal-access-token-pat-for-github-and-azure-devops-2b6c27"
author: jeny-amatya-qed
categories: Public
classification: Public
tags: [opinion,tutorials,getting-started]
date: 2025-04-11 05:05:47 
updatedBy: jeny-amatya-qed
updated: 2025-04-14 03:53:35 
likes: 0
---

# Overview

Personal Access Tokens (PATs) act like passwords and are used to authenticate against APIs, Git operations, and tools like GitHub CLI or Azure DevOps pipelines. This post walks you through creating PATs in both platforms so the user can interact with both repositories securely.

---

## ✅ GitHub: Creating a Personal Access Token

### 🔹 Step 1: Go to Developer Settings

1. Login to GitHub at [https://github.com](https://github.com).
2. Click on the profile picture (top right corner) → **Settings**.
3. Scroll down the left sidebar and click **Developer settings**.
4. Under “Developer settings,” click **Personal access tokens** > **Tokens (classic)** or **Fine-grained tokens**.

> 📝 GitHub recommends **Fine-grained tokens** for most use cases. These provide more control and are more secure than classic tokens.

---

### 🔹 Step 2: Generate the token

#### Option A: **Fine-grained token (recommended)**

1. Click **Generate new token** → **Fine-grained token**.
2. Name the token (e.g., _My PAT Token_).
3. Set an **expiration** (e.g., 90 days).
4. Choose the **repository access**:
   - Select **Only select repositories** or **All repositories** depending on your needs.
5. Select **permissions** (e.g., `Contents: Read and Write` if pushing code).
6. Click **Generate token**.
7. **Copy the token** and store it securely (e.g., in a password manager).

> 🔒 Please note that GitHub won’t show it again. If the user loses it, they must generate a new one.

#### Option B: **Classic token**

1. Click **Generate new token (classic)**.
2. Fill in token **name**, **expiration**, and select **scopes** (e.g., `repo`, `workflow`, `read:org`, etc.).
3. Click **Generate token** and copy it.

---

### ✅ How to use the GitHub PAT for LiveDoc

Once the user has generated the PAT, he/she can provide it to the Developer Portal team. They can store it in the Azure key vault securely. The Developer Portal team will provide the user a key that they can use in 'Token identifier' field while creating a LiveDoc configuration.

---

## 🔷 Azure DevOps: Creating a Personal Access Token

### 🔹 Step 1: Open user settings

1. Login to Azure DevOps at [https://dev.azure.com](https://dev.azure.com).
2. In the top-right corner, click on the user profile picture.
3. Select **Personal access tokens**.

---

### 🔹 Step 2: Generate a new token

1. Click **+ New Token**.
2. Enter a **name** (e.g., _Developer Portal PAT_).
3. Set **organization**, **expiration** (30, 60, 90 days, or custom).
4. Choose **Scopes**:
   - Common examples:
     - **Code (Read & Write)** to clone/push/pull repositories.
     - **Build (Read & Execute)** for pipelines.
     - **Work Items (Read & Write)** for DevOps boards integration.
5. Click **Create**.
6. **Copy the token** and store it in a safe place.

---

### ✅ How to Use the Azure DevOps PAT

Once the user has generated the PAT, he/she can provide it to the Developer Portal team. They can store it in the Azure key vault securely. The Developer Portal team will provide the user a key that they can use in 'Token identifier' field while creating a LiveDoc configuration.

---

## 🔒 Best Practices for PATs

- **Never commit a PAT** to source control.
- **Use fine-grained permissions** where possible.
- **Set short expiration periods** and regenerate when needed.
- **Store securely** in tools like Azure Key Vault, GitHub Secrets, or password managers.
- **Revoke** tokens if they are no longer needed or compromised.

---
