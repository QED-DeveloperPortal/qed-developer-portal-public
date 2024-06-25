---
title: Testing different special characters
author: jeny-amatya-qed
categories: [Public]
tags: [test]
date: 2024-06-25 06:05:31 
likes: 0
---

## Scenario 1

In Markdown, angle brackets < and > are used for embedding HTML tags. If there is no valid HTML tag between < >, it is ignored.
To show < > in Markdown, there are couple of options.
Using HTML entities
Hello \<world>
Using Code Span
Hello `<world>`
Using Backslash escaping
Hello \<world>

## Scenario 2

Asterisk is used to denote emphasis such as italics or bold.
To show \* in Markdown, we can use one of the following
This is a literal asterisk: \*
This is a literal asterisk: `*`
This is a literal asterisk: \*

## Scenario 3

Markdown renders single hyphen as bullets, if used at the beginning of the line.
To show a hyphen in Markdown, we can use of the following
\- Not a list item
`-` Not a list item
You can also try
\-\-\- renders as a horizontal line

* used in a sentence doesn't need special handling
* 

## Scenario 4

Backlash is used as an escape character in Markdown and it tells the Markdown processor to treat the following character as a literal, rather than as a Markdown syntax character.
The screenshot in this scenario shows expected behavior.

* Code
    At the command prompt, type `nano`.
* Escaping backticks
    `` Use `code` in your Markdown file. ``
* Code blocks

```html
    <html>
      <head>
      </head>
    </html>
```