BUG 1
Location: backend/src/main/java/com/internal/tasktracker/TaskRepository.java (and SQL reference files)
How I discovered it: Inspected the SQL query logic and noticed missing parentheses around the OR condition for title and description filtering.
Root cause: Missing parentheses caused AND/OR precedence issues, applying status/archived filters inconsistently.
Fix: Added explicit parentheses around the (LOWER(title) LIKE :term OR LOWER(description) LIKE :term) clause.
Why: Ensures that the status and archived constraints are consistently applied regardless of which side of the OR condition matches.

BUG 2
Location: backend/src/main/java/com/internal/tasktracker/TaskController.java
How I discovered it: Reviewed controller logic for artificial delays per instructions.
Root cause: An intentional `Thread.sleep` was dynamically injecting latency based on query length.
Fix: Removed the try-catch block containing Thread.sleep(queryWeight).
Why: Artificial latency degrades performance and user experience without providing functional value.

BUG 3
Location: backend/src/main/java/com/internal/tasktracker/TaskController.java
How I discovered it: Checked for page boundary edge cases.
Root cause: No validation existed to prevent 0 or negative page/pageSize values, or excessively large payload requests.
Fix: Added basic boundary clamp logic (e.g., if page < 1, page = 1) before fetching results.
Why: Prevents potential crashes, empty pages, and mitigates denial-of-service risks from massive pagination queries.

BUG 4
Location: frontend/src/hooks/useTasks.js
How I discovered it: Analyzed the useEffect hook for request life-cycle handling and debounce implementation.
Root cause: Missing error state resets, missing AbortController, and no debouncing led to UI state bugs (stale errors, race conditions) and excessive API requests on every keystroke.
Fix: Implemented a 300ms setTimeout debounce, AbortController cancellation, and an `ignore` flag to manage state cleanup.
Why: Improves Search UX by preventing API spam, and ensures state (loading, error, tasks) remains accurate even with rapid successive requests.
