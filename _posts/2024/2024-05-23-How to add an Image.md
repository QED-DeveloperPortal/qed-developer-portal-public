---
title: How to add an Image in Markdown editor
author: sushma-hazari-qed
categories: [public]
classification: Public
tags: [getting-started]
date: 2024-05-23 02:12:44 
updatedBy: Sushma Hazari (IA)
updated: 2024-06-28 05:53:53 
likes: 0
---

# How to Add an Image in Markdown Editor

Adding images to your Markdown posts is a great way to enhance your content and make it more engaging. Here’s a step-by-step guide on how to do it.

To add an image, add an exclamation mark (!), followed by alt text in brackets, and the path or URL to the image asset in parentheses. You can optionally add a title in quotation marks after the path or URL.

## Basic Image Syntax

The basic syntax for adding an image in Markdown is straightforward:

**1. Basic Image Embedding**

```
![Alt Text](ImageURL)
```

* Alt Text: A short description of the image.
* ImageURL: The direct URL to the image.

Example

Here’s an example of how to add an image, and the rendered output looks like this:

<img src="https://sadevportal3.blob.core.windows.net/root/img-qa-ops.png" alt="Alt text" width="500" height="400">

**2. Adding a Title**

You can also add a title to your image, which appears when you hover over it:

```
![Alt text](image_url "Image Title")
```

**3. Local Images**

If the image is stored locally, provide the relative path:

```
![Alt text](./path/to/image.jpg)
```

**4. Image Dimensions**

To specify the dimensions of the image, you can use HTML within your Markdown:

```
<"img src="https://example.com/image.jpg" alt="My Image" width="500" height="300">
```

**Conclusion**

Adding images to your Markdown posts is simple and effective for enhancing visual appeal and providing more context. Using the basic Markdown syntax, you can easily embed images with alt text for better accessibility. Adding titles that appear on hover is also straightforward. Although Markdown doesn’t support resizing images directly, integrating HTML allows you to adjust image dimensions to better fit your content layout. By understanding these methods, you can create more engaging and accessible posts in your Markdown editor.