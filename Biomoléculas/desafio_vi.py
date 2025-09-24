import requests
import re

def get_sequence(uniprot_id):
    url = f"https://www.uniprot.org/uniprotkb/{uniprot_id}.fasta"
    response = requests.get(url)
    if response.status_code == 200:
        lines = response.text.splitlines()
        sequence = ''
        for line in lines[1:]:
            sequence += line
        return sequence
    else:
        return None

def find_motif_positions(sequence):
    motif_regex = r'N[^P][ST][^P]'  # N no P, S o T, no P
    positions = []
    for match in re.finditer(motif_regex, sequence):
        positions.append(match.start() + 1)
    return positions

# Lista de IDs
ids = ['A2Z669', 'B5ZC00', 'P07204_TRBM_HUMAN', 'P20840_SAG1_YEAST']

for uniprot_id in ids:
    sequence = get_sequence(uniprot_id)
    if sequence:
        positions = find_motif_positions(sequence)
        if positions:
            print(uniprot_id)
            print(' '.join(map(str, positions)))
    else:
        print(f"No se pudo obtener la secuencia para {uniprot_id}")
