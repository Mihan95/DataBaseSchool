#!/usr/bin/python
# -*- coding: utf-8
        
def print_queries(cursor, no_eq_message):
    """Печатает содержимое списка, возвращенного из БД по запросу.
    
    rows -- список строк, который вернул запрос, 
    cursor -- курсор, управляющий БД MySQL,
    no_eq_message -- сообщение, которое необходимо печатать,
    если запрос вернул пустой список (нет записей с подходящими
    условиями).
    
    """
    rows = cursor.fetchall()    

    if rows:        # Если есть данные, соответствующие запросу
        for row in rows:
            print (row[0])
    else:
        print(no_eq_message)
        
class MyException(Exception):
    pass
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
