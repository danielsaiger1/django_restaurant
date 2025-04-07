"""
Serializers for restaurant APIs
"""
from rest_framework import serializers

from core.models import (
    Restaurant,
    Tag,
    )


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tags"""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']


class RestaurantSerializer(serializers.ModelSerializer):
    """Serializer for restaurants."""
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Restaurant
        fields = [
            'id', 'name', 'description', 'address',
            'link', 'tags',
        ]
        read_only_fields = ['id']

    def _get_or_create_tags(self, tags, restaurant):
        """Handle getting or creating tags as needed"""
        auth_user = self.context['request'].user  # gets the authenticated user
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(
                user=auth_user,
                **tag
            )
            restaurant.tags.add(tag_obj)

    def create(self, validated_data):
        """Create a restaurant"""
        tags = validated_data.pop('tags', [])
        ingredients = validated_data.pop('ingredients', [])
        restaurant = Restaurant.objects.create(**validated_data)
        self._get_or_create_tags(tags, restaurant)

        return restaurant

    def update(self, instance, validated_data):
        """Update a restaurant"""
        tags = validated_data.pop('tags', None)
        if tags is not None:
            instance.tags.clear()
            self._get_or_create_tags(tags, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

            instance.save()

        return instance


class RestaurantDetailSerializer(RestaurantSerializer):
    """Serializer for restaurant detail view"""

    class Meta(RestaurantSerializer.Meta):
        fields = RestaurantSerializer.Meta.fields + ['description', 'image'] #!!!!


class RestaurantImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to restaurants"""

    class Meta:
        model = Restaurant
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image': {'required': 'True'}}
