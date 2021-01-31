<template>
  <el-container class="home-container">
    <el-header>
      <div>
        <img src="../assets/img/triller.png" alt="">
        <span>主页面数据管理</span>
      </div>
      <el-button @click="logout" type="warning">退出</el-button>
    </el-header>
    <el-container>
      <!--侧边栏-->
      <el-aside :width="getAsideWidth">
        <div class="toggle-btn" @click="toggleCollapse">|||</div>
        <el-menu :default-active="activePath" background-color="#eee" text-color="#000" active-text-color="#409eff"
                 :collapse="isCollapse" unique-opened :collapse-transition="false" router>
          <!--一级菜单-->
          <el-submenu :index="item.id + ''" v-for="item in menuList" :key="item.id">
            <!--一级菜单模板区域-->
            <template slot="title">
              <!--图标-->
              <i :class="item.icon"></i>
              <!--文本-->
              <span class="menu-item">{{ item.authName }}</span>
            </template>
            <el-menu-item :index="subitem.path" v-for="subitem in item.children" :key="subitem.id"
                          @click="saveNavState(subitem.path)">
              <template slot="title">
                <!--图标-->
                <i class="el-icon-menu"></i>
                <!--文本-->
                <span class="menu-item">{{ subitem.authName }}</span>
              </template>
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main>
        <!--        <img src="../assets/img/tq.jpg" alt="">-->
        <router-view></router-view>
      </el-main>
    </el-container>
    <el-footer height="30px">Footer</el-footer>
  </el-container>

</template>

<script>
import {getMenus} from "@/net";

export default {
  name: "home",
  data() {
    return {
      // 左侧菜单数据
      menuList: [],
      isCollapse: false,
      activePath: ''
    }
  },
  created() {
    this.getMenuList()
    this.activePath = sessionStorage.getItem("activePath")
  },
  computed: {
    getAsideWidth() {
      return this.isCollapse ? "64px" : "200px"
    }
  },
  methods: {
    toggleCollapse() {
      this.isCollapse = !this.isCollapse
    },
    saveNavState(activePath) {
      sessionStorage.setItem("activePath", activePath)
    },

    logout() {
      // 清除token 跳转主页面
      sessionStorage.clear()
      this.$router.push('/login')
    },

    getMenuList() {
      getMenus().then(res => {
        window.console.log(res.data);
        this.menuList = res.data.data
      })
    }
  }
}
</script>

<style lang="less" scoped>
.home-container {
  height: 100%;
}

.el-header {
  background-color: #409eff;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-left: 0;
  font-size: 18px;

  > div {
    display: flex;
    align-items: center;
    color: #fff;

    > img {
      width: 50px;
      height: 50px;
      margin: 10px;
    }
  }
}

.el-aside {
  background-color: #eee;

  .el-menu {
    border-right: none;
    border-right: none;
  }
}

.el-main {
  background-color: #bbb;
  margin: 0;
  padding: 0;

  > img {
    width: 1196px;
    height: 563px;
  }
}

.toggle-btn {
  background-color: #ccc;
  font-size: 10px;
  line-height: 25px;
  color: #409eff;
  text-align: center;
  letter-spacing: 0.2em;
  cursor: pointer;
}

.menu-item {
  margin-left: 10px;
}
</style>