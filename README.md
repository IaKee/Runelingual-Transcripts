# dummy-packs

Pacotes **dummy** (bytes aleatórios, peso real) para simular o gerenciador de downloads do RuneLingual
enquanto o formato real dos transcripts está sendo reestruturado. Não contém traduções.

- `catalog.json`: catálogo (schema 1) com id, kind, version, file, sizeBytes, sha256, required por idioma.
- `packs/<lang>/<id>.bin`: arquivos dummy.
- Regenerar tudo: `python3 tools/make_dummy_catalog.py --version 2026.10.11-1`
- Simular atualização de um pacote: `python3 tools/make_dummy_catalog.py --version 2026.10.12-1 --bump pt_br-texts`
