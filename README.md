# Demo of pytest lack of before and after feature hook. 

There is no `pytest.fixture(scope="")` that runs just inbetween features when using `scenarios('features')`. See [conftest.py](/steps/conftest.py#L43) then run.

## Install

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Run

```bash
pytest --gherkin-terminal-reporter -vvs
```
