---
title: Pair program with Aider  your AI Assistant
author: andrew
categories: [Public]
classification: Unofficial (Everyone)
tags: [ai,opinion]
date: 2024-08-20 22:07:56 
updatedBy: jeny-amatya-qed
updated: 2024-08-21 03:00:56 
likes: 2
---

There has been much fan fare about the AI revolution and what it means for people who write and maintain software.

As a developer, the question arises as to where to start.

A developer might be tempted by the allure of AI products that can generate systems from scratch.

However, at least for the foreseeable future, developers will spend much more time testing and maintaining existing systems than writing new code.

So what would be really helpful is a tool that can:

```
• generate code from a description
• understand an existing code base
• understand existing documentation 
• gain understanding by being presented documentation via URLs
• modify existing code
• write tests
• fix bugs
• create documentation
• understand a code base
• automatically generate commit messages 
```

**Aider** is such a tool. ([https://aider.chat/](https://aider.chat/))

You drive it from the command line using commands such as
• /code - ask for code to be written
• /ask - ask questions about the codebase
• /add - add files to the current chat context
• /web - scrape a web page and add the content to the chat
• /map - print out the current repository map
• /clear - clear the chat history

An example scenario where it can be used is in updating documentation as shown at the link [https://aider.chat/examples/update-docs.html](https://aider.chat/examples/update-docs.html).

After installing via pip, you can use Aider simply by changing into the directory where a git repo is located, typing **aider** and hitting return.

You can integrate it with just about any LLM and even use a local LLM via Ollama.

There is also an active Discord channel where you can get help and see the types of systems that people have created using Aider.

Interestingly, Aider wrote 56% of the code that made it into it’s latest release that came out today, 21 August 2024.

Looking forward to getting really productive with this tool.

Other tools such as Continue.Dev can provide a similar experience but from inside VS Code - perhaps a post for another day.
