from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.observer.generics import (
    action,
)
from rest_framework.utils.serializer_helpers import ReturnDict

from .models import News
from .serializers import NewsSerializers


class NewsConsumer(GenericAsyncAPIConsumer):
    queryset = News.objects.all()
    serializer_class = NewsSerializers

    @model_observer(News)
    async def news_activity(
        self,
        message: ReturnDict,
        observer=None,
        subscribing_request_ids=[],
        **kwargs,
    ):
        await self.send_json(dict(message))

    @news_activity.serializer
    def news_activity(self, instance: News, action, **kwargs) -> ReturnDict:
        """This will return the comment serializer"""

        return NewsSerializers(instance).data

    @action()
    async def subscribe_to_news_activity(self, request_id, **kwargs):
        await self.news_activity.subscribe(request_id=request_id)
