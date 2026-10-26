# 项目变更管理与交付闭环

`project-change-delivery` 是面向 AI agent 的项目协作 skill，当前版本 **0.1.0 试用版**。规则内容以中文为主，可用于软件、文档、内容与数据项目。

## 包含什么

- 变更分级、相关验证、中文 Git 提交及原始材料保护。
- QUESTIONS 管重要变更与裁决，FEEDBACK 管会议反馈与整改；PR Review 专指代码评审。
- 用户可读记录与 agent 实时日志分层。
- 已有协作工具委派，以及代理中断后的接手续做。
- 本地与 GitHub Issue 分类同步规程：去重、三方比较、冲突保留和失败恢复。

入口为 [SKILL.md](project-change-delivery/SKILL.md)，参考文件按任务需要加载。

## 试用

下载 Release 中的 `project-change-delivery-v0.1.0.zip`，解压后阅读 [TRYOUT.md](TRYOUT.md)。不要把整个源码仓库当作 skill 目录安装；使用压缩包内的 `project-change-delivery/` 文件夹。

这是规则型 skill，不是同步程序或后台服务。GitHub 同步需要另外指定仓库、授权和可用工具；本版没有实测远程同步或跨宿主自动接手。四条执行规则含中文提交及验证要求，建议先在可恢复的测试项目试用。

## 维护与构建

`python scripts/package_release.py` 生成 ZIP、SHA256SUMS.txt 和文件清单。打包采用明确文件范围，不包括本机缓存、运行状态、项目历史提炼记录或凭据。

提炼依据见 [docs/extraction-notes.md](docs/extraction-notes.md)，验证范围见 [docs/validation.md](docs/validation.md)。

仓库为私有，试用 ZIP 可由维护者直接发给受邀朋友；未获仓库访问权限者无法直接下载私有 Release。试用不代表授予新的开源许可证。
