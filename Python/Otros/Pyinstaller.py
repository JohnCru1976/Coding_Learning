# pyinstaller

pyinstaller --clean --onefile --windowed --add-binary "./Day10-Pygame/files;files" --add-binary "./Day10-Pygame/freeSansBold.ttf;freeSansBold.ttf" --add-binary "./Day10-Pygame/todo-b8bdc-firebase-adminsdk-jryak-dcaab7f0ff.json;todo-b8bdc-firebase-adminsdk-jryak-dcaab7f0ff.json" ./Day10-Pygame/main.py

pyinstaller --clean --onefile --windowed --add-binary "files;files" --add-binary "freeSansBold.ttf;freeSansBold.ttf" --add-binary "key.json;key.json" main.py