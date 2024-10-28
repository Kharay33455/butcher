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
    path('my-account/my-investments', views.investments, name='investments'),
    path('my-account/create-new-account', views.create_account, name='create-account'),
    path('my-account/my-investments/<slug:number>/activate', views.activate, name='activate'),
    path('my-account/my-investments/<slug:number>/delete', views.delete, name='delete'),
    path('my-account/my-investments/<slug:number>/pending', views.pending, name='pending'),
    path('my-account/profile', views.profile, name='profile'),
    path('letter/', views.letter, name='letter'),
    path('support/', views.support, name='support'),
    path('support/ticket<slug:number>/', views.ticket, name='ticket'),
    path('support/new-issue', views.new_issue, name='new_issue'),
    path('my-account/profile/withdraw', views.withdraw, name='withdraw'),
    path('my-account/profile/withdraw/set-pin', views.set_pin, name='pin'),
    path('profile/withdrawal_request',views.withdrawal_request, name = 'withdrawals'),
    path('test', views.test, name='test'),

]
