<template>
  <div class="demo-collapse" style="margin-left: 10px;">
    <el-collapse v-model="activeName" accordion>
      <el-collapse-item title="常用正则类" name="1">
        <div>
          <el-form :model="form" ref="ruleForm" class="all">
            <el-form-item label="字段名称" class="long el-form-item">
              <el-input v-model="form.field_names" />
            </el-form-item>
            <el-form-item label="必填" class="el-form-item" required>
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
            <el-form-item label="类型" class="el-form-item">
            <el-select v-model="form.categroys" placeholder="选择文本类型" class="short3">
              <el-option
                v-for="item in categgroys"
                :key="item.value"
                :label="item.label"
                :value="item.value"
                :disabled="item.disabled"
              />
            </el-select>
            </el-form-item>
            <el-form-item label="加密方式" class="el-form-item" required>
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
            <el-form-item label="正则" class="el-form-item" required>
              <el-select v-model="form.regions" placeholder="选择正则方式" class="short3">
                <el-option
                  v-for="item in regionMethod"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                  :disabled="item.disabled"
                />
              </el-select>
            </el-form-item>
            <el-form-item style="width: 250px" label="备注" class="el-form-item">
              <el-input v-model="form.remarks" />
            </el-form-item>
            <el-form-item style="margin-left: 50px">
              <el-button type="primary" @click="onSubmit">添加</el-button>
              <el-button @click="cancel">取消</el-button>
            </el-form-item>
        </el-form>
        </div>
      </el-collapse-item>
      <el-collapse-item title="文本输入框类" name="2">
        <div>
          Decision making: giving advices about operations is acceptable, but do
          not make decisions for the users;
        </div>
        <div>
          Controlled consequences: users should be granted the freedom to
          operate, including canceling, aborting or terminating current
          operation.
        </div>
      </el-collapse-item>
      <el-collapse-item title="数字输入框类" name="3">
        <div>
          Operation feedback: enable the users to clearly perceive their
          operations by style updates and interactive effects;
        </div>
        <div>
          Visual feedback: reflect current state by updating or rearranging
          elements of the page.
        </div>
      </el-collapse-item>
      <el-collapse-item title="日期选择类" name="4">
        <div>
          Simplify the process: keep operating process simple and intuitive;
        </div>
        <div>
          Definite and clear: enunciate your intentions clearly so that the
          users can quickly understand and make decisions;
        </div>
        <div>
          Easy to identify: the interface should be straightforward, which helps
          the users to identify and frees them from memorizing and recalling.
        </div>
      </el-collapse-item>
      <el-collapse-item title="与其他接口字段关联" name="5">
        <div>
          Decision making: giving advices about operations is acceptable, but do
          not make decisions for the users;
        </div>
        <div>
          Controlled consequences: users should be granted the freedom to
          operate, including canceling, aborting or terminating current
          operation.
        </div>
      </el-collapse-item>
      <el-collapse-item title="与字段值关联" name="6">
        <div>
          Decision making: giving advices about operations is acceptable, but do
          not make decisions for the users;
        </div>
        <div>
          Controlled consequences: users should be granted the freedom to
          operate, including canceling, aborting or terminating current
          operation.
        </div>
      </el-collapse-item>
      <el-collapse-item title="附件类" name="7">
        <div>
          Decision making: giving advices about operations is acceptable, but do
          not make decisions for the users;
        </div>
        <div>
          Controlled consequences: users should be granted the freedom to
          operate, including canceling, aborting or terminating current
          operation.
        </div>
      </el-collapse-item>
    </el-collapse>
    <el-table :data="tableData" style="width: 100%; margin-left: 20px; margin-top: 30px">
      <el-table-column fixed prop="field_name" label="字段名称" width="180" />
      <el-table-column prop="musts" label="是否必填" width="100" />
      <el-table-column prop="categroys" label="字符类型" width="100" />
      <el-table-column prop="desc" label="详细描述" width="700" />
      <el-table-column prop="remark" label="备注" width="200" />
      <el-table-column fixed="right" label="操作" width="120">
        <template #default="scope">
          <el-button link type="primary" size="small"  @click="editRow(scope.row)">修改</el-button>
          <el-button link type="primary" size="small">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>

  <el-dialog v-model="dialogFormVisible" title="修改">
    <el-form :model="eidtform">
        <el-form-item label="字段名称" prop="field_names">
          <el-input v-model="eidtform.field_names"></el-input>
        </el-form-item>
        <el-form-item label="是否必填" prop="name">
          <el-select v-model="eidtform.musts" placeholder="是否必填" class="short">
                <el-option
                  v-for="item in islogin"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                  :disabled="item.disabled"
                />
              </el-select >
        </el-form-item>
        <el-form-item label="类型" class="el-form-item">
          <el-select v-model="eidtform.categroys" placeholder="选择文本类型" class="short3">
              <el-option
                v-for="item in categgroys"
                :key="item.value"
                :label="item.label"
                :value="item.value"
                :disabled="item.disabled"
              />
            </el-select>
        </el-form-item>
        <el-form-item label="加密方式" class="el-form-item" required>
          <el-select v-model="eidtform.encry_method" placeholder="选择加密方式" class="short3">
            <el-option
              v-for="item in encryMethods"
              :key="item.value"
              :label="item.label"
              :value="item.value"
              :disabled="item.disabled"
            />
          </el-select>
        </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="dialogFormVisible = false">
          确定
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'
import { ElMessage } from 'element-plus'
import {addField, addInter, getField, getInter} from "../apis/apis.js";
import { useRoute, useRouter } from "vue-router";
const route = useRoute()
const router = useRouter()
const ruleForm = ref()
// do not use same name with ref

const dialogFormVisible = ref(false)

const form = reactive({
  field_names: '',
  musts: '',
  categroys: '',
  inter_format: '',
  regions: '',
  remarks: '',
  iid: route.query.id
})

const eidtform = reactive({
  field_names: '',
  musts: '',
  categroys: '',
  encry_method: '',
  regions: '',
  remarks: '',
  iid: route.query.id
})

// 修改字段
const editRow = (row) => {
  dialogFormVisible.value = true
  // 需要在弹窗显示之后传值
  Object.assign(eidtform, row)   // 整体赋值方法
}

const tableData = ref()
getField({id: route.query.id}).then(res => {
      tableData.value = res.data
    })

const onSubmit = () => {
  addField(form).then(res => {
    ElMessage({
      message: res.message,
      type: 'success',
    })
    // 清空表单
    form.field_names = ""
    form.musts = ""
    form.categroys = ""
    form.inter_format = ""
    form.regions = ""
    form.remarks = ""
  })
}

const cancel = () => {
  router.back()
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
const regionMethod = [
  {
    value: '手机号码',
    label: '手机号码',
  },
  {
    value: '密码',
    label: '密码',
  },
  {
    value: '身份证号码',
    label: '身份证号码',
  },
  {
    value: '邮箱',
    label: '邮箱',
  },
  {
    value: '统一社会信用代码',
    label: '统一社会信用代码',
  },
  {
    value: '邮政编码',
    label: '邮政编码',
  },
  {
    value: '地区编码',
    label: '地区编码',
  },
  {
    value: '网址',
    label: '网址',
  },
]
const activeName = ref('1')
</script>

<style scoped>
.el-button--text {
  margin-right: 15px;
}
.el-select {
  width: 300px;
}
.el-input {
  width: 300px;
}
.dialog-footer button:first-child {
  margin-right: 10px;
}
  .all {
    display: flex;
    flex-wrap: wrap;
    justify-content: left;
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
  .el-form-item {
    margin-left: 7px;
  }
</style>