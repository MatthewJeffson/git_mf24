<script setup>
import { RouterView, useRouter } from 'vue-router';
import { NLayout, NLayoutContent, NFlex, NScrollbar, NModalProvider, NDialogProvider, NMessageProvider } from 'naive-ui';
import Header from './components/Header.vue';
import { onMounted } from 'vue';

const router = useRouter();

// Page switching logic: Switch from ViewPage to security_camera after 10 seconds, and back after 30 seconds.
onMounted(() => {
  // After 10 seconds, navigate to the security camera page
  setTimeout(() => {
    router.push('/security-camera');
  }, 100000); // 10 seconds delay

  // After 30 seconds (from the start), navigate back to the ViewPage
  setTimeout(() => {
    router.push('/');
  }, 300000); // 30 seconds delay
});
</script>

<template>
  <n-layout class="main-layout">
    <n-flex vertical class="main-layout">
      <!-- Header component -->
      <Header />
      
      <!-- Main Content -->
      <n-layout-content :content-style="{ width: '80%', margin: '20px auto'}">
        <n-scrollbar>
          <n-message-provider>
            <n-dialog-provider>
              <n-modal-provider>
                <!-- Router View to display the current page -->
                <RouterView />
              </n-modal-provider>
            </n-dialog-provider>
          </n-message-provider>
        </n-scrollbar>
      </n-layout-content>
    </n-flex>
  </n-layout>
</template>

<style>
html, body, #app, .main-layout {
  width: 100%;
  height: 100%;
}

html, body {
  margin: 0;
}

/* cancel the default style of router */
.router-link-active {
  text-decoration: none;
  color: #fff;
}
a {
  text-decoration: none;
  color: #fff;
}
</style>