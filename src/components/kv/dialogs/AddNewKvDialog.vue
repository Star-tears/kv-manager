<template>
  <div class="my-4 flex flex-col gap-4">
    <div class="flex flex-row items-center gap-2">
      <n-select
        v-model:value="addKeyLang"
        class="w-52"
        :options="langList"
        placeholder="选择key语种"
      />
      <n-input v-model:value="addKey" />
    </div>
    <div class="flex flex-row items-center gap-2">
      <n-select
        v-model:value="addValueLang"
        class="w-52"
        :options="langList"
        placeholder="选择value语种"
      />
      <n-input v-model:value="addValue" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { useKvStore, type KvItem } from '@/stores/kv';
import { storeToRefs } from 'pinia';

const kvStore = useKvStore();
const { langList } = storeToRefs(kvStore);

const addKeyLang = defineModel<string>('addKeyLang');
const addValueLang = defineModel<string>('addValueLang');
const addKey = defineModel<string>('addKey');
const addValue = defineModel<string>('addValue');
</script>

<style scoped></style>
