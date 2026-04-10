# 📊 Student Performance Analysis System

An automated student performance analysis application with GitHub Actions integration. This system analyzes student marks, calculates statistics, and generates beautiful HTML reports automatically.

## 🌟 Features

- **Automated Analysis**: Calculates total marks, averages, percentages, and grades
- **Performance Grading**: A+ to F grading system based on percentage
- **Statistical Insights**: Overall class statistics and subject-wise averages
- **Beautiful HTML Reports**: Professional, responsive HTML reports with modern design
- **GitHub Actions Integration**: Automatic workflow execution on push/PR
- **Artifact Storage**: Reports saved as downloadable artifacts
- **Optional GitHub Pages**: Deploy reports to GitHub Pages automatically

## 📋 Prerequisites

- Python 3.8 or higher
- Git installed locally
- GitHub account
- VS Code (optional, for local development)

## 🚀 Quick Start

### 1. Clone or Create Repository

```bash
# If starting fresh, create a new repository on GitHub first
# Then clone it locally
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Copy Project Files

Copy the entire `student-performance-app` directory to your repository:

```
your-repo/
├── .github/
│   └── workflows/
│       └── student-performance.yml
├── app.py
├── student_marks.json
├── requirements.txt
└── README.md
```

### 3. Customize Student Data

Edit [`student_marks.json`](student_marks.json:1) to add your student data:

```json
[
  {
    "id": "STU001",
    "name": "Student Name",
    "marks": {
      "Mathematics": 85,
      "Physics": 90,
      "Chemistry": 88,
      "English": 92,
      "Computer Science": 95
    }
  }
]
```

**Data Format Requirements:**
- Each student must have: `id`, `name`, and `marks`
- All students must have the same subjects
- Marks should be out of 100
- Minimum 40% required to pass

### 4. Push to GitHub

```bash
git add .
git commit -m "Add student performance analysis system"
git push origin main
```

## 🔄 GitHub Actions Workflow

The workflow automatically runs when:
- Code is pushed to `main` or `master` branch
- Pull request is created
- Manually triggered from GitHub Actions tab

### Workflow Steps:

1. **Checkout Code**: Gets the latest code from repository
2. **Setup Python**: Installs Python 3.11
3. **Install Dependencies**: Installs required packages (if any)
4. **Run Analysis**: Executes the performance analysis
5. **Upload Report**: Saves HTML report as artifact
6. **Deploy to Pages**: (Optional) Publishes to GitHub Pages

### Manual Trigger

1. Go to your repository on GitHub
2. Click on **Actions** tab
3. Select **Student Performance Analysis** workflow
4. Click **Run workflow** button
5. Select branch and click **Run workflow**

## 📥 Accessing Reports

### Method 1: Download from Artifacts

1. Go to **Actions** tab in your GitHub repository
2. Click on the latest workflow run
3. Scroll down to **Artifacts** section
4. Download `student-performance-report`
5. Extract and open `report.html` in your browser

### Method 2: GitHub Pages (Optional)

If GitHub Pages deployment is enabled:

1. Go to repository **Settings** → **Pages**
2. Enable GitHub Pages with source: `gh-pages` branch
3. Access report at: `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/report.html`

## 💻 Local Development

### Run Locally

```bash
cd student-performance-app
python app.py
```

The report will be generated as `report.html` in the same directory.

### Test with Custom Data

```bash
# Use custom input file
export MARKS_FILE=custom_marks.json
export OUTPUT_FILE=custom_report.html
python app.py
```

## 📊 Report Contents

The generated HTML report includes:

### 1. **Overview Statistics**
- Total number of students
- Average marks across all students
- Highest and lowest marks
- Pass/Fail count

### 2. **Subject-wise Performance**
- Average marks per subject
- Performance rating (Excellent/Good/Average/Needs Improvement)

### 3. **Individual Student Performance**
- Student ID and Name
- Total marks and average
- Percentage and grade
- Pass/Fail status

### 4. **Detailed Marks Table**
- Complete subject-wise marks for all students

## 🎯 Grading System

| Percentage | Grade |
|------------|-------|
| 90% - 100% | A+    |
| 80% - 89%  | A     |
| 70% - 79%  | B+    |
| 60% - 69%  | B     |
| 50% - 59%  | C     |
| 40% - 49%  | D     |
| Below 40%  | F     |

**Pass Criteria**: Minimum 40% required

## 🛠️ Customization

### Add More Subjects

Edit [`student_marks.json`](student_marks.json:1) and add subjects to each student's marks object:

```json
"marks": {
  "Mathematics": 85,
  "Physics": 90,
  "Biology": 88,
  "History": 92
}
```

### Change Grading Criteria

Edit the `_calculate_grade()` method in [`app.py`](app.py:68):

```python
def _calculate_grade(self, percentage: float) -> str:
    if percentage >= 95:
        return 'A+'
    # ... modify as needed
```

### Customize Report Styling

Edit the CSS section in the `generate_html_report()` method in [`app.py`](app.py:82).

## 📁 Project Structure

```
student-performance-app/
├── .github/
│   └── workflows/
│       └── student-performance.yml    # GitHub Actions workflow
├── app.py                             # Main application
├── student_marks.json                 # Student marks data
├── requirements.txt                   # Python dependencies
└── README.md                          # This file
```

## 🔧 Troubleshooting

### Workflow Fails

**Issue**: Python version mismatch
- **Solution**: Ensure Python 3.8+ is specified in workflow file

**Issue**: File not found error
- **Solution**: Check file paths in workflow YAML

### Report Not Generated

**Issue**: Invalid JSON format
- **Solution**: Validate [`student_marks.json`](student_marks.json:1) using a JSON validator

**Issue**: Missing student data
- **Solution**: Ensure all required fields (id, name, marks) are present

### GitHub Pages Not Working

1. Enable GitHub Pages in repository settings
2. Select `gh-pages` branch as source
3. Wait a few minutes for deployment
4. Check Actions tab for deployment status

## 📝 Adding New Students

1. Edit [`student_marks.json`](student_marks.json:1)
2. Add new student object with same structure
3. Commit and push changes
4. Workflow runs automatically
5. Download new report from Artifacts

## 🤝 Contributing

To add features or improvements:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## 📄 License

This project is open source and available for educational purposes.

## 🎓 Use Cases

- **Schools**: Track student performance across terms
- **Colleges**: Analyze class performance by subject
- **Training Centers**: Monitor trainee progress
- **Online Courses**: Generate automated progress reports

## 📞 Support

For issues or questions:
- Check the Troubleshooting section
- Review GitHub Actions logs
- Verify JSON data format
- Ensure Python 3.8+ is installed

## 🔄 Updates

To update the application:

```bash
git pull origin main
# Make your changes
git add .
git commit -m "Update: description"
git push origin main
```

---

**Built with ❤️ for automated student performance tracking**

*Powered by Python & GitHub Actions*