import os
import re

POSTS_DIR = "_posts"

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines or not lines[0].strip() == "---":
        return  # no frontmatter

    # Find end of frontmatter
    try:
        fm_end_idx = lines[1:].index("---\n") + 1
    except ValueError:
        return  # frontmatter not closed

    fm_lines = lines[1:fm_end_idx]

    # Skip if draft: true is present
    for line in fm_lines:
        if re.match(r'^\s*draft\s*:\s*true\s*$', line, re.IGNORECASE):
            return

    # Skip if publishedOn already exists
    for line in fm_lines:
        if re.match(r'^\s*publishedOn\s*:', line, re.IGNORECASE):
            return

    # Find value for publishedOn: use updated if exists, else date
    eff_date = None
    for line in fm_lines:
        if re.match(r'^\s*updated\s*:', line, re.IGNORECASE):
            eff_date = line.split(":", 1)[1].strip()
            break
    if not eff_date:
        for line in fm_lines:
            if re.match(r'^\s*date\s*:', line, re.IGNORECASE):
                eff_date = line.split(":", 1)[1].strip()
                break

    if not eff_date:
        return  # no date to set

    # Insert publishedOn before closing ---
    fm_lines.append(f"publishedOn: {eff_date}\n")
    new_lines = ["---\n"] + fm_lines + ["---\n"] + lines[fm_end_idx + 1:]

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"Updated publishedOn in: {file_path}")

# Walk through _posts folder
for root, dirs, files in os.walk(POSTS_DIR):
    for file in files:
        if file.endswith(".md"):
            process_file(os.path.join(root, file))
