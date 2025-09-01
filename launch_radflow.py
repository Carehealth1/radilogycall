#!/usr/bin/env python3
"""
RadFlow Pro Launcher Script
"""

import subprocess
import sys
import os

def check_requirements():
    """Check if required packages are installed"""
    try:
        import streamlit
        import pandas
        import plotly
        print("✅ All required packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing required package: {e}")
        print("Installing requirements...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        return True

def launch_app():
    """Launch the Streamlit application"""
    if check_requirements():
        print("🚀 Launching RadFlow Pro...")
        try:
            subprocess.run([sys.executable, "-m", "streamlit", "run", "radflow_streamlit_app.py"])
        except FileNotFoundError:
            print("❌ radflow_streamlit_app.py not found in current directory")
            print("Make sure all files are in the same folder")
        except KeyboardInterrupt:
            print("\n👋 RadFlow Pro stopped by user")

if __name__ == "__main__":
    print("🏥 RadFlow Pro - Radiology Workflow Management")
    print("=" * 50)
    launch_app()
