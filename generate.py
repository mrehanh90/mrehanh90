import datetime

# Get current date and time for the dynamic update
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Construct the markdown content for your profile
markdown_content = f"""
### Hello there 👋 I'm Rehan!

Welcome to my self-generating GitHub profile. This README updates itself automatically using Python and GitHub Actions!

---

### 🚀 Quick Stats & Status
* **Major:** Computer Science Undergraduate (Iqra University)
* **Core Tools:** Python, MySQL, Git, Cisco Packet Tracer
* **Current Focus:** Software Quality Assurance & Database Management Systems
* **Last Automated Update:** `{current_time}` (PKT)

### 📈 GitHub Metrics
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=mrehanh90&show_icons=true&theme=radical" alt="GitHub Stats" />
</p>
"""

# Write the content directly into README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown_content.strip())

print("README.md updated successfully!")