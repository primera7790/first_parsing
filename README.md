# Парсер информации о БЖУ

## Используемые технологии:
  - Язык программирования: &nbsp; `python` ;
  - Основные библиотеки: &nbsp; `beautifulsoup4` , `requests` , `lxml` .

## Описание:
  
  &nbsp; &nbsp; Парсинг информации о БЖУ с сайта полезного питания.<br>
  &nbsp; &nbsp; Программа собирает данные с сайта о различных продуктах и блюдах.<br>
  &nbsp; &nbsp; Формирует csv-таблицы по категориям. Для каждой позиции указывается содержание белков, жиров, углеводов и общую калорийность.
  <br>
  
  &nbsp; &nbsp; P.S. Также сохраняет страницы с категориями в .html формате и информацию о них в .json формате.

## Инструкция по запуску:
1. Скачать/скопировать данные репозитория;
2. Установить зависимости, указанные в файле `requirements.txt` ;
3. Запустить файл `health_diet_parser.py` .
  
## Нагляднее:

### Данные на сайте:
<p>
  <img width='600px' src='https://github.com/primera7790/health_diet_parser/blob/main/data/images/site.PNG' alt='website_data'/>
</p>

### Процесс исполнения:
<p>
  <img width='400px' src='https://github.com/primera7790/health_diet_parser/blob/main/data/images/work_process.PNG' alt='process'/>
</p>

### Фрагмент одной из результирующих таблиц:
<p>
  <img width='800px' src='https://github.com/primera7790/health_diet_parser/blob/main/data/images/result_table_small.PNG' alt='result_table'/>
</p>
