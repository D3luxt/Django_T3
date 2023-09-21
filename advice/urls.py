"""Ken URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Ken import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('productconfig',views.productconfig,name='productconfig'),
    path('paymentAdd',views.paymentAdd,name='paymentAdd'),
    path('index', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('source', views.source, name='source'),
    path('objective', views.objective, name='objective'),
    path('profile', views.profile, name='profile'),
    path('admin/', admin.site.urls),
    path('user/',include('Ken.urls')),
    path('productshow', views.productshow, name='productshow'),
    path('proaddhistory', views.proaddhistory, name='proaddhistory'),
    path('probuyhistory', views.probuyhistory, name='probuyhistory'),
    path('totalsalesaveweb', views.totalsalesaveweb, name='totalsalesaveweb'),
    path('ordershow', views.ordershow, name='ordershow'),
    path('ordershow/showOrder/<int:id>', views.showOrder, name='showOrder'),
    path('productshow/Approved/<int:pro_id>', views.productApproved, name='productApproved'),
    path('productshow/Rejected/<int:pro_id>', views.productRejected, name='productRejected'),
    path('ordershow/orderApproved/<int:or_id>/<int:pro_id_id>', views.orderApproved, name='orderApproved'),
    path('ordershow/Rejected/<int:or_id>', views.orderRejected, name='orderRejected'),
    path('productdelete/<int:pro_id>', views.productdelete, name='productdelete'),
    path('productupdate/<int:pro_id>', views.productupdate, name='productupdate'),
    path('productshow/showUser/<int:id>', views.showUser, name='showUser'),
    path('productshow/showProduct/<int:id>', views.showProduct, name='showProduct'),
    path('productshow/showProduct/productBuy/<int:pro_id>', views.productBuy, name='productBuy'),
    path('totalsaveED/<str:saved>', views.totalsaveED, name='totalsaveED'),
    path('about', views.about, name='about'),
    path('p01', views.p01, name='p01'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
