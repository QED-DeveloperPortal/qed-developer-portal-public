---
title: Source code summarisation with large language models
author: jeny-amatya-qed
categories: [Public]
classification: Unofficial (Everyone)
tags: [ai]
date: 2024-08-02 00:53:16 
updatedBy: Joyclyn
updated: 2024-08-02 01:42:39 
likes: 0
---

# Source code summarisation with large language models

The recent paper "[Source Code Summarization in the Era of Large Language Models](https://arxiv.org/pdf/2407.07959)" provides valuable insights into optimising large language models (LLMs) for generating code summaries. Here's a detailed overview:

## Key insights

### 1. Evaluation accuracy
Automated evaluations using GPT-4 show high alignment with human assessments, suggesting reliable performance metrics, compared to other LLMs included in the experimental study such as CodeLlama-Instruct , StarChat-β and GPT-3.5.

### 2. Effective prompting techniques
Five techniques were tested:
- **Zero-shot:** Generating summaries without any examples.
- **Few-shot:** Providing a few examples to guide the model.
- **Chain-of-thought:** Breaking down the problem into smaller steps.
- **Critique:** Asking the model to critique and improve its summaries.
- **Expert:** Simulating expert-level input and guidance.

Surprisingly, simple zero-shot prompting often yielded comparable results to more complex methods, indicating that straightforward approaches can be highly effective.

### 3. Optimal model settings
The study explored the impact of top_p and temperature settings on summary quality. Adjusting these parameters can enhance performance, though their effects vary by model and language. This customisation can fine-tune results for specific needs. As part of the study, the temperature was set to 0.1 to minimise the randomness of the LLM's responses, except for RQ3.

### 4. Language-specific performance
LLMs exhibit varying proficiency across programming languages, with particular difficulty in logic programming languages. Awareness of these limitations is crucial for setting realistic expectations and focusing improvement efforts.

### 5. Model comparisons
CodeLlama-Instruct (7 billion parameters) outperformed GPT-4 in producing detailed and accurate code summaries. This highlights the potential of specialised models tailored for code-related tasks.

## Categories of code summaries
The study classified the code summaries into six categories.
### 1. What 
Describes the functionality of the code snippet. Helps the developers to understand the main functionality of the code without diving into implementation details.

### 2. Why
Explains the reason why the code snippet is written or the design rationale of the code snippet.

### 3. How-it-is-done
Describes the implementation details of the code snippet, which is critical for developers, especially if the code complexity is high.

### 4. Property
Asserts properties of the code snippet, e.g. function's pre-conditions or post-conditions.

### 5. How-to-use
Describes the expected set-up of using the code snippet, such as platforms and compatible versions.

### 6. Others
Comments that do not fall under the above categories.

## Study Findings

- GPT-4 aligns well with human evaluations.
- Zero-shot prompting is often sufficient.
- Parameter tuning is essential for optimal performance.
- Specialised models like CodeLlama-Instruct excel in detail and accuracy.
- Logic programming languages remain challenging.

## Practical applications

These findings are instrumental for developers and researchers aiming to leverage LLMs for code summarisation. Here’s how you can apply these insights:

- **Choose the right prompting technique:** Start with simple zero-shot prompting for efficient results, and experiment with other techniques as needed.
- **Adjust model settings:** Fine-tune top_p and temperature settings based on the programming language and specific requirements to optimise summary quality.
- **Select appropriate models:** Consider using specialised models like CodeLlama-Instruct for more detailed and accurate summaries.

## Conclusion
As LLM technology evolves, its application in source code summarisation will become increasingly sophisticated. By understanding and applying these insights, developers can enhance their code understanding and maintenance processes significantly.

For an in-depth understanding, access the full paper [here](https://arxiv.org/pdf/2407.07959).