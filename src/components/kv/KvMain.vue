<template>
  <div class="flex h-full flex-col gap-3">
    <p>
      <vxe-input v-model="filterName" type="search" placeholder="全表搜索" @keyup="searchEvent">
      </vxe-input>
    </p>
    <LangSelect />
    <div class="h-0 grow">
      <vxe-table
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
        <vxe-column field="key" title="键" type="html">
          <template #edit="{ row }">
            <vxe-input v-model="row.key" type="text"></vxe-input>
          </template>
        </vxe-column>
        <vxe-column field="value" title="值" :edit-render="{ autofocus: '.vxe-input--inner' }">
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
        <vxe-column title="控制">
          <template #default="{ row }">
            <div class="flex flex-row gap-2">
              <n-button ghost @click="historyClicked(row)"> 查看历史版本 </n-button>
              <n-button type="error" ghost @click="deleteClicked(row)"> 删除 </n-button>
            </div>
          </template>
        </vxe-column>
      </vxe-table>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { NInput } from 'naive-ui';
import { ref } from 'vue';
import { useKvStore, type KvItem } from '@/stores/kv';
import { storeToRefs } from 'pinia';
import { KvService } from '@/client';
import KvHisDialog from './dialogs/KvHisDialog.vue';

const kvStore = useKvStore();
const { kvItemList, langKey, langValue } = storeToRefs(kvStore);

const filterName = ref('');
const list = ref<KvItem[]>([]);
const dialog = useDialog();

watch(kvItemList, () => {
  searchEvent();
});

const historyClicked = (row: KvItem) => {
  console.log(row);
  dialog.success({
    title: '历史记录',
    content: () => h(KvHisDialog, null),
    style: {
      width: '80vw'
    }
  });
};

const deleteClicked = (row: KvItem) => {
  console.log(row);
};

const valueChangeEvent = (row: KvItem) => {
  console.log(row);
  console.log(`${row} 触发 input 事件`);
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
