import { defineNuxtConfig } from "nuxt/config";

export default defineNuxtConfig({
  devServer: {
    host: "0.0.0.0",
  },

  app: {
    head: {
      meta: [
        { name: "viewport", content: "width=device-width, initial-scale=1" },
      ],
      link: [
        { rel: "preconnect", href: "https://fonts.googleapis.com" },
        { rel: "preconnect", href: "https://fonts.gstatic.com", crossorigin: "" },
        { rel: "stylesheet", href: "https://fonts.googleapis.com/css2?family=Caveat:wght@400;700&display=swap" },
      ],
    },
  },

  modules: ["motion-v/nuxt"],

  ssr: false,

  typescript: {
    strict: true,
  },

  css: ["~/assets/css/global.css", "~/public/bitcamp-brand/bitcamp.css"],
  compatibilityDate: "2024-09-13",
});
