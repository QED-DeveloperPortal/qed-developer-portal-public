---
title: OneSchool development standards and guidelines extract section 7 Cascade Style Sheet (CSS)
author: Joyclyn
categories: [Public]
tags: [standards,oneschool]
date: 2024-04-23 03:14:11 
likes: 0
---

# 7 Cascade Style Sheet (CSS)
## 7.1 CSS References
CSS files are delivered to the client via MVC bundling.
The precedence for CSS references on a page is controlled via the layout and for osf.Model implementations is as follows:
### 7.1.1 DETA.Framework
These files are rendered automatically
- framework.css
- Menu.css
### 7.1.2 Third Party
These files are rendered automatically
- kendo
### 7.1.3 OneSchool Framework
These files are rendered automatically
- oneschool.css
- tabs.css
- osf.mvc.*
### 7.1.4 MVC Area Specific
The file is rendered if `UseAreaCss` is set to true.
For example, oslp.schoolPlan.css
### 7.1.5 MVC Controller Specific
The file is rendered if `UseControllerCss`  is set to true.
For example, oslp.schoolPlan.school.css
### 7.1.6 MVC Action Specific
The file is rendered if `UseActionCss`  is set to true.
For example, oslp.schoolPlan.school.details.css
## 7.2 Module CSS File Content
Definition specifically associated with an area or controller should be placed in either "area" or "controller" CSS file.
## 7.3 Protocol
Omit the protocol portion (http:, https:) from URLs pointing to images and other media files, style sheets, and scripts unless the respective files are not available over both protocols.
Omitting the protocol, which makes the URL relative, prevents mixed content issues and results in minor file size savings.

**Not recommended**:
```
.example {
 background: url(http://www.google.com/images/example);
}
```
**Recommended**:
```
.example {
    background: url(//www.google.com/images/example);
}
```
## 7.4 Capitalisation
All code has to be lowercase.
**Not recommended**:
```
color: #E5E5E5;
```

**Recommended**:
```
color: #e5e5e5;
```

## 7.5 ID and Class Naming
Instead of presentational or cryptic names, always use ID and class names that reflect the purpose of the element in question, or that are otherwise generic.
Names that are specific and reflect the purpose of the element should be preferred as these are most understandable and the least likely to change.
Generic names are simply a fallback for elements that have no particular or no meaning different from their siblings. They are typically needed as "helpers."
Using functional or generic names reduces the probability of unnecessary document or template changes.

**Not recommended** (meaningless):
```
#yee-1901 {}
```

**Not recommended** (presentational):
```
.button-green {}
.clear {}
```

**Recommended** (specific):
```
#gallery {}
#login {}
.video {}
```

**Recommended** (generic):
```
.aux {}
.alt {}
```

## 7.6 ID and Class Name Style
Use ID and class names that are as short as possible but as long as necessary.
Try to convey what an ID or class is about while being as brief as possible.
Using ID and class names this way contributes to acceptable levels of understandability and code efficiency.

**Not recommended**:
```
#navigation {}
.atr {}
```

**Recommended**:
```
#nav {}
.author {}
```

## 7.7 Type Selectors
Unless necessary (for example with helper classes), do not use element names in conjunction with IDs or classes.
Avoiding unnecessary ancestor selectors is useful for performance reasons.

**Not recommended**:
```
ul#example {}
div.error {}
```

**Recommended**:
#example {}
.error {}

## 7.8 Shorthand Properties
CSS offers a variety of shorthand properties (like font) that should be used whenever possible, even in cases where only one value is explicitly set.
Using shorthand properties is useful for code efficiency and understandability.

**Not recommended**:
```
border-top-style: none;
font-family: palatino, georgia, serif;
font-size: 100%;
line-height: 1.6;
padding-bottom: 2em;
padding-left: 1em;
padding-right: 1em;
padding-top: 0;
```

**Recommended**:
```
border-top: 0;
font: 100%/1.6 palatino, georgia, serif;
padding: 0 1em 2em;
```

## 7.9 0 and Units
Do not use units after 0 values unless they are required.
```
margin: 0;
padding: 0;
```

## 7.10 Leading 0s
Do not put 0s in front of values or lengths between -1 and 1.
```
font-size: .8em;

```
## 7.11 Hexadecimal Notation
For colour values that permit it, 3 character hexadecimal notation is shorter and more succinct.

**Not recommended**:
```
color: #eebbcc;
```

**Recommended**:
```
color: #ebc;
```

## 7.12 Prefixes
Prefix selectors with an application-specific prefix (optional).
In large projects as well as for code that gets embedded in other projects or on external sites use prefixes (as namespaces) for ID and class names. Use short, unique identifiers followed by a dash.
Using namespaces helps preventing naming conflicts and can make maintenance easier, for example in search and replace operations.
```
.adw-help {} /* AdWords */
#maia-note {} /* Maia */
```

## 7.13 Class Name Delimiters
Separate words in ID and class names by a hyphen.
Do not concatenate words and abbreviations in selectors by any characters (including none at all) other than hyphens, in order to improve understanding and scannability.

**Not recommended** (does not separate the words "demo" and "image"):
```
.demoimage {
}
```

**Not recommended** (uses underscore instead of hyphen):

```
.error_status {
}

```
**Recommended**:
```
#video-id {
}
.ads-sample {
}
```


## 7.14 !important
The use of **!important** is discouraged, instead should apply cascading order to override rules.  Refer to <http://www.w3.org/TR/2011/REC-CSS2-20110607/cascade.html#cascade> for the full specification. 
In general, more specific rules override more general ones.  Specificity is defined based on how many IDs, classes, and element names are involved, as well as whether the **!important** declaration was used.  When multiple rules of the same "specificity level" exist, whichever one appears last wins.

## 7.15 Hacks
It's tempting to address styling differences over user agent detection or special CSS filters, workarounds, and hacks. Both approaches should be considered last resort in order to achieve and maintain an efficient and manageable code base. Put another way, giving detection and hacks a free pass will hurt projects in the long run as projects tend to take the way of least resistance. That is, allowing and making it easy to use detection and hacks means using detection and hacks more frequently---and more frequently is too frequently.

## 7.16 Code formatting
### 7.16.1 Indentations
Set the indentation to be 4 spaces. Make sure tab is replaced with spaces.
```
.example {
    color: blue;
}
```

### 7.16.2 Curly Braces
Always start your curly braces on the same line as the selector. For example:
```
.a-class-name {
    color: #fff
}
```