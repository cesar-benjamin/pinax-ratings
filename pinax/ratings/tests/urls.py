from django.urls import include, re_path

urlpatterns = [
    re_path(r"^", include("pinax.ratings.urls", namespace="pinax_ratings")),
]
