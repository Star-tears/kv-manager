import { ref, computed } from 'vue';
import { defineStore } from 'pinia';

export const useKvStore = defineStore('kv', () => {
  const bucketName = ref<string>('');
  const bucketList = ref<string[]>([]);

  return { bucketName, bucketList };
});
