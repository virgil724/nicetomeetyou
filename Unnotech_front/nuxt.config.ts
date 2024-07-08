// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  ssr: false,
  modules: ["@nuxtjs/tailwindcss", "shadcn-nuxt"],
  shadcn: {
    /**
     * Prefix for all the imported component
     */
    prefix: '',
    /**
     * Directory that the component lives in.
     * @default "./components/ui"
     */
    componentDir: './components/ui'
  }
  ,
  app: {
    head: {
      script: [
        { src: "https://platform.twitter.com/widgets.js" }
      ]
    },
  },
  nitro: {
    devProxy: {
      '/api/': 'http://127.0.0.1:8000/api/'
    }
  }

})