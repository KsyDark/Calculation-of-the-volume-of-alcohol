:: Запускает комплицию проекта с помощью pyinstaller
pyinstaller --onefile --noconsole --icon=alc.ico "Расчёт объёма спирта.py"
cd dist
start "Расчёт" "Расчёт объёма спирта.exe"