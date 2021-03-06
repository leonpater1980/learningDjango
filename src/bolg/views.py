from django.shortcuts import render
from django.http import HttpResponse
from watson_developer_cloud import DiscoveryV1
import json
from bolg import models
from django.template.context_processors import request

# Create your views here.


def index(request):
    print("start")
#     discovery = DiscoveryV1(
#     version='2018-12-03',
#     iam_apikey='eUfYzPqcSdv0Y4ionluvs2G2PARnrDXau4BrzWQdt6GF',
#     url='https://gateway.watsonplatform.net/discovery/api'
#     )
# 
#     discovery.set_detailed_response(True)
#     response = discovery.get_collection(collection_id='a925d1d3-d26d-4443-8749-b74bf737ee4c',environment_id='0a87da33-ccda-4827-a071-89b4f125b739');

    # # Access response from methodName
    # print(json.dumps(response.get_result(), indent=2))
    # # Access information in response headers
    # print(response.get_headers())
    # # Access HTTP response status
    # print(response.get_status_code())

    print("end")
#     article = models.Article.objects.get(pk = 1)
    articles = models.Article.objects.all()
    # return HttpResponse(json.dumps(response.get_result(), indent=2))
    return render(request, 'index.html', {'articles' : articles})
    # return render(request, 'index.html', {{'hello':'hello bolg'})

def article_page(request, article_id):
    article = models.Article.objects.get(pk = article_id)
    return render(request, 'article_page.html', {'article' : article})