
#name normolyze
def name_normolyze(name: str) -> str:
    name = name.strip()
    up = name.upper()[:1]
    down = name.lower()[1:]
    name = up+down
    return name

print(name_normolyze("   ферзУЛЛа   "))
