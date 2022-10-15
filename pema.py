import mysql.connector
from mysql.connector import Error
import pyttsx3
import os
import signal
import sys
import datetime
from datetime import timedelta, datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.runAndWait()

connection = mysql.connector.connect(host='localhost',
                                         database='pema',
                                         user='root',
                                         password='')

def getPeople():

    try:

        if connection.is_connected():
            db_Info = connection.get_server_info()
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            query = "SELECT * FROM people;"
            cursor.execute(query)
            records = cursor.fetchall()

            for row in records:
                
                print(row[0], "- ", row[1])

            p = input()
            p = int(p)
            print(p)
            cursor.close()
            db_Info = connection.get_server_info()
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            query = """SELECT * FROM people WHERE idPeople = %s"""
            cursor.execute(query, (p,))
            records = cursor.fetchall()

            

            for row in records:

                if p == row[0]:

                    print("Name: ", row[1])
                    pyttsx3.speak("Name: ")
                    pyttsx3.speak(row[1])

                    print("Age: ", row[2])
                    pyttsx3.speak("Age: ")
                    pyttsx3.speak(row[2])

                    print("Birthday: ", row[3])
                    pyttsx3.speak("Birthday: ")
                    pyttsx3.speak(row[3])

                    print("MBTI: ", row[4])
                    pyttsx3.speak("MBTI: ")
                    pyttsx3.speak(row[4])

                    print("Sun: ", row[5])
                    pyttsx3.speak("Sun: ")
                    pyttsx3.speak(row[5])

                    print("Moon: ", row[6])
                    pyttsx3.speak("Moon: ")
                    pyttsx3.speak(row[6])

                    print("Rising: ", row[7])
                    pyttsx3.speak("Rising: ")
                    pyttsx3.speak(row[7])

                    print("Favorite Color: ", row[8])
                    pyttsx3.speak("Favorite Color: ")
                    pyttsx3.speak(row[8])

                    print("Favorite Food: ", row[9])
                    pyttsx3.speak("Favorite Food: ")
                    pyttsx3.speak(row[9])

                    print("Favorite Drink: ", row[10])
                    pyttsx3.speak("Favorite Drink: ")
                    pyttsx3.speak(row[10])

                else:

                    print("query not working")

            cursor.close()

    except mysql.connector.Error as error:

        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
       
