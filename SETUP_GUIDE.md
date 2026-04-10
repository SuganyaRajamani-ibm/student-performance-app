# 🚀 GitHub Setup Guide for Student Performance Application

This guide will walk you through setting up the Student Performance Analysis application with GitHub Actions.

## 📋 Prerequisites

Before you begin, ensure you have:
- ✅ Git installed on your local machine
- ✅ GitHub account created
- ✅ Python 3.8+ installed locally (for testing)
- ✅ VS Code or any text editor

## 🎯 Step-by-Step Setup

### Step 1: Create a New GitHub Repository

1. Go to [GitHub](https://github.com)
2. Click the **"+"** icon in the top right corner
3. Select **"New repository"**
4. Fill in the details:
   - **Repository name**: `student-performance-app` (or your preferred name)
   - **Description**: "Automated student performance analysis with GitHub Actions"
   - **Visibility**: Choose Public or Private
   - ✅ Check "Add a README file" (optional)
5. Click **"Create repository"**

### Step 2: Clone the Repository Locally

Open your terminal/command prompt and run:

```bash
# Clone your repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Navigate into the directory
cd YOUR_REPO_NAME
```

Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual GitHub username and repository name.

### Step 3: Copy Project Files

Copy all files from the `student-performance-app` directory to your cloned repository:

```
your-repo/
├── .github/
│   └── workflows/
│       └── student-performance.yml
├── .gitignore
├── app.py
├── student_marks.json
├── requirements.txt
├── README.md
└── SETUP_GUIDE.md
```

**On Windows:**
```cmd
xcopy /E /I student-performance-app\* YOUR_REPO_NAME\
```

**On Mac/Linux:**
```bash
cp -r student-performance-app/* YOUR_REPO_NAME/
```

### Step 4: Verify File Structure

Check that all files are in place:

```bash
cd YOUR_REPO_NAME
dir  # Windows
ls -la  # Mac/Linux
```

You should see:
- `.github/workflows/student-performance.yml`
- `app.py`
- `student_marks.json`
- `requirements.txt`
- `README.md`
- `.gitignore`

### Step 5: Test Locally (Optional but Recommended)

Before pushing to GitHub, test the application locally:

```bash
python app.py
```

Expected output:
```
============================================================
Student Performance Analysis System
============================================================
[OK] Loaded 15 student records
[OK] Statistics calculated successfully
[OK] HTML report generated: report.html
============================================================
[OK] Analysis complete!
[OK] Report saved to: report.html
============================================================
```

Open `report.html` in your browser to verify the report looks correct.

### Step 6: Commit and Push to GitHub

```bash
# Add all files to git
git add .

# Commit the changes
git commit -m "Initial commit: Add student performance analysis application"

# Push to GitHub
git push origin main
```

**Note:** If your default branch is `master` instead of `main`, use:
```bash
git push origin master
```

### Step 7: Verify GitHub Actions Workflow

1. Go to your repository on GitHub
2. Click on the **"Actions"** tab
3. You should see the workflow "Student Performance Analysis" running
4. Click on the workflow run to see the progress

The workflow will:
- ✅ Checkout the code
- ✅ Set up Python 3.11
- ✅ Run the analysis
- ✅ Generate the HTML report
- ✅ Upload the report as an artifact

### Step 8: Download the Report

Once the workflow completes:

1. Stay on the workflow run page
2. Scroll down to the **"Artifacts"** section
3. Click on **"student-performance-report"** to download
4. Extract the ZIP file
5. Open `report.html` in your browser

## 🔄 Making Changes

### Update Student Data

1. Edit `student_marks.json` locally
2. Commit and push:
   ```bash
   git add student_marks.json
   git commit -m "Update student marks"
   git push origin main
   ```
3. GitHub Actions will automatically run and generate a new report

### Manually Trigger Workflow

1. Go to **Actions** tab
2. Select **"Student Performance Analysis"**
3. Click **"Run workflow"** button
4. Select branch (usually `main`)
5. Click **"Run workflow"**

## 🌐 Optional: Enable GitHub Pages

To view reports directly in your browser without downloading:

### Step 1: Enable GitHub Pages

1. Go to repository **Settings**
2. Scroll to **"Pages"** section (left sidebar)
3. Under **"Source"**, select:
   - Branch: `gh-pages`
   - Folder: `/ (root)`
4. Click **"Save"**

### Step 2: Wait for Deployment

- First deployment may take 2-5 minutes
- Check the Actions tab for deployment status

### Step 3: Access Your Report

Your report will be available at:
```
https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/report.html
```

## 🛠️ Troubleshooting

### Issue: Workflow Fails with "File not found"

**Solution:**
- Verify all files are in the correct location
- Check that `.github/workflows/student-performance.yml` exists
- Ensure `student_marks.json` is in the root directory

### Issue: Python Version Error

**Solution:**
- The workflow uses Python 3.11
- If you need a different version, edit `.github/workflows/student-performance.yml`:
  ```yaml
  - name: Set up Python
    uses: actions/setup-python@v5
    with:
      python-version: '3.9'  # Change to your preferred version
  ```

### Issue: Invalid JSON Error

**Solution:**
- Validate your `student_marks.json` using [JSONLint](https://jsonlint.com/)
- Ensure all brackets and commas are correct
- Check for trailing commas

### Issue: GitHub Pages Not Working

**Solution:**
1. Ensure `gh-pages` branch exists (created automatically by workflow)
2. Check repository Settings → Pages is enabled
3. Wait 5-10 minutes for first deployment
4. Check Actions tab for deployment errors

### Issue: Report Not Generated

**Solution:**
- Check workflow logs in Actions tab
- Verify `app.py` has no syntax errors
- Ensure `student_marks.json` has valid data

## 📊 Understanding the Workflow

The GitHub Actions workflow (`.github/workflows/student-performance.yml`) does the following:

1. **Triggers**: Runs on push to main/master, pull requests, or manual trigger
2. **Environment**: Uses Ubuntu latest runner
3. **Steps**:
   - Checks out code
   - Sets up Python 3.11
   - Installs dependencies
   - Runs the analysis script
   - Uploads report as artifact
   - (Optional) Deploys to GitHub Pages

## 🎓 Next Steps

### Customize for Your Needs

1. **Add More Students**: Edit `student_marks.json`
2. **Change Subjects**: Modify the marks structure
3. **Adjust Grading**: Edit `_calculate_grade()` in `app.py`
4. **Customize Report**: Modify HTML/CSS in `generate_html_report()`

### Schedule Automatic Runs

Add a schedule to the workflow to run automatically:

Edit `.github/workflows/student-performance.yml`:

```yaml
on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]
  workflow_dispatch:
  schedule:
    - cron: '0 0 * * 0'  # Runs every Sunday at midnight UTC
```

### Add Email Notifications

You can add email notifications when the workflow completes by using GitHub Actions marketplace actions.

## 📞 Support

If you encounter issues:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Review workflow logs in the Actions tab
3. Verify all files are correctly placed
4. Ensure JSON data is valid

## 🎉 Success Checklist

- ✅ Repository created on GitHub
- ✅ Files copied and pushed
- ✅ Workflow runs successfully
- ✅ Report generated and downloadable
- ✅ (Optional) GitHub Pages enabled and working

---

**Congratulations!** 🎊 Your Student Performance Analysis system is now set up and running automatically with GitHub Actions!