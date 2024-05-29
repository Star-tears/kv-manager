<template>
  <n-card
    hoverable
    :content-style="{ padding: '8px 8px 8px 8px' }"
    title="下载ts文件"
    :header-style="{ padding: '8px 8px 0px 8px' }"
  >
    <div class="flex flex-col gap-2">
      <n-select v-model:value="downloadLangValue" :options="downloadAllowList"></n-select>
      <n-button
        class="mb-2 w-full"
        :loading="isLoading"
        :disabled="isValid"
        @click="downloadBtnClicked"
        >下载</n-button
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
const { langList } = storeToRefs(kvStore);
const isLoading = ref(false);
const downloadLangValue = ref('');
const downloadAllowList = computed(() => {
  return langList.value.filter((item) => item.value !== 'English');
});
const isValid = computed(() => {
  return downloadLangValue.value === '';
});

const downloadBtnClicked = async () => {
  isLoading.value = true;
  const res = await KvService.kvGenTs({
    requestBody: {
      lang: downloadLangValue.value
    }
  });
  if (res.code === 0) {
    const filePath = (res.data as Record<string, any>)['file_path'];
    // 下载文件
    const downloadUrl = `/api/v1/kv/download-file/${filePath}`;
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
  }
  isLoading.value = false;
};
</script>

<style scoped></style>
