<template>
  <div class="flex flex-col gap-3">
    <p>
      <vxe-input
        v-model="filterName"
        type="search"
        placeholder="全表搜索"
        @keyup="searchEvent"
      ></vxe-input>
    </p>

    <vxe-table
      border
      show-overflow
      :column-config="{ resizable: true, useKey: true }"
      :row-config="{ useKey: true }"
      :edit-config="{ trigger: 'dblclick', mode: 'cell' }"
      :data="list"
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
            @change="valueChangeEvent({ row })"
          ></NInput>
        </template>
      </vxe-column>
      <vxe-column field="date" title="更新时间" type="html">
        <template #edit="{ row }">
          <vxe-input v-model="row.date" type="date" placeholder="更新时间" transfer></vxe-input>
        </template>
      </vxe-column>
    </vxe-table>
  </div>
</template>

<script lang="ts" setup>
import { NInput } from 'naive-ui';
import { ref } from 'vue';

interface RowVO {
  key: string;
  value: string;
  date: string;
  bucket: string;
}

const filterName = ref('');
const list = ref<RowVO[]>([]);

const tableData = ref<RowVO[]>([
  {
    key: 'Test1',
    value: 'Develop',
    date: '2024-05-24 09:49:04.215161',
    bucket: 'en2cn'
  },
  {
    key: 'Test2',
    value: 'Designer',
    date: '',
    bucket: 'en2cn'
  },
  {
    key: 'Test3',
    value: 'Test',
    date: '2020-09-10',
    bucket: 'en2cn'
  },
  {
    key: 'Test4',
    value: 'Designer',
    date: '',
    bucket: 'en2cn'
  }
]);

const valueChangeEvent = ({ row }: any) => {
  console.log(row);
  console.log(`${row} 触发 input 事件`);
};

const searchEvent = () => {
  const filterVal = String(filterName.value).trim().toLowerCase();
  if (filterVal) {
    const filterRE = new RegExp(filterVal, 'gi');
    const searchProps = ['key', 'value', 'date'];
    const rest = tableData.value.filter((item: any) =>
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
    list.value = tableData.value;
  }
};
searchEvent();
</script>
<style>
.keyword-lighten {
  background-color: yellow;
}
</style>
