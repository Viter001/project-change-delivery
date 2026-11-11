# Project Change Delivery · 项目推进与交付

当一个项目同时有十几个议题，逐条看完反馈，也未必知道今天该推进什么。Project Change Delivery 是一套供 AI agent 使用的中文 skill。它让 agent 从现有规划、反馈和验收记录中整理出当前阶段，接着推进已授权的工作，在需要你做取舍时给出具体问题。软件、文档、内容和数据项目都可以使用。

第一次使用或想查文件用途，请看[中文使用手册](USER-GUIDE.md)。手册用一次反馈整改演示从登记到验收，并索引全部技能参考文件。

## 从哪里看项目

**全景页**顶部用两句话说明「这一阶段要解决什么」和「现在正在做什么」。例如，编写指南的团队可能还不知道读者卡在哪里，这时阶段任务可以是观察一位新读者按指南完成安装。等有了观察结果，再决定改哪一节。相关议题放在阶段下，全景中的关系图展示它们之间已有依据的依赖。

**注意力页**默认打开，集中展示需要你决策、验收或介入的事项。普通修复可以作为成果告知，几个体验细节可以留到同一次阶段验收。当前没有需要你行动的事项时，页面可以显示零请求。

## 开始使用

1. 下载或克隆本仓库，将其中的 [project-change-delivery](project-change-delivery/) 文件夹放进你的 agent 支持的技能目录。也可以让 agent 直接读取仓库中的 [SKILL.md](project-change-delivery/SKILL.md)。
2. 在要推进的项目中提出一个具体任务。例如：「使用 project-change-delivery，读当前规划和反馈，告诉我这一阶段在解决什么、正在做什么，以及哪些事需要我决定。」
3. 想持续查看时，可以说：「在这个项目建立全景和注意力视图。」Agent 按[生成与维护规范](project-change-delivery/references/project-view-generation.md)创建项目自己的视图。后续就在推进项目的会话里更新主记录并刷新。

## 工作如何接续

重要取舍记入 Questions，普通反馈进入整改清单。阶段成果、对话复盘和 agent 的运行记录各有入口，方便负责人看结果，也方便下一位 agent 接手时找到未完成的工作。变更交付时，agent 根据影响选择验证方式，区分已实现、已验证和已由用户验收。

项目可以只在本地使用。在具备 GitHub 连接并获得同步授权时，agent 也可以按 [Issue 同步规程](project-change-delivery/references/issue-sync.md)上传、拉取或双向同步事项。

更多使用场景见[试用指南](TRYOUT.md)，已验证的范围见[验证记录](docs/validation.md)。维护者可运行 `python scripts/package_release.py` 生成分发包。
