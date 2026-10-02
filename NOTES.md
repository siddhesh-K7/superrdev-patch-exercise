
# Patch Notes

## Summary of Changes
- **SQL Logic:** Fixed AND/OR precedence bugs in `TaskRepository.java`, `search_tasks.sql`, and `task_search_package.sql` by adding parentheses around the OR condition.
- **Backend Performance:** Removed the intentional `Thread.sleep` block from `TaskController.java` that was artificially delaying API responses.
- **Pagination Validation:** Added basic boundary checks in `TaskController.java` to prevent invalid page (`< 1`) or excessively large page sizes (`> 100`).
- **Frontend State & UX:** Rewrote the `useTasks` hook to fix stale loading and error states, implement request cancellation (`AbortController`), and introduce a lightweight 300ms debounce to prevent firing an API request on every keystroke. Added `AbortSignal` support to `fetchTasks`.

## What I Chose Not to Change
- Did not restructure frontend components (e.g., search or filter components), as a large refactor was unnecessary for fixing search UX.
- Maintained the existing Spring Boot application architecture without introducing complex state management libraries.

## Biggest Remaining Risk
- Using native SQL queries directly bound to entities limits flexibility if database schemas migrate in the future, but it suffices for this small exercise.

## Tools / AI Used
- AI (Gemini) was utilized to analyze the codebase, identify logic flaws (like SQL precedence and frontend state issues), and format this patch summary.
