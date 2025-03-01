# 🦮 Commit Guidelines for osaka's ai lab

Standards to maintain a semantic and organized history.

---

## Commit Types

| Type       | Emoji | Description                                        | Example                                     |
| ---------- | ----- | -------------------------------------------------- | ------------------------------------------- |
| `study`    | 📚    | New study content (code, exercise, notebook).      | `study: add pandas data cleaning example`   |
| `add`      | 🆕    | Addition of new files (code, datasets, etc.).      | `add: include housing dataset CSV`          |
| `assets`   | 🖼️    | Images, charts, or multimedia files.               | `assets: add EDA visualization plots`       |
| `docs`     | 📝    | Documentation (README, comments, guides).          | `docs: update README installation steps`    |
| `fix`      | 🐛    | Bug/code/documentation fixes.                      | `fix: resolve index error in data loader`   |
| `refactor` | ♻️    | Code restructuring without changing functionality. | `refactor: simplify training loop`          |
| `style`    | 💄    | Formatting (linting, spacing, line breaks).        | `style: apply PEP8 to data_processing.py`   |
| `chore`    | 🔧    | Configuration or organization changes.             | `chore: reorganize folder structure`        |
| `content`  | 🗂️    | Study materials (notes, slides, summaries).        | `content: add ML glossary notes`            |
| `config`   | ⚙️    | Configuration files (`.env`, YAML, JSON).          | `config: update hyperparameters in YAML`    |
| `temp`     | 🚧    | Temporary commit (e.g., WIP).                      | `temp: draft neural network implementation` |

---

## Commit Message Structure

```
🧠 type(scope): [short desc] [optional body]
```

### Components:

1. **Type**: Required. Defines the change category (e.g., `study`, `add`).
2. **Scope**: Optional. Indicates the module, course, or context (e.g., `kaggle`, `nlp`).
3. **Short Description**: Concise and imperative (e.g., "add", "fix", not "added" or "fixed").
4. **Body**: Technical details or context (optional).

---
