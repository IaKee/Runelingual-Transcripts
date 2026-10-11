#!/usr/bin/env python3
"""Gera pacotes dummy (bytes pseudoaleatórios, incompressíveis) + catalog.json
para simular o gerenciador de downloads do RuneLingual.

Uso: python3 tools/make_dummy_catalog.py [--version 2026.10.11-1] [--bump pt_br-texts ...]
- Sem --bump: (re)gera tudo com --version.
- Com --bump: só os pacotes listados recebem a nova versão e conteúdo novo
  (para testar "Atualização disponível"); os demais mantêm versão/arquivo atuais.
"""
import argparse, datetime, hashlib, json, os, random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG = os.path.join(ROOT, "catalog.json")

# idiomas com pack local hoje no plugin; cjk = precisa de imagens de caracteres
LANGS = {"pt_br": False, "no": False, "tr": False, "ja": True, "zh": True, "ru": True, "pt": False, "es": False}
# kind -> (tamanho base em bytes, obrigatório, só cjk)
KINDS = {
    "texts":      (4_200_000, True,  False),
    "sprites":    (1_300_000, False, False),
    "charImages": (6_500_000, True,  True),
}


def make_file(rel, size, seed):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    rnd = random.Random(seed)
    h = hashlib.sha256()
    with open(path, "wb") as f:
        left = size
        while left:
            n = min(left, 1 << 16)
            chunk = rnd.getrandbits(8 * n).to_bytes(n, "little")
            f.write(chunk)
            h.update(chunk)
            left -= n
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", default=datetime.date.today().strftime("%Y.%m.%d") + "-1")
    ap.add_argument("--bump", nargs="*", default=None)
    a = ap.parse_args()

    old = {}
    if os.path.exists(CATALOG):
        with open(CATALOG, encoding="utf-8") as f:
            for lang, entry in json.load(f)["languages"].items():
                for p in entry["packs"]:
                    old[p["id"]] = p

    languages = {}
    for i, (lang, cjk) in enumerate(LANGS.items()):
        packs = []
        for j, (kind, (base, required, only_cjk)) in enumerate(KINDS.items()):
            if only_cjk and not cjk:
                continue
            pid = f"{lang}-{kind}"
            if a.bump is not None and pid not in a.bump and pid in old:
                packs.append(old[pid])
                continue
            size = base + (i * 97_000) + (j * 13_000)
            rel = f"packs/{lang}/{pid}.bin"
            sha = make_file(rel, size, f"{pid}:{a.version}")
            packs.append({
                "id": pid, "kind": kind, "version": a.version, "file": rel,
                "sizeBytes": size, "sha256": sha, "required": required,
                "dummy": True,
            })
        languages[lang] = {"packs": packs}

    catalog = {
        "schema": 1,
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "note": "DUMMY packs for download-manager simulation. Content is random bytes.",
        "languages": languages,
    }
    with open(CATALOG, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"catalog.json: {sum(len(v['packs']) for v in languages.values())} packs")


if __name__ == "__main__":
    main()
