# 移动应用构建项目

这是一个配置了自动化构建流程的移动应用开发项目，支持通过GitHub Actions手动触发Android APK构建。

## 项目概述

本项目提供了完整的Android应用构建和CI/CD工作流，适用于React Native、Cordova、Ionic等跨平台移动开发框架。

## 功能特性

- 🚀 **自动化构建**: 支持Debug和Release版本的APK构建
- ⚙️ **手动触发**: 通过GitHub Actions界面手动启动构建流程
- 📦 **构建产物**: 自动上传生成的APK文件作为GitHub Artifacts
- 🔧 **多环境支持**: 支持开发和生产环境配置
- 📱 **跨平台**: 基于现代移动开发技术栈

## 快速开始

### 环境要求

- Node.js 18+
- Java 17 (OpenJDK Temurin)
- Android SDK
- Gradle 8.0.1+

### 本地开发

1. **克隆项目**
   ```bash
   git clone <repository-url>
   cd cursor-test
   ```

2. **安装依赖**
   ```bash
   npm install
   ```

3. **配置Android环境**
   ```bash
   # 确保ANDROID_HOME环境变量已设置
   export ANDROID_HOME=$HOME/Android/Sdk
   export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools
   ```

4. **运行项目**
   ```bash
   # 开发模式
   npm start
   
   # 构建Android应用
   cd android
   ./gradlew assembleDebug
   ```

## GitHub Actions 构建

### 手动触发构建

1. 进入GitHub仓库页面
2. 点击 **Actions** 选项卡
3. 选择 **Manual APK Build** 工作流
4. 点击 **Run workflow** 按钮
5. 选择构建类型：
   - `debug`: 开发版本，包含调试信息
   - `release`: 生产版本，已优化和签名

### 构建产物下载

构建完成后，可以在以下位置下载APK文件：
- 进入对应的workflow运行页面
- 在 **Artifacts** 部分下载生成的APK文件
- 文件名格式：`android-{build_type}-apk`

## 项目结构

```
.
├── README.md                           # 项目文档
├── .github/
│   └── workflows/
│       └── manual-build.yml           # GitHub Actions构建配置
├── android/                           # Android平台相关文件
├── package.json                       # Node.js项目配置
└── src/                              # 源代码目录
```

## 配置说明

### GitHub Actions 工作流

位置：`.github/workflows/manual-build.yml`

主要功能：
- 🔧 自动配置构建环境（Node.js、Java、Android SDK）
- 📦 安装项目依赖
- 🏗️ 执行Gradle构建
- 📤 上传构建产物

### 支持的构建类型

- **Debug构建**：包含调试信息，适用于开发和测试
- **Release构建**：经过优化的生产版本

## 开发指南

### 添加新功能

1. 从主分支创建功能分支
2. 进行开发和测试
3. 提交代码并创建Pull Request
4. 使用GitHub Actions验证构建

### 构建优化

- 确保`android/gradle.properties`配置正确
- 检查ProGuard规则（Release构建）
- 验证签名配置

## 常见问题

### 构建失败

1. **依赖问题**：检查`package.json`和`build.gradle`配置
2. **环境问题**：确认Node.js、Java版本符合要求
3. **权限问题**：确保`gradlew`脚本有执行权限

### APK下载

- 构建成功后，APK文件会在Artifacts中保留30天
- 可以直接安装到Android设备进行测试

## 贡献指南

1. Fork项目仓库
2. 创建功能分支
3. 提交更改
4. 创建Pull Request

## 技术支持

如有问题或建议，请：
- 创建GitHub Issue
- 查看项目Wiki文档
- 联系项目维护者

## 许可证

本项目采用 [MIT许可证](LICENSE)

---

> 💡 **提示**: 首次使用建议先运行Debug构建进行测试
