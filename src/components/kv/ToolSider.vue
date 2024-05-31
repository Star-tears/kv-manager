<template>
  <div class="flex flex-col gap-4">
    <n-card title="操作栏" :header-style="{ padding: '4px 4px 4px 12px' }" />
    <DownloadZip />
    <AddNewKv />
    <DownloadSelect />
    <CheckAllEmpty />
    <UploadMerge />
    <UploadNewLang />
    <DeleteLang />
  </div>
</template>

<script setup lang="ts">
import AddNewKv from './Tools/AddNewKv.vue';
import CheckAllEmpty from './Tools/CheckAllEmpty.vue';
import DeleteLang from './Tools/DeleteLang.vue';
import DownloadZip from './Tools/DownloadZip.vue';
</script>

<style scoped></style>
