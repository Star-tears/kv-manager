<template>
  <div class="flex flex-col gap-4">
    <n-card title="操作栏" :header-style="{ padding: '4px 4px 4px 12px' }" />
    <DownloadZip />
    <DownloadSelect />
    <UploadMerge />
    <UploadNewLang />
  </div>
</template>

<script setup lang="ts">
import DownloadZip from './Tools/DownloadZip.vue';
</script>

<style scoped></style>
