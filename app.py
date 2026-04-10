#!/usr/bin/env python3
"""
Student Performance Analysis Application
Analyzes student marks and generates performance reports
"""

import json
import os
from datetime import datetime


class StudentPerformanceAnalyzer:
    def __init__(self, marks_file: str):
        self.marks_file = marks_file
        self.students_data = []
        self.statistics = {}
        
    def load_marks(self) -> None:
        """Load student marks from JSON file"""
        try:
            with open(self.marks_file, 'r') as f:
                self.students_data = json.load(f)
            print(f"[OK] Loaded {len(self.students_data)} student records")
        except FileNotFoundError:
            print(f"[ERROR] File {self.marks_file} not found")
            raise
        except json.JSONDecodeError:
            print(f"[ERROR] Invalid JSON in {self.marks_file}")
            raise
    
    def calculate_statistics(self) -> None:
        """Calculate performance statistics"""
        if not self.students_data:
            return
        
        total_marks = []
        subject_marks = {}
        
        for student in self.students_data:
            student_total = sum(student['marks'].values())
            total_marks.append(student_total)
            student['total'] = student_total
            student['average'] = student_total / len(student['marks'])
            student['percentage'] = (student_total / (len(student['marks']) * 100)) * 100
            student['grade'] = self._calculate_grade(student['percentage'])
            
            for subject, marks in student['marks'].items():
                if subject not in subject_marks:
                    subject_marks[subject] = []
                subject_marks[subject].append(marks)
        
        self.statistics = {
            'total_students': len(self.students_data),
            'average_marks': sum(total_marks) / len(total_marks),
            'highest_marks': max(total_marks),
            'lowest_marks': min(total_marks),
            'pass_count': sum(1 for s in self.students_data if s['percentage'] >= 40),
            'fail_count': sum(1 for s in self.students_data if s['percentage'] < 40),
            'subject_averages': {
                subject: sum(marks) / len(marks) 
                for subject, marks in subject_marks.items()
            }
        }
        
        print("[OK] Statistics calculated successfully")
    
    def _calculate_grade(self, percentage: float) -> str:
        """Calculate grade based on percentage"""
        if percentage >= 90:
            return 'A+'
        elif percentage >= 80:
            return 'A'
        elif percentage >= 70:
            return 'B+'
        elif percentage >= 60:
            return 'B'
        elif percentage >= 50:
            return 'C'
        elif percentage >= 40:
            return 'D'
        else:
            return 'F'
    
    def generate_html_report(self, output_file: str = 'report.html') -> None:
        """Generate HTML performance report"""
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Performance Report</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{ font-size: 2.5em; margin-bottom: 10px; }}
        .header p {{ font-size: 1.1em; opacity: 0.9; }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
        }}
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.3s;
        }}
        .stat-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 5px 20px rgba(0,0,0,0.15);
        }}
        .stat-card h3 {{ color: #667eea; font-size: 2em; margin-bottom: 10px; }}
        .stat-card p {{ color: #666; font-size: 0.9em; }}
        .content {{ padding: 30px; }}
        .section {{ margin-bottom: 40px; }}
        .section h2 {{
            color: #333;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        th {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }}
        td {{ padding: 12px 15px; border-bottom: 1px solid #ddd; }}
        tr:hover {{ background: #f8f9fa; }}
        .grade {{
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            color: white;
        }}
        .grade-A-plus {{ background: #28a745; }}
        .grade-A {{ background: #5cb85c; }}
        .grade-B-plus {{ background: #5bc0de; }}
        .grade-B {{ background: #0275d8; }}
        .grade-C {{ background: #f0ad4e; }}
        .grade-D {{ background: #ff9800; }}
        .grade-F {{ background: #d9534f; }}
        .pass {{ color: #28a745; font-weight: bold; }}
        .fail {{ color: #d9534f; font-weight: bold; }}
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            border-top: 1px solid #ddd;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Student Performance Report</h1>
            <p>Academic Year 2024-2025 | Generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
        </div>
        
        <div class="stats-grid">
            <div class="stat-card">
                <h3>{self.statistics['total_students']}</h3>
                <p>Total Students</p>
            </div>
            <div class="stat-card">
                <h3>{self.statistics['average_marks']:.2f}</h3>
                <p>Average Marks</p>
            </div>
            <div class="stat-card">
                <h3>{self.statistics['highest_marks']}</h3>
                <p>Highest Marks</p>
            </div>
            <div class="stat-card">
                <h3>{self.statistics['lowest_marks']}</h3>
                <p>Lowest Marks</p>
            </div>
            <div class="stat-card">
                <h3 class="pass">{self.statistics['pass_count']}</h3>
                <p>Students Passed</p>
            </div>
            <div class="stat-card">
                <h3 class="fail">{self.statistics['fail_count']}</h3>
                <p>Students Failed</p>
            </div>
        </div>
        
        <div class="content">
            <div class="section">
                <h2>📈 Subject-wise Average Performance</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Subject</th>
                            <th>Average Marks</th>
                            <th>Performance</th>
                        </tr>
                    </thead>
                    <tbody>
"""
        
        for subject, avg in self.statistics['subject_averages'].items():
            performance = "Excellent" if avg >= 80 else "Good" if avg >= 60 else "Average" if avg >= 40 else "Needs Improvement"
            html_content += f"""                        <tr>
                            <td>{subject}</td>
                            <td>{avg:.2f}</td>
                            <td>{performance}</td>
                        </tr>
"""
        
        html_content += """                    </tbody>
                </table>
            </div>
            
            <div class="section">
                <h2>👨‍🎓 Individual Student Performance</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Student ID</th>
                            <th>Name</th>
                            <th>Total Marks</th>
                            <th>Average</th>
                            <th>Percentage</th>
                            <th>Grade</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
"""
        
        for student in sorted(self.students_data, key=lambda x: x['total'], reverse=True):
            status = "PASS" if student['percentage'] >= 40 else "FAIL"
            status_class = "pass" if status == "PASS" else "fail"
            grade_class = f"grade-{student['grade'].replace('+', '-plus')}"
            
            html_content += f"""                        <tr>
                            <td>{student['id']}</td>
                            <td>{student['name']}</td>
                            <td>{student['total']}</td>
                            <td>{student['average']:.2f}</td>
                            <td>{student['percentage']:.2f}%</td>
                            <td><span class="grade {grade_class}">{student['grade']}</span></td>
                            <td class="{status_class}">{status}</td>
                        </tr>
"""
        
        html_content += """                    </tbody>
                </table>
            </div>
            
            <div class="section">
                <h2>📋 Detailed Subject-wise Marks</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Student Name</th>
"""
        
        if self.students_data:
            for subject in self.students_data[0]['marks'].keys():
                html_content += f"                            <th>{subject}</th>\n"
        
        html_content += """                        </tr>
                    </thead>
                    <tbody>
"""
        
        for student in self.students_data:
            html_content += f"""                        <tr>
                            <td>{student['name']}</td>
"""
            for marks in student['marks'].values():
                html_content += f"                            <td>{marks}</td>\n"
            html_content += "                        </tr>\n"
        
        html_content += """                    </tbody>
                </table>
            </div>
        </div>
        
        <div class="footer">
            <p>🎓 Generated by Student Performance Analysis System</p>
            <p>Powered by GitHub Actions | Automated Workflow</p>
        </div>
    </div>
</body>
</html>
"""
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"[OK] HTML report generated: {output_file}")


def main():
    """Main execution function"""
    print("=" * 60)
    print("Student Performance Analysis System")
    print("=" * 60)
    
    marks_file = os.getenv('MARKS_FILE', 'student_marks.json')
    output_file = os.getenv('OUTPUT_FILE', 'report.html')
    
    analyzer = StudentPerformanceAnalyzer(marks_file)
    
    analyzer.load_marks()
    analyzer.calculate_statistics()
    analyzer.generate_html_report(output_file)
    
    print("=" * 60)
    print("[OK] Analysis complete!")
    print(f"[OK] Report saved to: {output_file}")
    print("=" * 60)


if __name__ == "__main__":
    main()

# Made with Bob
