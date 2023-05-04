from django.urls import path
from CompoMaker import views

# not needed
app_name = "compo_maker"


urlpatterns = []
urlpatterns += [
    path('', views.home, name='home'),
    # path('minigames/<int:minigame_chosen_id>/', views.minigames, name='minigames_id'),
    ]