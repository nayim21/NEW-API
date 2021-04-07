from django.urls import path , include
from .views import ArticleList,ArticleCustomList,ArticleDetail,ArticleUpdate,ArticleDestroy,ArticlePost#,PostArticle

app_name="backend"
urlpatterns = [
    path ("list",ArticleList.as_view(),name="list1"),
    path ("post",ArticlePost),
    #path ("post2",PostArticle.as_view(),name="post"),
    path ("customlist",ArticleCustomList.as_view(),name="customlist"),
    path ("destroylist",ArticleDestroy.as_view(),name="destroy"),
    #path ("<int:pk>" , ArticleDetail.as_view() , name="detail"),
    path ("<int:pk>", ArticleUpdate.as_view(),name="update"),

    ]
