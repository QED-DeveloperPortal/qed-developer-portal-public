---
title: CSS standards and guidelines
author: g-morton
categories: [Public]
classification: Unofficial (Everyone)
tags: [standards]
date: 2024-08-29 02:01:48 
updatedBy: sushma-hazari
updated: 2024-09-03 00:23:49 
likes: 0
---

#### CSS file references
CSS files should be organised and referenced based on their purpose and scope. The typical order of precedence for CSS references on a page is as follows:

**Framework-level CSS**
- These files are rendered automatically and include essential styles for the overall framework.

**Third-party CSS**
- These files include styles provided by third-party libraries or frameworks.

**Project-specific CSS**
- These files include styles unique to the project or application and are automatically rendered based on configuration.

**Area-specific CSS**
- Area-specific styles are rendered conditionally based on configuration flags (e.g., `UseAreaCss`).

**Controller-specific CSS**
- Controller-specific styles are rendered conditionally (e.g., `UseControllerCss`).

**Action-specific CSS**
- Action-specific styles are rendered conditionally (e.g., `UseActionCss`).


***

#### Module CSS file content
CSS definitions specific to a particular area or controller should be placed in the respective "area" or "controller" CSS file.

#### URL protocol
When referencing URLs for images, media files, style sheets, and scripts, omit the protocol (e.g., `http:` or `https:`) unless the file is not available over both protocols. This practice helps prevent mixed content issues and results in minor file size savings.

**Example:**
```css
/* Not recommended */
.example {
    background: url(http://www.example.com/images/sample);
}
/* Recommended */
.example {
    background: url(//www.example.com/images/sample);
}
```

#### Capitalisation
All CSS code should be written in lowercase to maintain consistency and readability.

**Example:**
```css
/* Not recommended */
color: #E5E5E5;
/* Recommended */
color: #e5e5e5;
```

#### ID and class naming
Use descriptive, purpose-oriented names for IDs and classes rather than presentational or cryptic names. This approach enhances code readability and maintainability.

**Example:**
```css
/* Not recommended */
#yee-1901 {}
.button-green {}
.clear {}

/* Recommended */
#gallery {}
#login {}
.video {}
.aux {}
.alt {}
```

#### ID and class name style
ID and class names should be as brief as possible while still conveying their purpose.

**Example:**
```css
/* Not recommended */
#navigation {}
.atr {}

/* Recommended */
#nav {}
.author {}
```

#### Type selectors
Avoid using element names in conjunction with IDs or classes unless necessary, as it can negatively impact performance.

**Example:**
```css
/* Not recommended */
ul#example {}
div.error {}

/* Recommended */
#example {}
.error {}
```

#### Shorthand properties
Utilise shorthand properties in CSS whenever possible to enhance code efficiency and clarity.

**Example:**
```css
/* Not recommended */
border-top-style: none;
font-family: palatino, georgia, serif;
font-size: 100%;
line-height: 1.6;
padding-bottom: 2em;
padding-left: 1em;
padding-right: 1em;
padding-top: 0;

/* Recommended */
border-top: 0;
font: 100%/1.6 palatino, georgia, serif;
padding: 0 1em 2em;
```

#### Zero and units
Do not use units after zero values unless required.

**Example:**
```css
margin: 0;
padding: 0;
```

#### Leading zeros
Avoid using leading zeros for values between -1 and 1.

**Example:**
```css
font-size: .8em;
```

#### Hexadecimal notation
Use the shorthand 3-character hexadecimal notation for colour values when possible.

**Example:**
```css
/* Not recommended */
color: #eebbcc;

/* Recommended */
color: #ebc;
```

#### Prefixes
For large projects or code that might be embedded in other projects, prefix selectors with an application-specific identifier to prevent naming conflicts.

**Example:**
```css
/* Application-specific prefixes */
.adw-help {} /* AdWords */
#maia-note {} /* Maia */
```

#### Class name delimiters
Separate words in ID and class names with hyphens for better readability.

**Example:**
```css
/* Not recommended */
.demoimage {}
.error_status {}

/* Recommended */
#video-id {}
.ads-sample {}
```

#### `!important` usage
The use of `!important` should be avoided in favour of properly utilising CSS specificity and cascading rules.

#### Avoiding hacks
Avoid using hacks or user agent detection in CSS. Such practices should be a last resort to maintain an efficient and manageable codebase.

#### Code formatting

**Indentation**
- Set indentation to 4 spaces. Ensure that tabs are replaced with spaces.

**Example:**
```css
.example {
    colour: blue;
}
```

**Curly braces**
- Start curly braces on the same line as the selector.

**Example:**
```css
.a-class-name {
    colour: #fff;
}
```