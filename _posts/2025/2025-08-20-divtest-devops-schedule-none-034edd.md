---
title: "Divtest DevOps Schedule None 1"
slug: "divtest-devops-schedule-none-034edd"
author: Divya
owner: Divya
categories: Public
classification: Public
tags: [auto-import, agile]
date: 2025-08-20 04:34:58
likes: 0
imported: True 
import-source: "azure-devops"
import-reference: ""
import-config-id: "3eeb2c58-6473-45fd-b1b9-f63d05e6c7b0"
---

By David Ramel
05/21/2024

Azure AI Studio is now generally available, emerging from preview on day one of the Microsoft Build 2024 developer conference.

Azure AI Studio serves as a cloud-based platform -- akin to an IDE -- for developing and deploying generative AI applications. Part of Microsoft's overall copilot AI assistant initiative, it's described as a pro-code environment for customizing and configuring generative AI applications with Azure-grade security, privacy and compliance.

The platform offers a mix of visual and code-first tooling, along with pre-built quick-start templates to streamline and accelerate copilot creation using various Azure AI services and tools, including Azure OpenAI Service and Azure AI Search.

Developers can work with a bevy of AI services and models for various use cases, including language, speech, content safety and more. At the heart of the platform is an extensive model catalog providing access to more than 1,600 models from providers such as Meta, Mistral, Microsoft and OpenAI, highlighted by the addition of new small language models (SLMs) in Microsoft's Phi3 family, which are open models as opposed to the more common proprietary approach.

"We are introducing Phi-3-vision, a multimodal model that brings together language and vision capabilities. You can try Phi-3-vision today," Microsoft said in a post today (May 21).

Also in the model catalog is OpenAI's latest/greatest model, GPT-4o (with the "o" standing for omni), which debuted last week and was immediately available in the Azure Playground. It also sports OpenAI's GPT 4 Turbo with Vision, which combines language and vision capabilities.

Azure AI Studio also includes model benchmarks to compare the performance of models across various industry-standard datasets, providing evaluations using metrics such as accuracy, coherence, fluency and GPT similarity. Users can view benchmark results in dashboard graph and list formats, enabling side-by-side model comparisons.

Along with the model catalog is a prompt catalog allowing developers hone their "prompt engineering" skills by browsing prompt samples for common use cases. "Choose a sample prompt to see how it works or as a starting point for your project," the catalog says [link requires Azure account]. "Then customize it for your scenario and evaluate how it performs before integrating into your app."

That's also where the aforementioned playground comes into play.

"Experiment with prompts in the playground," Microsoft said in a May 21 post announcing general availability of Azure AI Studio. "Developers are equipped with a suite of dev-light playgrounds within AI Studio, encompassing areas like chatbots , assistants , image generation , and text completion. This flexible sandbox allows developers to experiment with various models, refine system prompts through iterative testing, and customize models -- securely using their own datasets for tailored results. Developers can also experiment with safety system messages. "
Other features include:

Data retrieval with Azure AI Search: Azure AI Search is now seamlessly integrated within Azure AI Studio for Retrieval-Augmented Generation (RAG) use cases, allowing developers to employ data retrieval techniques to base their responses on secure, customer-specific information.
- Fine tuning: For generative AI applications, developers can use RAG for tasks needing external knowledge and fine-tuning for tasks with specific labeled data. Fine-tuning customizes pre-trained models for specialized tasks within a narrow scope. In Azure AI Studio, users can fine-tune models like Babbage, Davinci, GPT-35-Turbo, GPT-4 in addition to the Llama 3 and Phi-3 families.
- Agent-based orchestration: Developers are increasingly using LLMs and SLMs to create sophisticated applications, leveraging tools like the Azure OpenAI Service Assistants API, function-based apps, and the AutoGen framework to tackle complex, open-ended problems, Microsoft said. This shift introduces new challenges due to the nature of agent-based orchestration.
- Tracing and debugging: Tracing is vital for understanding complex copilot workflows, where traditional IDE breakpoints fall short due to asynchronous operations and streaming data, Microsoft said. Azure AI Studio's tracing feature, accessible through the prompt flow SDK, aids in debugging by tracking latency, LLM errors, token usage, function calls and dependency issues. Developers can use a local playground for comprehensive unit testing, logging traces to Azure AI Studio or a local repository, starting the service from the command line or automatically with trace initiation.

Microsoft also detailed the evaluation process, which includes manual and automated evaluations to assess the accuracy, quality and safety of generated outputs. Manual evaluations are useful for tracking progress on targeted priorities, while automated evaluations measure quality and safety at scale, the company said. Azure AI Studio helps address a common customer blocker -- a lack of high-quality adversarial test data -- by automatically generating adversarial inputs and role-playing attacks to create a test dataset for evaluation.

"To create responsible and truly transformative, customized, production-ready copilots that support advanced use cases, multiple interoperating APIs need to be combined with models, prompts, and grounding data, fine-tuned, tested, and deployed at scale," Microsoft summarized. "To accomplish this, developers need the right tools."

The three-day in-person (Seattle) and online Microsoft Build 2024 developer conference runs through May 23.

About the Author

David Ramel is an editor and writer for Converge360.