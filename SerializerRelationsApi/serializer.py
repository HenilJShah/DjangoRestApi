from rest_framework import serializers

from .models import Singer, Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration']


class SingerSerializer(serializers.ModelSerializer):
    # TODO: https://www.django-rest-framework.org/api-guide/relations/#serializer-relations
    # read it DOCS if you have any doubt

    # Note: https://www.django-rest-framework.org/api-guide/relations/#stringrelatedfield
    # songs = serializers.StringRelatedField(many=True, read_only=True)

    # Note: https://www.django-rest-framework.org/api-guide/relations/#primarykeyrelatedfield
    # songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # Note: https://www.django-rest-framework.org/api-guide/relations/#hyperlinkedrelatedfield
    # view_name - The view name that should be used as the target of the relationship. If you're using the standard router classes this will be a string with the format <modelname>-detail. required.
    # songs = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')

    # Note: slug_field - The field on the target that should be used to represent it. This should be a field that uniquely identifies any given instance. For example, username. required
    # songs = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    # Note: https://www.django-rest-framework.org/api-guide/relations/#hyperlinkedidentityfield
    # view_name - The view name that should be used as the target of the relationship. If you're using the standard router classes this will be a string with the format <model_name>-detail. required.
    songs = serializers.HyperlinkedIdentityField(view_name='song-detail')

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'songs']
