<template>
  <div style="height: 20px"></div>
  <el-form :model="form" label-width="120px" top="20px">
    <el-form-item label="项目名称">
      <el-input v-model="form.pname" />
    </el-form-item>
    <el-form-item label="项目接口地址">
      <el-input v-model="form.purl" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">添加</el-button>
      <el-button>取消</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { reactive } from 'vue'
import { addProjects } from "../apis/apis.js";


// do not use same name with ref
const form = reactive({
  pname: '',
  purl: '',
})

const onSubmit = () => {
  addProjects(form)

}
</script>
