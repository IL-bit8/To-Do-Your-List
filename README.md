# To-Do-Your-List
A small app for the computer lover but have their procrastination.

## How To Use
Click the *Start a To-Do* button to add new To-Do task.

Click the *Check if press button* button to see when you last pressed the button.

## Configurable
You can choose your preferred *language*.

You can choose your favorite *ringtone*.

## 1. Graphical Abstract
![系统架构与用例概览](./docs/abstract.png)

## 2. Purpose of the Software
- **Development process selection**：We use **Agile (Scrum)** instead of the waterfall model because the requirements for note-taking tools iterate rapidly based on user feedback (e.g., inputting to-do names, countdown timers, alarm countdowns, Markdown support for documents, etc.). Agile development allows us to deliver a usable incremental version every 1-2 days.

- **Sprints** allow for timely prioritization, avoiding the high costs associated with later modifications in a waterfall model.

- We use **Git** for version control, **GitHub Issues** for managing user stories and tasks, and **GitHub Actions** for continuous integration, supporting rapid iteration.

- **Target Users**: University students and knowledge workers who need a lightweight to-do tool.

## 3. Software Development Plan

### 3.1 Team member roles and division of labor
| Name | Task | Workload Percentage |
|-------|---------------------|------------|
| 刘灏 | 框架设计和测试与文档 | 50% |
| 許駿恆 | 内容实现和完善与宣传 / 后端 | 50% |

### 3.2 Sprint Schedule
![用例图](./docs/sprint.md)

### 3.3 Core Algorithm Brief
- 使用 **bcrypt** 进行密码哈希加盐存储。
- 笔记搜索采用 **TF-IDF** 进行关键词匹配（引用 `scikit-learn` 库）。

### 3.4 Current Status and Future Plans
- **Current**: 功能测试集成完毕，后续处理readme，文档补全和演示视频。
- **Future**: 增加To-do-list分享功能，支持 Markdown 实时预览。

## 4. System Design Model
### 用例图
![用例图](./docs/usecase.png)

### 类图
![类图](./docs/classdiagram.png)

## 5. Reference
![外部引用声明](./docs/reference.md)
