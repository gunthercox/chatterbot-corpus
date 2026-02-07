# Contributing to ChatterBot Corpus

Thank you for your interest in contributing to the ChatterBot Corpus! This project relies on community contributions to provide high-quality, diverse training data for chatbots across multiple languages.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Content Guidelines](#content-guidelines)
- [Getting Started](#getting-started)
- [Submitting Contributions](#submitting-contributions)
- [Style Guide](#style-guide)
- [Legal Requirements](#legal-requirements)

## Code of Conduct

This project adheres to a code of conduct that emphasizes respect, inclusivity, and constructive collaboration. By participating, you are expected to uphold this code. Please be respectful and considerate in all interactions.

## How Can I Contribute?

### Adding New Language Support

We welcome contributions that add support for new languages! To add a new language:

1. Create a new directory under `chatterbot_corpus/data/` with the language name (e.g., `chatterbot_corpus/data/polish/`)
2. Add conversation files in YAML format (`.yml`)
3. Follow the existing structure from other language directories

### Improving Existing Content

You can also help by:

- Adding new conversation topics to existing languages
- Correcting factual errors in existing conversations
- Fixing spelling, grammar, or formatting issues
- Expanding topic coverage within a language
- Improving the natural flow of conversations

### Reporting Issues

If you find errors, inappropriate content, or have suggestions for improvement:

1. Check if an issue already exists
2. Create a new issue with a clear description
3. Tag the issue appropriately (e.g., `bug`, `enhancement`, `content-quality`)

## Content Guidelines

### Factual Correctness

**The corpus aims for factual correctness as best as possible.** All contributions should:

- Provide accurate information when discussing factual topics
- Avoid spreading misinformation or false claims
- Cite or reference verifiable information when appropriate
- Avoid controversial or unverified claims presented as facts

If a conversation includes factual information (dates, scientific facts, historical events, etc.), please verify its accuracy before submitting.

### Quality Content Structure

All contributions must meet high standards for quality:

#### Spelling and Grammar
- Use correct spelling according to the language's standard conventions
- Follow proper grammar rules for the target language
- Proofread your contributions before submitting
- Use appropriate punctuation and capitalization

#### Conversation Flow
- Ensure conversations flow naturally
- Keep responses contextually appropriate
- Maintain consistency within conversation threads
- Avoid non-sequiturs or confusing transitions

#### Organization
- Use clear, descriptive filenames (e.g., `greetings.yml`, `technology.yml`)
- Group related conversations together
- Use appropriate categories in your YAML files
- Follow the existing file structure

## Getting Started

### Setting Up Your Development Environment

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/chatterbot-corpus.git
   cd chatterbot-corpus
   ```
3. **Create a new branch** for your contribution:
   ```bash
   git checkout -b add-language-polish
   ```
   Or for improvements:
   ```bash
   git checkout -b fix-spanish-greetings
   ```

### Creating Corpus Files

All corpus data files use YAML format (`.yml`). Here's the basic structure:

```yaml
categories:
- greetings
- casual

conversations:
- - Hello
  - Hi there!
- - How are you?
  - I'm doing well, thank you! How about you?
- - What's your name?
  - I'm a chatbot. What's your name?
```

#### Structure Explanation:

- `categories`: Tags that categorize the conversation content (1-3 recommended)
- `conversations`: A list of conversation exchanges
- Each conversation is a list of statements that flow sequentially

### File Organization

Place your files in the appropriate directory:

```
chatterbot_corpus/data/
├── english/
│   ├── greetings.yml
│   ├── conversations.yml
│   └── ...
├── spanish/
│   └── ...
└── [your-language]/
    └── [your-topic].yml
```

## Submitting Contributions

### Before Submitting

- [ ] Review your content for **factual accuracy**
- [ ] Check **spelling and grammar**
- [ ] Ensure conversations flow naturally
- [ ] Verify proper YAML formatting
- [ ] Test your YAML files are valid (no syntax errors)
- [ ] Review legal requirements below

### Pull Request Process

1. **Commit your changes** with clear, descriptive messages:
   ```bash
   git add .
   git commit -m "Add Polish language greetings and basic conversations"
   ```

2. **Push to your fork**:
   ```bash
   git push origin add-language-polish
   ```

3. **Create a Pull Request** on GitHub:
   - Provide a clear title describing your contribution
   - Include a detailed description of what you've added or changed
   - Reference any related issues
   - Explain any special considerations or decisions made

4. **Wait for review**: Maintainers will review your PR and may request changes

5. **Address feedback**: Make requested changes and push updates to your branch

6. **Merge**: Once approved, a maintainer will merge your contribution

### Pull Request Title Examples

Good:
- "Add Portuguese language support with greetings and basic conversations"
- "Fix grammar errors in Spanish emotions.yml"
- "Add technology-related conversations to English corpus"

Not ideal:
- "Update files"
- "Changes"
- "Fix stuff"

## Style Guide

### YAML Formatting

- Use 2 spaces for indentation (no tabs)
- Use UTF-8 encoding
- Keep lines under 120 characters when possible
- Use consistent formatting across all files

### Conversation Style

- Keep individual statements concise (1-3 sentences)
- Use natural, conversational language
- Avoid overly formal or robotic responses
- Include appropriate variations in responses
- Consider cultural context for the target language

### Language-Specific Guidelines

- Use the standard dialect for the language unless creating dialect-specific content
- Follow the language's convention for formality (e.g., tú vs. usted in Spanish)
- Include proper diacritical marks and special characters
- Consider regional variations when appropriate

## Legal Requirements

### Copyright and Licensing

**IMPORTANT:** Contributions must not include copyrighted material or anything that legally cannot be included in the corpus.

All contributions must:

- ✅ Be your original work
- ✅ Be freely licensed or in the public domain
- ✅ Not violate any copyright, trademark, or intellectual property rights
- ✅ Not include content copied from books, movies, songs, or other copyrighted sources
- ✅ Be appropriate for public distribution

### What You Can Include

- Original conversations you've written
- Common phrases and idioms that are not copyrighted
- Factual information that is publicly available
- Translations you've created yourself

### What You Cannot Include

- ❌ Dialogue copied from movies, TV shows, or books
- ❌ Song lyrics or poetry (unless in public domain)
- ❌ Content from proprietary sources
- ❌ Copyrighted characters, names, or settings
- ❌ Content that violates someone's privacy
- ❌ Illegal, harmful, or offensive content

### License Agreement

By contributing to this project, you agree that your contributions will be licensed under the same license as the project (see [license.md](license.md)). You certify that you have the right to submit the contribution and that it does not violate any third-party rights.

## Questions?

If you have questions about contributing, please:

1. Check existing issues and pull requests
2. Review this contributing guide thoroughly
3. Open an issue with your question if you can't find an answer

## Recognition

Contributors will be recognized for their valuable additions to the project. Thank you for helping make ChatterBot and it's surrounding software ecosystem better for everyone!

## Additional Resources

- [Project README](readme.md)
- [ChatterBot Documentation](https://docs.chatterbot.us/)
- [YAML Syntax Guide](https://yaml.org/spec/1.2/spec.html)

---

Thank you for contributing to ChatterBot Corpus! Your efforts help create better conversational AI for everyone. 🌟
