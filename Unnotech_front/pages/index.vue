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

            <TableRow @click="handleOnClick(id)" v-for="(item, id) in data" :id="id">
                <TableCell>
                    <img :src="item.news_photo.imgUrl" alt="" class="h-[150px]">
                </TableCell>
                <TableCell class='text-xl'>{{ item.title }}
                </TableCell>
            </TableRow>
        </TableBody>
    </Table>
</template>

<script setup lang="ts">
import data from "~/assets/example.json";


const router = useRouter();
const handleOnClick = (id) => {

    console.log(id)
    router.push({ path: `/nba/${id}` })
}
</script>