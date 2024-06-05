<template>
  <n-card
    hoverable
    :content-style="{ padding: '8px 8px 8px 8px' }"
    title="下载所有ts文件(.zip)"
    :header-style="{ padding: '8px 8px 0px 8px' }"
  >
    <div class="flex flex-col gap-2">
      <n-input v-model:value="fileName" placeholder="rbk-i18N.zip" />
      <n-button
        class="mb-2 w-full"
        :loading="isLoading"
        :disabled="isValid"
        type="info"
        @click="downloadBtnClicked"
        >下载ZIP</n-button
      >
    </div>
  </n-card>
</template>

<script setup lang="ts">
import { KvService } from '@/client';
import { useKvStore } from '@/stores/kv';
import { storeToRefs } from 'pinia';

const message = useMessage();
const kvStore = useKvStore();
const isLoading = ref(false);
const fileName = ref('rbk-i18N.zip');
const isValid = computed(() => {
  return fileName.value === '';
});

const downloadBtnClicked = async () => {
  isLoading.value = true;
  // 下载文件
  const downloadUrl = `/api/v1/kv/download-all-with-zip/${fileName.value}`;
  // 创建隐藏的可下载链接
  const element = document.createElement('a');
  element.setAttribute('href', downloadUrl);
  element.setAttribute('download', '');
  document.body.appendChild(element);
  // 触发点击
  element.click();
  // 然后移除
  document.body.removeChild(element);
  message.info('开始下载');
  isLoading.value = false;
};
</script>

<style scoped></style>
