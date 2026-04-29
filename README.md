# NCBI GenBank Sequence Identifier

Program BioPython untuk identifikasi hasil sekuensing terhadap database GenBank NCBI menggunakan BLAST online, dengan kalkulasi **persen identitas akurat**.

---

## Langkah Pertama (wajib)

```bash
# 1. Instalasi otomatis semua dependensi
python setup.py

# 2. Jalankan program
python src/identifier.py
```

---

## Struktur Proyek

```
blast_project/
├── src/
│   └── identifier.py        ← Program utama
├── data/
│   ├── input/
│   │   └── sampel_demo.fasta  ← File FASTA contoh
│   └── output/              ← Hasil analisis (CSV, laporan, JSON)
├── config/
│   └── settings.json        ← Konfigurasi default
├── .vscode/
│   ├── launch.json          ← Konfigurasi Run/Debug VS Code
│   └── settings.json        ← Pengaturan workspace
├── setup.py                 ← Instalasi otomatis
├── requirements.txt
└── README.md
```

---

## Cara Menjalankan

### VS Code
1. Buka folder `blast_project/` di VS Code
2. Tekan **F5** → pilih konfigurasi yang diinginkan
3. Edit email di `launch.json` sebelum menjalankan

### Terminal — Mode Interaktif
```bash
python src/identifier.py
```
Program akan menampilkan menu interaktif untuk input email, database, sekuens, dll.

### Terminal — CLI Langsung
```bash
# Sekuens tunggal
python src/identifier.py \
  --email saya@email.com \
  --sequence "AGAGTTTGATCCTGGCTCAG..." \
  --database 16S_ribosomal_RNA \
  --identity 97

# File FASTA
python src/identifier.py \
  --email saya@email.com \
  --fasta data/input/sampel_demo.fasta \
  --database 16S_ribosomal_RNA \
  --identity 95 \
  --json
```

---

## Rumus Persen Identitas

```
% Identity = (jumlah posisi identik / panjang alignment) × 100
```
Ini adalah formula standar yang sama dengan tampilan di web NCBI BLAST.

---

## Database yang Direkomendasikan

| Jenis Sampel | Database | Program |
|---|---|---|
| Bakteri (16S rRNA) | `16S_ribosomal_RNA` | blastn |
| Fungi (ITS) | `ITS_RefSeq_Fungi` | blastn |
| DNA umum | `nt` | blastn |
| Protein | `nr` | blastp |

---

## Interpretasi Persen Identitas (16S rRNA)

| % Identitas | Arti |
|---|---|
| ≥ 99% | Identik / strain sama |
| 97–99% | Spesies yang sama |
| 95–97% | Kemungkinan spesies sama |
| 90–95% | Genus yang sama |
| 80–90% | Familia yang sama |
| < 80% | Hubungan jauh |

---

## Output

Hasil disimpan di `data/output/`:
- `hasil.csv` — tabel lengkap semua hits
- `hasil_laporan.txt` — laporan naratif dengan detail alignment
- `hasil.json` — format JSON (opsional dengan flag `--json`)
