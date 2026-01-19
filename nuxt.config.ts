import { defineNuxtConfig } from "nuxt/config";

export default defineNuxtConfig({
  modules: ["motion-v/nuxt"],

  ssr: false,

  typescript: {
    strict: true,
  },

  css: ["~/assets/css/global.css", "~/public/bitcamp-brand/bitcamp.css"],
  compatibilityDate: "2024-09-13",
});
