# -*- coding: utf-8 -*-
import sys
import os
import numpy as np

class question:
    """ classe correspondant a une question, avec pour
    attributs une categorie, le texte de la question, et le texte de la réponse
    """
    def __init__(self,Cat,TextQuestion,TextAnswer):
        self.category = Cat
        self.QuestTxt = TextQuestion
        self.AnswerTxt = TextAnswer
    
    def __str__(self):
        String = 'Question type: '+self.category+'\n'+self.QuestTxt
        return String
        
    def categorycheck(self,*args):
        for i in args:
            if self.category == i[0]:
                return True
        return False

class Quizz:
    """ Classe du quizz à proprement dit, contient, 
    l'ensemble des questions, et les catégories possibles
    """
    def __init__(self):
        self.questionlist = initTrivia()
        self.categorylist = ListCate(initTrivia())
        self.scores = [[],[]]
     
    def QueryCatList(self):
        Toprint = 'Les categories disponibles sont: \n'
        ii = 1
        while ii < len(self.categorylist):
            Toprint = Toprint+str(ii)+' - '+str(self.categorylist[ii])+'\n'
            ii += 1
        print(Toprint)
        
def ListCate(QuestionTable):
    List = []
    List.append(QuestionTable[0].category)
    for question in QuestionTable:
        Alreadyin = False
        for j in List:
            if j == question.category:
                Alreadyin = True
        if Alreadyin == False:
            if len(question.category)>1:
                List.append(question.category)
    return List
        
def initTrivia():
    """ Fonction qui récupère les questions dans le fichier texte TriviaData.txt
    les questions doivent être sous le format suivant:
    Catégorie;Question;Reponse;Catégorie;Question;Reponse;Catégorie;Question;Reponse <-- trois questions par ligne
    """
    File = open("TriviaData.csv","r")
    QuestionTable = []
    Raw_Table = File.readlines()
    for i in Raw_Table:
        if len(i.split(";" )) > 2:
            Question1 = question(i.split(";")[0],i.split(";")[1],i.split(";")[2])
            QuestionTable.append(Question1)
        if len(i.split(";" )) > 6:
            Question2 = question(i.split(";")[4],i.split(";")[5],i.split(";")[6])
            QuestionTable.append(Question2)
            if len(i.split(";"))==11:
                Question3 = question(i.split(";")[8],i.split(";")[9],i.split(";")[10])
                QuestionTable.append(Question3)
    return QuestionTable
    
QuizzTest = Quizz()
QuizzTest.QueryCatList()                   