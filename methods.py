#!/usr/bin/python
# -*- coding: utf8 -*-

import string
from sys import argv
import MySQLdb
import funcs

def get_tutors_list(self):
    """Печатает список имен всех учителей, которые есть в БД."""
    try:
        conn = MySQLdb.connect(host="localhost", user="root", passwd="",
                                db="school", charset = "utf8")
        cursor = conn.cursor()
        cursor.execute('SELECT name FROM Teachers')

        funcs.print_queries(cursor, "В школе нет учителей")
                
    except MySQLdb.Error as e:
        print(e)
        
    finally:
        conn.close()
        
#--------------------------------------------------------------------------------------------------------------------------------------------#	  
  
def get_pupils_list(self, class_name):
    """Печатает список имен всех учеников, которые обучаются
    в классе class_name.
    
    """
    try:
        conn = MySQLdb.connect(host="localhost", user="root", passwd="",
                               db="school", charset = "utf8")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM Pupils " \
                       "WHERE class='%s'" % class_name)
            
        funcs.print_queries(cursor, "В классе нет учеников")
                
    except MySQLdb.Error as e:
        print(e)
        
    finally:
        conn.close()
        
#--------------------------------------------------------------------------------------------------------------------------------------------#	
             
def get_class_stat(self, class_name, teacher_id):
    """Печатает все оценки в классе по всем ученикам, от имени конкретного преподавателя.
    
    class_name -- название класса, в котором смотрятся оценки,
    teacher_id -- id учителя, от чьего имени делается запрос.
    
    """
    try:
        conn = MySQLdb.connect(host="localhost", user="root", passwd="",
                               db="school", charset = "utf8")
        cursor = conn.cursor()
        """Выбираем все предметы, которые ведет учитель с id == teacher_id
        в классе class_name
        """
        cursor.execute("SELECT subject FROM Teaching WHERE class='%s' " \
                       "AND id_teach='%d'" % (class_name, teacher_id))
        subjects = cursor.fetchall()    
        """Выбираем id всех учеников из класса class_name"""
        cursor.execute("SELECT pkid FROM Pupils WHERE class='%s'" % class_name)
        pkids = cursor.fetchall()
        
        """Проверка.
        
        Проверяем, есть ли данные, соответствующие запросам.
        Если нет, то сообщаем об этом и выходим и метода.
        
        """    
        if not (pkids):
            print("В этом классе нет учеников")
            return
        elif not (subjects):
            print("Этот учитель не преподает у данного класса")
            return
        
        """ Для каждого из предметов, которые ведет учитель в классе class_name,
        рассматриваем каждого ученика в классе. Для каждого из этих учеников 
        запрашиваем его оценки и печатаем их.
        """
        for subject in subjects:
            print(subject[0])                    
            
            for pkid in pkids:         
                cursor.execute("SELECT marks FROM Getting WHERE id_pup='%d' " \
                               "AND subject='%s'" % (pkid[0], subject[0]))
                marks = cursor.fetchall()    
                    
                print(" Id ученика", end=": ")
                print(pkid[0], end=" | ")                        
                for mark in marks:
                    print("Оценки", end=": ")
                    print(mark[0])                                                 

    except MySQLdb.Error as e:
        print(e)
        
    finally:
        conn.close()
             
#--------------------------------------------------------------------------------------------------------------------------------------------#	
        
def get_pupil_disciplines(self, pupil_id):
    """Печатает число предметов у заданного ученика (ученик определяется 
    своим id).
    pupil_id -- заданное id ученика.
    """
    try:
        conn = MySQLdb.connect(host="localhost", user="root", passwd="",
                               db="school", charset = "utf8")
        cursor = conn.cursor()
        cursor.execute("SELECT subject FROM Getting WHERE id_pup='%d'" % pupil_id)
        """Пока не кончаться записи, достаем их по одной и прибавляем 1 к общему количеству,
        после чего, печатаем количество записей
        """
        i = 0
        subjects = cursor.fetchone()        
        while subjects is not None:
            i = i + 1
            subjects = cursor.fetchone()
                
        if (i > 0):
            print("Id ученика:", pupil_id, " | Предметов:", i)
        else:
            print("У этого ученика нет предметов (он здесь не учится)")
                
    except MySQLdb.Error as e:
        print(e)
        
    finally:
        conn.close()        
    
#--------------------------------------------------------------------------------------------------------------------------------------------#	

def get_pupil_stat_list(self, pupil_id):
    """Печатает оценки по всем дисциплинам у заданного ученика (ученик определяется 
    своим id).
    pupil_id -- заданное id ученика
    """
    try:
        conn = MySQLdb.connect(host="localhost", user="root", passwd="",
                               db="school", charset = "utf8")
        
        cursor = conn.cursor()
        cursor.execute("SELECT subject,marks FROM Getting " \
                       "WHERE id_pup='%d'" % pupil_id)
        pupil_stat = cursor.fetchall()
        
        if not (pupil_stat): # Если про заданного ученика нет никакой статистики
            print("У этого ученика нет предметов (он здесь не учится)")
            return
            
        print("Id ученика:", pupil_id)
        for stat in pupil_stat:
            print(" Предмет:", stat[0], "| Оценки:", stat[1])
                
    except MySQLdb.Error as e:
        print(e)
        
    finally:
        conn.close()
        
#--------------------------------------------------------------------------------------------------------------------------------------------#	
           
