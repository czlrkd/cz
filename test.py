from pathlib import Path
import re

folder = Path.cwd()
print("현재 폴더:", folder)

for path in list(folder.iterdir()):
    if not path.is_file():
        continue

    new_name = re.sub(r'^([A-Za-z])(\d+)(\..+)$', r'\1_\2\3', path.name)

    if new_name == path.name:
        continue

    new_path = path.with_name(new_name)

    if new_path.exists():
        print(f"건너뜀: {path.name} -> {new_name} 이미 존재")
        continue

    try:
        path.rename(new_path)
        print(f"변경: {path.name} -> {new_name}")
    except FileNotFoundError:
        print(f"실패: {path.name} 파일을 못 찾음")