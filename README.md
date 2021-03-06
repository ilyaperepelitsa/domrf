# Тестовое задание дом.рф
Илья Перепелица

## Результаты
Файлы data.csv и scrapy_data.csv доступны для использования - таблицы
совпадают по количеству рядов.
Отличие - scrapy файл - на базе SQL с допущением NULL при отсутствии значений.
Различия в конкретных ячейках не тестировались.

Scrapy в этой среде запускается раз в 12 часов. Чтобы не ждать первого запуска
долго - можете ввести следующую команду в терминале (после запуска
docker-compose up):

curl http://0.0.0.0:6801/schedule.json -d project=domrf_scrapy -d
spider=domrf_spider

## Структура данных:
* developer_group_id - ID Девелопера (источник - API)
* developer_group_name - наименование девелопера
* developer_group_address - адрес девелопера
* region_id - ID региона (источник - API). 1 - Итого, по всем регионам.
Остальные - регионы
* region_name - название региона. Значение "Итого" - по всем регионам.
Остальные - наименования регионов.
* startDate - начало отчетного периода. Даты отчета используются как ключи для
идентификации новых данных. При появлении новых дат приложение добавит новые
данные для построения временных рядов с расчетом на то, что данные дом.рф будут
меняться со временем.
* endDate - конец отчетного периода
* total_living_floor_size - площадь строящегося жилья, м²
* appt_num - количество строящихся квартир
* object_count - количество строящихся домов
* total_living_floor_size_pct - доля застройщика в регионе
* typed_volume_pct - доля типового жилья в общем объеме строительства
* rating - место в общероссийском/региональном рейтинге групп компаний

## Структура репозитория:
* data.csv - файл с выгрузкой через скрипт test_api.py
* data_missing.csv - неотсортированный (есть дубликаты) список девелоперов по
которым нет данных
* scrapy_data.csv - идентичный файл-выгрузка с использованием scrapy и sqlite
* docker-compose.yml - докер файл для деплоймента полного scrapy приложения
* domrf_scrapy - scrapy приложение

## Описание

Финальный оптимизированный код - в docker-compose.yml. Использовано приложение
на базе докер контейнера, состоящее из
* scrapy приложения
* postgresql
* tor
* cron (для управления scrapy приложением, запускает раз в 12 часов)


## Deployment
Перейдите в директорию с файлом docker-compose.yml и введите:
docker-compose up

## PostgreSQL queries
Контейнер Postgres будет доступен под localhost:5432, база данных: domrf_test,
имя пользователя: vtbuser, пароль: example


## Обоснование Scrapy + PostgreSQL

* Скрипт на базе Python requests занимал несколько часов
* Второй bottleneck - в pandas .read_csv и .write_csv - SQL гораздо быстрее
* Scrapy на базе SQLite занимает 15 минут для перебора 16 тысяч API запросов
* Scrapy на базе PostgreSQL в docker занимает 10 минут + серверные базы данных
(а не файловые как SQLite) больше подходят для производственной среды
* Для уменьшения рисков блокирования по IP осуществляется переадресация через
TOR

## Отказ от браузерного скрейпинга

Дом.рф не закрыли API адреса для внешних запросов. Внутренние запросы сайта к
своей базе данных обнаружили адреса, через которые возможно отгружать ту же
информацию, которую выводит интерфейс сайта.
