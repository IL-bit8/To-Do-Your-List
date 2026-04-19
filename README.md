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
| Liu Hao | Framework design, testing, and documentation | 50% |
| Xu Junheng | Content implementation and improvement, promotion / backend  | 50% |

### 3.2 Sprint Schedule
![用例图](./docs/sprint.md)

### 3.3 Current Status and Future Plans
- **Current**: Functional testing integration completed; next steps: work on README, complete documentation, and create a demo video.
- **Future**: Add to‑do list sharing functionality with real‑time Markdown preview.

## 4. System Design Model
### Use Case Diagram
![用例图](./docs/usecase.png)

### Class Diagram
![类图](./docs/classdiagram.png)

## 5. Reference

HOW TO USE:
Firstly get into the "TO-DO-YOUR-LIST".Then, in Termainal, input 
```python
python start.py
```
you can use it.

## 5. Reference
![外部引用声明](./docs/reference.md)
