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
      <n-breadcrumb-item @click="backHome">
        <div class="flex flex-row gap-1">
          <Icon icon="ic:round-home" />
          <div>home</div>
        </div>
      </n-breadcrumb-item>
      <n-breadcrumb-item>
        <div class="flex flex-row gap-1">
          <Icon icon="ph:link-bold" />
          <div>all-empty</div>
        </div>
      </n-breadcrumb-item>
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
        <vxe-column field="lang_value" title="值语种" :filters="langList" width="120" sortable>
        </vxe-column>
        <vxe-column
          field="value"
          title="新值"
          :edit-render="{ autofocus: '.vxe-input--inner' }"
          sortable
        >
          <template #edit="{ row }">
            <div class="flex flex-row gap-2">
              <n-input
                v-model:value="row.value"
                type="text"
                placeholder="请输入值"
                @change="valueChangeEvent(row)"
              >
              </n-input>
              <n-button
                ghost
                text
                type="info"
                :loading="transIsloadingId === row.kv_id"
                @click="translateByFeishu(row)"
              >
                <Icon icon="hugeicons:translate" width="24" height="24" />
              </n-button>
            </div>
          </template>
        </vxe-column>
      </vxe-table>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { Icon } from '@iconify/vue/dist/iconify.js';
import { FeishuService, KvService } from '@/client';
import { useKvStore, type CheckEmptyItem } from '@/stores/kv';
import { storeToRefs } from 'pinia';
import type { VxeTable } from 'vxe-table';

const kvStore = useKvStore();
const { kvEditStatus, checkEmptyCount, checkEmptyIsLoading, langList } = storeToRefs(kvStore);
const tableRef = ref<InstanceType<typeof VxeTable>>(null);
const list = ref<CheckEmptyItem[]>([]);
const message = useMessage();
const transIsloadingId = ref<number>();

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

const valueChangeEvent = async (row: CheckEmptyItem) => {
  await KvService.kvUpdateKv({
    requestBody: {
      key: row.key,
      langKey: row.lang_key,
      value: row.value,
      langValue: row.lang_value,
      kvId: row.kv_id
    }
  });
  //@ts-ignore
  tableRef.value.clearEdit();
};

const translateByFeishu = async (row: CheckEmptyItem) => {
  transIsloadingId.value = row.kv_id;
  const res = await FeishuService.feishuTransText({
    sourceLanguage: row.lang_key,
    text: row.key,
    lang: row.lang_value
  });
  if (res.code === 0) {
    row.value = (res.data as Record<string, any>)['text'];
    await KvService.kvUpdateKv({
      requestBody: {
        key: row.key,
        langKey: row.lang_key,
        value: row.value,
        langValue: row.lang_value,
        kvId: row.kv_id
      }
    });
  }
  transIsloadingId.value = -1;
};
</script>
<style>
.keyword-lighten {
  background-color: yellow;
}
</style>
