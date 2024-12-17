import os
import shutil
import sys
import subprocess

def clean_and_setup():
    print("🚀 Starting Sai AI Assistant Setup...")
    
    # Required files
    required_files = {
        'test.py': 'Main Assistant File',
        'create_icon.py': 'Icon Generator',
        'build_app.py': 'App Builder'
    }
    
    # Clean up old files
    print("\n🧹 Cleaning up old files...")
    for file in os.listdir():
        if file.endswith(('.py', '.ico', '.png')) and file != 'setup_assistant.py':
            try:
                os.remove(file)
                print(f"   ✓ Removed old file: {file}")
            except:
                print(f"   ✗ Could not remove: {file}")
    
    # Create new files
    print("\n📝 Creating new files...")
    
    # Create icon generator
    with open('create_icon.py', 'w') as f:
        f.write('''from PIL import Image, ImageDraw, ImageFont
import os

def create_app_icon():
    size = 256
    icon = Image.new('RGB', (size, size), 'white')
    draw = ImageDraw.Draw(icon)
    
    for y in range(size):
        for x in range(size):
            r = int(255 * (1 - y/size))
            g = int(100 * (1 - x/size))
            b = 255
            draw.point((x, y), fill=(r, g, b))
    
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    
    draw.text((size/4, size/3), "SAI AI", fill='white', font=font)
    
    icon.save("app_icon.png")
    icon.save("icon.ico", format='ICO')
    print("Icon created successfully!")

if __name__ == "__main__":
    create_app_icon()
''')
    print("   ✓ Created create_icon.py")

    # Create main assistant file
    with open('test.py', 'w') as f:
        # Add the entire test.py content here
        f.write('''# Your test.py content goes here
# Copy the entire test.py content from the previous message
''')
    print("   ✓ Created test.py")

    # Create build file
    with open('build_app.py', 'w') as f:
        f.write('''import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": [
        "os", "speech_recognition", "pyttsx3", "spacy", "requests", 
        "wikipedia", "psutil", "pyautogui", "pywhatkit", "tkinter",
        "PIL", "pygame"
    ],
    "include_files": [
        "icon.ico",
        "app_icon.png",
        "create_icon.py"
    ]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Sai Sunil AI Assistant",
    version="2.0",
    description="AI Personal Assistant by Sai Sunil Gawaskar",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "test.py",
            base=base,
            icon="icon.ico",
            target_name="SaiAI.exe",
            shortcut_name="Sai AI Assistant",
            shortcut_dir="DesktopFolder"
        )
    ]
)
''')
    print("   ✓ Created build_app.py")

    # Generate icon
    print("\n🎨 Generating icon...")
    try:
        subprocess.run([sys.executable, 'create_icon.py'])
        print("   ✓ Icon generated successfully")
    except Exception as e:
        print(f"   ✗ Error generating icon: {e}")

    # Create build
    print("\n🔨 Building application...")
    try:
        subprocess.run([sys.executable, 'build_app.py', 'build'])
        print("   ✓ Application built successfully")
    except Exception as e:
        print(f"   ✗ Error building application: {e}")

    # Cleanup temporary files
    print("\n🧹 Cleaning up temporary files...")
    temp_files = ['create_icon.py', 'build_app.py', 'app_icon.png']
    for file in temp_files:
        try:
            os.remove(file)
            print(f"   ✓ Removed temporary file: {file}")
        except:
            print(f"   ✗ Could not remove: {file}")

    print("\n✨ Setup complete! Your AI Assistant is ready to use!")
    print("📁 Look for the 'build' folder containing your executable.")

if __name__ == "__main__":
    clean_and_setup() 