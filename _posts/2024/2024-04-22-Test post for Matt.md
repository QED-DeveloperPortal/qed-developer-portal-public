---
title: Test post for Matt
author: Joyclyn
categories: [Public]
tags: [test]
date: 2024-04-22 00:34:41 
likes: 0
---

# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
 Paragraph 

**Bold text**

*Italic text*

<span style="color: #4bbce5">Coloured text</span>

~~Strikethrough~~

Horizontal line:

***

> Quoted text

* Dot points
* Dot points
* Dot points

1. Numbered list
2. Numbered list
3. Numbered list

* [ ] Checkbox 

How to get more than one space between lines?

| Row |Title  |Text  |
| --- | --- | --- |
| Row | 1 |data  |
| Row | 2 |data  |
| Row | 3 |data  |

[Hyperlink to Queensland Government site](https://www.qld.gov.au/)

`Inline code`

```
Code block 
Code block
Code block
```

| Table|with  |dot points  |
| --- | --- | --- |
| Row 1 | Column 2 | * Dot point 1 <br> * Dot point 2 <br> * Dot point 3  |
| Row | 2 |data  |
| Row | 3 |data  |


## Block tags
Block tags are typically used inside \<remarks> and \<example> sections to add structure to the text:

**Tag**: \<para\>
Enables adding of structure to the text. Used inside a tag such as \<summary>, \<remains>, or \<returns>.

|Rule | Acceptable | 
| -- | -- |
| 1. | Follow the standard pattern, as appropriate, when naming namespaces: `<CompanyName>.<ApplicationName \| Technology>.<Top Level Module>.<Bottom Level Module>...`   <br> For example: DET.ApplicationName.BusinessLogic, OneFramework.Web.Forms.  |
| 2. | Separate logical components with full stops.   |
| 3. | Prefix namespaces with a meaningful identifier representing the scope of work (e.g. OneFramework, OneFramework.Web). There should be a clear relationship between the namespace and the folder structure in the solution. |
| 4. | Use plural namespace names where appropriate (e.g. use `System.Collections` rather than `System.Collection`).  Exceptions to this rule are brand names and abbreviations (e.g. use `System.IO` rather than `System.IOs`). |


**Example**

```
<span style="color: #0000FF">public void</span> Update(
  <span style="color: #2B91AF">Guid</span> id,
  <span style="color: #0000FF">string</span> lastName,
  <span style="color: #0000FF">string</span> firstName,
  <span style="color: #2B91AF">DateTime</span> dateOfBirth,
  <span style="color: #2B91AF">Int16</span> yearLevel)
{

}
```


**Example** 
```
<span style="color: #0000FF">private const string</span> ENTITY_NAME = <span style="color: #A31515">"Student"</span>;
<span style="color: #0000FF">internal const</span> Int32 SESSION_TIMEOUT_MINUTES = 60;
<span style="color: #0000FF">public const string</span> MIME_TYPE_TEXT = <span style="color: #A31515">"text/plain"</span>;
<span style="color: #0000FF">public const string</span> MIME_TYPE_HTML = <span style="color: #A31515">"text/html"</span>;
<span style="color: #0000FF">public const string</span> MIME_TYPE_GIF = <span style="color: #A31515">"image/gif"</span>;
<span style="color: #0000FF">public void</span> Create()
{
  <span style="color: #0000FF">const</span> <span style="color: #2B91AF">Int16</span> DEFAULT_YEAR_LEVEL = 1;
  …
}
```