def getDate():

    date = datetime.now()

    today = date.strftime("%Y-%m-%d")

    tomorrow = date + timedelta(days=1)
    tomorrow = tomorrow.strftime("%Y-%m-%d")

    day_of_the_week = date.weekday()
    days_until_sunday = 6 - day_of_the_week
    next_sunday = date + timedelta(days=days_until_sunday)
    next_sunday = next_sunday.strftime("%Y-%m-%d")

    typeCalendar = input()

    while True:

        if typeCalendar == "nevermind":

            break

        else: 

            dateCalendar = input()

            while True:

                if typeCalendar == "tasks":

                    if dateCalendar == "today":

                        try:

                            if connection.is_connected():
                                db_Info = connection.get_server_info()
                                cursor = connection.cursor()
                                cursor.execute("select database();")
                                record = cursor.fetchone()
                                query = """SELECT * FROM tasks WHERE dateTask = %s;"""
                                cursor.execute(query, (today,))
                                records = cursor.fetchall()
                                
                                pyttsx3.speak("Today we have to")

                                for row in records:

                                    print(row[1])
                                    pyttsx3.speak(row[1])
                            
                                cursor.close()

                        except mysql.connector.Error as error:

                            print("Failed to get record from MySQL table: {}".format(error))

                        finally:
                            if connection.is_connected():
                                cursor.close()
                                connection.close()

                    elif dateCalendar == "tomorrow":

                        try:

                            if connection.is_connected():
                                db_Info = connection.get_server_info()
                                cursor = connection.cursor()
                                cursor.execute("select database();")
                                record = cursor.fetchone()
                                query = """SELECT * FROM tasks WHERE dateTask = %s;"""
                                cursor.execute(query, (tomorrow,))
                                records = cursor.fetchall()

                                pyttsx3.speak("Tomorrow we have to")

                                for row in records:

                                    print(row[1])
                                    pyttsx3.speak(row[1])
                            
                                cursor.close()

                        except mysql.connector.Error as error:

                            print("Failed to get record from MySQL table: {}".format(error))

                        finally:
                            if connection.is_connected():
                                cursor.close()
                                connection.close()

                    elif dateCalendar == "this week":

                        try:

                            if connection.is_connected():
                                db_Info = connection.get_server_info()
                                cursor = connection.cursor()
                                cursor.execute("select database();")
                                record = cursor.fetchone()
                                query = """SELECT * FROM tasks WHERE dateTask >= %s AND dateTask <= %s ORDER BY dateTask;"""
                                cursor.execute(query, (today, next_sunday))
                                records = cursor.fetchall()

                                pyttsx3.speak("This week we have to")

                                for row in records:

                                    pyttsx3.speak("On")
                                    query_date = row[2].day
                                    pyttsx3.speak(query_date)
                                    pyttsx3.speak("we have")
                                    print(row[1], " ", row[2])
                            
                                cursor.close()

                        except mysql.connector.Error as error:

                            print("Failed to get record from MySQL table: {}".format(error))

                        finally:
                            if connection.is_connected():
                                cursor.close()
                                connection.close()
                    
                    elif dateCalendar == "all":

                        try:

                            if connection.is_connected():
                                db_Info = connection.get_server_info()
                                cursor = connection.cursor()
                                cursor.execute("select database();")
                                record = cursor.fetchone()
                                query = """SELECT * FROM tasks WHERE dateTask >= %s ORDER BY dateTask;"""
                                cursor.execute(query, (today,))
                                records = cursor.fetchall()

                                for row in records:

                                    pyttsx3.speak("On")
                                    query_date = row[2].day
                                    pyttsx3.speak(query_date)
                                    pyttsx3.speak("we have")
                                    print(row[1], " ", row[2])
                            
                                cursor.close()

                        except mysql.connector.Error as error:

                            print("Failed to get record from MySQL table: {}".format(error))

                        finally:
                            if connection.is_connected():
                                cursor.close()
                                connection.close()

                    else:

                        print("invalid")

                elif typeCalendar == "events":

                    if dateCalendar == "today":

                        try:

                            if connection.is_connected():
                                db_Info = connection.get_server_info()
                                cursor = connection.cursor()
                                cursor.execute("select database();")
                                record = cursor.fetchone()
                                query = """SELECT * FROM events WHERE dateEvent = %s;"""
                                cursor.execute(query, (today,))
                                records = cursor.fetchall()
                                
                                pyttsx3.speak("Today we have to")

                                for row in records:

                                    print(row[1])
                                    pyttsx3.speak(row[1])
                            
                                cursor.close()

                        except mysql.connector.Error as error:

                            print("Failed to get record from MySQL table: {}".format(error))

                        finally:
                            if connection.is_connected():
                                cursor.close()
                                connection.close()

                    elif dateCalendar == "tomorrow":

                        try:

                            if connection.is_connected():
                                db_Info = connection.get_server_info()
                                cursor = connection.cursor()
                                cursor.execute("select database();")
                                record = cursor.fetchone()
                                query = """SELECT * FROM events WHERE dateEvent = %s;"""
                                cursor.execute(query, (tomorrow,))
                                records = cursor.fetchall()

                                pyttsx3.speak("Tomorrow we have to")

                                for row in records:

                                    print(row[1])
                                    pyttsx3.speak(row[1])
                            
                                cursor.close()

                        except mysql.connector.Error as error:

                            print("Failed to get record from MySQL table: {}".format(error))

                        finally:
                            if connection.is_connected():
                                cursor.close()
                                connection.close()

                    elif dateCalendar == "this week":

                        try:

                            if connection.is_connected():
                                db_Info = connection.get_server_info()
                                cursor = connection.cursor()
                                cursor.execute("select database();")
                                record = cursor.fetchone()
                                query = """SELECT * FROM events WHERE dateEvent >= %s AND dateEvent <= %s ORDER BY dateEvent;"""
                                cursor.execute(query, (today, next_sunday))
                                records = cursor.fetchall()

                                pyttsx3.speak("This week we have to")

                                for row in records:

                                    pyttsx3.speak("On")
                                    query_date = row[2].day
                                    pyttsx3.speak(query_date)
                                    pyttsx3.speak("we have")
                                    print(row[1], " ", row[2])
                            
                                cursor.close()

                        except mysql.connector.Error as error:

                            print("Failed to get record from MySQL table: {}".format(error))

                        finally:
                            if connection.is_connected():
                                cursor.close()
                                connection.close()
                    
                    elif dateCalendar == "all":

                        try:

                            if connection.is_connected():
                                db_Info = connection.get_server_info()
                                cursor = connection.cursor()
                                cursor.execute("select database();")
                                record = cursor.fetchone()
                                query = """SELECT * FROM events WHERE dateEvent >= %s ORDER BY dateEvent;"""
                                cursor.execute(query, (today,))
                                records = cursor.fetchall()

                                for row in records:

                                    pyttsx3.speak("On")
                                    query_date = row[2].day
                                    pyttsx3.speak(query_date)
                                    pyttsx3.speak("we have")
                                    print(row[1], " ", row[2])
                            
                                cursor.close()

                        except mysql.connector.Error as error:

                            print("Failed to get record from MySQL table: {}".format(error))

                        finally:
                            if connection.is_connected():
                                cursor.close()
                                connection.close()

                    else:

                        print("invalid")

                else:

                    print("invalid")

