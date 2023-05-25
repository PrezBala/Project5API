from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer, UserSerializer


class IsAdminUser(permissions.BasePermission):
    """
    Custom permission to only allow admins to edit or delete a movie.
    """
    def has_permission(self, request, view):
        # Write permissions are only allowed to admin users.
        return bool(request.user and request.user.is_staff)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, IsAdminUser,)

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user

            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = (
                    {
                        'message': 'Rating updated',
                        'result': serializer.data
                    }
                )
                return Response(response, status=status.HTTP_200_OK)
            except Rating.DoesNotExist:
                rating = Rating.objects.create(
                    user=user,
                    movie=movie,
                    stars=stars
                )
                serializer = RatingSerializer(rating, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            response = {'message': 'provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant update rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You cant create rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
