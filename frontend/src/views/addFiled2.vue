<template>
  <div style="margin-top: 10px">
    <div style="height: 20px">文本类</div>
    <el-form :model="form" top="20px" ref="ruleForm" class="all">
      <el-form-item label="字段名称" class="long">
        <el-input v-model="form.field_name" />
      </el-form-item>
      <el-form-item label="必填" >
        <el-select v-model="form.musts" placeholder="是否必填" class="short">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select >
      </el-form-item>
      <el-form-item label="类型">
        <el-select v-model="form.categgroy" placeholder="选择文本类型" class="short3">
          <el-option
            v-for="item in categgroys"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="加密方式">
        <el-select v-model="form.inter_format" placeholder="选择加密方式" class="short3">
          <el-option
            v-for="item in encryMethods"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="最短长度">
        <el-input v-model="form.shorts" class="short"/>
      </el-form-item >
      <el-form-item label="最长长度" >
        <el-input v-model="form.shorts" class="short"/>
      </el-form-item>
      <el-form-item label="中文">
        <el-select v-model="form.chinese" placeholder="是否支持中文" class="short3">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="英文">
        <el-select v-model="form.English" placeholder="是否支持英文" class="short3">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="数字">
        <el-select v-model="form.English" placeholder="是否支持数字" class="short3">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="特殊字符">
        <el-select v-model="form.English" placeholder="是否支持特殊字符" class="short2">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="是否区分大小写">
        <el-select v-model="form.English" placeholder="是否区分大小写" class="short2">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="是否唯一">
        <el-select v-model="form.English" placeholder="是否唯一" class="short">
          <el-option
            v-for="item in islogin"
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
    <div style="height: 20px">数字类</div>
    <el-form :model="form" top="20px" ref="ruleForm" class="all">
      <el-form-item label="字段名称" class="long">
        <el-input v-model="form.field_name" />
      </el-form-item>
      <el-form-item label="必填" >
        <el-select v-model="form.musts" placeholder="是否必填" class="short">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select >
      </el-form-item>
      <el-form-item label="类型">
        <el-select v-model="form.categgroy" placeholder="选择文本类型" class="short3">
          <el-option
            v-for="item in categgroys"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="加密方式">
        <el-select v-model="form.inter_format" placeholder="选择加密方式" class="short3">
          <el-option
            v-for="item in encryMethods"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="最短长度">
        <el-input v-model="form.shorts" class="short"/>
      </el-form-item >
      <el-form-item label="最长长度" >
        <el-input v-model="form.shorts" class="short"/>
      </el-form-item>
      <el-form-item label="中文">
        <el-select v-model="form.chinese" placeholder="是否支持中文" class="short3">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="英文">
        <el-select v-model="form.English" placeholder="是否支持英文" class="short3">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="数字">
        <el-select v-model="form.English" placeholder="是否支持数字" class="short3">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="特殊字符">
        <el-select v-model="form.English" placeholder="是否支持特殊字符" class="short2">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="是否区分大小写">
        <el-select v-model="form.English" placeholder="是否区分大小写" class="short2">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="是否唯一">
        <el-select v-model="form.English" placeholder="是否唯一" class="short">
          <el-option
            v-for="item in islogin"
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
    <div style="height: 20px">日期类</div>
    <el-form :model="form" top="20px" ref="ruleForm" class="all">
      <el-form-item label="字段名称" class="long">
        <el-input v-model="form.field_name" />
      </el-form-item>
      <el-form-item label="必填" >
        <el-select v-model="form.musts" placeholder="是否必填" class="short">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select >
      </el-form-item>
      <el-form-item label="类型">
        <el-select v-model="form.categgroy" placeholder="选择文本类型" class="short3">
          <el-option
            v-for="item in categgroys"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="加密方式">
        <el-select v-model="form.inter_format" placeholder="选择加密方式" class="short3">
          <el-option
            v-for="item in encryMethods"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="最短长度">
        <el-input v-model="form.shorts" class="short"/>
      </el-form-item >
      <el-form-item label="最长长度" >
        <el-input v-model="form.shorts" class="short"/>
      </el-form-item>
      <el-form-item label="中文">
        <el-select v-model="form.chinese" placeholder="是否支持中文" class="short3">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="英文">
        <el-select v-model="form.English" placeholder="是否支持英文" class="short3">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="数字">
        <el-select v-model="form.English" placeholder="是否支持数字" class="short3">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="特殊字符">
        <el-select v-model="form.English" placeholder="是否支持特殊字符" class="short2">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="是否区分大小写">
        <el-select v-model="form.English" placeholder="是否区分大小写" class="short2">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="是否唯一">
        <el-select v-model="form.English" placeholder="是否唯一" class="short">
          <el-option
            v-for="item in islogin"
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
    <div style="height: 20px">关联类</div>
    <el-form :model="form" top="20px" ref="ruleForm" class="all">
      <el-form-item label="字段名称" class="long">
        <el-input v-model="form.field_name" />
      </el-form-item>
      <el-form-item label="必填" >
        <el-select v-model="form.musts" placeholder="是否必填" class="short">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select >
      </el-form-item>
      <el-form-item label="类型">
        <el-select v-model="form.categgroy" placeholder="选择文本类型" class="short3">
          <el-option
            v-for="item in categgroys"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="加密方式">
        <el-select v-model="form.inter_format" placeholder="选择加密方式" class="short3">
          <el-option
            v-for="item in encryMethods"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="最短长度">
        <el-input v-model="form.shorts" class="short"/>
      </el-form-item >
      <el-form-item label="最长长度" >
        <el-input v-model="form.shorts" class="short"/>
      </el-form-item>
      <el-form-item label="中文">
        <el-select v-model="form.chinese" placeholder="是否支持中文" class="short3">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="英文">
        <el-select v-model="form.English" placeholder="是否支持英文" class="short3">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="数字">
        <el-select v-model="form.English" placeholder="是否支持数字" class="short3">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="特殊字符">
        <el-select v-model="form.English" placeholder="是否支持特殊字符" class="short2">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="是否区分大小写">
        <el-select v-model="form.English" placeholder="是否区分大小写" class="short2">
          <el-option
            v-for="item in islogin"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="是否唯一">
        <el-select v-model="form.English" placeholder="是否唯一" class="short">
          <el-option
            v-for="item in islogin"
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
      <el-table-column fixed prop="inter_name" label="字段名称" width="180" />
      <el-table-column prop="inter_url" label="是否必填" width="320" />
      <el-table-column prop="request_method" label="请求方式" width="120" />
      <el-table-column prop="request_form" label="请求格式" width="250" />
      <el-table-column prop="inter_token" label="是否需要登录" width="150" />
      <el-table-column prop="remark" label="备注" width="200" />
      <el-table-column fixed="right" label="操作" width="120">
        <template #default>
          <el-button link type="primary" size="small" @click="handleClick">编辑</el-button>
          <el-button link type="primary" size="small">删除</el-button>
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


const handleClick = () => {
  console.log('click')
}



const value = ref('')
const categgroys = [
  {
    value: 'string',
    label: 'string',
  },
  {
    value: 'int',
    label: 'int',
  },
  {
    value: 'list',
    label: 'list',
  },
  {
    value: 'object',
    label: 'object',
  },
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
const encryMethods = [
  {
    value: '无',
    label: '不需要加密',
  },
  {
    value: 'DES',
    label: 'DES',
  },
  {
    value: 'AES',
    label: 'AES',
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
    margin-top: 10px;
  }
  .inna {
    width: 500px;
  }
  .long{
    width: 220px;
  }
  .short{
    width: 100px;
  }
  .short2{
    width: 160px;
  }
  .short3{
    width: 130px;
  }
</style>
