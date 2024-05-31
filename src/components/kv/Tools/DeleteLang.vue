<template>
  <n-card
    hoverable
    :content-style="{ padding: '8px 8px 8px 8px' }"
    title="删除语言"
    :header-style="{ padding: '8px 8px 0px 8px' }"
  >
    <div class="flex flex-col gap-2">
      <n-select v-model:value="deleteLangValue" :options="deleteAllowList"></n-select>
      <n-button
        class="mb-2 w-full"
        type="error"
        :loading="isLoading"
        :disabled="isValid"
        @click="deleteBtnClicked"
      >
        删除
      </n-button>
    </div>
  </n-card>
</template>

<script setup lang="ts">
import { KvService } from '@/client';
import { useKvStore } from '@/stores/kv';
import { storeToRefs } from 'pinia';

const message = useMessage();
const dialog = useDialog();
const kvStore = useKvStore();
const { langList } = storeToRefs(kvStore);
const isLoading = ref(false);
const deleteLangValue = ref('');
const deleteAllowList = computed(() => {
  return langList.value.filter((item) => item.value !== 'English');
});
const isValid = computed(() => {
  return deleteLangValue.value === '';
});

const deleteBtnClicked = async () => {
  const d = dialog.error({
    title: '警告',
    content: '确定要删除吗？',
    positiveText: '确定',
    negativeText: '取消',
    onPositiveClick: async () => {
      d.loading = true;
      const res = await KvService.kvDeleteLang({
        requestBody: {
          lang: deleteLangValue.value
        }
      });
      if (res.code === 0) {
        kvStore.refreshLanglist();
        message.success('删除成功');
        d.loading = false;
      }
    }
  });
};
</script>

<style scoped></style>
