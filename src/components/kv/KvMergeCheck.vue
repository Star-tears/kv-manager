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
      <n-breadcrumb-item> merge-check</n-breadcrumb-item>
    </n-breadcrumb>
    <div class="h-0 grow">
      <vxe-table
        ref="tableRef"
        border
        show-overflow
        :column-config="{ resizable: true, useKey: true }"
        :row-config="{ useKey: true, isHover: true }"
        :edit-config="{ trigger: 'dblclick', mode: 'cell' }"
        :data="mergeCheckItemList"
        height="auto"
        :scroll-y="{ enabled: true }"
      >
        <vxe-column type="seq" width="60"></vxe-column>
        <vxe-column field="lang_key" title="键语种" width="100"> </vxe-column>
        <vxe-column field="key" title="键"> </vxe-column>
        <vxe-column field="lang_value" title="值语种" width="100"> </vxe-column>
        <vxe-column field="curr_value" title="当前值"> </vxe-column>
        <vxe-column
          field="new_value"
          title="新值"
          :edit-render="{ autofocus: '.vxe-input--inner' }"
        >
          <template #edit="{ row }">
            <NInput v-model:value="row.new_value" type="text" placeholder="请输入值"> </NInput>
          </template>
        </vxe-column>
        <vxe-column title="控制" width="150">
          <template #default="{ row }">
            <div class="flex flex-row gap-2">
              <n-button ghost :loading="isLoadingIndex === row.id" @click="merge(row)">
                合并
              </n-button>
            </div>
          </template>
        </vxe-column>
      </vxe-table>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { KvService } from '@/client';
import { useKvStore, type MergeCheckItem } from '@/stores/kv';
import { storeToRefs } from 'pinia';
import type { VxeTable } from 'vxe-table';

const kvStore = useKvStore();
const { mergeCheckItemList, kvEditStatus } = storeToRefs(kvStore);
const tableRef = ref<InstanceType<typeof VxeTable>>(null);
const isLoadingIndex = ref(-1);
const message = useMessage();
const backHome = () => {
  kvEditStatus.value = 'main';
};

const merge = async (row: MergeCheckItem) => {
  isLoadingIndex.value = row.id;
  const res = await KvService.kvUpdateKv({
    requestBody: {
      key: row.key,
      langKey: row.lang_key,
      value: row.new_value,
      langValue: row.lang_value
    }
  });
  if (res.code === 0) {
    await tableRef.value?.remove(row);
    message.success('合并成功');
  } else {
    message.error('Something error');
  }
};
</script>
<style>
.keyword-lighten {
  background-color: yellow;
}
</style>
