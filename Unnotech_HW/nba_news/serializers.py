from rest_framework import serializers

from .models import News, News_Photo


class NewsPhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = News_Photo
        fields = ("imgUrl", "comment")


class NewsDetailSerializers(serializers.ModelSerializer):
    news_photo = NewsPhotoSerializers(many=True)

    class Meta:
        model = News
        fields = "__all__"

    def create(self, validated_data):
        news_photos = validated_data.pop("news_photo")
        news = News.objects.create(**validated_data)
        for news_photo in news_photos:
            News_Photo.objects.create(news=news, **news_photo)

        return news


class NewsSerializers(serializers.ModelSerializer):
    news_photo = NewsPhotoSerializers(many=True, read_only=True)

    class Meta:
        model = News
        fields = ["id", "title", "author", "paper", "news_photo"]
