#!/usr/bin/python
# -*- coding: utf8 -*-
import string
import MySQLdb

def insert_from_file(conn, cursor, file_name, nFields,
                     fields_name, table_name):
    """Заполняет БД school из файлов, используется скриптом fillingDB.py.
    
    conn -- подключение к БД,
    cursor -- курсор, управляющий БД MySQL,
    file_name -- имя файла, из которого берутся данные для заполнения,
    nFields -- количество полей в таблице, которую надо заполнить,
    fields_name -- список имен полей, которые нужно заполнить,
    table_name -- имя таблицы.
    
    Каждая таблица устроена так:
    - Номер, соответствующий id ученика/учителя, (1)
    - Остальный записи.
    В таблицах Teachrs и Pupils также, помимо id, есть номер типа (1) (по факту, дублирует id), это сделано
    с целью унификации заполнения БД.
    
    """
    try:
        j = 0;
        fin   = open(file_name, "r")
        lines = fin.readlines()
        
        for line in lines:
            j = j + 1        # Считаем номер извлекаемой строки
            els = line.split(";")
            """Сначала заносим в таблицу номера типа (1)"""
            cursor.execute("INSERT INTO %s (%s)  VALUES ('%d')"
                           % (table_name, fields_name[0], int(els[0])))
            conn.commit()
            
            """Заносим в таблицу другие записи"""
            for i in range(1, nFields):                
                els = line.split(";")
                
                cursor.execute("UPDATE %s SET %s='%s' WHERE pkid=%d" 
                               % (table_name, fields_name[i], els[i], j))
                conn.commit()
                
    except EOFError as e:
        fin.close()
        print(e)
        
    except Exception as e:
        print(e)
        
    else:
        fin.close()


def filling_db():
    """Создает и заполняет БД.
    Описание БД в README.md или school.py
    Заполнение происходит из файлов teachERS.csv, pupils.csv, teachING.csv, getting.csv.
    """
    try:
        conn   = MySQLdb.connect(host="localhost", user="root", passwd="", db="mysql", charset = "utf8")
        cursor = conn.cursor()
        cursor.execute('CREATE DATABASE `school`;')
        
        cursor.execute('USE `school`')
            
        cursor.execute("ALTER DATABASE `school` CHARACTER SET 'utf8' COLLATE 'utf8_unicode_ci'")

        cursor.execute('CREATE TABLE Teachers (pkid INT AUTO_INCREMENT, id_teach INT, name    TEXT,                PRIMARY KEY (pkid))')
        cursor.execute('CREATE TABLE Pupils   (pkid INT AUTO_INCREMENT, id_pup   INT, name    TEXT, class   TEXT,  PRIMARY KEY (pkid))')
        cursor.execute('CREATE TABLE Teaching (pkid INT AUTO_INCREMENT, id_teach INT, class   TEXT, subject TEXT,  PRIMARY KEY (pkid))')
        cursor.execute('CREATE TABLE Getting  (pkid INT AUTO_INCREMENT, id_pup   INT, subject TEXT, marks   TEXT,  PRIMARY KEY (pkid))')          

        fields_names = 'id_teach', 'name'
        insert_from_file(conn, cursor, "teachERS.csv", 2, fields_names, 'Teachers')
            
        fields_names = 'id_pup', 'name', 'class' 
        insert_from_file(conn, cursor, "pupils.csv",   3, fields_names, 'Pupils')
            
        fields_names = 'id_teach', 'class', 'subject' 
        insert_from_file(conn, cursor, "teachING.csv", 3, fields_names, 'Teaching') 
            
        fields_names = 'id_pup', 'subject', 'marks' 
        insert_from_file(conn, cursor, "getting.csv",  3, fields_names, 'Getting')   
        
        print ('db created')
            
    except MySQLdb.Error as e:
        print(e)
            
    finally:
        conn.close()

filling_db()            