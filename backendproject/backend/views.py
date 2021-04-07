from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions  import IsAuthenticated
from  backend.serializers import ArticleSerializer
from rest_framework.generics import ListAPIView,DestroyAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView
from . models import article
# ok hast
class ArticleList(ListAPIView):
    queryset=article.objects.all()
    serializer_class= ArticleSerializer
# ok nist
class ArticleDestroy(DestroyAPIView):
    serializer_class= ArticleSerializer
    def get_queryset(self):
        queryset = article.objects.filter(fav=False)
        return queryset
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_default == True:
            return Response("Cannot delete default system category", status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
# ok hast
class ArticleCustomList(ListAPIView):
    queryset=article.objects.filter(author='bardia')
    serializer_class= ArticleSerializer
# ok nist
class ArticleDetail(ListAPIView):
    queryset=article.objects.all()
    serializer_class= ArticleSerializer
# ok hast
class ArticleUpdate(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset=article.objects.all()
    serializer_class= ArticleSerializer
    #lookup_fields = ['title', 'fav']
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ArticlePost(request):
    serializer_class= ArticleSerializer(data=request.data)
    serializer_class.save()

#class PostArticle(ListCreateAPIView):
#    def posti(request):
#       querset=article.objects.create()
#        serializer_class= ArticleSerializer
#        serializer_class.save()
