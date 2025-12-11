from datetime import date
from pathlib import Path
from subprocess import run

from primary_edu import gen_data

STATIC_PATH = Path.cwd().joinpath("static")
STATIC_PATH.mkdir(exist_ok=True)


def main():
    today = date.today().strftime("%Y-%m-%d")

    static_path = STATIC_PATH
    qf = static_path.joinpath(f"{today}.pdf")

    if qf.exists():
        print(qf)
        return

    data_path = static_path.joinpath("data.csv")
    with open(data_path, "w", encoding="utf-8") as fp:
        fp.write("\n".join(f"{q},{a}" for q, a in gen_data()))

    tmpl = static_path.joinpath("tmpl.typ")
    cmd = f"typst compile {tmpl} --input".split()

    qaf = static_path.joinpath(f"{today}-ans.pdf")
    run([*cmd, "show_ans=true", qaf])
    run([*cmd, "show_ans=false", qf])
    print(qf)


if __name__ == "__main__":
    main()
