<template>
    <Table class="mx-10">
        <TableHeader>
            <TableRow>
                <TableHead class="w-[30%]">
                    Thumbnail
                </TableHead>
                <TableHead class="w-[70%]">Title</TableHead>

            </TableRow>
        </TableHeader>
        <TableBody>

            <TableRow @click="handleOnClick(item.id)" v-for="item in data" :id="item.id">
                <TableCell>
                    <img :src="item.news_photo[0].imgUrl" alt="" class="h-[150px]">
                </TableCell>
                <TableCell class='text-xl'>{{ item.title }}
                </TableCell>
            </TableRow>
        </TableBody>
    </Table>
</template>

<script setup lang="ts">
import type { News } from '../utils/typesdeclare'
const { data, status, error, refresh, clear } = await useFetch<Array<News>>('/api/nba/', {
})
const router = useRouter();
const handleOnClick = (id: number) => {

    router.push({ path: `/nba/${id}` })
}
</script>