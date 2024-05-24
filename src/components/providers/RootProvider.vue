<template>
  <div>
    <NConfigProvider>
      <NDialogProvider>
        <n-message-provider>
          <NNotificationProvider>
            <slot />
          </NNotificationProvider>
        </n-message-provider>
      </NDialogProvider>
      <NGlobalStyle />
    </NConfigProvider>
  </div>
</template>

<script setup lang="ts">
import {
  NConfigProvider,
  NGlobalStyle,
  NDialogProvider,
  NMessageProvider,
  NNotificationProvider
} from 'naive-ui';
import { darkTheme } from 'naive-ui';
import { useColorMode } from '@vueuse/core';

const mode = useColorMode();
mode.value = 'light';
</script>

<style scoped></style>
