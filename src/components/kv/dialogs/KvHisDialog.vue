<template>
  <div class="flex flex-col gap-2">
    <div class="flex flex-row items-center gap-2">
      <div>键：</div>
      <n-tag type="info">{{ props.kv_key }}</n-tag>
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
      <vxe-column title="控制" width="90">
        <template #default="{ row }">
          <div class="flex flex-row gap-2">
            <n-button
              type="info"
              ghost
              :loading="rollBackLoadingId === row.id"
              @click="rollBackClick(row)"
            >
              回滚
            </n-button>
          </div>
        </template>
      </vxe-column>
    </vxe-table>
  </div>
</template>

<script setup lang="ts">
import { KvService } from '@/client';

type KvRecord = {
  id: number;
  kv_id: number;
  value: string;
  updated_at: string;
  language: string;
};

type Props = {
  kv_id: number;
  kv_key: string;
  lang_value: string;
};

const props = defineProps<Props>();
const emit = defineEmits<{
  (e: 'update-kv', kv_value: string): void;
}>();

const list = ref<KvRecord[]>(null);
const rollBackLoadingId = ref<number>();

onMounted(() => {
  KvService.kvGetKvRecord({
    requestBody: {
      langValue: props.lang_value,
      kvId: props.kv_id
    }
  }).then((res) => {
    if (res.code == 0) {
      list.value = res.data as KvRecord[];
    }
  });
});
const rollBackClick = (row: KvRecord) => {
  rollBackLoadingId.value = row.id;
  emit('update-kv', row.value);
};
</script>

<style scoped></style>
