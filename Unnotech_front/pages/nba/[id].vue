<template>

    <div class="px-[10%] py-[1rem]">
        <h1 class="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl">
            {{ posts.full_title }}
        </h1>
        <div class="content" v-html="posts.content">
        </div>

    </div>

</template>
<script lang="ts" setup>
import data from "~/assets/example.json";

const { params: { id } } = useRoute();
const posts = computed(() => data[id])

</script>

<style scoped>
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
