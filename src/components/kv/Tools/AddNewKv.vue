<template>
  <n-card
    hoverable
    :content-style="{ padding: '8px 8px 8px 8px' }"
    title="新增键值对"
    :header-style="{ padding: '8px 8px 0px 8px' }"
  >
    <div class="flex flex-col gap-2">
      <n-button class="mb-2 w-full" type="primary" @click="addNewClick">新增</n-button>
    </div>
  </n-card>
</template>

<script setup lang="ts">
import { KvService } from '@/client';
import { useKvStore } from '@/stores/kv';
import { storeToRefs } from 'pinia';
import AddNewKvDialog from '../dialogs/AddNewKvDialog.vue';

const dialog = useDialog();
const message = useMessage();
const kvStore = useKvStore();
const { langList, kvItemAddCount } = storeToRefs(kvStore);
const isLoading = ref(false);

const addKeyLang = ref<string>('');
const addValueLang = ref<string>('');
const addKey = ref<string>('');
const addValue = ref<string>('');

const addNewClick = async () => {
  const d = dialog.success({
    title: '新增键值对',
    content: () =>
      h(AddNewKvDialog, {
        addKeyLang: addKeyLang.value,
        addValueLang: addValueLang.value,
        addKey: addKey.value,
        addValue: addValue.value,
        'onUpdate:addKeyLang': (v: string) => (addKeyLang.value = v),
        'onUpdate:addValueLang': (v: string) => (addValueLang.value = v),
        'onUpdate:addKey': (v: string) => (addKey.value = v),
        'onUpdate:addValue': (v: string) => (addValue.value = v)
      }),
    style: {
      width: '70vw'
    },
    positiveText: '确定',
    negativeText: '取消',
    onPositiveClick: async () => {
      d.loading = true;
      if (addKeyLang.value && addValueLang.value && addKey.value && addValue.value) {
        const res = await KvService.kvUpdateKv({
          requestBody: {
            key: addKey.value,
            langKey: addKeyLang.value,
            value: addValue.value,
            langValue: addValueLang.value
          }
        });
        if (res.code === 0) {
          message.success('新增成功');
          kvItemAddCount.value++;
        }
      } else {
        message.error('请填写完整信息');
      }
      d.loading = false;
    }
  });
};
</script>

<style scoped></style>
