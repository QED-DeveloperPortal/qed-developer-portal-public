---
title: "Choosing better titles for developer posts"
slug: "choosing-a-suitable-title-for-your-post-ef5813"
author: jeny-amatya-qed
categories: Public
classification: Public
tags: [getting-started,faq]
date: 2023-05-18 00:27:58 
updatedBy: jeny-amatya-qed
updated: 2026-02-03 22:40:38 
publishedOn: 2026-02-03 22:40:38 
likes: 2
---

### Overview
A good title helps developers understand what they will get, improves search visibility and avoids frustrating validation or build issues.

 This post will look at how titles are validated, why those rules exist and how to write titles that are both developer-friendly and system-friendly, using regular expressions (regex) under the hood.


### How title validation works
The validation logic applies two simple but crucial cleanup steps to the title.

#### 1. Remove unsupported characters
This step removes any characters that aren't:
     - Letters or numbers
     - Whitespace
     - Hyphens

It ensures that the titles are predictable and safe for places like YAML frontmatter, URLs and search indexing. This strips out symbols like `!`, `@`, `&`, `#` and `?` and avoids parsing issues and inconsistent rendering across platforms.

 ```csharp
 string validTitle = Regex.Replace(title, @"[^\w\s-]", "");
 ```
#### 2. Normalise whitespaces
This step replaces multiple spaces with a single space and removes leading or trailing whitespace. This ensures that titles look clean in navigation menus, search results and page headers.
```csharp
validTitle = Regex.Replace(validTitle, @"\s+", " ").Trim();
```


### Tips for writing valid (and useful) titles
1. Focus on meaningful keywords
    Think about what a developer would actually search for.
    - Getting started with OAuth in a Developer Portal
    - How to add API versioning in .NET
   
2.  Be clear and specific
    Avoid vague titles that don't explain the value.
    - Helpful Tips ❌
    - 5 tips for improving API documentation usability ✅
    
3. Keep titles concise
    Aim for 50-60 characters when possible to avoid truncation in search results.

4. Use hyphens and spaces intentionally
    Hyphens can improve readability when used sparingly.
    - Step--by--step--guide ❌
    - Step-by-step guide to publishing APIs ✅   
    
5. Watch you spacing
    Extra spaces will be normalised.

### Examples
**Invalid titles (before validation)**
* "The Best!@# Developer Guide"
* "    Too Many     Spaces   "
* "Build & Deploy APIs"

**Valid titles (after validation)**
* "The Best Developer Guide"
* "Too Many Spaces"
* "Build and deploy APIs"

### Final Thoughts
A strong title should be easy for developers to understand at a glance, friendly to search engines and safe for validation rules, frontmatter and build pipelines.