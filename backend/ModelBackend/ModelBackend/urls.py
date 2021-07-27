# from django.contrib import admin
# from django.urls import path
# from firstPage import views
# from django.views.decorators.csrf import csrf_exempt

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('scoreJson',csrf_exempt(views.scoreJson),name="Predict Random Forest"),
#     path('scoreFile',csrf_exempt(views.scoreFile), name ="Predict Random Forest File"),
#     path('predictDecisionTree',csrf_exempt(views.predictDecisionTree), name ="Predict Decision Tree"),
#     path('predictDecisionTreeFile',csrf_exempt(views.predictDecisionTreeFile), name ="Predict Decision Tree File"),
#     path('predictNaiveBayes',csrf_exempt(views.predictNaiveBayes), name ="Predict Naive Bayes"),
#     path('predictNaiveBayesFile',csrf_exempt(views.predictNaiveBayesFile), name ="Predict Naive Bayes File"),
# ]

from django.contrib import admin
from django.urls import path
from firstPage import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('predictRandomForest',csrf_exempt(views.predictRandomForest),name="Predict Random Forest"),
    path('predictRandomForestFile',csrf_exempt(views.predictRandomForestFile), name ="Predict Random Forest File"),
    path('predictDecisionTree',csrf_exempt(views.predictDecisionTree), name ="Predict Decision Tree"),
    path('predictDecisionTreeFile',csrf_exempt(views.predictDecisionTreeFile), name ="Predict Decision Tree File"),
    path('predictNaiveBayes',csrf_exempt(views.predictNaiveBayes), name ="Predict Naive Bayes"),
    path('predictNaiveBayesFile',csrf_exempt(views.predictNaiveBayesFile), name ="Predict Naive Bayes File"),
]