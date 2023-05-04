### Hexlet tests and linter status:
[![Actions Status](https://github.com/TarakanovAndrey/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/TarakanovAndrey/python-project-50/actions)  

[![Python CI](https://github.com/TarakanovAndrey/python-project-50/actions/workflows/tarakanov-check.yml/badge.svg)](https://github.com/TarakanovAndrey/python-project-50/actions/workflows/tarakanov-check.yml)  

<a href="https://codeclimate.com/github/TarakanovAndrey/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/16787555bd5efca240e9/maintainability" /></a>  

[![Test Coverage](https://api.codeclimate.com/v1/badges/16787555bd5efca240e9/test_coverage)](https://codeclimate.com/github/TarakanovAndrey/python-project-50/test_coverage)  

## Описание проекта  
"Вычислитель отличий" - это программа, определяющая разницу между двумя структурами данных.
Поддерживает входные форматы yaml и json. Генерирует отчеты в виде plain text, stylish и json
(примеры выводов в аскинемах ниже).  
По умолчанию отчет генерируется в виде stylish. Пример вызова:  
```
gendiff path1/file1.json path2/file2.json  
```
Для генерации отчета в виде plain text необходимо явно указать параметр plain. Пример вызова:  
```
gendiff --format plain path1/file1.json path2/file2.json  
```
Для генерации отчета в виде json необходимо явно указать параметр json. Пример вызова: 
```
gendiff --format json path1/file1.json path2/file2.json  
```

## Установка программы  
В командоной строке введите:
```
pip install git+https://github.com/TarakanovAndrey/python-project-50.git
```

## Примеры работы программы с разными форматами и генерация отчетов в форматах stylish, plain text, json.  

### Сравнение двух плоских файлов в формате '.json'  

[![asciicast](https://asciinema.org/a/XGd8a8OQ9crni2Ky6SE2vxh6D.svg)](https://asciinema.org/a/XGd8a8OQ9crni2Ky6SE2vxh6D)  

### Сравнение двух плоских файлов в формате '.yml', '.yaml'  

[![asciicast](https://asciinema.org/a/lkXGwtCEjuoQpyZjoY5Jgxjyg.svg)](https://asciinema.org/a/lkXGwtCEjuoQpyZjoY5Jgxjyg)  

### Сравнение двух файлов с вложенной структурой в форматах '.json', '.yml', '.yaml'  

[![asciicast](https://asciinema.org/a/7kUlTgQpqZADGP1QWF0AAHDGF.svg)](https://asciinema.org/a/7kUlTgQpqZADGP1QWF0AAHDGF)  

### Сравнение двух файлов с вложенной структурой в форматах '.json', '.yml', '.yaml' и вывод в формате plain  

[![asciicast](https://asciinema.org/a/a2yvELdxFr5hd9YNLqW7cM8Hv.svg)](https://asciinema.org/a/a2yvELdxFr5hd9YNLqW7cM8Hv)  

### Сравнение двух файлов с вложенной структурой в форматах '.json', '.yml', '.yaml' и вывод в формате json  

[![asciicast](https://asciinema.org/a/x4rTSrft0iG5R9g5vIc6vbmm4.svg)](https://asciinema.org/a/x4rTSrft0iG5R9g5vIc6vbmm4)