import os

ROAST = "I asked my agent to do one thing. It made a plan, reviewed the plan, and is still waiting for me to approve the plan."

def main():
    if not ROAST.strip():
        raise SystemExit("roast must not be blank")
    if len(ROAST) > 200:
        raise SystemExit("roast must be at most 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    print(ROAST)

if __name__ == "__main__":
    main()
