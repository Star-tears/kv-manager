<template>
  <div>
    <ToggleGroup
      v-model="bucketName"
      type="single"
      orientation="vertical"
      class="flex-col gap-4"
      size="lg"
    >
      <template v-for="bucket in bucketList" :key="bucket">
        <ToggleGroupItem
          :value="bucket"
          :aria-label="bucket"
          class="px-1"
          :style="getActiveStyle(bucket)"
        >
          <NAvatar :style="getActiveColor(bucket)">{{ bucket }}</NAvatar>
        </ToggleGroupItem>
      </template>
    </ToggleGroup>
  </div>
</template>

<script setup lang="ts">
import { ToggleGroup, ToggleGroupItem } from '@/components/ui/toggle-group';
import { NAvatar } from 'naive-ui';
import { useThemeVars } from 'naive-ui';
import { useKvStore } from '@/stores/kv';
import { storeToRefs } from 'pinia';
import { KvService } from '@/client';

const kvStore = useKvStore();
const { bucketName, bucketList } = storeToRefs(kvStore);

onMounted(() => {
  KvService.kvGetBucketList().then((res) => {
    if (res.code === 0) {
      bucketList.value = res.data as string[];
    }
  });
});

const themeVars = useThemeVars();
const getActiveStyle = (value: string) => {
  const styleValue: Record<string, any> = {};
  if (bucketName.value === value) {
    styleValue.borderLeft = '1.5px solid ' + themeVars.value.primaryColor;
    styleValue.borderRight = '1.5px solid ' + themeVars.value.primaryColor;
  }

  return styleValue;
};
const getActiveColor = (value: string) => {
  const styleValue: Record<string, any> = { color: themeVars.value.textColor1 };
  if (bucketName.value === value) {
    styleValue.backgroundColor = themeVars.value.primaryColor;
    styleValue.color = 'white';
  }

  return styleValue;
};
</script>
