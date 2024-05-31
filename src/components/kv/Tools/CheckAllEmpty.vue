<template>
  <n-card
    hoverable
    :content-style="{ padding: '8px 8px 8px 8px' }"
    title="检查全部语言空值"
    :header-style="{ padding: '8px 8px 0px 8px' }"
  >
    <div class="flex flex-col gap-2">
      <n-button class="mb-2 w-full" type="primary" @click="checkClick">检查</n-button>
    </div>
  </n-card>
</template>

<script setup lang="ts">
import { useKvStore } from '@/stores/kv';
import { storeToRefs } from 'pinia';

const message = useMessage();
const kvStore = useKvStore();
const { checkEmptyCount, kvEditStatus, checkEmptyIsLoading } = storeToRefs(kvStore);

const checkClick = async () => {
  checkEmptyIsLoading.value = true;
  setTimeout(() => {
    checkEmptyIsLoading.value = false;
  }, 10000);
  kvEditStatus.value = 'all-empty';
  checkEmptyCount.value++;
};
</script>

<style scoped></style>
