# ts-flow

> Qt翻译ts文件键值对管理器
>
> 功能包含：上传键值对文件，编辑，记录版本管理，下载键值对文件，飞书自动翻译

## 开发环境配置

准备nodejs和python3.10环境

- Node: 20.12.1
- Python: 3.10

安装`yarn`包管理

```bash
npm install --global yarn
```

安装`poetry`管理python项目的环境和依赖

```bash
pip install poetry
```

使用`poetry`创建虚拟环境

```bash
# 进入server目录
cd server

poetry env use python3.10

# 查看当前项目激活环境
poetry env list
```

> 开发时，python想获取正确补全提示需指定虚拟环境解释器路径
>
> 虚拟环境所在路径一般在`~/.cache/pypoetry/virtualenvs`目录下
>
> 如解释器路径`/root/.cache/pypoetry/virtualenvs/kv-2lXqAPel-py3.10/bin/python`

回到项目根目录，安装前后端所有依赖

```bash
yarn install-all
```

开发环境调试前，在`server`目录下新建`.web-server`目录和`.env.dev`文件

`.web-server`目录结构示例：

```bash
.web-server
├── kv
│   ├── backup
│   ├── database
│   └── downloads
└── uploads
```

`.env.dev`文件内容示例：

```bash
KV_SERVER_ADDRESS=0.0.0.0
KV_SERVER_PORT=11028
KV_WEBSERVER_PATH=../.web-server
KV_FRONTEND_PATH=../dist
FEISHU_APP_ID=cli_xxxxxxxxxxxxxxx
FEISHU_APP_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxx
```

运行

```bash
# 生成前端打包后的dist文件夹
yarn build

# 启动后端服务
yarn dev-server
```

访问

```bash
http://localhost:11028/ts-flow
```

打包相关指令看下文

## 编译和运行

### 运行

> 开发环境

```bash
yarn build

yarn dev-server

yarn dev

# 生产环境预览
yarn build-all
yarn preview-after-build
```

> 生产环境

### 打包

```bash
yarn build-all

# 打成tar包
yarn package-tar
```

命令行运行·，示例：

```bash
./ts-flow-start
```
