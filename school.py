#!/usr/bin/python
# -*- coding: utf8 -*-

import string
import MySQLdb
import funcs
from methods import *

"""Класс базы данных школы.

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
    
"""

class SchoolDataBase:            

    get_class_stat  = get_class_stat      # Получить список преподавателей
    set_pupil_point = set_pupil_point     # Поставить оценку по определеннному предмету, 
                                          # от имени определенного преподавателя, определенному ученику
    get_tutors_list = get_tutors_list     # Получить список преподавателей
    get_pupils_list = get_pupils_list     # Получить оценки по всем дисциплинам у заданного ученика
    get_pupil_stat  = get_pupil_stat      # Получить оценки по конкретной дисциплине у заданного ученика
    
    get_pupil_stat_list   = get_pupil_stat_list   # Получить ценки по всем дисциплинам у заданного ученика
    get_pupil_disciplines = get_pupil_disciplines # Получить количество дисциплин у заданного ученика
    
    parser = parser          # Обработчик параметров командной строки
    
    
base = SchoolDataBase()
base.parser()


























