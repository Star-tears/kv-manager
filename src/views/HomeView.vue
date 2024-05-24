<template>
  <n-layout style="height: 100vh; width: 100vw">
    <n-layout-header style="height: 64px; padding: 24px" bordered>
      <div class="font-semibold">键值对管理工具</div>
    </n-layout-header>
    <n-layout position="absolute" style="top: 64px" has-sider>
      <n-layout-sider content-style="padding: 24px;" width="80" :native-scrollbar="false" bordered>
        <SiderBar />
      </n-layout-sider>
      <n-layout has-sider sider-placement="right">
        <n-layout content-style="padding: 24px;" :native-scrollbar="false"><KvMain /> </n-layout>

        <n-layout-sider
          content-style="padding: 24px;"
          width="400"
          :native-scrollbar="false"
          bordered
        >
        </n-layout-sider>
      </n-layout>
    </n-layout>
  </n-layout>
</template>

<script setup lang="ts">
import KvMain from '@/components/kv/KvMain.vue';
import SiderBar from '@/components/kv/SiderBar.vue';
</script>
