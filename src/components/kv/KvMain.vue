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
    <div class="flex flex-row items-center justify-between">
      <n-breadcrumb separator=">">
        <n-breadcrumb-item> home</n-breadcrumb-item>
      </n-breadcrumb>
      <div class="w-80">
        <vxe-input
          v-model="filterName"
          type="search"
          placeholder="全表搜索"
          @keyup="searchEvent"
          :style="{ width: '100%' }"
        >
        </vxe-input>
      </div>
    </div>

    <LangSelect />
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
        <vxe-column type="seq" width="60"></vxe-column>
        <vxe-column field="key" title="键" type="html" sortable> </vxe-column>
        <vxe-column
          field="value"
          title="值"
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
        <vxe-column title="控制" width="230">
          <template #default="{ row }">
            <div class="flex flex-row gap-2">
              <n-button ghost @click="historyClicked(row)"> 查看历史版本 </n-button>
              <n-button
                type="error"
                ghost
                :loading="deleteLoadingId === row.kv_id"
                @click="deleteClicked(row)"
              >
                删除
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
import { NInput } from 'naive-ui';
import { ref } from 'vue';
import { useKvStore, type KvItem } from '@/stores/kv';
import { storeToRefs } from 'pinia';
import { FeishuService, KvService } from '@/client';
import KvHisDialog from './dialogs/KvHisDialog.vue';
import type { VxeTable } from 'vxe-table';

const kvStore = useKvStore();
const { langKey, langValue, kvItemAddCount } = storeToRefs(kvStore);
const tableRef = ref<InstanceType<typeof VxeTable>>(null);
const message = useMessage();
const filterName = ref('');
const list = ref<KvItem[]>([]);
const dialog = useDialog();
const deleteLoadingId = ref<number>();
const transIsloadingId = ref<number>();
const kvItemList = ref<KvItem[]>([]);

watch(langKey, () => {
  searchEvent();
});
watch(langValue, () => {
  searchEvent();
});

watch(kvItemAddCount, () => {
  searchEvent();
});

const historyClicked = (row: KvItem) => {
  const d = dialog.success({
    title: '历史记录',
    content: () =>
      h(
        KvHisDialog,
        {
          kv_id: row.kv_id,
          kv_key: row.key,
          lang_value: row.lang_value,
          'onUpdate-kv': (kv_value: string) => {
            row.value = kv_value;
            KvService.kvUpdateKv({
              requestBody: {
                key: row.key,
                langKey: row.lang_key,
                value: row.value,
                langValue: row.lang_value,
                kvId: row.kv_id
              }
            }).then(() => {
              message.success('记录更新成功');
              d.destroy();
            });
          }
        },
        null
      ),
    style: {
      width: '80vw'
    }
  });
};

const translateByFeishu = async (row: KvItem) => {
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

const deleteClicked = async (row: KvItem) => {
  const d = dialog.error({
    title: '警告',
    content: '确定要删除吗，这将会删除所有此键对应的其他语种记录？',
    positiveText: '确定',
    negativeText: '取消',
    onPositiveClick: async () => {
      d.loading = true;
      deleteLoadingId.value = row.kv_id;
      const res = await KvService.kvDeleteKv({
        requestBody: {
          kvId: row.kv_id
        }
      });
      if (res.code === 0) {
        // @ts-ignore
        await tableRef.value?.remove(row);
        kvItemList.value = kvItemList.value.filter((item) => item.kv_id !== row.kv_id);
        message.success('删除成功');
        d.loading = false;
      }
    }
  });
};

const valueChangeEvent = (row: KvItem) => {
  KvService.kvUpdateKv({
    requestBody: {
      key: row.key,
      langKey: row.lang_key,
      value: row.value,
      langValue: row.lang_value,
      kvId: row.kv_id
    }
  });
  const itemWithKvId = kvItemList.value.find((item) => item.kv_id === row.kv_id);
  if (itemWithKvId) {
    itemWithKvId.value = row.value;
  }
  //@ts-ignore
  tableRef.value.clearEdit();
};

const searchEvent = () => {
  const filterVal = String(filterName.value).trim().toLowerCase();
  if (filterVal) {
    const filterRE = new RegExp(filterVal, 'gi');
    const searchProps = ['key', 'value', 'updated_at'];
    const rest = kvItemList.value.filter((item: any) =>
      searchProps.some((key) => String(item[key]).toLowerCase().indexOf(filterVal) > -1)
    );
    list.value = rest.map((row) => {
      const item: any = Object.assign({}, row);
      searchProps.forEach((key) => {
        if (key != 'value') {
          item[key] = String(item[key]).replace(
            filterRE,
            (match) => `<span class="keyword-lighten">${match}</span>`
          );
        }
      });
      return item;
    });
  } else {
    if (!langKey.value || !langValue.value) {
      return;
    }
    KvService.kvGetKvData({
      requestBody: {
        langKey: langKey.value,
        langValue: langValue.value
      }
    }).then((res) => {
      if (res.code === 0) {
        kvItemList.value = res.data as KvItem[];
        list.value = res.data as KvItem[];
      }
    });
  }
};
searchEvent();
</script>
<style>
.keyword-lighten {
  background-color: yellow;
}
</style>
