<template>
  <n-card :content-style="{ padding: '8px 8px 8px 8px' }">
    <n-upload
      multiple
      directory-dnd
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
  </n-card>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { ArchiveOutline as ArchiveIcon } from '@vicons/ionicons5';

export default defineComponent({
  components: {
    ArchiveIcon
  }
});
</script>
