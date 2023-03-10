<template>
  <div style="height: 20px"></div>
  <div>
    <el-form :model="form" label-width="120px" top="20px" ref="ruleForm" class="all">
      <el-form-item label="接口名称" >
        <el-input v-model="form.inter_name" />
      </el-form-item>
      <el-form-item class="inna" label="接口地址">
        <el-input v-model="form.inter_url" />
      </el-form-item>
      <el-form-item label="接口请求方式">
        <el-select v-model="form.inter_methods" placeholder="选择请求方式">
          <el-option
            v-for="item in methodOptions"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="请求格式">
        <el-select v-model="form.inter_format" placeholder="选择请求格式">
          <el-option
            v-for="item in formatOptions"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="是否需要登录">
        <el-select v-model="form.inter_token" placeholder="是否需要登录">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="接口分类">
        <el-select v-model="form.inter_category" placeholder="选择接口分类">
          <el-option
            v-for="item in interCate"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item class="inna" label="备注">
        <el-input v-model="form.remarks" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">添加</el-button>
        <el-button @click="cancel">取消</el-button>
      </el-form-item>
    </el-form>
    <el-table :data="tableData" style="width: 100%; margin-left: 20px; margin-top: 30px">
      <el-table-column fixed prop="inter_name" label="接口名称" width="180" />
      <el-table-column prop="inter_url" label="接口地址" width="320" />
      <el-table-column prop="request_method" label="请求方式" width="120" />
      <el-table-column prop="request_form" label="请求格式" width="250" />
      <el-table-column prop="inter_token" label="是否需要登录" width="150" />
      <el-table-column prop="remark" label="备注" width="200" />
      <el-table-column fixed="right" label="操作" width="120">
        <template #default="scope">
          <el-button link type="primary" size="small" @click="handleClick(scope.row.id)">详情</el-button>
          <el-button link type="primary" size="small" >删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>



<script lang="ts" setup>
import { reactive, ref } from 'vue'
import { ElMessage } from 'element-plus'
import { addInter, getInter } from "../apis/apis.js";
import { useRoute, useRouter } from "vue-router";
const route = useRoute()
const router = useRouter()
const ruleForm = ref()

// 数组
const apps = ref()
const tableData = ref()

// get传参
getInter({id: route.query.id}).then(res => {
  // Object.assign(apps, res.data)
  tableData.value = res.data
})

// // get传参
// getInter(route.query.id).then(res => {
//   // Object.assign(apps, res.data)
//   apps.value = res.data
// })

const handleClick = (id) => {
  router.push({ name: 'infiled', query: { id } })
  // router.push({ name: 'ifcs'})
}




const value = ref('')
const methodOptions = [
  {
    value: 'POST',
    label: 'POST',
  },
  {
    value: 'GET',
    label: 'GET',
  },
  {
    value: 'PUSH',
    label: 'PUSH',
  },
  {
    value: 'DELETE',
    label: 'DELETE',
  },
  // {
  //   value: 'Option2',
  //   label: 'Option2',
  //   disabled: true,
  // },
]
const formatOptions = [
  {
    value: 'application/x-www-form-urlencoded',
    label: 'x-www-form-urlencoded',
  },
  {
    value: 'application/json, charset=utf-8',
    label: 'application/json',
  }
]
const islogin = [
  {
    value: '1',
    label: '是',
  },
  {
    value: '2',
    label: '否',
  }
]
const interCate = [
  {
    value: 'backend',
    label: '后端接口',
  },
  {
    value: 'openapi',
    label: '第三方接口',
  }
]

// do not use same name with ref
const form = reactive({
  inter_name: '',
  inter_url: '',
  inter_methods: '',
  inter_format: '',
  inter_category: '',
  inter_token: '',
  remarks: '',
  pid: route.query.id
})

const cancel = () => {
  router.back()
}

const onSubmit = () => {
  addInter(form).then(res => {
    ElMessage({
      message: res.message,
      type: 'success',
    })
    getInter({id: route.query.id}).then(res => {
      tableData.value = res.data
    })   //重新获取列表数据
    // 清空表单
    form.inter_name = ""
    form.inter_url = ""
    form.inter_methods = ""
    form.inter_token = ""
    form.inter_format = ""
    form.inter_category = ""
    form.remarks = ""
  })
}


</script>

<style type="text/css">
  .all {
    display: flex;
    flex-wrap: wrap;
    justify-content: left;
  }
  .inna {
    width: 500px;
  }
</style>
