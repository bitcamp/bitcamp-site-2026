import { defineNuxtConfig } from "nuxt/config";

export default defineNuxtConfig({
  devServer: {
    host: "0.0.0.0",
  },

  modules: ["motion-v/nuxt"],

  ssr: false,

  typescript: {
    strict: true,
  },

  css: ["~/assets/css/global.css", "~/public/bitcamp-brand/bitcamp.css"],
  compatibilityDate: "2024-09-13",
});
