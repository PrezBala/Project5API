from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.action == 'rate_movie':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]

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
                response = {
                    'message': 'Rating updated',
                    'result': serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
            except Rating.DoesNotExist:
                rating = Rating.objects.create(
                    user=user,
                    movie=movie,
                    stars=stars
                )
                serializer = RatingSerializer(rating, many=False)
                response = {
                    'message': 'Rating created',
                    'result': serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'Provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.action in ['update', 'create']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]

    def update(self, request, *args, **kwargs):
        response = {'message': 'You cannot update the rating like that'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You cannot create the rating like that'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)
