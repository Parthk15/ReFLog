# 🚀 Reflog

> **Analyze any GitHub profile directly from your terminal.**

Reflog is a Python-powered CLI application that helps developers explore GitHub profiles, repositories, and contribution insights without opening a browser. It presents repository statistics, language analysis, and useful metrics in a clean terminal interface.

---

## ✨ Features

* 📊 Analyze any public GitHub profile
* 📁 Browse repositories in a clean interface
* ⭐ View stars, forks, and repository details
* 🏆 Find the most starred repository
* 💻 Discover the most-used programming language
* 📈 View repository analytics

  * Total repositories
  * Average stars
  * Average forks
  * Newest repository
  * Oldest repository
* 🔍 Search repositories instantly
* 🎨 Beautiful terminal output

---

## 📸 Preview

```
╔════════════════════════════════════╗
        GITHUB PROFILE ANALYZER
╚════════════════════════════════════╝

Username: torvalds

──────────────────────────────────────

📊 Repository Analytics

Total Repositories : 8
Total Stars        : 194K
Total Forks        : 56K
Top Repository     : linux
Most Used Language : C

──────────────────────────────────────

1. View Repository List
2. View Repository Details
3. Analyze Another User
4. Exit
```

---

## 🛠️ Built With

* Python 3
* GitHub REST API
* Requests
* Rich

---

## 📂 Project Structure

```text
Reflog/
│
├── analyzer.py
├── api.py
├── ui.py
├── utils.py
├── main.py
├── requirements.txt
├── README.md
└── assets/
```

---

## ⚡ Installation

Clone the repository

```bash
git clone https://github.com/Parthk15/Reflog.git
```

Move into the project

```bash
cd Reflog
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

---

## 📌 Example Workflow

```
Enter GitHub Username
        │
        ▼
Fetch Profile
        │
        ▼
Fetch Repositories
        │
        ▼
Generate Analytics
        │
        ▼
Browse Repository Details
```

---

## 🎯 Future Roadmap

* [ ] GitHub contribution graph
* [ ] Repository topic analysis
* [ ] Repository size statistics
* [ ] Export reports as PDF
* [ ] Export reports as CSV
* [ ] Repository recommendations
* [ ] GitHub streak analysis
* [ ] AI-powered repository summaries
* [ ] Compare two GitHub profiles
* [ ] Interactive charts

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new feature branch

```bash
git checkout -b feature/amazing-feature
```

3. Commit your changes

```bash
git commit -m "Add amazing feature"
```

4. Push your branch

```bash
git push origin feature/amazing-feature
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Parth K**

GitHub: **@Parthk15**

---

<p align="center">
Made with ❤️ and Python
</p>
