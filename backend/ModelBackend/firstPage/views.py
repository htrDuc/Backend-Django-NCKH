  
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
import json
import pandas as pd
from django.core.files.storage import FileSystemStorage
import joblib

modelRandomForest=joblib.load('modelRandomForest.pkl')

def predictRandomForest(request):
    print (request.body)
    data =json.loads(request.body)
    dataF=pd.DataFrame({'x':data}).transpose()
    score=modelRandomForest.predict_proba(dataF)[:,-1][0]
    score=float(score)

    return JsonResponse({'score':score})


def predictRandomForestFile(request):
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)
    filePath='.'+filePathName

    data =pd.read_csv(filePath)
    score=modelRandomForest.predict_proba(data)[:,-1]

    score={j:k for j,k in zip(data['Loan_ID'],score)}

    score =sorted(score.items(),key=lambda x: x[1],reverse=True)

    return JsonResponse({'result':score})

modelDecisionTree = joblib.load('modelDecisionTree.pkl')

def predictDecisionTree(request):
    data =json.loads(request.body)
    dataF=pd.DataFrame({'x':data}).transpose()
    pre=modelDecisionTree.predict(dataF)
    print(pre)
    return JsonResponse({'predict':pre.tolist()})

def predictDecisionTreeFile(request):
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)
    filePath='.'+filePathName

    data =pd.read_csv(filePath)
    score=modelDecisionTree.predict(data)
    score={j:k for j,k in zip(data['Loan_ID'],score)}

    score =sorted(score.items(),key=lambda x: x[1],reverse=True)

    return JsonResponse({'result':score })


modelGaussianNB = joblib.load('modelGaussianNB.pkl')

def predictNaiveBayes(request):
    data =json.loads(request.body)
    dataF=pd.DataFrame({'x':data}).transpose()
    pre=modelGaussianNB.predict(dataF)
    print(pre)
    return JsonResponse({'predict':pre.tolist()})

def predictNaiveBayesFile(request):
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)
    filePath='.'+filePathName

    data =pd.read_csv(filePath)
    score=modelGaussianNB.predict(data)
    score={j:k for j,k in zip(data['Loan_ID'],score)}

    score =sorted(score.items(),key=lambda x: x[1],reverse=True)

    return JsonResponse({'result':score })