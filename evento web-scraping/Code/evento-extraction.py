#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 19:23:09 2019

@author: bajk
"""

import pandas as pd 
import numpy as np
import re

def readCoursesAllDeptN (file_path):
    f = open(file_path, "r")
    return(f.read())
    
    
def saveCoursesAllDeptN (courseList,file_path):
    f = open(file_path, "w")
#    f.write(" ".join(moduleList))
    f.write(courseList)
    f.close()
    
#**************************************************  
def init_course_keyword_extraction(print_true, file_path, source_file_name):
    # opens, reads nd iterate over the evento course extraction and returns it for futher computation
#    file_path = '/Users/bajk/Desktop/DigitalSkills/'
    global course_dept_n
    global all_courses_list
    
    course_dept_n = readCoursesAllDeptN(file_path + source_file_name)
#    all_courses_list = []
#    keyword_list =  {}
#    keyword_list_all_courses = []
      
    course_record = course_dept_n.split("[")   #splt the impoorted string into a list seperated by []
#    all_courses_list = "Course_url;Course_Nr;Course_Skills;'\n'"
    if print_true: print(str(len(course_record)))
    return(course_record)

def extract_course_keyword_list(print_true, course_record, global_keyword_list):
    
    all_courses_list = []
    
    for i in range(1,10):
        keyword_single_course_dict = {}
        courses = []
#    for i in range(0,len(course_record)):
        if 'https://' in course_record[i]:
            course_url = course_record[i].split(",")[0].replace("'","").replace("[","").replace("]","") + ";"
            course_nr = course_record[i].split(",")[1].replace("'","") + ";"
#            course_skills= course_record[i+1].replace(chr(10), ",").replace("', ","").replace(",'",",")[1:-5] + ";"
            course_skills = course_record[i+1]
            course_list = course_skills.split(",")
            
            for j in range(0,len(global_keyword_list)):
                for k in range(0,len(course_list)):
                    if global_keyword_list[j].lower() in course_list[k].lower():
#                        print(global_keyword_list[j],course_list[k])
#                        print(course_list[k].replace("'","").replace(" ","").replace("[","").replace("]",""))
                        keyword_single_course_dict[course_list[k].replace("'","")] = 1
                        
#            print(list(keyword_single_course_dict))
                        
#        if keyword_single_course_dict != {}:
#            all_courses_list = str(all_courses_list) + str(course_url) + str(course_nr) + str(keyword_single_course_dict).replace(" ","")
            courses.append(course_url.split(";").append(course_url.split(";")).append(append(course_nr.split(";"))))
#            courses.append(course_nr.split(";"))
            print(courses)
#            courses.append(list(keyword_single_course_dict))
            
            all_courses_list.append(courses)
            print(all_coursess)
            
    if print_true: print(all_courses_list)
    return(all_courses_list)



data = {'Country': ['Belgium', 'India', 'Brazil']}
#,'Capital': ['Brussels', 'New Delhi', 'Brasília'],'Population': [11190846, 1303171035, 207847528]}
df_sample = pd.DataFrame(data,columns=['Country'])
#, 'Capital', 'Population'])
df_sample
#                    
#                    pattern = re.compile(global_keyword_list[i])
#                    res = course_skills.match(global_keyword_list[i])
#                    
#                    res = re.findall(pattern,course_skills)
#                    print(res)
#                    
#                    pattern = re.compile(global_keyword_list[i])                   
#                    re.compile(r'\bsystem%\b')
#                    res = re.findall(pattern,course_skills)
#                    print(res)

             
#             
#            for i in range(0,len(global_keyword_list)):
#                u = global_keyword_list[i]
#                print("r'\'" + u + "'\b")
#                res = re.compile("r'\'" + u + "'\b" % course_skills, re.I)
#                res = re.search()
#                print(res)
            
#            res = [ele for ele in global_keyword_list if(ele in course_skills)] 
#            if bool(res)==True:
#                keyword_single_course_set = set() #empty dict. for collecting and counting all keywords found in the course descriptions
#                for j in course_skills.split(","):
#                    if j.find("]") == -1:
#                        keyword_single_course_set.add(j)
#                        if print_true: print(j)

#                        keyword_single_course_dict[j] = keyword_single_course_dict[k] #keyword_single_course_dict[j] + 1 # if keyword exists, increase the counter=value by 1
#                    else:
#                        keyword_single_course_dict[j] = 1 # if new keyword, initialize with value = 1
#                
#        print(keyword_single_course_dict)
                        
                        
#                keyword_single_course_set = str(keyword_single_course_set).replace("'","").replace(" ","").replace('"',"")
#                all_courses_list = str(all_courses_list) + str(course_url) + str(course_nr) + keyword_single_course_set + '\n\n'
#    if print_true: print(all_courses_list)
#    return(all_courses_list)


#**************************************************     

# MAIN start
# initi variables
source_file_path = '/Users/bajk/Desktop/DigitalSkills/'
source_file_name = 'CourseListDeptN_655_tot.txt'
global_keyword_list = ['digit','techni','system','method','mathemat','comput','verfahren','nachricht','kommunika','Masch','Mashin','Daten','Internet','netz','online']

init_course_keyword_extraction(False, source_file_path, source_file_name)
course_record = init_course_keyword_extraction(False, source_file_path, source_file_name)
all_courses_list = extract_course_keyword_list(True, course_record,global_keyword_list)
saveCoursesAllDeptN (all_courses_list, file_path + 'CourseListDeptN_655_test.txt')









#****************************************
        course_skills = str(keyword_single_course_set).replace("{","").replace("}","")
#        print(course_skills)
        
        for i in range(1,len(global_keyword_list)):
            if global_keyword_list[i] in course_skills:
                print(global_keyword_list[i])
                print(course_skills)
        
        res = [ele for ele in global_keyword_list if(ele in course_skills)] 
        if bool(res)==True:
            print(course_skills)