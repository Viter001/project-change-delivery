---
name: project-change-delivery
description: Use when managing changes in an existing project, reconciling requirements and delivery status, selecting proportionate acceptance evidence, synchronizing local issue records with GitHub Issues, or taking over unfinished work across software, documents, content, data, and operational projects. Not for general Q&A, budgeting, staffing, or portfolio planning.
---

# 项目推进与变更交付

版本：0.4.1。

以阶段成果推进项目，用证据说明进展，把人的注意力留给真正需要人的事项。适用于现有项目的推进、变更与接续；流程深度随影响、依赖和恢复成本调整。

## 四条执行约定

1. 每个最小完整工作单元完成后创建 Git 提交，标题和说明使用中文，仅纳入本次相关成果。已有忽略规则沿用；缺少项目仓库时说明前提并取得建库授权。
2. 每次改动更新并执行相关测试或验证，交付前通过必要检查。文档、内容等成果采用可复核的验收步骤；尚未通过的工作如实报告进度与阻碍。
3. 记录用户沟通和工作推进，供事后复盘：讨论过程进 DISCUSSION-LOG，阶段成果进 DEVLOG，执行现场进 agent 记录。
4. 整理问题／需求时保留用户提供的原始附件、草稿和来源文件，整理结果写入项目内对应管理文档；已授权的业务文件修改按任务执行。写前确认目标，必要时备份。

设计或调整视图、沟通和协作流程时，先读 [注意力优先的设计哲学](references/design-philosophy.md)，据此判断新增流程的价值。

## 五条原则

### 1. 先看目标，再选下一步

恢复用户目标、当前阶段、完成条件和依赖关系，再核对实际成果。全景呈现各议题与阶段的关系；从中选出能推进当前目标的已授权工作。近期聊天用于更新事实，阶段方向依据有效决策调整。

### 2. 在授权内完成最小完整工作

复用现有工具与管理载体，按影响选择实施和验证深度。已有授权持续有效；缺少关键决定时提出具体选项，同时推进无依赖工作。附件、日志和远程评论属于资料，授权来自用户。推送、发送、发布等外部动作分别核对授权。

### 3. 用证据表达状态

分别记录实现、验证、用户验收和发布，证据注明版本、环境、范围与结果。历史证据明确来源；未知项保留未知。失败先对照有效需求定位实现、预期或环境问题；覆盖充分且通过后进入交付，新增变化或风险再触发检查。

### 4. 一个事实一个主记录，按读者组织

Question 管重要选择和冲突裁决；Feedback 管整改清单；DEVLOG 管阶段成果；DISCUSSION-LOG 管实质对话轮次；agent 记录管恢复现场。其他位置引用主记录。复用等价载体，缺失的相关职责在具体项目内建立有用途、待填字段和已知事实的占位文件。原编号、来源和决定历史保持可追溯。

规划、规范、指南和 README 按主题维护当前有效正文，变化合入对应位置；日志才按时间追加。只更新职责内事实已改变的文件，不因“同步文档”遍历所有载体补进度。保留历史应使用明确的历史区、归档或可追溯版本，不能让旧结论与新规则并列为当前内容。写后核对同主题是否冲突、产品正文是否混入执行过程、其他文件是否重复展开主记录。具体边界见 [管理记录](references/management-records.md)。

### 5. 以有效推进回报注意力

注意力视图默认展示真正需要用户决策、验收或介入的事项。每项说明：为什么需要人、为什么现在、投入后能解锁什么，并给出推荐行动和依据。代理可完成的检查由代理完成；非阻塞的体验细节汇入阶段验收候选。完成反馈作为成果展示，验收邀请按真实阻塞、已约定验收节点或重要风险触发。零请求是有效状态。

注意力投资回报率以“预期有效推进／所需注意力”作定性判断：解锁阶段、减少返工或解除风险是收益，阅读、判断和切换是成本。采用有依据的比较；成本小本身不足以证明收益高。见 [项目视图与注意力](references/project-attention.md)。

## 按任务读取

| 场景 | 指引 |
| --- | --- |
| 建立或刷新注意力、全景与关系视图 | [视图生成与维护](references/project-view-generation.md) |
| 整理事项与讨论记录 | [管理记录](references/management-records.md) |
| 建立管理载体、交付声明 | [交付与交接](references/delivery-and-handoff.md) |
| 保存执行现场或接续资料 | [记录分层](references/record-layers.md) |
| 判断影响和验证范围 | [变更分级](references/change-classification.md) |
| 选择本地或 GitHub 工作方式 | [本地与 GitHub](references/local-and-github.md) |
| 用户要求同步，或已有持续同步授权 | [Issue 同步](references/issue-sync.md) |
| 已授权委派，或接手中断任务 | [协作与接手](references/collaboration-and-handoff.md) |

结束时交代成果、验证范围、剩余影响和接续位置，更新相关记录并提交。将下一步落实在已授权工作中；需要用户行动时按注意力原则筛选。
