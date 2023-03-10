<template>
  <div style="height: 20px"></div>
  <el-form :model="form" label-width="120px" top="20px" ref="ruleForm">
    <el-form-item label="项目名称">
      <el-input v-model="form.project_name" />
    </el-form-item>
    <el-form-item label="项目接口地址">
      <el-input v-model="form.project_url" />
    </el-form-item>
    <el-form-item label="备注">
      <el-input v-model="form.remarks" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">添加</el-button>
<!--      <el-button>取消</el-button>-->
    </el-form-item>
  </el-form>
  <el-row :gutter="20"  class="el-row" type="flex" >
    <el-col :span="8" v-for="(item, index) in apps" :key="item.id" class="el-col">
      <el-card class="el-card" :key="index"  @click="skips(item.id)">
        <div slot="header" class="clearfix">
          <span>{{item.project_name}}</span>
        </div>
        <div class="infos">
          <div class="text item">
            <div class="item_tag" >
              <span >项目接口地址：</span>
            </div>
            <div class="item_desr">
              <span class="spanStyle"> {{item.project_url}}</span>
            </div>
          </div>
          <div class="text item">
            <div class="item_tag" >
              <span >备注：</span>
            </div>
            <div class="item_desr">
              <span class="spanStyle"> {{item.remark}}</span>
            </div>
          </div>
        </div>
      </el-card>
    </el-col>
  </el-row>
<!--  <div v-for="item in list">{{item.name}}</div>-->
</template>



<script lang="ts" setup>
import { reactive, ref } from 'vue'
import { ElMessage } from 'element-plus'
import { addProjects, getPj } from "../apis/apis.js";
import { useRouter } from "vue-router";
const router = useRouter()
const ruleForm = ref()

// 对象
// const apps = reactive({
//   id: "",
//   appname: "",
//   tag: "",
//   remarks: ""
// })

// 数组
const apps = ref()

getPj().then(res => {
  // Object.assign(apps, res.data)
  apps.value = res.data
})

const skips = (id) => {
  router.push({ name: 'ifcs', query: { id } })
  // router.push({ name: 'ifcs'})
}


// do not use same name with ref
const form = reactive({
  project_name: '',
  project_url: '',
  remarks: '',
})

const onSubmit = () => {
  addProjects(form).then(res => {
    ElMessage({
      message: res.message,
      type: 'success',
    })
    getPj()   //重新获取列表数据
    // 清空表单
    form.project_name = ""
    form.project_url = ""
    form.remarks = ""
  })


}
</script>

<style type="text/css">
  .item {
    margin-bottom: 10px;
  }
  .item_tag{
    float:left;
    text-align:left;
  }
  .item_desr{
    margin-left: 30%;
    min-height: 30px;
    text-align: left;
  }
  .text{
    width: 100%;
    font-size: 15px;
    font-family: "Microsoft YaHei";
    color: #909399;
  }
  .el-card {
    min-width: 100%;
    height: 100%;
    margin-right: 10px;
    /*transition: all .5s;*/
  }
  .el-row {
    margin-bottom: 30px;
    display: flex;
    flex-wrap: wrap
  }
  .el-col {
    margin-top: 20px;
    margin-left: 30px;
    /*border-radius: 40px;*/
    align-items: stretch;
    margin-bottom: 40px;
  }
  .clearfix {
    text-align: center;
  }
  .infos {
    margin-top: 20px;
  }
  .spanStyle {
    display: inline-block;
    white-space: normal;
    width: 300px;
    overflow: hidden; /*超出的文本隐藏*/
    text-overflow: ellipsis; /* 溢出用省略号*/
  }
</style>