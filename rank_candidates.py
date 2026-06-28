import json
import csv

# Path to data
DATA_PATH = r"C:\Users\deepi\Desktop\india_runs_model"

# Key skills to match
job_skills = [
    "python", "machine learning", "ai", "data science", "deep learning",
    "tensorflow", "pytorch", "sql", "react", "javascript", "flask",
    "nlp", "computer vision", "aws", "firebase", "git", "api",
    "scikit", "keras", "pandas", "numpy", "docker", "kubernetes"
]

def score_candidate(candidate):
    score = 0
    profile = candidate.get("profile", {}) or {}

    career = candidate.get("career_history", []) or []
    total_exp = len(career) * 2
    score += min(total_exp, 30)

    skills = candidate.get("skills", []) or []
    skills_text = " ".join([str(s).lower() for s in skills])
    for skill in job_skills:
        if skill in skills_text:
            score += 3

    education = candidate.get("education", []) or []
    for edu in education:
        degree = str(edu.get("degree", "")).lower()
        if "phd" in degree or "doctorate" in degree:
            score += 20
        elif "master" in degree or "mtech" in degree or "mba" in degree:
            score += 15
        elif "bachelor" in degree or "btech" in degree or "be" in degree:
            score += 10

    certs = candidate.get("certifications", []) or []
    score += min(len(certs) * 3, 15)

    signals = candidate.get("redrob_signals", {}) or {}
    signal_score = signals.get("overall_score", 0) or 0
    score += signal_score * 2

    return score


print("Loading candidates...")
candidates = []

with open(f"{DATA_PATH}\\sample_candidates.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    candidates = data if isinstance(data, list) else [data]

print(f"Loaded {len(candidates)} candidates")

scored = []
for c in candidates:
    candidate_id = c.get("candidate_id", "unknown")
    profile = c.get("profile", {}) or {}

    # FIXED: use anonymized_name field
    name = profile.get("anonymized_name") or profile.get("full_name") or profile.get("name") or "Candidate_" + str(candidate_id)

    score = score_candidate(c)
    exp = len(c.get("career_history", []) or [])

    scored.append({
        "candidate_id": str(candidate_id),
        "score": score,
        "name": name,
        "experience_roles": exp,
        "skills_count": len(c.get("skills", []) or []),
        "certifications": len(c.get("certifications", []) or [])
    })

scored.sort(key=lambda x: x["score"], reverse=True)

for i, c in enumerate(scored):
    c["rank"] = i + 1

print(f"\nTop 10 candidates:")
for c in scored[:10]:
    print(f"Rank {c['rank']}: {c['name']} | Score: {c['score']} | Roles: {c['experience_roles']} | Skills: {c['skills_count']}")

output_file = "ranked_candidates.csv"
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["rank", "candidate_id", "score", "name", "experience_roles", "skills_count", "certifications"])
    writer.writeheader()
    writer.writerows(scored)

print(f"\n✅ Saved {len(scored)} ranked candidates to {output_file}")