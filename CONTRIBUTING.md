# Contributing

Thanks for helping people learn by adding problems and solutions.

## Ways to contribute

- Add a **new problem** that is not already in `problems/`
- Add a **solution** in a language that is missing
- Improve an existing solution with a clearer explanation or a better approach
- Fix a typo or an incorrect example

## Add a solution

1. Fork this repo and create a branch.
2. Open the problem folder, for example `problems/0001-two-sum/`.
3. Create a language folder if it does not exist:
   - `python/`
   - `javascript/`
   - `java/`
   - `cpp/`
   - `csharp/`
   - `go/`
   - `typescript/`
4. Add your file as `solution.<ext>`.
5. Put a short comment at the top with time and space complexity.
6. Open a pull request.

Example:

```text
problems/0001-two-sum/python/solution.py
problems/0001-two-sum/javascript/solution.js
```

## Add a new problem

1. Copy `templates/PROBLEM.md`.
2. Create a folder using this name:

```text
problems/<4-digit-number>-<kebab-case-title>/
```

Examples: `0001-two-sum`, `0020-valid-parentheses`.

3. Add a `README.md` with:
   - Title and difficulty
   - Problem statement in your own words
   - Examples
   - Constraints
   - A short hint, not a full walkthrough
4. You may add one starter solution, or leave it open for others.

## Solution guidelines

- Write original code. Do not paste from LeetCode, paid courses, or other repos.
- Keep the code easy to read. Prefer a clear approach over a clever one-liner.
- Include a brief complexity note.
- Do not include secrets, personal data, or generated dumps.
- One approach per file is enough. If you have another approach, add `solution-two-pointers.py` or similar.

## Pull request checklist

- [ ] Folder and file names follow the pattern above
- [ ] Problem text is original, not copied from LeetCode
- [ ] Solution runs against the examples in the problem README
- [ ] Complexity is mentioned in a comment
