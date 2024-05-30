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
};

export type MergeCheckItem = {
  id: number;
  key: string;
  curr_value: string;
  new_value: string;
  lang_key: string;
  lang_value: string;
};

export type CheckEmptyItem = {
  kv_id: number;
  key: string;
  value: string;
  lang_key: string;
  lang_value: string;
};

export const useKvStore = defineStore('kv', () => {
  const langKey = ref<string>('');
  const langValue = ref<string>('');
  const langList = ref<Record<string, any>[]>([]);
  const kvEditStatus = ref<'main' | 'merge-check' | 'all-empty'>('main');
  const mergeCheckLang = ref<string>('');
  const mergeCheckFilePath = ref<string>('');
  const mergeIsLoading = ref<boolean>(false);
  const checkEmptyCount = ref<number>(0);
  const checkEmptyIsLoading = ref<boolean>(false);

  const refreshLanglist = async () => {
    const res = await KvService.kvGetLangList();
    if (res.code === 0) {
      langList.value = (res.data as Record<string, any>[]).map((item) => {
        item['label'] = item.lang;
        item['value'] = item.lang;
        return item;
      });
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
    checkEmptyIsLoading
  };
});
