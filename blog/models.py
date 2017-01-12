# coding: utf-8
from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Catagory(models.Model):
    """
    博客分类
    """
    name = models.CharField('分类',max_length = 30)
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    """
    博客标签
    """
    name = models.CharField('标签',max_length = 15)

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    """
        博客主体
    """
    title = models.CharField('标题',max_length = 15)
    author = models.CharField('作者',max_length = 15)
    introduce = models.TextField('介绍', max_length = 70)
    content = models.TextField('博客正文')
    image = models.ImageField(null = True, blank = True, upload_to='images/%Y/%m/%d') #ull=True,数据库可以为空；blank=True，后台输入可以为空
    created = models.DateTimeField('发布时间',auto_now_add=True)
    category = models.ForeignKey(Catagory)
    tags = models.ManyToManyField(Tag)


    def __unicode__(self):
        return self.title




class Comment(models.Model):
    """
    评论
    """
    blog = models.ForeignKey(Blog)
    name = models.CharField(max_length = 15)
    email = models.EmailField()
    content = models.CharField(max_length=240)
    created = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return self.content




      
class Achievement(models.Model):
    """
    军事成就
    """

    title = models.CharField('指挥战役', max_length = 20)
    created = models.DateTimeField(auto_now_add=True, null=True)
    content = models.TextField('战役简介', max_length = 500, null=True)
   
    def __unicode__(self):
        return self.title 

class Person(models.Model):
    """
    人物
    """
    name = models.CharField('姓名',max_length = 20,null=True)
    introduction = models.CharField('简介', max_length = 30, null=True)
    image = models.ImageField(null = True, blank = True, upload_to='images/%Y/%m/%d') #ull=True,数据库可以为空；blank=True，后台输入可以为空
    person = models.TextField('个人介绍',max_length = 300)
    achievements = models.ManyToManyField(Achievement)
    content = models.TextField('个人评价',max_length = 400)
    

    def __unicode__(self):
        return self.name            


class Speak(models.Model):
    """
    碎言碎语
    """
    title = models.CharField('题目', max_length = 20, null=True)
    content = models.TextField('碎言碎语', max_length = 200)
    image = models.ImageField(null = True, blank=True, upload_to='images/%Y/%m/%d')#ull=True,数据库可以为空；blank=True，后台输入可以为空
    created = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        # return self.title

        return u'%s %s' % (self.title, self.content)

class Skill(models.Model):
    """
    专业技能
    """

    title = models.CharField('专业技能', max_length = 20)

    def __unicode__(self):
        return self.title


class Life(models.Model):
    """
    生活相关
    """
    title = models.CharField('生活相关',max_length = 50)  

    def __unicode__(self):
        return self.title      



class Aboutme(models.Model):
    """
    关于我
    """
    name = models.CharField('姓名',max_length = 10)
    nickname = models.CharField('昵称',max_length = 20)
    motto = models.CharField('座右铭', max_length = 20)
    birthday = models.CharField('生日',max_length = 10)
    university = models.CharField('大学',max_length = 50)
    image = models.ImageField(null = True, blank=True, upload_to='images/%Y/%m/%d')#ull=True,数据库可以为空；blank=True，后台输入可以为空
    skills = models.ManyToManyField(Skill)
    lifes = models.ManyToManyField(Life)
    
    def __unicode__(self):
        return self.name
















