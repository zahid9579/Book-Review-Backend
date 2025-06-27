from django.urls import path
from .views import CreateBookView, AllBookView, ReviewBookView, AllReviewsBookView        

urlpatterns = [
    path("api/book/create/", CreateBookView.as_view(), name="create_book"),
    path("api/book/allbooks/", AllBookView.as_view(), name="all_book"),
    path("api/book/review/<int:id>/", ReviewBookView.as_view(), name="review_book"),
    path("api/book/allreview/", AllReviewsBookView.as_view(), name="all_reviews"),
]

