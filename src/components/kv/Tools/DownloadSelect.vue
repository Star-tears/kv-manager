<template>
  <n-card
    hoverable
    :content-style="{ padding: '8px 8px 8px 8px' }"
    title="下载ts文件"
    :header-style="{ padding: '8px 8px 0px 8px' }"
  >
    <div class="flex flex-col gap-2">
      <n-select></n-select>
      <n-button class="mb-2 w-full">下载</n-button>
    </div>
  </n-card>
</template>

<script setup lang="ts"></script>

<style scoped></style>
