# Uat Coverage

Requirement coverage and acceptance-test readiness checks.

Requirement IDs are matched to passed, failed or pending scenarios. The result separates missing coverage, incomplete acceptance and orphaned scenarios.

## Run

Python 3.11 or newer; no external packages.

```sh
python main.py
python -m unittest discover -s tests -v
```

The module exposes its calculation as an importable function and includes a runnable example.
