set results=.\results
set rep_history=.\final-report\history
set report=.\final-report

rmdir /s /q %results%
pytest --alluredir=%results%
move %rep_history% %results%
rmdir /s /q %report%
allure generate %results% -o %report%
allure open ".\final-report"
