@echo off
echo ============================================
echo   E-Commerce Selenium Framework - DEMO RUN
echo ============================================
echo.

echo [1/3] Cleaning old logs...
if exist logs\*.log del /Q logs\*.log
echo      Done.

echo [2/3] Cleaning old screenshots...
if exist screenshots\*.png del /Q screenshots\*.png
echo      Done.

echo [3/3] Cleaning old report...
if exist reports\report.html del /Q reports\report.html
echo      Done.

echo.
echo ============================================
echo  PART 1: The Master End-to-End Journey (PyTest)
echo  1 Browser. 1 Serial Flow. Highly Organized.
echo ============================================
pytest -v
echo.

echo ============================================
echo  PART 2: Running Unittest Suite separately
echo ============================================
python -m unittest tests/unittest_login.py -v
echo.

echo ============================================
echo Report saved at: reports\report.html
echo Open it in your browser to view results.
echo ============================================
pause
