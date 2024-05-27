import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import { KvService } from '@/client';

export const useKvStore = defineStore('kv', () => {
  const langKey = ref<string>('');
  const langValue = ref<string>('');
  const langList = ref<Record<string, any>[]>([]);

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
  return { langKey, langValue, langList, refreshLanglist };
});
