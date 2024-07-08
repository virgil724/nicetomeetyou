<template>
  <div>
    <NuxtPage />
  </div>
  <Toaster />
</template>
<script lang="ts" setup>
import { useToast } from '@/components/ui/toast/use-toast'
const { toast } = useToast()
const popToast = (description: string) => {
  console.log('click')
  toast({
    title: '有新新聞',
    description: description,
  });
}
const ws = new WebSocket("ws://localhost:8000/ws/nba/")
ws.onopen = function () {
  ws.send(JSON.stringify({
    action: "subscribe_to_news_activity",
    request_id: new Date().getTime(),
  }))
}
ws.onmessage = function (e) {
  const { title } = JSON.parse(e.data)
  popToast(title)
}


</script>