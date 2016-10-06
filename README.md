Тестировалось на версии Python 3.4.3+, MySQL 5.6.31-0ubuntu0.15.10.1 

school.py -- основной файл,
funcs.py, methods.py -- вспомогательные модули,
fillingDB.py -- создает и заполняет БД school,
dropDB.py -- удаляет БД school.

check.sh -- скрипт проверки запросов.
\n

Параметры запуска:
    ./school.py get_tutors_list
    ./school.py get_pupils_list <класс>
    ./school.py get_class_stat <класс> <id преподавателя>
    ./school.py get_pupil_disciplines <id ученика>
    ./school.py get_pupil_stat_list <id ученика>
    ./school.py get_pupil_stat <предмет> <id ученика>
    ./school.py set_pupil_point <предмет> <отметка> <id ученика> <id преподавателя>
    

БД школы school состоит из 4-x таблиц:
1. Teachers -- состоит из 3-x столбцов:
    1.1. pkid -- уникальный номер строки (INT PRIMARY KEY),
    1.2. id_teach -- номер учителя, совпадает с pkid, нужно для унификации
         процесса заполнения БД, (INT)
    1.3. name -- имя учителя. (TEXT)
2. Pupils -- состоит из 4-x столбцов:
    2.1. pkid -- уникальный номер строки (INT PRIMARY KEY),
    2.2. id_pup -- номер учителя, совпадает с pkid, нужно для унификации
         процесса заполнения БД, (INT)
    2.3. name -- имя ученика, (TEXT)
    2.4. class -- класс ученика. (TEXT)
3. Teaching -- содержит информацию о процессе обучения учителем,
    состоит из 4-х столбцов:
    3.1. pkid -- уникальный номер строки (INT PRIMARY KEY),
    3.2. id_teach -- номер учителя, совпадает с pkid, нужно для унификации
         процесса заполнения БД, (INT)
    3.3. class -- класс, у которого ведет учитель (TEXT)
    3.4. subject -- предмет, который ведет учитель (TEXT)
4. Getting -- содержит информацию о процессе обучения учеником,
    состоит их 4-х столбцов:
    4.1. pkid -- уникальный номер строки (INT PRIMARY KEY),
    4.2. id_pup -- номер ученика (INT),
    4.3. subject -- предмет, который осваивает ученик (TEXT),
    4.4. marks -- оценки ученика по предмету (TEXT)
Заполнение БД происходит из файлов teachERS.csv, pupils.csv, teachING.csv, getting.csv.