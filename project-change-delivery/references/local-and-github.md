# 本地与 GitHub

| 概念 | 本地载体 | GitHub 载体 |
| --- | --- | --- |
| Question／Decision | QUESTIONS.md，Q-编号 | decision 类 Issue |
| Feedback | FEEDBACK.md，FB-编号 | meeting-feedback 类 Issue |
| Commit | 中文提交，修改快照 | 推送后的同一提交 |
| Review | 代码评审记录 | PR review |
| Checks | 本地执行结果与证据 | 平台实际运行的检查 |
| PR | 合入说明草稿 | 真实分支合入请求 |
| DEVLOG | 阶段成果 | 可由 PR 引用 |
| Changelog | 面向使用者的版本变化 | 可用于 Release notes |

沿用当前模式：纯本地使用 Git 和管理文件；仅 GitHub 管事项时可保留代码在本地；本地开发并同步 GitHub 时按授权推送、创建 PR、合入或发布。每种平台状态以真实操作结果为据，合入与发布分别记录。

创建 Issue：在确认的仓库填写标题、现状、期望、完成条件与必要附件，提交后以真实 URL 绑定本地编号。具体入口和工具参数使用时核对官方文档。Issues 内容会保存到远程，按授权选择上传范围。

模式迁移保留来源、编号与 URL 映射。远程主记录模式在本地留索引；启用 [双向同步](issue-sync.md) 时，本地可编辑正文通过共同基线与远程协调。Discussion、Devlog 保留各自职责，重复内容用链接关联；替换既有载体依据用户授权。
