# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2025-09-17
### Added
- First stable release of **RUPTRK CLI** 🎉
- Core features:
  - Add & restock stock
  - Edit, delete, and search products
  - Track sales (with auto-fill for repeated bills)
  - Manage serial numbers
  - Export reports (last 3 months & quarterly) in CSV
- Config system:
  - Auto-creates `.ruptrk-cli` (Linux/macOS) or local config folder (Windows)
  - Stores database and preferences automatically
- CLI entry point: `ruptrk-cli`
- Supports importing `ruptrk_cli` functions directly in Python scripts.

---

## [Unreleased]
- Add more report types (profit/loss, yearly summary).
- Multi-database management improvements.
- Packaging for Windows executable.
