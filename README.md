# To-Do-Your-List
a small app for the computer lover but have their procrastination

# Usage
Click the *Start* button to add new task alarm clock.

## 1. Graphical Abstract
![系统架构与用例概览](./docs/abstract.png)

## 2. Purpose of the Software
- **开发流程选型**：我们采用 **Agile (Scrum)** 而非瀑布模型，因为……
- **目标用户**：大学生及知识工作者，需要一个轻量级的云笔记工具。

## 3. Software Development Plan

### 3.1 团队成员角色与分工
| 姓名 | 角色 | 职责 | 工作量占比 |
|------|------|------|------------|
| 张三 | Scrum Master / 后端 | Sprint 进度跟踪、API 开发 | 35% |
| 李四 | 前端开发 | UI 实现与联调 | 35% |
| 王五 | 测试与文档 | 测试用例、README 撰写 | 30% |

### 3.2 Sprint 计划表
（此处插入上文的 Sprint 表格）

### 3.3 核心算法简述
- 使用 **bcrypt** 进行密码哈希加盐存储。
- 笔记搜索采用 **TF-IDF** 进行关键词匹配（引用 `scikit-learn` 库）。

### 3.4 当前状态与未来计划
- **当前**：完成 Sprint 3，核心功能已跑通。
- **未来**：增加笔记分享功能，支持 Markdown 实时预览。

## 4. 系统设计模型
### 用例图
![用例图](./docs/usecase.png)

### 类图
![类图](./docs/classdiagram.png)