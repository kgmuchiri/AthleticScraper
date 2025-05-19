import subprocess

# List your scripts in the order you want them to run
scripts = [
    "./scraper_final.py",
    "./preprocessing.py",
    "./combine.py",
    "./split_by_type.py",
]

for script in scripts:
    print(f"🚀 Running {script}...")
    subprocess.run(["python", script], check=True)
    print(f"✅ Finished {script}\n")
