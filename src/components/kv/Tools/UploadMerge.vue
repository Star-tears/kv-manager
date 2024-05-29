<template>
  <n-card
    hoverable
    :content-style="{ padding: '8px 8px 8px 8px' }"
    title="新文件合并"
    :header-style="{ padding: '8px 8px 0px 8px' }"
  >
    <div class="flex flex-col gap-2">
      <n-upload
        multiple
        directory-dnd
        accept=".ts"
        action="https://www.mocky.io/v2/5e4bafc63100007100d8b70f"
        :max="1"
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
      <n-button class="mb-2 w-full">合并检查</n-button>
    </div>
  </n-card>
</template>

<script setup lang="ts">
import { ArchiveOutline as ArchiveIcon } from '@vicons/ionicons5';
import type { UploadFileInfo } from 'naive-ui';

const fileSet = ref<Set<string>>(new Set<string>());

const onFileUploadFinish = (options: { file: UploadFileInfo; event?: ProgressEvent }) => {
  fileSet.value.add(options.file.name);
};

const onFileRemove = (options: {
  file: UploadFileInfo;
  fileList: Array<UploadFileInfo>;
  index: number;
}) => {
  fileSet.value.delete(options.file.name);
  return true;
};
</script>