def get_pupil_stat(self, subject, pupil_id):
    try:
    """Печатает оценки по всем заданной дисциплине у заданного ученика.
    
    subject -- название предмета, по которому нужно получить статистику оценок,
    pupil_id -- id ученика, у которого проверяем оценки.
    """
        conn = MySQLdb.connect(host="localhost", user="root", passwd="", 
                               db="school", charset = "utf8")
        cursor = conn.cursor()
        cursor.execute("SELECT marks FROM Getting WHERE id_pup='%d' " \
                       "AND subject='%s'" % (pupil_id, subject))
        marks_stat = cursor.fetchone()
        """Проверяем наличие статистики (есть ли заданный предмет у ученика) по заданному ученику,
        если она есть, то печатаем.
        """
        if marks_stat:
            print("Id ученика:", pupil_id, "| Предмет:", subject, end=" | ")
            print("Оценки:", marks_stat[0])
        else:
            print("Нет такого ученика или предмета, убедитесь, многосложные " \
                  "названия взяты в двойные ковычки")
            
    except MySQLdb.Error as e:
        print(e)
        
    finally:
        conn.close()
        
#--------------------------------------------------------------------------------------------------------------------------------------------#	
 
def set_pupil_point(self, subject, new_mark,
                    pupil_id, teacher_id):
    """Печатает оценку по определеннному предмету, от имени определенного
    преподавателя, определенному ученику.
    
    subject -- название предмета, по которому нужно поставить оценку,
    new_mark -- оценка, которую нужно поставить,
    pupil_id -- id ученика, которому нужно поставить оценку,
    teacher_id -- id учителя, от имени которого ставится оценка.
    
    """
    try:
        conn = MySQLdb.connect(host="localhost", user="root", passwd="",
                               db="school", charset = "utf8")
        cursor = conn.cursor()
            
        if not (new_mark > 0 and new_mark < 6):
            print("Неправильная отметка")
            return
        """Получаем класс, в котором учится заданный ученик."""    
        cursor.execute("SELECT class FROM Pupils WHERE id_pup='%d'" % pupil_id)
        pupil_class = cursor.fetchone()
        
        if not (pupil_class):
            print("Нет такого ученика")
            return

        """Делаем запрос и проверяем, ведет ли заданный учитель заданный 
        предмет в классе заданного ученика. Если ведет, то запрашиваем
        отметки заданного ученика по предмету subject, добавляем к ним 
        new_mark, обновляем запись в БД.
        """
        cursor.execute("SELECT * FROM Teaching WHERE id_teach='%d' " \
                       "AND subject='%s' AND class='%s'" 
                       % (teacher_id, subject, pupil_class[0]))
        teacher_info = cursor.fetchall()
            
        if teacher_info:
            cursor.execute("SELECT marks FROM Getting WHERE id_pup='%d' " \
                           "AND subject='%s'" % (pupil_id, subject))
            old_marks = cursor.fetchone()
            
            changed_marks = str(old_marks[0]) + " " + str(new_mark)
                
            cursor.execute("UPDATE Getting SET marks='%s' WHERE id_pup='%d' " \
                           "AND subject='%s'" % (changed_marks, pupil_id, subject))
            conn.commit()
            print("Оценка поставлена")
        else:
            print("Учитель с id", teacher_id, "не ведет предмет", subject,
                  "у ученика с id", pupil_id)
            return   
            
    except MySQLdb.Error as e:
        print(e)
       
    finally:
        conn.close()
        
#--------------------------------------------------------------------------------------------------------------------------------------------#	

def parser(self):
    """Просто парсер командной строки.
    В зависимости аргументов вызывает тот или иной метод или пишет что аргументы не верны.
    """
    arg_len = len(argv)
    if (arg_len > 1) and (argv[1] == "get_tutors_list"):
        get_tutors_list(self)
              
    elif (arg_len > 2) and (argv[1] == "get_pupils_list"):
        get_pupils_list(self, argv[2])
                
    elif (arg_len > 3) and (argv[1] == "get_class_stat"):
        if argv[3].isdigit():
            get_class_stat(self, argv[2], int(argv[3]))
        else:
            print("Id должен быть числом")
            return
                
    elif (arg_len > 2) and (argv[1] == "get_pupil_disciplines"):
        if argv[2].isdigit():
            get_pupil_disciplines(self, int(argv[2]))
        else:
            print("Id должен быть числом")
            return
                
    elif (arg_len > 2) and (argv[1] == "get_pupil_stat_list"):
        if argv[2].isdigit():
            get_pupil_stat_list(self, int(argv[2]))
        else:
            print("Id должен быть числом")
            return
                
    elif (arg_len > 3) and (argv[1] == "get_pupil_stat"):
        if argv[3].isdigit():
            get_pupil_stat(self, argv[2], int(argv[3]))
        else:
            print("Id должен быть числом")
            return
          
    elif (arg_len > 5) and (argv[1] == "set_pupil_point"):
        if argv[3].isdigit() and argv[4].isdigit() and argv[5].isdigit:
            set_pupil_point(self, argv[2], int(argv[3]),
                            int(argv[4]), int(argv[5]))
        else:
            print("Id отметка должны быть числом")
            return
    else:
        print("Неверный формат команды \nВерные форматы:" \
        "\n./school.py get_tutors_list" \
        "\n./school.py get_pupils_list <класс>" \
        "\n./school.py get_class_stat <класс> <id преподавателя>" \
        "\n./school.py get_pupil_disciplines <id ученика>" \
        "\n./school.py get_pupil_stat_list <id ученика>" \
        "\n./school.py get_pupil_stat <предмет> <id ученика>" \
        "\n./school.py set_pupil_point <предмет> <отметка> <id ученика> <id преподавателя>")
        