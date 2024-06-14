from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.base, name='home'),
    path('about-us/', views.about_us, name='about-us'),
    path('about-us/principles/', views.principles, name='principles'),
    path('about-us/history', views.history, name='history'),
    path('about-us/global-impact/', views.global_impact, name='global-impact'),
    path('about-us/doing-business-with-kaizen/', views.business, name='business'),
    path('news-overview/', views.news, name='news'),
    path('insights/kaizen-investment-stewardship/', views.kis, name='kis'),
    path('insights/our-approach-to-sustainability/', views.sustainability, name='sustainability'),
    path('insights/long-term-capitalism/', views.capitalism, name='capitalism'),
    path('insights/disclaimer', views.disclaimer, name='disclaimer'),
    path('join-us/start-investing', views.investing, name='investing'),
    path('login', views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('logout-user', views.logout_request, name='logout'),
    path('my-kaizen/my-investments', views.investments, name='investments'),
    path('my-kaizen/create-new-account', views.create_account, name='create-account'),
    path('my-kaizen/my-investments/<slug:number>/activate', views.activate, name='activate'),
    path('my-kaizen/my-investments/<slug:number>/delete', views.delete, name='delete'),
    path('my-kaizen/my-investments/<slug:number>/pending', views.pending, name='pending'),
    path('my-kaizen/profile', views.profile, name='profile'),

]
