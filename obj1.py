#!/usr/bin/env python3
# coding:utf-8

class Student(object):
    # 双下划线开头,并且以双下划线结尾的,是特殊变量

    def __init__(self, name, score):
        # 私有变量(private)
        self.__name = name
        self.__score = score

    # 外部代码获取name和score
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def print_score(self):
        print('%s : %d - %s' % (self.__name, self.__score, self.get_grade()))

    # 外部代码修改name和score
    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score

    # 判断成绩
    def get_grade(self):
        if self.__score >= 90:
            return '优良'
        elif self.__score >= 60:
            return '及格'
        else:
            return '差'

