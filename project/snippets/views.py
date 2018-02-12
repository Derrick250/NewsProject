

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.db.models import Q
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from project.snippets.models import Snippet, User, Articles, Comments, UserTags, ArticleTags
from project.snippets.serializers import SnippetSerializer, UserSerializer, ArticleSerializer,CommentSerializer,UserTagSerializer,ArticleTagSerializer, InitialSerializer
import itertools
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import logging
import json
import nltk

logger = logging.getLogger(__name__)
nltk.download('punkt')

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


@csrf_exempt
def user_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = User.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():

            serializer.save()

            snippets = Articles.objects.all()
            articleSerializer = ArticleSerializer(snippets, many=True)
            mySerializer = InitialSerializer(articleSerializer,serializer)
            mySerializer.is_valid()

            # logger.error('An error occured in trying to present {} '.format(mySerializer))
            return JsonResponse({
                'user': serializer.data,
                'articles': articleSerializer.data,
                'status': 'true',
            })

            # return JsonResponse(mySerializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)



@csrf_exempt
def article_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Articles.objects.all()
        serializer = ArticleSerializer(snippets, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            tagger(serializer.data['description'], serializer.data['id'])
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def article_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        """
        the pk received should be the users ID. Get all tags that have that userID. Get all articles. Then sort the articles by those the number of similar tags then by date&time
        """

        serialized_data = serializers.serialize('json', UserTags.objects.filter(userID=pk), fields=('tag'))
        json_data = json.loads(serialized_data)
        myArticleIDs = []
        for element in json_data:
            tag = element['fields']['tag']
            print("My like snippets are " + str(tag))
            mySerialized_data = serializers.serialize('json', ArticleTags.objects.filter(tag=tag), fields=('articleID'))
            newArticles = json.loads(mySerialized_data)

            for article in newArticles:
                articleID = article['fields']['articleID']

                if int(articleID) not in myArticleIDs:
                    myArticleIDs.append(int(articleID))


        my_filter_qs = Q()
        for article in myArticleIDs:
            my_filter_qs = my_filter_qs | Q(pk=article)

        articles = serializers.serialize('json', Articles.objects.filter(my_filter_qs))

    except Articles.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        json_data = json.loads(articles)

        totalResponse = []
        for element in json_data :
            totalResponse.append(element['fields'])
        return JsonResponse(totalResponse, safe=False)

        # return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet = UserTags.objects.all()
        snippet.delete()
        snippet = ArticleTags.objects.all()
        snippet.delete()
        snippet = User.objects.all()
        snippet.delete()
        snippet = ArticleTags.objects.all()
        snippet.delete()
        return HttpResponse(status=204)


def tagger(document, id):
    # with open("myText.txt", "r") as myfile:
    #     data = myfile.read().replace('\n', ' ')
    data = document

    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(data)
    myList = []
    for word in word_tokens:
        newWord = word.lower()
        if newWord not in stop_words:
            myList.append(newWord)

    tags = Counter(myList).most_common(5)







    for word in tags:
        print(word[0])
        articleTags = ArticleTags()
        articleTags.articleID = id
        articleTags.tag = word
        articleTags.save()






@csrf_exempt
def comment_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Comments.objects.all()
        serializer = CommentSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def comment_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Comments.objects.get(articleID=pk)

    # /  Comments.articleID=pk ...... Here, the pk is an articleID that is used to get all the comments that are of that article. Consider putting this in list;a
    except Comments.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CommentSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)



@csrf_exempt
def usertag_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = UserTags.objects.all()
        serializer = UserTagSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        print("hello" + str(data['userID']))
        pk = data['articleID']
        # snippet = ArticleTags.objects.filet(articleID=pk)

        # mySerializer = ArticleTagSerializer(snippet)

        serialized_data = serializers.serialize('json', ArticleTags.objects.filter(articleID=pk), fields=('tag'))
        # print("HEHEHE " + str(serialized_data['elements']))

        json_data = json.loads(serialized_data)
        for element in json_data :
            print("Hahahaha " + str(element['fields']['tag']))
            newData = {}
            newData['userID'] = data['userID']
            newData['tag'] = element['fields']['tag']
            serializer = UserTagSerializer(data=newData)
            if serializer.is_valid():
                serializer.save()

        return JsonResponse(serializer.data, status=201)



@csrf_exempt
def usertag_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = UserTags.objects.get(pk=pk)
    except UserTags.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserTagSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserTagSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


@csrf_exempt
def articletag_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = ArticleTags.objects.all()
        serializer = ArticleTagSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleTagSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def articletag_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = ArticleTags.objects.get(pk=pk)
    except ArticleTags.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleTagSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleTagSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)