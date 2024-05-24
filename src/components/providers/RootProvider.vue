<template>
  <div>
    <NConfigProvider>
      <NDialogProvider>
        <slot />
      </NDialogProvider>
      <NGlobalStyle />
    </NConfigProvider>
  </div>
</template>

<script setup lang="ts">
import { NConfigProvider, NGlobalStyle, NDialogProvider } from 'naive-ui';
import { darkTheme } from 'naive-ui';
import { useColorMode } from '@vueuse/core';

const mode = useColorMode();
mode.value = 'light';
</script>

<style scoped></style>
