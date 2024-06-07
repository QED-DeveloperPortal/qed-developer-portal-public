---
title: Test and evaluate your custom summarization models
author: matt
categories: [public]
tags: [auto-import,test, ai]
date: 2024-06-04 00:49:53 
likes: 0
imported: true
import-source: Azure Devops
import-reference: 1234
---

## Overview
This document provides elaborate guidelines on testing and evaluating custom summarisation models during creation. It underscores the importance of splitting data for testing and training, with emphasis on size, overlap and diversity of the data. It further delves into methods to evaluate the models, detailing both automatic and manual evaluation methods and what each entails. Automated evaluation employs the ROUGE metric which measures the overlap between computer-generated summaries and 'ideal' human-created summaries. Manual evaluation identifies crucial features such as fluency, coherence, coverage, relevance and the avoidance of unusable data ('hallucinations') in-powered models.

## Key Takeaways

- When splitting data into training and testing sets, ensure the specificity of certain options:
    - Sufficient 'Size' of your test set for adequate confidence in model quality,
    - Attain 'No Overlap' in terms of documents used for both training and testing stages is achieved, not doing so will overestimate the quality result and impose limitations negatively into future application,
    - Check 'Diversity' of the test sets and stretch regularity allowing noticeably different lengths, topics and 
    styles of your units.  

- Final summary serves both Automatic and Manual model evaluation and the prpositions making these models is achieved via
    - Automated evaluation cue is set in a node for overlapping units as evaluated by the computer immitation this is catergorised under [Rouge Guide](https://en.wikipedia.org/wiki/ROUGE_(metric))
    -  Meditate upon this information manuallay and screen such Term extraction for differences calculated in fluency, coherency, coverage,frequency( if right that counts as space competencyRelevance)
    and content similarity Encoding percieved summary identification    
[domain dialog with anything](  https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00373/100686/SummEval-Re-evaluating-Summarization-Evaluation).
