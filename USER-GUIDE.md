# Project Change Delivery 使用手册

这份手册面向使用 agent 推进项目的人。先用一个真实任务试一轮。想查某个文件时，可以直接跳到「业务项目里的文件」或「技能包里的文件」。

## 第一次使用

下载仓库源码或解压试用包，把含有 `SKILL.md` 和 `references/` 的整个 `project-change-delivery/` 文件夹放到所用工具的技能目录。如果工具支持直接读文件，也可以给它技能入口的实际路径。然后在**你要推进的业务项目**中打开会话，说明工作目录和任务。

> 请使用 project-change-delivery。先读 SKILL.md 和本项目现有规划、问题清单，告诉我这个阶段在解决什么、正在做什么，并列出依据。这轮只梳理现状。

第一次看结果时，点开它引用的一条规划或反馈，确认阶段描述与原文相符。探索期可以写「正在找出新用户在哪一步中断」和「正在观察第一次安装」，后续方向等观察有结果再确定。准备好实施时，直接指定事项，例如「处理 FB-003，验证导出结果并更新相关记录」。

## 跟着一条反馈走一遍

假设同事说「导出的清单缺少日期」。以下编号仅作示例。

1. **登记。** 请 agent 整理反馈。打开 `FEEDBACK.md`，应能从顶部清单看到 FB-003、现象、状态和下一步。原始反馈保留，细节在同一条记录内维护。
2. **决定。** 如果规范已经定义日期为导出日，agent 可以按授权修复。如果导出日与业务发生日都合理，且选哪一个会改变已有报表含义，agent 才把具体选择写入 `QUESTIONS.md`，由 FB-003 引用。决定后更新原条目。
3. **验证与交付。** 要求 agent 用一份实际导出物核对日期。验收记录写清使用的版本、输入和结果，DEVLOG 简记阶段成果。涉及用户体验的判断保留真实验收状态。完成的相关改动按项目约定以中文提交。
4. **查看全局。** 若项目已有视图，在同一会话说「刷新项目视图」。修复结果进入成果区。只有仍需你决定日期口径，或已到约定验收节点等情况，才会在注意力页看到行动请求。

## 业务项目里的文件

以下是常用名称。Agent 先寻找项目现有的等价载体，缺少当前工作需要的载体时才建立有用途和待填内容的占位文件。

| 想了解什么 | 去哪里看 | 谁在什么时候更新 |
| --- | --- | --- |
| 项目怎么开始、当前范围多大 | 项目 README、规划、规范与指南 | Agent 把已批准的范围或行为变化合入对应主题。使用者看这里了解当前约定。 |
| 哪些问题需要我拍板 | `QUESTIONS.md` | Agent 列明选项、影响和来源，你决定后更新同一个 Q，并跟踪落实状态。 |
| 会议提了哪些问题、还剩哪些 | `FEEDBACK.md` | Agent 在顶部维护未关闭清单，在 FB 详情记录整改、复验与关闭原因。 |
| 这个阶段交付了什么 | `DEVLOG.md` | 有阶段成果时，agent 记录结果、验证范围及剩余影响。 |
| 当时为什么改方向 | `DISCUSSION-LOG.md` | 有实质讨论时，agent 记录你的要求、回应及推进结果。可通过 D 编号追溯。 |
| 实际检查过什么 | `docs/acceptance.md` 或既有验收系统 | 执行者记录条件、环境、版本、结果和证据，人工确认单列。 |
| 上个 agent 中断后如何继续 | `.agent/runs/<任务>/<运行>/checkpoint.md` | 执行者在关键进展时留下恢复点。接手者确认目标、仍在运行的任务、实际文件和 Git 差异，再续做。 |
| 十几个议题之间是什么关系 | 项目视图目录，例如 `docs/project-views/` | Agent 根据主记录重建。注意力页看当前请求，全景顶部看阶段问题和行动，网络图看议题依赖。 |

首次需要视图时说「在本项目建立注意力和全景视图」。常见配套有 `index.html`（打开看）、`view-model.json` 或等价摘要（供生成）、`sources.json`（检查快照来源）、目录内的 README（记录刷新方式）及项目自己的生成和检查脚本。业务有变化时告诉推进项目的会话，由 agent 先更新主记录再生成页面。新会话可从项目入口和维护说明接手。

若使用 GitHub，可以说「把 FB-003 上传到指定仓库」或「双向同步已绑定的 Issues」。先确认目标仓库、授权范围及连接。`.issue-sync/config.json` 记录仓库和字段映射，`.issue-sync/state.json` 保存远程身份、上次同步的值和未完成操作。遇到双方改了同一段正文时，查看冲突版本再决定取哪一份。纯本地项目也可以直接用 Q 和 FB 编号管理事项。

## 技能包里的文件

这些文件供 agent 按任务查阅。你想调整使用方式或理解某次判断时，也可以直接看对应原文。

| 文件 | 什么时候读，以及能查到什么 |
| --- | --- |
| [SKILL.md](project-change-delivery/SKILL.md) | 每次启用的入口。规定中文提交、验证、开发记录、保护原件，并指向本次任务需要的参考。 |
| [management-records.md](project-change-delivery/references/management-records.md) | 一条信息不知道记到哪里时读。判断是待裁决事项、整改反馈、阶段成果还是讨论过程。 |
| [document-formats.md](project-change-delivery/references/document-formats.md) | 已选好文档、准备写入时读。查看清单和卡片字段，以及该更新原条目还是追加记录。 |
| [record-layers.md](project-change-delivery/references/record-layers.md) | 人要复盘或 agent 要接手时读。决定哪些内容给负责人看、哪些放运行目录、哪些证据需长期保存。 |
| [delivery-and-handoff.md](project-change-delivery/references/delivery-and-handoff.md) | 缺管理载体或准备交付时读。查看占位文件最少写什么，以及声称实现、验证、验收、发布各需要什么依据。 |
| [change-classification.md](project-change-delivery/references/change-classification.md) | 决定验证深度时读。按影响、依赖和恢复成本选择检查范围，例如共享模板需检查代表性导出物。 |
| [collaboration-and-handoff.md](project-change-delivery/references/collaboration-and-handoff.md) | 多个 agent 分工或中断接手时读。明确写入责任，核对任务跨越的提交及未提交成果。 |
| [project-attention.md](project-change-delivery/references/project-attention.md) | 判断要不要打扰负责人时读。检查为什么需要人、为什么现在、回答能解锁什么。 |
| [project-view-generation.md](project-change-delivery/references/project-view-generation.md) | 建立或刷新视图时读。给出当前阶段、关系网络、数据来源、刷新顺序和页面验收方式。 |
| [design-philosophy.md](project-change-delivery/references/design-philosophy.md) | 调整沟通方式或增加视图字段时读。根据注意力成本和行动价值判断是否值得保留。 |
| [local-and-github.md](project-change-delivery/references/local-and-github.md) | 选择工作方式时读。对照本地记录与 GitHub Issue、Commit、Checks、Review、PR 的作用。 |
| [issue-sync.md](project-change-delivery/references/issue-sync.md) | 实际上传、拉取或双向同步时读。规定 Q／FB 路由、稳定身份、三方比较及超时后的查重与恢复。 |

## 在下载包或仓库中找到说明

[TRYOUT.md](TRYOUT.md) 提供可自行尝试的场景，[VERSION](VERSION) 标识当前版本，[RELEASE-NOTES.md](RELEASE-NOTES.md) 记录各版本变化。源码仓库中的 `docs/` 保存设计与试验依据，`scripts/package_release.py` 供维护者制作分发包。日常工作时，直接在业务项目会话使用已安装的技能即可。
