<template>
  <el-header class="layout-container-demo" style="height:50px; text-align: right; font-size: 16px; background-color: #a0cfff;display: flex">
      <h3 style="margin-left: 50px;">接口及接口数据文档</h3>
  </el-header>
  <el-container class="layout-container-demo" style="height: 960px">
    <el-aside width="200px">
      <el-scrollbar>
        <el-menu router :default-openeds="['1']" :default-active="$route.path">
          <el-sub-menu index="1">
            <template #title>
              <el-icon><CirclePlus /></el-icon>  项目
            </template>
            <el-menu-item index="/">添加项目</el-menu-item>
          </el-sub-menu>
        </el-menu>
      </el-scrollbar>
    </el-aside>
    <el-container>
      <el-main>
        <el-scrollbar>
          <router-view></router-view>
        </el-scrollbar>
      </el-main>
    </el-container>
  </el-container>

</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const route = useRouter()


</script>

<style scoped>
.layout-container-demo .el-header {
  position: relative;
  background-color: var(--el-color-primary-light-7);
  color: var(--el-text-color-primary);
}
.layout-container-demo .el-aside {
  color: var(--el-text-color-primary);
  background: var(--el-color-primary-light-8);
}
.layout-container-demo .el-menu {
  border-right: none;
}
.layout-container-demo .el-main {
  padding: 0;
}
</style>

