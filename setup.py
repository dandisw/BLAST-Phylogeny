#!/usr/bin/env python3
"""
setup.py — Instalasi otomatis semua dependensi
Jalankan sekali sebelum pertama kali menggunakan program.

    python setup.py
"""

import subprocess
import sys
from pathlib import Path

REQUIRED = {
    "biopython"  : "Bio",
    "pandas"     : "pandas",
    "requests"   : "requests",
    "matplotlib" : "matplotlib",
    "numpy"      : "numpy",
}

BANNER = """
+======================================================+
|   Setup NCBI Sequence Identifier + Phylo Tree       |
|   Instalasi dan verifikasi semua dependensi          |
+======================================================+
"""

print(BANNER)
print(f"Python : {sys.version}")
print(f"Lokasi : {sys.executable}\n")

all_ok = True
for pkg, import_name in REQUIRED.items():
    try:
        __import__(import_name)
        print(f"  [OK] {pkg}")
    except ImportError:
        print(f"  [--] {pkg} tidak ditemukan. Menginstal ...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", pkg],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            print(f"  [OK] {pkg} berhasil diinstal.")
        else:
            print(f"  [ERR] Gagal menginstal {pkg}:\n{result.stderr}")
            all_ok = False

# ── Verifikasi BioPython ───────────────────────────────────────────────────
print()
try:
    from Bio import SeqIO, Entrez
    from Bio.Blast import NCBIWWW, NCBIXML
    from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
    from Bio import Phylo
    import Bio
    print(f"  BioPython versi  : {Bio.__version__}")
    print(f"  BioPython Phylo  : OK")
except Exception as e:
    print(f"  [ERR] BioPython error: {e}")
    all_ok = False

# ── Verifikasi matplotlib ──────────────────────────────────────────────────
try:
    import matplotlib
    print(f"  matplotlib versi : {matplotlib.__version__}")
except Exception as e:
    print(f"  [ERR] matplotlib error: {e}")

# ── Cek software MSA eksternal (opsional) ─────────────────────────────────
print()
print("  Cek software MSA eksternal (opsional):")
import shutil
for tool in ["clustalw", "clustalw2", "muscle", "mafft"]:
    found = shutil.which(tool)
    status = f"ditemukan di {found}" if found else "tidak ditemukan (opsional)"
    print(f"    {tool:<12}: {status}")

print()
print("  Catatan: Software MSA eksternal TIDAK wajib.")
print("  Program akan otomatis menggunakan metode internal jika")
print("  ClustalW/MUSCLE/MAFFT tidak tersedia.")

# ── Buat direktori ────────────────────────────────────────────────────────
print()
dirs = ["data/input", "data/output", "config"]
for d in dirs:
    Path(d).mkdir(parents=True, exist_ok=True)
    print(f"  Direktori siap : {d}/")

# ── Ringkasan ─────────────────────────────────────────────────────────────
print()
if all_ok:
    print("=" * 56)
    print("  Setup selesai! Semua dependensi siap.")
    print()
    print("  Cara menjalankan:")
    print()
    print("  Mode interaktif (+ pohon filogenetik):")
    print("    python src/identifier.py")
    print()
    print("  Mode pohon saja (dari FASTA yang sudah ada):")
    print("    python src/phylo_tree.py")
    print("=" * 56)
else:
    print("  [!] Ada dependensi yang gagal. Coba: pip install -r requirements.txt")
