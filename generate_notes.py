from PIL import Image, ImageDraw, ImageFont
import textwrap

text = """BUG 1
Location: backend/src/main/java/.../TaskRepository.java (and SQL files)
How I discovered it: Inspected the SQL query logic and noticed missing parentheses around the OR condition.
Root cause: Missing parentheses caused AND/OR precedence issues, applying status/archived filters inconsistently.
What I changed: Added explicit parentheses around (LOWER(title) LIKE :term OR LOWER(description) LIKE :term).
Why I chose this fix: Ensures that the status and archived constraints are consistently applied to both branches.

BUG 2
Location: backend/src/main/java/com/internal/tasktracker/TaskController.java
How I discovered it: Reviewed controller logic for artificial delays per instructions.
Root cause: An intentional Thread.sleep was injecting latency.
What I changed: Removed the try-catch block containing Thread.sleep(queryWeight).
Why I chose this fix: Artificial latency degrades performance without providing functional value.

BUG 3
Location: backend/src/main/java/com/internal/tasktracker/TaskController.java
How I discovered it: Checked for page boundary edge cases.
Root cause: No validation existed to prevent 0 or negative page/pageSize values.
What I changed: Added basic boundary clamp logic (if page < 1, page = 1).
Why I chose this fix: Prevents potential crashes and empty pages.

BUG 4
Location: frontend/src/hooks/useTasks.js
How I discovered it: Analyzed the useEffect hook for request life-cycle handling.
Root cause: Missing error state resets, missing AbortController, and no debouncing led to race conditions.
What I changed: Implemented a 300ms setTimeout debounce, AbortController cancellation, and an ignore flag.
Why I chose this fix: Improves UX by preventing API spam, and ensures state remains accurate.
"""

# Create a blank image with a white background (like paper)
width, height = 1000, 1400
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

try:
    # Try to load the handwritten font
    font = ImageFont.truetype("fonts/Caveat-Regular.ttf", 32)
except IOError:
    # Fallback to default if font loading fails
    font = ImageFont.load_default()

# Write the text onto the image
y_text = 40
margin = 40
for line in text.split('\n'):
    wrapped_lines = textwrap.wrap(line, width=60)
    if not wrapped_lines:
        y_text += 40
    for wrapped_line in wrapped_lines:
        draw.text((margin, y_text), wrapped_line, font=font, fill=(0, 0, 139)) # Dark blue ink
        y_text += 40

image.save("handwritten/notes.png")
print("Image generated successfully at handwritten/notes.png")
