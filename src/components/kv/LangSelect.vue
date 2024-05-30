<template>
  <div class="flex w-full flex-row items-center gap-4">
    <n-select v-model:value="langKey" :options="langList" />
    <Icon icon="icon-park-outline:switch" width="48" height="48" />
    <n-select v-model:value="langValue" :options="langList" />
  </div>
</template>

<script setup lang="ts">
import { Icon } from '@iconify/vue/dist/iconify.js';
import { useKvStore } from '@/stores/kv';
import { storeToRefs } from 'pinia';

const kvStore = useKvStore();
const { langKey, langValue, langList } = storeToRefs(kvStore);

onMounted(() => {
  kvStore.refreshLanglist();
});
</script>

<style scoped></style>
