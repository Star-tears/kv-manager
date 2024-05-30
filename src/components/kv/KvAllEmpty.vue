<template>
  <div
    class="flex h-full flex-col gap-3"
    v-motion
    :initial="{
      opacity: 0,
      y: 100
    }"
    :enter="{
      opacity: 1,
      y: 0,
      transition: {
        duration: 500,
        type: 'keyframes',
        ease: 'easeInOut'
      }
    }"
  >
    <n-breadcrumb separator=">">
      <n-breadcrumb-item @click="backHome"> home</n-breadcrumb-item>
      <n-breadcrumb-item> all-empty</n-breadcrumb-item>
    </n-breadcrumb>
    <div class="h-0 grow">
      <vxe-table
        ref="tableRef"
        border
        show-overflow
        :column-config="{ resizable: true, useKey: true }"
        :row-config="{ useKey: true, isHover: true }"
        :edit-config="{ trigger: 'dblclick', mode: 'cell' }"
        :data="list"
        height="auto"
        :scroll-y="{ enabled: true, oSize: 80 }"
      >
        <vxe-column type="seq" width="40"></vxe-column>
        <vxe-column field="lang_key" title="键语种" width="100" sortable> </vxe-column>
        <vxe-column field="key" title="键" sortable> </vxe-column>
        <vxe-column field="lang_value" title="值语种" width="100" sortable> </vxe-column>
        <vxe-column
          field="value"
          title="新值"
          :edit-render="{ autofocus: '.vxe-input--inner' }"
          sortable
        >
          <template #edit="{ row }">
            <NInput
              v-model:value="row.value"
              type="text"
              placeholder="请输入值"
              @change="valueChangeEvent(row)"
            >
            </NInput>
          </template>
        </vxe-column>
      </vxe-table>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { KvService } from '@/client';
import { useKvStore, type CheckEmptyItem } from '@/stores/kv';
import { storeToRefs } from 'pinia';
import type { VxeTable } from 'vxe-table';

const kvStore = useKvStore();
const { kvEditStatus, checkEmptyCount, checkEmptyIsLoading } = storeToRefs(kvStore);
const tableRef = ref<InstanceType<typeof VxeTable>>(null);
const list = ref<CheckEmptyItem[]>([]);
const message = useMessage();

watch(checkEmptyCount, async () => {
  const res = await KvService.kvGetAllNullValueKv({
    requestBody: {
      lang: 'English'
    }
  });
  if (res.code === 0) {
    list.value = res.data as CheckEmptyItem[];
    checkEmptyIsLoading.value = false;
  }
});

onMounted(async () => {
  const res = await KvService.kvGetAllNullValueKv({
    requestBody: {
      lang: 'English'
    }
  });
  if (res.code === 0) {
    list.value = res.data as CheckEmptyItem[];
    checkEmptyIsLoading.value = false;
  }
});

const backHome = () => {
  kvEditStatus.value = 'main';
};

const valueChangeEvent = (row: CheckEmptyItem) => {
  KvService.kvUpdateKv({
    requestBody: {
      key: row.key,
      langKey: row.lang_key,
      value: row.value,
      langValue: row.lang_value,
      kvId: row.kv_id
    }
  });
};
</script>
<style>
.keyword-lighten {
  background-color: yellow;
}
</style>
