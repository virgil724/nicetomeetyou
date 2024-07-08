<template>

    <div class="px-[10%] py-[1rem]">
        <h1 class="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl">
            {{ posts!.title }}
        </h1>
        <figure class="photo_center photo-story">
            <img style="aspect-ratio: 1279/856;" :src="posts!.news_photo[0].imgUrl"
                :title="posts!.news_photo[0].comment" :alt="posts!.news_photo[0].comment">
            <figcaption>{{ posts!.news_photo[0].comment }}</figcaption>
        </figure>
        <div class="content" v-html="posts!.content">
        </div>

    </div>

</template>
<script lang="ts" setup>
import type { NewsDetail } from '~/utils/typesdeclare';


const { params: { id } } = useRoute();
const { data: posts, status, error, refresh, clear } = await useFetch<NewsDetail>(`/api/nba-detail/${id}/`, {
})


</script>

<style scoped>
.photo_center {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 80vw
}

.content {
    :deep(p) {
        line-height: 1.75rem;
        margin-top: 30px;
        text-indent: 1em;

    }

    :deep(.embedded-content) {
        margin-left: auto;
        margin-right: auto;
        width: 500px
    }

    :deep(.video-container),
    :deep(.photo_center) {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 80vw
    }



    :deep(.embedded-content+p+p) {
        text-align: center;
        display: none;

    }
}
</style>
