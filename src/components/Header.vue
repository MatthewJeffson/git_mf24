<script setup>
import { ref } from 'vue';
import { NFlex, NH1, NLayoutHeader, NIcon, NButton } from 'naive-ui';
import { Settings } from '@vicons/ionicons5';
import logoUrl from '../assets/logo.jpg';
import { RouterLink, useRouter } from 'vue-router';

const router = useRouter();

// Navbar visibility state, default is hidden
const isNavbarVisible = ref(false);

// Toggle navbar visibility
const toggleNavbar = () => {
  isNavbarVisible.value = !isNavbarVisible.value;
};
</script>

<template>
  <!-- Toggle Navbar Button -->
  <n-button @click="toggleNavbar" style="position: fixed; right: 20px; top: 20px; z-index: 1001;">
    <!-- Show the text "Hide Navbar" when the navbar is visible -->
    <template v-if="isNavbarVisible">
      Hide Navbar
    </template>

    <!-- Show the logo image when the navbar is hidden -->
    <template v-else>
      <img :src="logoUrl" alt="Show Navbar" style="width: 100px;" />
    </template>
  </n-button>

  <!-- Conditionally render the navbar based on `isNavbarVisible` -->
  <n-layout-header
    v-if="isNavbarVisible"
    style="padding-left: 20px; padding-right: 20px; position: fixed; top: 0; width: 100%; z-index: 1000;"
    bordered
  >
    <n-flex justify="space-between" align="center" size="large">
      <fragment>
        <n-flex align="center" size="small">
          <router-link to="/">
            <img
              width="200"
              :src="logoUrl"
              alt="logo"
              style="display: block; margin: auto"
            />
          </router-link>
        </n-flex>
      </fragment>

      <n-h1 style="margin-right: 150px;">Dashboard</n-h1>

      <router-link to="/settings">
        <n-button text>
          <template #icon>
            <n-icon>
              <Settings />
            </n-icon>
          </template>
          Settings
        </n-button>
      </router-link>
    </n-flex>
  </n-layout-header>
</template>

<style scoped>
/* Add padding to avoid content being hidden behind the navbar */
body {
  padding-top: 60px;
}
</style>