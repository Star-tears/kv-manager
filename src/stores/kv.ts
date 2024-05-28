import { ref, computed } from 'vue';
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

export const useKvStore = defineStore('kv', () => {
  const langKey = ref<string>('');
  const langValue = ref<string>('');
  const langList = ref<Record<string, any>[]>([]);
  const kvItemList = ref<KvItem[]>([]);

  const refreshKvItemList = async () => {
    if (!langKey.value || !langValue.value) {
      return;
    }
    const res = await KvService.kvGetKvData({
      requestBody: {
        langKey: langKey.value,
        langValue: langValue.value
      }
    });
    if (res.code === 0) {
      kvItemList.value = res.data as KvItem[];
    }
  };

  const refreshLanglist = async () => {
    const res = await KvService.kvGetLangList();
    if (res.code === 0) {
      langList.value = (res.data as Record<string, any>[]).map((item) => {
        item['label'] = item.lang;
        item['value'] = item.lang;
        return item;
      });
    }
    console.log(langList.value);
  };
  return { langKey, langValue, langList, refreshLanglist, refreshKvItemList, kvItemList };
});
