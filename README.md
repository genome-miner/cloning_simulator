# 🧬 In Silico Restriction Cloning Simulator
> **Simulate restriction enzyme cloning digitally without stepping into a lab.**

![Python](https://img.shields.io/badge/python-3.10.11-blue)
![Biopython](https://img.shields.io/badge/Biopython-1.86-green)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-informational)
![OOP](https://img.shields.io/badge/Architecture-OOP-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Table of Contents

- [What Is This](#what-is-this)
- [Tools & Technologies](#tools--technologies)
- [Project Architecture](#project-architecture)
- [Application Workflow](#application-workflow)
- [Sample Output](#sample-output)
- [Exception Handling Strategy](#exception-handling-strategy)
- [Key Concepts Demonstrated](#key-concepts-demonstrated)
- [How to Run](#how-to-run)
- [Future Roadmap](#future-roadmap)
- [Author & Contact](#author--contact)
- [License](#license)

---

## What Is This?

**In Silico Restriction Cloning Simulator** is a desktop application that digitally simulates the process of restriction enzyme cloning. One of the most fundamental techniques in molecular biology.

Given a DNA insert sequence, a plasmid sequence, and a restriction enzyme; the app automatically finds cut sites, validates compatibility, simulates the digestion and ligation, and calculates the resulting recombinant plasmid.

Built entirely in Python using Object-Oriented Programming and [Biopython](https://biopython.org/) library, this project bridges **wet lab molecular biology** with **computational thinking** simulating a real lab workflow in code.

> _"Will my gene fit into this plasmid? Ask the simulator."_

---

## Tools & Technologies

| Tool | Role |
|------|------|
| **Python 3.10.11** | Core programming language |
| **Tkinter** | Native desktop GUI framework |
| **Biopython** | Restriction enzyme database & site detection |
| **OOP** | Class-based modular architecture |
| **FASTA parsing** | Clean sequence extraction from raw input |
| **Exception Handling** | Robust multi-level error management |

---

## Project Architecture
```
restriction-cloning-simulator/
│
├── cloning_simulator.py     # Core application class (OOP)
│   ├── __init__()           # Window & screen configuration
│   ├── window()             # App title widget
│   ├── DNA_label()          # DNA input label
│   ├── DNA_text_label()     # DNA FASTA text box
│   ├── plasmid_label()      # Plasmid input label
│   ├── plasmid_text_label() # Plasmid sequence text box
│   ├── restriction()        # Load all enzymes from Biopython
│   ├── enzyme_label()       # Enzyme input label
│   ├── text_entry()         # Enzyme search entry with StringVar
│   ├── listbox()            # Enzyme search results listbox
│   ├── filter_enzymes()     # Real-time enzyme filtering
│   ├── clean_sequence()     # FASTA header removal & formatting
│   ├── cloning_work()       # Core cloning simulation logic
│   ├── container()          # Results container frame
│   ├── frame()              # Results inner frame
│   ├── results()            # Display cloning results
│   └── button_creation()    # Submit button
│   ├── open_gel_window()    # Opens virtual gel visualization window
│   ├── visual_simulation()  # Adds 'View Virtual Gel' button to results
│   └── canva()              # Creates black canvas for gel bands
├── main.py                  # Entry point
└── README.md                # Project documentation
```

---

## Application Workflow

```
User pastes DNA FASTA sequence
User pastes Plasmid sequence
User selects Restriction Enzyme
        │
        ▼
[ Empty Input Check ]
        │
        ▼
[ DNA & Plasmid Validation ]
Only A, T, G, C allowed
        │
        ▼
[ Get Enzyme from Biopython ]
getattr(Bio.Restriction, enzyme_name)
        │
        ▼
[ Get Recognition Site ]
enzyme.site → e.g. GAATTC
        │
        ▼
[ Cut Site Search ]
Is site present in BOTH sequences?
        │
        ▼
[ Single Cut Verification ]
Enzyme must cut only once in each
        │
        ▼
[ Simulate Digestion ]
DNA.split(site) → 2 fragments
Plasmid.split(site) → 2 fragments
        │
        ▼
[ Simulate Ligation ]
plasmid[0] + site + DNA + site + plasmid[1]
        │
        ▼
[ Display Results ]
        │
        ▼
[ View Virtual Gel Button ]
        │
        ▼
[ Opens New Window ]
Band positions calculated by sequence length
Plasmid vs Recombinant Plasmid compared
```

---

## Sample Output

> **Example Input:** E. coli genomic sequence + pUC19c plasmid + EcoRI

<p align="center">
  <img src="https://github.com/genome-miner/cloning_simulator/blob/main/Cloning_result.png?raw=true" alt="Alt text" width="500">
</p>

---

## Enzyme Database

This application uses **Biopython's built-in restriction enzyme database** (`Bio.Restriction`) which contains 700+ commercially available enzymes with recognition sequences.

**Smart enzyme search:**
- Real-time filtering as user types
- Case-insensitive search
- Instant listbox update on every keystroke

---

## Exception Handling Strategy

| Scenario | Handling |
|----------|----------|
| Empty DNA input | Error dialog before processing |
| Empty plasmid input | Error dialog before processing |
| No enzyme selected | Error dialog before processing |
| Invalid DNA characters | Validates against `{A, T, G, C}` set |
| Wrong enzyme name | `AttributeError` → enzyme not found message |
| Cut site not found | Informs user enzyme incompatible with sequences |
| Multiple cut sites | Warns user to choose different enzyme |
| Unexpected error | General exception handler ✅ |

---

## Key Concepts Demonstrated

1. **Molecular Biology Logic**: Restriction digestion and ligation simulation
2. **Biopython**: Professional bioinformatics library usage
3. **FASTA Parsing**: Stripping headers, joining multiline sequences
4. **Object-Oriented Programming**: Clean class-based architecture
5. **Real-time Search**: StringVar + trace_add for live filtering
6. **GUI Development**: Tkinter grid, frames, Text widgets, Listbox
7. **Exception Handling**: Multi-level validation and error management
8. **Multi-window GUI**: Toplevel window management in Tkinter
9. **Visual Band Simulation**: Canvas-based gel electrophoresis visualization

---

## How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/yourusername/cloning-simulator.git
cd cloning-simulator
```

**2. Install required library:**
```bash
pip install biopython
```

**3. Run:**
```bash
python main.py
```

**4. How to use:**
- Paste your **DNA insert sequence** in FASTA format
- Paste your **Plasmid sequence**
- Type enzyme name (Filtered list)
- Click **Submit** → view results instantly!

---

## Future Roadmap

| Feature | Description |
|---------|-------------|
| 🌐 NCBI Integration | Fetch sequences via Accession Numbers using Entrez API |
| 💾 Export Results | Save recombinant sequence as FASTA file |
| 🗺 Plasmid Map | Visual circular plasmid map showing insert position |

---

## Author & Contact

**Sana Aziz Sial**  
Biotechnologist and Bioinformatician
- 🎓 [University of Veterinary and Animal Sciences](https://www.uvas.edu.pk/)
- 📧 [Email](sanaazizsial@gmail.com)
- 🐙 [GitHub](https://github.com/genome-miner)
- 🔗 [LinkedIn](in/sana-aziz-sial-73b189265)

---

## License

[MIT License](https://github.com/genome-miner/cloning_simulator/blob/main/LICENSE) is free to use, modify, and distribute with attribution.

---

<div align="center">

⭐ If you found this useful, consider giving it a star!

_Built with Python & Biopython • Enzyme data from Bio.Restriction_

</div>
