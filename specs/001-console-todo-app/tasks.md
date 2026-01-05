---

description: "Task list for Console Todo App implementation"
---

# Tasks: Console Todo App (In-Memory)

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan in src/
- [ ] T002 Initialize Python 3.13+ project with basic directory structure
- [x] T003 [P] Create basic directory structure: src/models/, src/services/, src/cli/, src/lib/, tests/unit/, tests/integration/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 [P] Create Task model in src/models/task.py based on data-model.md
- [x] T005 [P] Create TaskService in src/services/task_service.py with basic CRUD operations
- [x] T006 Create main application entry point in src/cli/menu.py
- [x] T007 Implement in-memory storage mechanism using Python dictionaries/lists
- [x] T008 Create utility functions in src/lib/utils.py for input validation and formatting

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks to their todo list with title and optional description

**Independent Test**: Can add a task with a title and optional description, then verify it appears in the task list.

### Implementation for User Story 1

- [x] T009 [US1] Implement add_task function in src/services/task_service.py with validation
- [x] T010 [US1] Create add task UI function in src/cli/menu.py
- [x] T011 [US1] Add input validation to ensure title is not empty
- [x] T012 [US1] Implement unique ID generation for new tasks
- [ ] T013 [US1] Test adding tasks with valid and invalid inputs

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P2)

**Goal**: Allow users to view all their tasks with ID, title, description, and completion status

**Independent Test**: Can add tasks and then view the complete list with all details.

### Implementation for User Story 2

- [x] T014 [US2] Implement get_all_tasks function in src/services/task_service.py
- [x] T015 [US2] Create view tasks UI function in src/cli/menu.py
- [x] T016 [US2] Format task display with ID, title, description, and status (✔/❌)
- [x] T017 [US2] Handle case when no tasks exist with friendly message
- [ ] T018 [US2] Test viewing tasks when none exist and when multiple exist

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task Details (Priority: P3)

**Goal**: Allow users to update existing tasks with new title and/or description

**Independent Test**: Can update an existing task and verify the changes persist.

### Implementation for User Story 3

- [x] T019 [US3] Implement update_task function in src/services/task_service.py
- [x] T020 [US3] Create update task UI function in src/cli/menu.py
- [x] T021 [US3] Add validation to ensure task ID exists before updating
- [x] T022 [US3] Ensure only provided fields are updated (partial updates)
- [ ] T023 [US3] Test updating tasks with valid and invalid IDs

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Tasks (Priority: P4)

**Goal**: Allow users to delete tasks they no longer need

**Independent Test**: Can delete a task and verify it no longer appears in the task list.

### Implementation for User Story 4

- [x] T024 [US4] Implement delete_task function in src/services/task_service.py
- [x] T025 [US4] Create delete task UI function in src/cli/menu.py
- [x] T026 [US4] Add validation to ensure task ID exists before deletion
- [ ] T027 [US4] Test deleting tasks with valid and invalid IDs
- [ ] T028 [US4] Verify deleted task no longer appears in task list

**Checkpoint**: At this point, User Stories 1-4 should all work independently

---

## Phase 7: User Story 5 - Mark Tasks Complete/Incomplete (Priority: P5)

**Goal**: Allow users to toggle task completion status

**Independent Test**: Can toggle a task's completion status and verify the change is reflected.

### Implementation for User Story 5

- [x] T029 [US5] Implement toggle_task_status function in src/services/task_service.py
- [x] T030 [US5] Create mark task UI function in src/cli/menu.py
- [x] T031 [US5] Add validation to ensure task ID exists before toggling
- [x] T032 [US5] Display updated status to user after toggle
- [ ] T033 [US5] Test toggling completion status for both complete and incomplete tasks

**Checkpoint**: At this point, all user stories should be independently functional

---

## Phase 8: Menu System & Navigation

**Goal**: Implement the main menu system that allows users to navigate between all features

### Implementation for Menu System

- [x] T034 Create main menu loop in src/cli/menu.py
- [x] T035 Implement menu options 1-6 as specified in feature spec
- [x] T036 Add error handling for invalid menu inputs
- [x] T037 Implement graceful exit functionality
- [ ] T038 Test menu navigation between all options

---

## Phase 9: Error Handling & Validation

**Goal**: Ensure all inputs are handled safely without application crashes

### Implementation for Error Handling

- [x] T039 Add input validation across all user inputs
- [x] T040 Implement graceful handling of invalid task IDs
- [x] T041 Add error messages for all failure scenarios
- [ ] T042 Test all error handling paths
- [x] T043 Ensure application doesn't crash on invalid inputs

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T044 [P] Add unit tests for all model and service functions in tests/unit/
- [x] T045 [P] Add integration tests for CLI interactions in tests/integration/
- [x] T046 Code cleanup and refactoring
- [x] T047 Documentation updates in README.md
- [x] T048 Run quickstart.md validation
- [x] T049 Final end-to-end testing of all features

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4 → P5)
- **Menu System (Phase 8)**: Depends on all user stories being implemented
- **Error Handling (Phase 9)**: Can be done in parallel with other phases
- **Polish (Phase 10)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Models before services
- Services before UI components
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Add Menu System → Test complete application
8. Add Error Handling → Ensure robustness
9. Polish and test → Final product ready
10. Each story adds value without breaking previous stories

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence