from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

"""
# 함수형 view
@api_view(['GET', 'POST'])
def articleAPI(request):
    if request.method == 'GET':
        temp = Article.objects.all()
        article = temp[0]
        serializer = ArticleSerializer(article)
        serializer_all = ArticleSerializer(temp, many=True)

        # article_data = {
        #     "title":article.title,
        #     "content":article.content,
        #     "created_now": article.created_now,
        #     "updated_now": article.updated_now
        # }
        
        return Response(serializer_all.data)
    elif request.method == 'POST':
        # print(request.data)
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid(): # 검증이 없으면 에러가 뜸
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
class ArticleList(APIView):
    def get(self, request, format=None):
        temp = Article.objects.all()
        serializer = ArticleSerializer(temp, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=ArticleSerializer)
    def post(self, request, format=None):
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
# 험수형 view
@api_view(['GET', 'PUT', 'DELETE'])
def articleDetailAPI(request, article_id):
    if request.method == 'GET':
        # article = Article.objects.get(id=article_id)
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article, data = request.data) # article을 data로 바꾸어줌
        # 수정할때는 위와 같은 식으로 get, post 방식을 응용하여 사용
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

class ArticleDetail(APIView):
    def get(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    def delete(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)