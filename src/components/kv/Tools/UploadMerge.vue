<template>
  <n-card
    hoverable
    :content-style="{ padding: '8px 8px 8px 8px' }"
    title="新文件合并"
    :header-style="{ padding: '8px 8px 0px 8px' }"
  >
    <div class="flex flex-col gap-2">
      <n-select v-model:value="langName" :options="langList" placeholder="选择合并语言"></n-select>
      <n-upload
        ref="uploadRef"
        multiple
        directory-dnd
        accept=".ts"
        action="/api/v1/kv/upload-file"
        :max="1"
        :on-finish="onFileUploadFinish"
        :on-remove="onFileRemove"
      >
        <n-upload-dragger>
          <div style="margin-bottom: 12px">
            <n-icon size="48" :depth="3">
              <archive-icon />
            </n-icon>
          </div>
          <n-p depth="3" style="margin: 8px 0 0 0"> 点击或者拖动ts文件到该区域来上传 </n-p>
        </n-upload-dragger>
      </n-upload>
      <n-button
        class="mb-2 w-full"
        :disabled="isValid"
        :loading="mergeIsLoading"
        @click="mergeCheckBtnCLicked"
      >
        合并检查
      </n-button>
    </div>
  </n-card>
</template>

<script setup lang="ts">
import { KvService } from '@/client';
import { useKvStore, type MergeCheckItem } from '@/stores/kv';
import { ArchiveOutline as ArchiveIcon } from '@vicons/ionicons5';
import type { NUpload, UploadFileInfo } from 'naive-ui';
import { storeToRefs } from 'pinia';

const kvStore = useKvStore();
const { langList, kvEditStatus, mergeCheckLang, mergeCheckFilePath, mergeIsLoading } =
  storeToRefs(kvStore);

const uploadRef = ref<InstanceType<typeof NUpload>>();
const langName = ref(null);
const fileUploaded = ref<string>('');
const message = useMessage();

const onFileUploadFinish = (options: { file: UploadFileInfo; event?: ProgressEvent }) => {
  fileUploaded.value = options.file.name;
};

const onFileRemove = (options: {
  file: UploadFileInfo;
  fileList: Array<UploadFileInfo>;
  index: number;
}) => {
  fileUploaded.value = '';
  return true;
};
const isValid = computed(() => {
  return fileUploaded.value === '' || langName.value === null;
});

const mergeCheckBtnCLicked = async () => {
  if (kvEditStatus.value === 'merge-check') {
    message.warning('请先完成当前合并检查');
    return;
  }
  mergeIsLoading.value = true;
  mergeCheckLang.value = langName.value;
  mergeCheckFilePath.value = fileUploaded.value;
  setTimeout(() => {
    langName.value = null;
    uploadRef.value.clear();
    mergeIsLoading.value = false;
  }, 10000);
  kvEditStatus.value = 'merge-check';
  langName.value = null;
  uploadRef.value.clear();
};
</script>

<style scoped></style>
