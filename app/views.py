from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import BookSerializer, ReviewSerializer
from .models import Book,Review

# To Create/Add a  new Boook
class CreateBookView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response( {"msg": "Book Created Successfully!", "response": serializer.data}, status=status.HTTP_201_CREATED)
            
            except Exception as e:
                return Response({"msg": "Something went wrong", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"msg": "Validation Failed", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# To List all the Books
class AllBookView(APIView):
    def get(self, request):
        try:
            all_books = Book.objects.all()
            serializer = BookSerializer(all_books, many=True)
            return Response({"msg": "All Books", "data": serializer.data}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"msg": "Failed to fetch all books", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)     
        
        

#  To Post a review
class ReviewBookView(APIView):
    def post(self, request, id):
        try:
            book = Book.objects.get(id=id)
            
        except Book.DoesNotExist:
            return Response({"msg": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

        # Add book reference to review data
        data = request.data.copy()
        data['book'] = book.id 

        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({"msg": "Review submitted successfully", "data": serializer.data}, status=status.HTTP_201_CREATED )
            except Exception as e:
                return Response({"msg": "Error while saving review", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"msg": "Validation failed", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            
            
            
# To list all the reviews Books
class AllReviewsBookView(APIView):
    def get(self, request):
        try:
            all_reviews = Review.objects.all()
            serializer = ReviewSerializer(all_reviews, many=True)
            return Response({"msg": "All reviews for books", "data": serializer.data}, status=status.HTTP_200_OK)

        except Exception as a: 
            return Response({"msg": "something went wrong", "errors":serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    