<template>
  <div>
    <div class="flex flex-col gap-2">
      <div class="flex flex-row items-center gap-1">
        <n-tag type="info"> 存储桶名: </n-tag>
      </div>
      <n-input
        placeholder="输入存储桶名"
        v-model:value="bucketName"
        :status="inputValidationStatus"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { NTag, NInput } from 'naive-ui';
import type { FormValidationStatus } from 'naive-ui/es/form/src/interface';

const bucketName = defineModel<string>('bucketName');
const inputValidationStatus = computed(() => {
  return bucketName.value === '' ? ('error' as FormValidationStatus) : undefined;
});
</script>

<style scoped></style>
