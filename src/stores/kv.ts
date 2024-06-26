import { ref } from 'vue';
import { defineStore } from 'pinia';
import { KvService } from '@/client';

export type KvItem = {
  kv_id: number;
  key: string;
  value: string;
  lang_key: string;
  lang_value: string;
  updated_at: string;
  feishu_language: string;
};

export type MergeCheckItem = {
  id: number;
  key: string;
  curr_value: string;
  new_value: string;
  lang_key: string;
  lang_value: string;
  feishu_language: string;
};

export type CheckEmptyItem = {
  kv_id: number;
  key: string;
  value: string;
  lang_key: string;
  lang_value: string;
  feishu_language: string;
};

export const useKvStore = defineStore('kv', () => {
  const langKey = ref<string>('');
  const langValue = ref<string>('');
  const langList = ref<Record<string, any>[]>([]);
  const kvItemAddCount = ref<number>(0);
  const kvEditStatus = ref<'main' | 'merge-check' | 'all-empty'>('main');
  const mergeCheckLang = ref<string>('');
  const mergeCheckFilePath = ref<string>('');
  const mergeIsLoading = ref<boolean>(false);
  const checkEmptyCount = ref<number>(0);
  const checkEmptyIsLoading = ref<boolean>(false);

  watch(langList, () => {
    if (langList.value.find((obj) => obj.value === langKey.value) === undefined) {
      langKey.value = '';
    }
    if (langList.value.find((obj) => obj.value === langValue.value) === undefined) {
      langValue.value = '';
    }
  });
  const refreshLanglist = async () => {
    const res = await KvService.kvGetLangList();
    if (res.code === 0) {
      langList.value = (res.data as Record<string, any>[]).map((item) => {
        item['label'] = item.lang;
        item['value'] = item.lang;
        return item;
      });
      if ((res.data as Record<string, any>[]).length > 0) {
        langKey.value = (res.data as Record<string, any>[])[0].lang;
        langValue.value = (res.data as Record<string, any>[])[1].lang;
      }
    }
  };
  return {
    langKey,
    langValue,
    langList,
    refreshLanglist,
    kvEditStatus,
    mergeCheckLang,
    mergeCheckFilePath,
    mergeIsLoading,
    checkEmptyCount,
    checkEmptyIsLoading,
    kvItemAddCount
  };
});
