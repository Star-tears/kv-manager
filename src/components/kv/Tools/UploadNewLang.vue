<template>
  <n-card
    hoverable
    :content-style="{ padding: '8px 8px 8px 8px' }"
    title="上传新语言(ts文件)"
    :header-style="{ padding: '8px 8px 0px 8px' }"
  >
    <div class="flex flex-col gap-2">
      <n-input v-model:value="newLangName" placeholder="语言名称"></n-input>
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
        :loading="isLoading"
        type="info"
        @click="addNewLangBtnCLicked"
        >新增语言</n-button
      >
    </div>
  </n-card>
</template>

<script setup lang="ts">
import { KvService } from '@/client';
import { useKvStore } from '@/stores/kv';
import { ArchiveOutline as ArchiveIcon } from '@vicons/ionicons5';
import type { NUpload, UploadFileInfo } from 'naive-ui';

const kvStore = useKvStore();

const uploadRef = ref<InstanceType<typeof NUpload>>();
const newLangName = ref('');
const fileUploaded = ref<string>('');
const isLoading = ref(false);
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
  return fileUploaded.value === '' || newLangName.value === '';
});

const addNewLangBtnCLicked = async () => {
  isLoading.value = true;
  const res = await KvService.kvUploadNewLang({
    requestBody: {
      lang: newLangName.value,
      path: fileUploaded.value
    }
  });
  if (res.code === 0) {
    kvStore.refreshLanglist();
    message.success('新增语言成功');
    newLangName.value = '';
    fileUploaded.value = '';
    uploadRef.value.clear();
  }
  isLoading.value = false;
};
</script>

<style scoped></style>
