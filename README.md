# 🎓 Student Management System (Python OOP & Design Patterns)

A comprehensive, object-oriented Student Management System built in Python. This project demonstrates clean code practices, encapsulation with properties, inheritance, method overriding, dynamic reporting, and optional Factory Design Pattern integration.

---

## 🌟 Key Features

* **Class Hierarchy & Inheritance:** Base `Student` class with specialized `UndergraduateStudent` and `GraduateStudent` subclasses.
* **Encapsulation & Validation:** Private attributes (`__email`, `__marks`) secured using `@property` getters and setters with built-in input validation.
* **Dynamic Student Identification:** Override-enabled `get_student_type()` method for dynamic runtime identification (Polymorphism).
* **Automated Result Calculation:** Evaluates numerical marks and computes letter grades (`A+` to `Fail`).
* **Adaptive Display Output:** Built-in `hasattr()` check in `display_info()` to dynamically print course details (`Semester` vs. `Research Topic`) in a clean UI box.
* **Explicit Parameter Passing:** Robust constructor architecture avoiding fragile `*args` positional mismatches.

---

## 🛠️ System Architecture & Classes

```text
               ┌────────────────────────┐
               │        Student         │ (Base Class)
               ├────────────────────────┤
               │ - name                 │
               │ - id                   │
               │ - __email (Property)   │
               │ - age                  │
               │ - department           │
               │ - __marks (Property)   │
               └───────────┬────────────┘
                           │
             ┌─────────────┴─────────────┐
             │                           │
┌────────────▼────────────┐ ┌────────────▼────────────┐
│  UndergraduateStudent   │ │     GraduateStudent     │
├─────────────────────────┤ ├─────────────────────────┤
│ + semester              │ │ + research              │
└─────────────────────────┘ └─────────────────────────┘
