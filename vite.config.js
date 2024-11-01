import { defineConfig } from 'vite'
import { fileURLToPath, URL } from 'node:url'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  build: {
    outDir: 'dist',  // Ensure the build output is in the "dist" directory
    assetsDir: 'static',  // Put static assets in the "static" folder inside "dist"
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
})