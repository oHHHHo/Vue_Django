<template>
  <div class="login_container">
    <div class="login_box">
      <div class="avatar_box">
        <img src="../assets/img/triller.png" alt="">
      </div>
      <!--表单登录区域-->
      <el-form :model="loginForm" :rules="rules" ref="refForm" class="login_form">
        <el-form-item prop="username">
          <el-input type="text" prefix-icon="el-icon-user" placeholder="账号" v-model="loginForm.username"></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input type="password" prefix-icon="el-icon-lock" v-model="loginForm.password" placeholder="密码"></el-input>
        </el-form-item>
        <el-form-item class="btn_s">
          <el-button type="primary" :loading="logining" @click="loginBtn()">登陆</el-button>
          <el-button type="info" @click="resetBtn()">重置</el-button>
        </el-form-item>
      </el-form>
    </div>

  </div>
</template>
<script>
import {login} from "@/net";

export default {
  name: "Login",
  data() {
    return {
      logining: false,
      loginForm: {
        username: "",
        password: "",
      },
      rules: {
        username: [
          {required: true, message: "请输入账号", trigger: "blur"},
          {
            pattern: /^(?!(\d+)$)[a-zA-Z\d_]{4,20}$/,
            message: "账号长度4-20，可包括数字、字母、下划线",
            trigger: "blur"
          }
        ],
        password: [
          {required: true, message: "请输入密码", trigger: "blur"},
          // {
          //   pattern: /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,20}$/,
          //   message: "密码长度为6-20位，可以为数字、字母",
          //   trigger: "blur"
          // }
        ]
      }
    };
  },
  methods: {
    //密码判断渲染，true:暗文显示，false:明文显示
    changePass(value) {
      this.visible = !(value === "show");
    },
    // <!--提交登录-->
    loginBtn() {
      this.$refs.refForm.validate(valid => {
        if (valid) {
          this.logining = true;

          let formData = new FormData();
          for (let key in this.loginForm) {
            formData.append(key, this.loginForm[key]);
          }

          // 请求登录
          login(formData).then(res => {
            let result = res.data.result
            if (result == 'success') {
              this.$message.success('登录成功！')
              sessionStorage.setItem("token", res.data.token)
              this.$router.push('/home')
            } else {
              this.$message.error('登录失败！')
            }
            this.logining = false;
          })
        } else {
          window.console.log("error submit!!");
        }
      });
    },

    resetBtn() {
      this.$refs.refForm.resetFields()
    }
  }
};
</script>
<style lang="less" scoped>

.login_container {
  background: #2b4b6b;
  height: 100%;
}

.login_box {
  width: 450px;
  height: 300px;
  background: #eee;
  border-radius: 3px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.avatar_box {
  height: 130px;
  width: 130px;
  border: 1px solid #eee;
  border-radius: 50%;
  padding: 5px;
  background-color: #fff;
  box-shadow: 0 0 10px #ddd;
  position: absolute;
  left: 50%;
  transform: translate(-50%, -50%);

  img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background-color: #eee;
  }
}

.login_form {
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 0 30px;
  box-sizing: border-box;
}

.btn_s {
  text-align: center
}
</style>