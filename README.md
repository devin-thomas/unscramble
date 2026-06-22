# Unscramble Computer Science Problems

This repository contains a submission-ready solution for the Udacity Data Structures and Algorithms Nanodegree project "Unscramble Computer Science Problems." The project analyzes a small September 2016 phone and text dataset across five standalone Python tasks and documents the runtime complexity of each approach.

## Project Structure

- `Task0.py` prints the first text record and the last call record.
- `Task1.py` counts distinct telephone numbers across both datasets.
- `Task2.py` finds the number that spent the most time on calls.
- `Task3.py` extracts Bangalore call codes and calculates the Bangalore-to-Bangalore call percentage.
- `Task4.py` identifies numbers that could be telemarketers.
- `Analysis.md` explains the worst-case Big-O runtime for each solution.
- `texts.csv` and `calls.csv` are the provided datasets required by the task scripts.
- `docs/index.html` is a lightweight project page for GitHub Pages.

## Setup

This project targets Python 3 and does not require third-party dependencies.

```powershell
python Task0.py
python Task1.py
python Task2.py
python Task3.py
python Task4.py
```

Run each command from the repository root so the scripts can load `texts.csv` and `calls.csv`.

## Implementation Notes

Each task is intentionally self-contained because the Udacity project expects six separate submission files. The solutions favor simple loops, conditionals, and list-based tracking so the logic is easy to review against the assignment requirements.

The runtime analysis in `Analysis.md` reflects the implemented list-based approach rather than an optimized dictionary or set solution. That tradeoff keeps the code close to the learning goals of the introductory project while still producing correct results.

## Verification

The scripts were verified locally by executing all five task files against the supplied CSV data and checking that each printed only the required output. A small CI workflow is included to repeat that verification on GitHub.

## Submission Deliverable

The expected submission archive is `submit.zip` containing only:

- `Task0.py`
- `Task1.py`
- `Task2.py`
- `Task3.py`
- `Task4.py`
- `Analysis.md`

The archive itself is ignored in version control to avoid duplicating tracked source files.
