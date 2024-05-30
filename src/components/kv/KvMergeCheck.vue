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
        :data="list"
        height="auto"
        :scroll-y="{ enabled: true }"
      >
        <vxe-column type="seq" width="40"></vxe-column>
        <vxe-column field="lang_key" title="键语种" width="100" sortable> </vxe-column>
        <vxe-column field="key" title="键" sortable> </vxe-column>
        <vxe-column field="lang_value" title="值语种" width="100" sortable> </vxe-column>
        <vxe-column field="curr_value" title="当前值" sortable> </vxe-column>
        <vxe-column
          field="new_value"
          title="新值"
          :edit-render="{ autofocus: '.vxe-input--inner' }"
          sortable
        >
          <template #edit="{ row }">
            <NInput v-model:value="row.new_value" type="text" placeholder="请输入值"> </NInput>
          </template>
        </vxe-column>
        <vxe-column title="控制" width="150">
          <template #default="{ row }">
            <div class="flex flex-row gap-2">
              <n-button type="info" ghost :loading="isLoadingIndex === row.id" @click="merge(row)">
                合并
              </n-button>
              <n-button
                type="error"
                ghost
                :loading="deleteLoadingIndex === row.id"
                @click="deleteMerge(row)"
              >
                舍弃
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
const { kvEditStatus, mergeCheckLang, mergeCheckFilePath, mergeIsLoading } = storeToRefs(kvStore);
const tableRef = ref<InstanceType<typeof VxeTable>>(null);
const list = ref<MergeCheckItem[]>([]);
const isLoadingIndex = ref(-1);
const deleteLoadingIndex = ref(-1);
const message = useMessage();

onMounted(async () => {
  const res = await KvService.kvMergeCheck({
    requestBody: {
      lang: mergeCheckLang.value,
      path: mergeCheckFilePath.value
    }
  });
  if (res.code === 0) {
    list.value = res.data as MergeCheckItem[];
    mergeIsLoading.value = false;
  }
});

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
    list.value = list.value.filter((item) => item.id !== row.id);
    message.success('合并成功');
    if (list.value.length === 0) {
      message.success('处理完毕');
      backHome();
    }
  } else {
    message.error('Something error');
  }
};

const deleteMerge = async (row: MergeCheckItem) => {
  deleteLoadingIndex.value = row.id;
  list.value = list.value.filter((item) => item.id !== row.id);
  if (list.value.length === 0) {
    message.success('处理完毕');
    backHome();
  }
};
</script>
<style>
.keyword-lighten {
  background-color: yellow;
}
</style>
