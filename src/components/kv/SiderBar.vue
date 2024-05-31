<template>
  <div class="flex flex-col items-center gap-4">
    <!-- <ToggleGroup
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
    <n-button class="p-3" @click="showCreateBucketDialog"
      ><Icon icon="material-symbols:add"
    /></n-button> -->
  </div>
</template>

<script setup lang="ts">
// import { ToggleGroup, ToggleGroupItem } from '@/components/ui/toggle-group';
// import { NAvatar } from 'naive-ui';
// import { useThemeVars } from 'naive-ui';
// import { useKvStore } from '@/stores/kv';
// import { storeToRefs } from 'pinia';
// import { KvService } from '@/client';
// import { Icon } from '@iconify/vue/dist/iconify.js';
// import CreateBucketDialog from './dialogs/CreateBucketDialog.vue';

// const message = useMessage();
// const kvStore = useKvStore();
// const { bucketName, bucketList } = storeToRefs(kvStore);
// const newBucketName = ref<string>('');
// const dialog = useDialog();

// onMounted(() => {
//   KvService.kvGetBucketList().then((res) => {
//     if (res.code === 0) {
//       bucketList.value = res.data as string[];
//     }
//   });
// });

// const themeVars = useThemeVars();
// const getActiveStyle = (value: string) => {
//   const styleValue: Record<string, any> = {};
//   if (bucketName.value === value) {
//     styleValue.borderLeft = '1.5px solid ' + themeVars.value.primaryColor;
//     styleValue.borderRight = '1.5px solid ' + themeVars.value.primaryColor;
//   }

//   return styleValue;
// };
// const getActiveColor = (value: string) => {
//   const styleValue: Record<string, any> = { color: themeVars.value.textColor1 };
//   if (bucketName.value === value) {
//     styleValue.backgroundColor = themeVars.value.primaryColor;
//     styleValue.color = 'white';
//   }

//   return styleValue;
// };

// const createBucket = async () => {
//   if (newBucketName.value === '') {
//     message.error('存储桶名不能为空');
//     return;
//   }
//   await KvService.kvCreateBucket({
//     requestBody: {
//       bucketName: newBucketName.value
//     }
//   });
//   message.success('创建成功');
//   const res = await KvService.kvGetBucketList();
//   if (res.code === 0) {
//     bucketList.value = res.data as string[];
//   }
// };

// const showCreateBucketDialog = () => {
//   newBucketName.value = '';
//   const d = dialog.success({
//     title: '新建存储桶',
//     content: () =>
//       h(CreateBucketDialog, {
//         bucketName: newBucketName.value,
//         'onUpdate:bucketName': (val: string) => {
//           newBucketName.value = val;
//         }
//       }),
//     positiveText: '确认创建',
//     onPositiveClick: () => {
//       d.loading = true;

//       return new Promise((resolve) => {
//         createBucket().then(resolve);
//       });
//     }
//   });
// };
</script>
