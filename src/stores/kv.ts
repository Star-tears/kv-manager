import { ref, computed } from 'vue';
import { defineStore } from 'pinia';

export const useKvStore = defineStore('kv', () => {
  const bucketName = ref('');
  const bucketList = ref([]);

  return { bucketName, bucketList };
});
