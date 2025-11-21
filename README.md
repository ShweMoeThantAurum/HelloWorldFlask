# Hello World Flask on AWS Elastic Beanstalk

A minimal, production-ready Flask “Hello World” application fully automated with **GitHub Actions CI/CD** and deployed on **AWS Elastic Beanstalk**.

---

## Overview

This project demonstrates a **real-world Flask deployment setup** with proper CI/CD automation, version control, and GitHub Actions workflows already configured for you.

---

## Features

- Minimal Flask app (`application.py`)
- Deployment-ready using **Gunicorn**
- Fully automated **CI + CD**
- Three GitHub Actions workflows:
  - `ci.yml` – linting (flake8) + tests (pytest)
  - `cd.yml` – single-stage deploy (legacy)
  - `deploy.yml` – **two-stage Build → Deploy pipeline**

---

## Project Structure

```bash
.
├── application.py          ← Main Flask app (must be named this for EB)
├── requirements.txt        ← Production dependencies only
├── Procfile                ← Tells EB how to run the app
├── tests/                  ← Pytest unit tests
├── .github/
│   └── workflows/
│       ├── ci.yml          ← Lint + test
│       ├── cd.yml          ← Simple deploy (legacy)
│       └── deploy.yml      ← Main 2-stage pipeline
└── README.md
