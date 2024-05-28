<template>
  <div class="flex flex-col gap-2">
    <div class="flex flex-row items-center gap-2">
      <div>键：</div>
      <n-tag type="info">key</n-tag>
    </div>
    <vxe-table
      border
      show-overflow
      :column-config="{ resizable: true, useKey: true }"
      :row-config="{ useKey: true, isHover: true }"
      :data="list"
      height="500"
      :scroll-y="{ enabled: true }"
    >
      <vxe-column type="seq" width="40"></vxe-column>
      <vxe-column field="value" title="值"> </vxe-column>
      <vxe-column field="updated_at" title="更新时间"> </vxe-column>
      <vxe-column title="控制">
        <template #default="{ row }">
          <div class="flex flex-row gap-2">
            <n-button type="info" ghost> 回滚 </n-button>
          </div>
        </template>
      </vxe-column>
    </vxe-table>
  </div>
</template>

<script setup lang="ts">
type KvRecord = {
  id: number;
  kv_id: number;
  value: string;
  updated_at: string;
  language: string;
};
const list = ref<KvRecord[]>([
  {
    language: 'Ch',
    value: '不支持该设备',
    updated_at: '2024-05-28T13:49:35.914333',
    id: 2,
    kv_id: 1
  },
  {
    language: 'Ch',
    value: '不支持该设备1',
    updated_at: '2024-05-28T16:39:25.459262',
    id: 6397,
    kv_id: 1
  },
  {
    language: 'Ch',
    value: '不支持该设备12',
    updated_at: '2024-05-28T16:39:44.694133',
    id: 6398,
    kv_id: 1
  },
  {
    language: 'Ch',
    value: '不支持该设备123',
    updated_at: '2024-05-28T16:40:31.475905',
    id: 6399,
    kv_id: 1
  }
]);
</script>

<style scoped></style>
