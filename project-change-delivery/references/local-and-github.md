# 本地与 GitHub 工作流

## 术语与载体

| 概念 | 纯本地载体 | GitHub 载体 |
| --- | --- | --- |
| Question／Decision：重大变更与裁决 | QUESTIONS.md，Q-编号 | Issue，分类标签 decision |
| Feedback：会议反馈与整改 | FEEDBACK.md，FB-编号，旧 REVIEW 编号保留映射 | Issue，分类标签 meeting-feedback |
| Commit：修改快照 | 本地 Git commit，中文标题与说明 | 推送后同一提交出现在远程历史 |
| Review：代码修改评审 | 相关条目或开发日志的代码评审栏 | PR review 和讨论；不等于会议反馈 |
| Checks：验证执行 | 本地测试与验收证据，标明本地执行 | 已配置并实际运行的检查结果 |
| PR：请求合入分支 | 可准备 PR 草稿；本地不存在 GitHub PR 对象 | 比较远程 head/base 分支的真实 Pull Request |
| 开发日志 | DEVLOG.md，保留沟通与工作流摘要 | 仍保留日志；PR 引用相关条目，不整段重复 |
| Changelog：面向使用者的版本变化 | 需要时维护 CHANGELOG.md | 可用于 Release notes；不代替开发日志 |

验收条件与 Checks 结果分开：条件定义合格标准，结果说明某个版本的一次执行。Review 不能冒充用户验收；本地检查成功不能写成 GitHub Checks 成功。

## 三种模式

### 纯本地，不使用 GitHub

在具体项目目录使用 Git 保存提交、分支、差异与合并；Question 与 Feedback 以各自文件记录。按四条规则补管理载体、验证、开发日志和中文提交。无需账户、远程仓库或 PR。

举例：FB-001 描述一个导出缺陷，修复并验证后在复验栏记录验收结果，必要时另记代码评审意见，DEVLOG 记执行摘要，中文 commit 引用 FB-001，最后更新状态。一个条目只在主要载体维护，其他文件引用。

### 用 GitHub 管需求，代码仍只在本地

可在有权限且启用 Issues 的 GitHub 仓库管理任务，不要求先把业务代码推上去。Issue 文字和附件会保存到 GitHub，私有仓库也不是本地存储。代码未同步时，不能把本地修改描述成已经可在 GitHub 审查的 PR。

### 本地开发并同步 GitHub

开发、运行和调试仍在本机进行；获授权后把分支提交推送到 GitHub，创建 PR，关联 Issue，在平台记录 review/checks，按授权合入。Merge 不等于部署或发布；创建远程、推送与外部操作不由改名自动授权。

## 新手如何创建 Issue

在目标仓库打开 Issues → New issue，按模板或空白表单填写标题与描述，再提交。标题说明要解决的问题；描述包含现状、期望结果、完成条件与必要附件。获得真实 URL 后才能报告“GitHub Issue 已创建”。本地写好草稿不是已提交。

创建 Issue 不要求写代码，也不自动启动开发。界面入口不可用时先检查登录权限和仓库是否启用 Issues。

## 切换与去重

默认保留现有工作模式，不因采用 GitHub 名词自动迁移。迁移时把本地编号映射到实际 GitHub URL，保留来源，确定主要维护位置。采用远程主记录模式时，本地 README 或两类事项索引放链接和映射；启用 [双向同步](issue-sync.md) 后，本地可以保留可编辑正文，但必须保存共同基线并按冲突规则同步，不再视为独立状态。不要假定 FB-001 就是 GitHub #1。

开发日志的沟通和工作流摘要继续保留，详细运行日志按记录分层保存在 agent 目录，Issue 负责需求状态，PR 负责该组修改与合入讨论；重复材料用链接连接。只有用户允许替换记录载体时，才以 PR 全面替代开发日志。

## 官方参考

- [Git 与 GitHub](https://docs.github.com/en/get-started/using-git/about-git)
- [创建 Issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue)
- [创建 PR](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request)

本参考解释概念与入口，具体界面和工具参数使用时按官方文档核对。
