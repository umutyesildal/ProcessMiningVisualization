# Research Paper: Event Type Distribution Over Time

## Overview

This directory contains a 10-page research paper for the **Informatik** field, focusing on **Task 10: Event type distribution over time axis**. The paper presents an interactive dashboard using violin charts for process mining analysis.

## Paper Details

- **Title:** Visualizing Event Type Distributions Over Time: Interactive Violin Charts for Process Mining Analysis
- **Field:** Informatik (Computer Science)
- **Supervisor:** Prof. Dr. Jan Mendling
- **Task:** Task 10 - Event type distribution over time axis
- **Target Length:** 10 pages
- **Format:** Academic paper (not thesis)

## File Structure

```
paper/
├── main.tex              # Main LaTeX document (ready for Overleaf)
├── references.bib        # Bibliography file with relevant citations
├── figures/              # Directory for figures and images
└── README.md            # This file
```

## How to Use with Overleaf

1. **Upload to Overleaf:**
   - Create a new project in Overleaf
   - Upload `main.tex` and `references.bib`
   - Create a `figures/` folder if you plan to add images

2. **Compile:**
   - The document uses standard LaTeX packages
   - Compile with pdfLaTeX
   - Bibliography is handled with BibTeX

3. **Required Packages:**
   All required packages are included in the preamble:
   - `inputenc`, `babel` for encoding and language
   - `amsmath`, `amsfonts`, `amssymb` for mathematics
   - `graphicx` for figures
   - `booktabs` for tables
   - `hyperref` for links and references
   - `cite` for citations
   - `geometry` for page layout
   - `listings` for code snippets
   - `xcolor` for colors

## Paper Structure

The research paper follows the exact required structure:

1. **Introduction** - Background, motivation, and contributions
2. **Research Problem and Requirements** - Problem definition and system requirements
3. **Design and Implementation** - Technical approach, architecture, and algorithms
4. **Evaluation and Discussion** - Results, analysis, and validation
5. **Conclusion** - Summary, contributions, and future work
6. **References** - Bibliography

## Key Features

- **Research Paper Format:** Simple 10-page research paper (not thesis)
- **No Abstract:** Follows standard research paper structure without abstract
- **Complete Bibliography:** Relevant references included
- **Ready for Overleaf:** No additional setup required

## Content Highlights

- Interactive visualization using violin charts
- Smart filtering algorithm for event logs
- Cross-domain evaluation (healthcare, finance, government)
- Multiple time transformation methods
- Statistical sorting capabilities
- Performance analysis and scalability

## Usage Notes

- The paper is self-contained and ready for submission
- Figures can be added to the `figures/` directory
- Bibliography can be extended with additional references
- Code listings are properly formatted with syntax highlighting
- All citations are properly linked

## Compilation Commands

If compiling locally:
```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

For Overleaf, simply click "Recompile" - it handles the bibliography automatically.
