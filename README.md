# CI/CD Beginner Demo

This repository demonstrates a **beginner-friendly CI/CD pipeline** using **GitHub Actions**. It is designed for someone who has **never built a CI/CD pipeline before** and serves as **work proof** for learning, interviews, and audits.

---

## What This Project Does (In Simple Terms)
When you make a code change and push it to GitHub:
1. GitHub automatically starts a pipeline
2. The pipeline installs required tools
3. Automated tests are executed
4. If tests pass → deployment step runs
5. If tests fail → deployment is blocked

This automation is called **CI/CD (Continuous Integration / Continuous Deployment)**.

---

## Repository Structure

```
ci-cd-beginner-demo/
│
├── app.py                 # Simple application code
├── test_app.py            # Automated test for the app
├── README.md              # Project documentation (this file)
└── .github/
    └── workflows/
        └── ci.yml         # CI/CD pipeline definition
```

---

## Tools Used
- **GitHub** – Source control
- **GitHub Actions** – CI/CD automation
- **Python 3.10** – Sample application language
- **Pytest** – Test framework

All tools are **free** and **industry-standard**.

---

## Application Code

`app.py` contains a very small function:

```python
def add(a, b):
    return a + b
```

This keeps the focus on learning CI/CD, not application complexity.

---

## Automated Test

`test_app.py` validates that the application works correctly:

```python
from app import add

def test_add():
    assert add(2, 3) == 5
```

If this test fails, the pipeline will fail.

---

## CI/CD Pipeline Explanation

The pipeline is defined in:

```
.github/workflows/ci.yml
```

### Pipeline Triggers
The pipeline runs automatically when:
- Code is pushed to the `main` branch
- A pull request is created

---

### Pipeline Jobs

#### 1. Build and Test Job
This job:
- Checks out the code
- Sets up Python
- Installs dependencies
- Runs automated tests

If **any test fails**, the pipeline stops.

#### 2. Deploy Job
This job:
- Runs **only if tests pass**
- Simulates deployment

```yaml
needs: build-and-test
```

This line enforces quality gates.

---

## How to Prove the Pipeline Works

### Test Failure Proof
1. Change `app.py` to return incorrect results
2. Commit and push
3. Pipeline fails ❌

### Test Success Proof
1. Fix the code
2. Commit and push
3. Pipeline passes ✅

These runs provide **real CI/CD work evidence**.

---

## What This Demonstrates

- Source control usage (GitHub)
- CI pipeline automation
- Automated test execution
- Failure prevention
- Deployment sequencing
- YAML-based pipeline configuration

This is **hands-on CI/CD experience**, not theory.

---

## Who This Is For

- Beginners learning CI/CD
- QA engineers moving into DevOps
- Interview preparation
- CI/CD work proof demonstrations

---

## Next Enhancements (Optional)

- Add test reports
- Add manual approval before deployment
- Add security scanning
- Convert pipeline to Azure DevOps or Jenkins

---

✅ **This repository is intentionally simple to focus on CI/CD fundamentals.**
