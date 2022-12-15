import school
import sys
from pathlib import Path

file_path = Path("./school")

def run_all():
    for file in file_path.rglob("*.py"):
        if file.is_dir():
            continue
        if file.name in ["__init__.py", "__main__.py"]:
            continue
        file_rel_path = file.relative_to(file_path)
        file_name = str(file_rel_path)[:-len(file_rel_path.suffix)]
        print(20*"=")
        print("Đang chạy bài", file.stem.replace("_", "."), "(Tự động)")
        print(20*"=")
        school.exec_file(file_name.replace("/", "."))

    print(20*"=")
    print("Đã chạy xong tất cả các bài.")

def run_all_noinputemu():
    for file in file_path.rglob("*.py"):
        if file.is_dir():
            continue
        if file.name in ["__init__.py", "__main__.py"]:
            continue
        print(20*"=")
        print("Đang chạy bài", file.stem.replace("_", "."))
        print(20*"=")
        exec(get_source(file.stem.replace("_", ".")))
        
def run_assignment(assignment: str):
    for file in file_path.rglob("*.py"):
        if file.is_dir():
            continue
        if file.stem.replace("_", ".") != assignment:
            continue
        file_rel_path = file.relative_to(file_path)
        file_name = str(file_rel_path)[:-len(file_rel_path.suffix)]
        print(20*"=")
        print("Đang chạy bài", file.stem.replace("_", "."), "(Tự động)")
        print(20*"=")
        school.exec_file(file_name.replace("/", "."))
        break

def run_assignment_noinputemu(assignment: str):
    for file in file_path.rglob("*.py"):
        if file.is_dir():
            continue
        if file.stem.replace("_", ".") != assignment:
            continue
        print(20*"=")
        print("Đang chạy bài", file.stem.replace("_", "."))
        print(20*"=")
        exec(get_source(file.stem.replace("_", ".")))
        break

def get_source(assignment: str):
    for file in file_path.rglob("*.py"):
        if file.is_dir():
            continue
        if file.stem.replace("_", ".") != assignment:
            continue
        with file.open("r") as f:
            lines = f.readlines()
        content = "".join(lines)
        if not "### Bài bắt đầu từ đây" in content:
            return content
        src = ""
        begin_src = False
        for line in lines:
            if begin_src:
                src += line
                continue
            if line.strip() == "### Bài bắt đầu từ đây":
                begin_src = True
        return src

def view_source(assignment: str):
    print(20*"=")
    print("Mã nguồn của bài", assignment)
    print(20*"=")
    print(get_source(assignment))

if len(sys.argv) < 2:
    run_all()
else:
    interactive = False
    action = "execute"
    assignments = []
    for i, v in enumerate(sys.argv):
        if v == "-I":
            interactive = True
        elif v == "-A" and i < len(sys.argv) - 1:
            assignments.append(sys.argv[i + 1])
        elif (v == "-S" or v == "--src") and i < len(sys.argv) - 1:
            action = "view-source"
            assignments.append(sys.argv[i + 1])
    match action:
        case "execute":
            if assignments == []:
                if interactive:
                    run_all_noinputemu()
                else:
                    run_all()
            else:
                for i in assignments:
                    if interactive:
                        run_assignment_noinputemu(i)
                    else:
                        run_assignment(i)
        case "view-source":
            for i in assignments:
                view_source(i)
