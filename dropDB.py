#!/usr/bin/python
# -*- coding: utf8 -*-

import MySQLdb
 
"""Удаляет БД school"""
def drop_db():
    try:
        conn   = MySQLdb.connect(host="localhost", user="root", passwd="", db="school", charset = "utf8")
        cursor = conn.cursor()
        cursor.execute('DROP DATABASE `school`;')
            
        print ('db dropped')
            
    except MySQLdb.Error as e:
        print(e)
        
drop_db()
            