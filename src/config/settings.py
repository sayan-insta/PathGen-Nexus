from pathlib import Path

PROJECTS_JSON = Path("data/metadata/projects.json")
CASES_JSON = Path("data/metadata/cases.json")
FILES_JSON = Path("data/metadata/files.json")
RNA_JSON = Path("data/metadata/rna.json")

RNA_DOWNLOAD_DIR = Path("data/downloads/rna")

SKIP_PROJECT_DOWNLOAD = PROJECTS_JSON.exists()
SKIP_CASE_DOWNLOAD = CASES_JSON.exists()
SKIP_FILE_DOWNLOAD = FILES_JSON.exists()
SKIP_RNA_METADATA = RNA_JSON.exists()

SKIP_RNA_DOWNLOAD = RNA_DOWNLOAD_DIR.exists() and any(RNA_DOWNLOAD_DIR.iterdir())