
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home, name="Home"),
    path("category/<slug:category_slug>",views.Home, name="FilterCategory"),
    path("Details/<slug:slug>/",views.BookDetailsView.as_view(), name="bookDetails"),
    path("return/<int:id>/",views.BookReturn, name="returnbook"),
    path("accounts/",include("accounts.urls")),
    path("transaction/",include("transactions.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
