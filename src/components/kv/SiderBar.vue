<template>
  <div>
    <ToggleGroup type="single" orientation="vertical" class="flex-col gap-4" size="lg">
      <ToggleGroupItem
        value="bold"
        aria-label="Toggle bold"
        class="px-1"
        :style="getActiveStyle('pkg-manager')"
      >
        <NAvatar>en2cn</NAvatar>
      </ToggleGroupItem>
      <ToggleGroupItem value="italic" aria-label="Toggle italic">
        <FontItalicIcon class="size-4" />
      </ToggleGroupItem>
      <ToggleGroupItem value="underline" aria-label="Toggle underline">
        <UnderlineIcon class="size-4" />
      </ToggleGroupItem>
    </ToggleGroup>
  </div>
</template>

<script setup lang="ts">
import { FontBoldIcon, FontItalicIcon, UnderlineIcon } from '@radix-icons/vue';

import { ToggleGroup, ToggleGroupItem } from '@/components/ui/toggle-group';
import { NAvatar } from 'naive-ui';
import { useThemeVars } from 'naive-ui';
import { useKvStore } from '@/stores/kv';
import { storeToRefs } from 'pinia';

const kvStore = useKvStore();
const { bucketName, bucketList } = storeToRefs(kvStore);

onMounted(() => {});

const themeVars = useThemeVars();
const getActiveStyle = (value: string) => {
  const styleValue: Record<string, any> = {};
  // if (ideInfo.value.edgeContainerValue === value)
  styleValue.borderLeft = '1.5px solid ' + themeVars.value.primaryColor;

  return styleValue;
};
</script>