def getMovies():

    try:

        if connection.is_connected():
            db_Info = connection.get_server_info()
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            query = "SELECT * FROM movies;"
            cursor.execute(query)
            records = cursor.fetchall()

            for row in records:

                print(row[0], "- ", row[1])
            
            cursor.close()

            i = input()

            if "1" in i or "2" in i or "3" in i or "4" in i or "5" in i or "6" in i or "7" in i or "8" in i or "9" in i or "0" in i:

                i = int(i)

            else:

                i = i.lower()

            if i != "thank you":

                db_Info = connection.get_server_info()
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                query = "SELECT * FROM movies;"
                cursor.execute(query)
                records = cursor.fetchall()

                for row in records:

                    row1 = row[1].lower()

                    if i == row[0] or str(i) == row1:

                        print("Title: ", row[1])
                        print("Genre: ", row[2])
                        print("Release Date: ", row[3])
                        print("Your Rating: ", row[4])
                        print("Watched on: ", row[5])
                        print("Notes: ", row[6])
                        print("")
                        break

                    elif i != row[0] and str(i) != row1:

                        res = isinstance(i, str)

                        if res == True:
                        
                            if i != row1 and i in row1:

                                print("Title: ", row[1])
                                print("Genre: ", row[2])
                                print("Release Date: ", row[3])
                                print("Your Rating: ", row[4])
                                print("Watched on: ", row[5])
                                print("Notes: ", row[6])
                                print("")

                    else:

                        print("invalid")
                
                cursor.close()
            

    except mysql.connector.Error as error:

        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def getBooks():

    try:

        if connection.is_connected():
            db_Info = connection.get_server_info()
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            query = "SELECT * FROM books;"
            cursor.execute(query)
            records = cursor.fetchall()

            for row in records:
                
                print(row[0], "- ", row[1])

            cursor.close()

            i = input()

            if "1" in i or "2" in i or "3" in i or "4" in i or "5" in i or "6" in i or "7" in i or "8" in i or "9" in i or "0" in i:

                i = int(i)

            else:

                i = i.lower()

            if i != "thank you":

                db_Info = connection.get_server_info()
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                query = "SELECT * FROM books;"
                cursor.execute(query)
                records = cursor.fetchall()

                for row in records:

                    row1 = row[1].lower()

                    if i == row[0] or str(i) == row1:

                        print("Title: ", row[1])
                        pyttsx3.speak("Title")
                        pyttsx3.speak(row[1])
                        print("Author: ", row[2])
                        pyttsx3.speak("Author")
                        pyttsx3.speak(row[2])
                        print("Genre: ", row[3])
                        pyttsx3.speak("Genre")
                        pyttsx3.speak(row[3])
                        print("Release Date: ", row[4])
                        pyttsx3.speak("Release Date")
                        pyttsx3.speak(row[4])
                        print("Read in: ", row[5])
                        pyttsx3.speak("Read in")
                        pyttsx3.speak(row[5])
                        print("Your Rating: ", row[6])
                        pyttsx3.speak("Your Rating")
                        pyttsx3.speak(row[6])
                        print("")
                        break

                    elif i != row[0] and str(i) != row1:

                        res = isinstance(i, str)

                        if res == True:
                        
                            if i != row1 and i in row1:

                                print("Title: ", row[1])
                                print("Author: ", row[2])
                                print("Genre: ", row[3])
                                print("Release Date: ", row[4])
                                print("Read in: ", row[5])
                                print("Your Rating: ", row[6])
                                print("")

                    else:

                        print("invalid")
                
                cursor.close()
            

    except mysql.connector.Error as error:

        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def getMoods():

    w = input()

    while True:

        date = datetime.now()

        today = date.strftime("%Y-%m-%d")

        day_of_the_week = date.weekday() + 1
        past_sunday = date - timedelta(days=day_of_the_week) 
        past_sunday = past_sunday.strftime("%Y-%m-%d")

        if w == "this week":

            try:

                if connection.is_connected():
                    db_Info = connection.get_server_info()
                    cursor = connection.cursor()
                    cursor.execute("select database();")
                    record = cursor.fetchone()
                    query = """SELECT * FROM moods WHERE dateMood >= %s AND dateMood < %s;"""
                    cursor.execute(query,(past_sunday, today))
                    records = cursor.fetchall()

                    for row in records:
                        
                        print("")
                        print("Date: ", row[1])
                        print("Mood: ", row[2], "/10")

            except mysql.connector.Error as error:

                print("Failed to get record from MySQL table: {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        elif w == "this month":

            print("")

        elif w == "this year":

            print("")

        elif w == "all":

            print("")

        elif w == "nevermind":

            break

        else:

            print("")
            print("invalid")

def getConcerts():

    try:

        if connection.is_connected():
            db_Info = connection.get_server_info()
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            query = "SELECT * FROM concerts;"
            cursor.execute(query)
            records = cursor.fetchall()

            for row in records:
                
                print(row[0], "- ", row[1])

            cursor.close()

            i = input()

            if "1" in i or "2" in i or "3" in i or "4" in i or "5" in i or "6" in i or "7" in i or "8" in i or "9" in i or "0" in i:

                i = int(i)

            else:

                i = i.lower()

            if i != "thank you":

                db_Info = connection.get_server_info()
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                query = "SELECT * FROM concerts;"
                cursor.execute(query)
                records = cursor.fetchall()

                for row in records:

                    row1 = row[1].lower()

                    if i == row[0] or str(i) == row1:

                        print("Artist: ", row[1])
                        print("Date: ", row[2])
                        print("Your Rating: ", row[3])
                        print("Notes: ", row[4])
                        print("")
                        break

                    elif i != row[0] and str(i) != row1:

                        res = isinstance(i, str)

                        if res == True:
                        
                            if i != row1 and i in row1:

                                print("Artist: ", row[1])
                                print("Date: ", row[2])
                                print("Your Rating: ", row[3])
                                print("Notes: ", row[4])
                                print("")
                                print("")

                    else:

                        print("invalid")
                
                cursor.close()
            

    except mysql.connector.Error as error:

        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

print("Hi, my name is Jared. How can I help you?")
pyttsx3.speak("Hi, my name is Jared. How can I help you?")
print("")
print("1. New")
print("2. Check")
q = input()
#novo ou ver
#depois opções normais


while True:

    if q == "1" or q == "new":

        print("")

    elif q == "2" or q == "check":

        print("")
        print("1. Moods")
        print("3. People")
        print("5. Calendar")
        print("6. Movies")
        print("7. Books")
        print("8. Concerts")
        print("0. Exit")

        p = input(" ")

        while p != "0":

            while True:
        
                if p == "1":

                    getMoods()

                elif p == "2":

                    print("2")

                elif p == "3":

                    getPeople()

                elif p == "4":

                    print("4")

                elif p == "5":

                    getDate()
                    break

                elif p == "6":

                    getMovies()
                    break

                elif p == "7":

                    getBooks()
                    break

                elif p == "8":

                    getConcerts()
                    break

                elif p == "0":

                    print("Exiting...")
                    pyttsx3.speak("Exiting...")
                    break

                else:

                    print("Oh, oh, that's not an option")
                    pyttsx3.speak("Oh, oh, that's not an option")

    elif q == "nevermind":

        print("")
        print("Exiting...")
        pyttsx3.speak("Exiting...")

    else:

        print("")
        print("Oh, oh, that's not an option")
        pyttsx3.speak("Oh, oh, that's not an option")





#if KeyboardInterrupt:

    #sys.exit()