import os
import shutil
import argparse

POSTS_ROOT = "_posts"

LEGACY_PREFIXES = [
    "likes:",
    "draft:",
    "published:",
    "imported:",
    "livedoc:",
    "product-canvas:",
    "classification:"
]

IMPORT_KEYS = [
    "import-source:",
    "import-reference:",
    "import-url:",
    "import-config-id:",
    "source-published-on:",
    "source-updated-on:"
]

LIVEDOC_KEYS = [
    "repo-source:",
    "repo-url:",
    "livedoc-config-id:",
    "source-published-on:",
    "source-updated-on:"
]

CANVAS_KEYS = [
    "canvas-type:",
    "repo-source:",
    "repo-url:",
    "livedoc-title:",
    "livedoc-config-id:"
]


def process_file(filepath, dry_run=False):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        return

    parts = content.split("---", 2)
    if len(parts) < 3:
        return

    _, frontmatter_raw, body = parts
    lines = frontmatter_raw.strip("\n").split("\n")

    new_lines = []

    existing_post_type = None
    existing_status = None
    product_canvas = False
    draft_flag = False
    published_false = False
    imported_flag = False
    livedoc_flag = False
    classification_value = None
    categories_value = None

    import_fields = {}
    livedoc_fields = {}
    canvas_fields = {}

    # --------------------------------------------------
    # FIRST PASS — Detect Values
    # --------------------------------------------------
    for line in lines:
        stripped = line.strip()

        if stripped.startswith("post-type:"):
            existing_post_type = stripped.split(":", 1)[1].strip().strip('"')

        if stripped.startswith("status:"):
            existing_status = stripped.split(":", 1)[1].strip().strip('"')

        if stripped.startswith("classification:"):
            classification_value = stripped.split(":", 1)[1].strip().strip('"').lower()

        if stripped.startswith("categories:"):
            categories_value = stripped.split(":", 1)[1].strip()

        if stripped.startswith("product-canvas:") and "true" in stripped.lower():
            product_canvas = True

        if stripped.startswith("draft:") and "true" in stripped.lower():
            draft_flag = True

        if stripped.startswith("published:") and "false" in stripped.lower():
            published_false = True

        if stripped.startswith("imported:") and "true" in stripped.lower():
            imported_flag = True

        if stripped.startswith("livedoc:") and "true" in stripped.lower():
            livedoc_flag = True

        # Capture Import fields
        for key in IMPORT_KEYS:
            if stripped.startswith(key):
                value = stripped.split(":", 1)[1].strip()
                import_fields[key.replace(":", "")] = value

        # Capture LiveDoc fields
        for key in LIVEDOC_KEYS:
            if stripped.startswith(key):
                value = stripped.split(":", 1)[1].strip()
                livedoc_fields[key.replace(":", "")] = value

        # Capture Canvas fields
        for key in CANVAS_KEYS:
            if stripped.startswith(key):
                value = stripped.split(":", 1)[1].strip()
                canvas_fields[key.replace(":", "")] = value

    # --------------------------------------------------
    # STATUS LOGIC (FIXED)
    # --------------------------------------------------
    # Priority:
    # 1. Legacy draft flag
    # 2. Legacy published:false
    # 3. Existing status
    # 4. Default to published

    if draft_flag:
        status = "draft"
    elif published_false:
        status = "archived"
    elif existing_status:
        status = existing_status
    else:
        status = "published"

    # --------------------------------------------------
    # POST TYPE LOGIC
    # --------------------------------------------------
    post_type = existing_post_type

    if product_canvas:
        post_type = "canvas"

    elif not existing_post_type:
        if imported_flag:
            post_type = "imported"
        elif livedoc_flag:
            post_type = "livedoc"
        else:
            post_type = "standard"

    # --------------------------------------------------
    # CATEGORIES LOGIC
    # --------------------------------------------------
    if classification_value:
        if classification_value == "public":
            categories_value = "public"
        elif classification_value == "internal":
            categories_value = "internal"

    elif categories_value:
        categories_value = categories_value.lower().strip()
        if categories_value not in ["public", "internal"]:
            categories_value = "public"

    # --------------------------------------------------
    # SECOND PASS — Rebuild Frontmatter
    # --------------------------------------------------
    for line in lines:
        stripped = line.strip()

        if any(stripped.startswith(prefix) for prefix in LEGACY_PREFIXES):
            continue

        if stripped.startswith("post-type:") or stripped.startswith("status:"):
            continue

        if stripped.startswith("categories:"):
            continue

        if any(stripped.startswith(key) for key in IMPORT_KEYS + LIVEDOC_KEYS + CANVAS_KEYS):
            continue

        new_lines.append(line)

    # --------------------------------------------------
    # Append Updated Values
    # --------------------------------------------------
    if categories_value:
        new_lines.append(f"categories: {categories_value}")

    new_lines.append(f"post-type: {post_type}")
    new_lines.append(f"status: {status}")

    # --------------------------------------------------
    # METADATA BLOCK
    # --------------------------------------------------
    metadata_fields = {}

    if post_type == "imported":
        metadata_fields = import_fields
    elif post_type == "livedoc":
        metadata_fields = livedoc_fields
    elif post_type == "canvas":
        metadata_fields = canvas_fields

    # Explicitly remove source dates for canvas
    if post_type == "canvas":
        metadata_fields.pop("source-published-on", None)
        metadata_fields.pop("source-updated-on", None)

    if metadata_fields:
        new_lines.append("metadata:")
        for key, value in metadata_fields.items():
            new_lines.append(f"  {key}: {value}")

    new_frontmatter = "\n".join(new_lines)
    new_content = "---\n" + new_frontmatter + "\n---" + body

    if new_content == content:
        return

    print("Updated:", filepath)

    if dry_run:
        return

    backup_path = filepath + ".bak"
    if not os.path.exists(backup_path):
        shutil.copy(filepath, backup_path)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)


def process_all(dry_run=False):
    for root, _, files in os.walk(POSTS_ROOT):
        for file in files:
            if file.endswith(".md"):
                process_file(os.path.join(root, file), dry_run)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    process_all(args.dry_run)