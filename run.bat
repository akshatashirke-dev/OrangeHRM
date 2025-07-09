@echo off
call .venv\Scripts\activate
pytest -v -s -m "regression" --html=reports/report.html --browser chrome
pause