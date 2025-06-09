# 🔢 Integer to Roman Numeral Converter 

This Python script converts a given integer to its **Roman numeral** representation using a **greedy subtraction-based approach**.

---

## 📘 Problem Statement

Given an integer `n` (1 ≤ n ≤ 3999), convert it to a Roman numeral.

### Roman Numerals:
| Symbol | Value |
|--------|-------|
| I      | 1     |
| IV     | 4     |
| V      | 5     |
| IX     | 9     |
| X      | 10    |
| XL     | 40    |
| L      | 50    |
| XC     | 90    |
| C      | 100   |
| CD     | 400   |
| D      | 500   |
| CM     | 900   |
| M      | 1000  |

---

## 🧠 Approach

- A dictionary `rm` maps Roman numeral symbols to their integer values.
- The function performs **greedy subtraction**:
  - Start from the largest possible numeral (`M`, `CM`, `D`, etc.)
  - Repeatedly subtract and append Roman symbols to the result string.
