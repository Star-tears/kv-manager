<template>
  <n-layout style="height: 100vh; width: 100vw">
    <n-layout-header style="height: 64px; padding: 24px" bordered>
      <div class="font-semibold">Qt翻译ts文件管理工具</div>
    </n-layout-header>
    <n-layout position="absolute" style="top: 64px" has-sider sider-placement="right">
      <n-layout content-style="padding: 12px 24px 12px 24px;"><KvMain /> </n-layout>
      <n-layout-sider content-style="padding: 24px;" width="400" :native-scrollbar="false" bordered>
        <ToolSider />
      </n-layout-sider>
    </n-layout>
  </n-layout>
</template>

<script setup lang="ts">
import KvMain from '@/components/kv/KvMain.vue';
</script>
