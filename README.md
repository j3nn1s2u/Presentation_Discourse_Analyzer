# Presentation Discourse Analyzer (PDA)

The **Presentation Discourse Analyzer (PDA)** is a lightweight rule-based system designed to help teachers and students evaluate the structural integrity of student presentations. This project began as a personal experiment to explore how Natural Language Processing (NLP) techniques could support classroom feedback without relying on machine learning.

## Project Motivation

I don’t come from a computer science or NLP background. But after completing a simpler tool called **GradePredictor**, I wanted to build something more relevant to language teaching — something that could provide real feedback on student content.

I often say: *"If I want to make a cake, I need to know what a cake looks like."* This project was my first attempt at baking one.

I used large language models like GPT as scaffolding — to understand programming concepts, debug errors, and explore best practices. Every implementation decision was ultimately mine, shaped by my growing understanding of NLP logic and design. My goal is to gradually polish my skills while building something useful.

## System Evolution

| Version | Core Function                   | Techniques                                      | Purpose                                            |
| ------- | ------------------------------- | ----------------------------------------------- | -------------------------------------------------- |
| V1      | Paragraph classifier            | Rule-based keyword matching                     | Identify presentation structure                    |
| V2      | Structural completeness checker | Batch processing, directory I/O                 | Detect missing parts and prepare for classroom use |
| V3      | Full-scale batch analyzer       | Template-based suggestions, basic visualization | Support feedback, comparison, and reflection       |

Each version builds on the previous, adding practical functionality while keeping the system transparent and easy to maintain. I deliberately avoided ML, TF-IDF, or syntax parsing to keep the logic explainable for education.

## V1 Overview

* Preprocess and split text into paragraphs
* Label each paragraph with one of six categories:

  * Opening
  * Background
  * Research & Value Creation
  * Marketing 4Ps Analysis
  * Action Ideas
  * Closing
* Output results as a JSON file

## V2 Upgrades

* Added `batch_run.py` for batch processing multiple student reports
* Organized inputs/outputs using folder structure (`/data_cleaned/` ➝ `/output/`)
* Modular design improves maintainability and scaling
* Still fully rule-based — no machine learning, keeping it interpretable

## V3 (In Progress)

The next version will:

* Strengthen batch processing logic
* Add checks for structural completeness (e.g., missing conclusion)
* Provide template-based suggestions for improvement
* Generate simple visual summaries (e.g., bar charts in Markdown)

This tool is designed for **human-in-the-loop** use: the system assists, but final judgments come from instructors. Presentation structures vary depending on class goals, and PDA is meant to support — not replace — professional expertise.

## Use Cases

* As a **feedback assistant** for instructors reviewing multiple student presentations
* As a **reflection tool** for students to self-check structure
* As a **starting point** for educators or researchers exploring NLP in teaching

## Technical Details

* Language: Python
* Libraries: `nltk`, `spacy`
* No machine learning
* Designed for terminal use (CLI only)

---

This project is part of my application for the University of Stuttgart's Computational Linguistics program. It represents both my curiosity and my growth — not just as a student of NLP, but as someone bridging language education and practical programming.
