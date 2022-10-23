from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('categories/', views.CategoriesView.as_view()),
    path('transaction/', views.TransactionView.as_view()),
    path('piggy_bank/', views.PiggyBankView.as_view()),


]

'''
10100
10111
11111
10010

10100
10111
11122
1222


63

 3
3 

443


123
321

444

222  
222


443

172
271











1 2 3 5 8 * * * * * _

 '''