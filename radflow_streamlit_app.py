#!/usr/bin/env python3
"""
RadFlow Ultimate - Complete Application Launcher
All original web app features + Streamlit enhancements
"""

import subprocess
import sys
import os

def print_banner():
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                    RadFlow Ultimate v3.0                     ║
    ║            COMPLETE Radiology Workflow Management            ║
    ║              All Original Features + Enhanced UI             ║
    ╚══════════════════════════════════════════════════════════════╝

    🎯 ALL Original Web App Features Included
    📅 True Visual Calendar with Interactive Grid
    🏷️ Real-time Bidding with Live Updates
    🤖 AI-Powered Smart Distribution
    💬 Expert Consultation Network
    🔒 HIPAA-Compliant Security
    """
    print(banner)

def check_requirements():
    """Check and install required packages"""
    required = ['streamlit', 'pandas', 'plotly', 'python-dateutil']
    missing = []

    for package in required:
        try:
            __import__(package.replace('-', '_'))
            print(f"✅ {package}")
        except ImportError:
            missing.append(package)
            print(f"❌ {package}")

    if missing:
        print(f"\n📦 Installing: {', '.join(missing)}")
        subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing)
        print("✅ Installation complete!")

    return True

def check_files():
    """Verify all required files are present"""
    required_files = [
        'radflow_ultimate_complete.py',
        'data_models_ultimate.py', 
        'utils_ultimate.py'
    ]

    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - Missing")
            return False

    return True

def launch_app():
    """Launch RadFlow Ultimate"""
    print("\n🚀 Launching RadFlow Ultimate...")
    print("📱 Opening in your browser at http://localhost:8501")
    print("\n🎯 Complete Feature Set Available:")
    print("   • Visual Calendar Scheduler")
    print("   • Smart Call Management") 
    print("   • Live Bidding Arena")
    print("   • Expert Consultation Network")
    print("   • Multi-Location Command Center")
    print("   • Advanced Analytics Suite")
    print("   • Complete Data Export")
    print("\n🛑 Press Ctrl+C to stop")
    print("=" * 60)

    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run",
            "radflow_ultimate_complete.py",
            "--server.port=8501"
        ])
    except KeyboardInterrupt:
        print("\n\n👋 RadFlow Ultimate stopped")
        print("Thank you for using RadFlow Ultimate!")

def main():
    print_banner()

    print("🔍 System Check...")
    print("-" * 40)

    if not check_files():
        input("\nPress Enter to exit...")
        return

    print("\n📦 Package Check...")
    print("-" * 40)

    if not check_requirements():
        input("\nPress Enter to exit...")
        return

    print("\n🎉 All systems ready!")
    input("\nPress Enter to launch RadFlow Ultimate...")

    launch_app()

if __name__ == "__main__":
    main()
