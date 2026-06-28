# 🏆 India Runs – Data & AI Challenge
### Smart Candidate Ranking Pipeline | Hack2Skill × Redrob AI

## 📌 Problem Statement
Traditional hiring relies on keyword-based filtering which misses great talent.
This project builds an intelligent scoring and ranking pipeline that evaluates candidates
holistically — going beyond keywords to rank the most suitable candidates for AI/tech roles.

## 💡 My Approach

| Factor | Weight | Logic |
|--------|--------|-------|
| Work Experience | Up to 30 pts | Each role = 2 pts |
| Skills Match | 3 pts each | Matched against 23 AI/tech skills |
| Education | Up to 20 pts | PhD=20, Master=15, Bachelor=10 |
| Certifications | Up to 15 pts | Each cert = 3 pts |
| Redrob Signals | Variable | Overall signal score × 2 |

## 🛠️ Tech Stack
- Python 3.14
- Libraries: json, csv (no extra installs needed)
- Dataset: sample_candidates.json (50 candidates)

## ▶️ How to Run
1. Clone the repo
2. Place sample_candidates.json in the same folder
3. Run: python rank_candidates.py
4. Output: ranked_candidates.csv

## 📊 Sample Output

| Rank | Name | Score | Roles | Skills |
|------|------|-------|-------|--------|
| 1 | Vikram Mittal | 26 | 7 | 6 |
| 2 | Ved Sen | 22 | 5 | 8 |
| 3 | Anjali Khanna | 22 | 5 | 9 |
| 4 | Rahul Joshi | 21 | 6 | 16 |
| 5 | Anil Pandey | 20 | 4 | 8 |

## 👩‍💻 Built By
Deepika R — Chennai Institute of Technology
India Runs Hackathon 2026 — Track 1: Data & AI Challenge

*Built for Hack2Skill × Redrob AI | #IndiaRuns*
