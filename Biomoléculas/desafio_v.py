def predict_secondary_structure(sequence):
    # Propensiones aproximadas (Chou-Fasman simplificado)
    propensities = {
        'A': {'H': 1.42, 'B': 0.83, 'L': 0.66}, 'C': {'H': 0.70, 'B': 1.19, 'L': 1.19},
        'D': {'H': 1.01, 'B': 0.54, 'L': 1.46}, 'E': {'H': 1.51, 'B': 0.37, 'L': 0.74},
        'F': {'H': 1.13, 'B': 1.38, 'L': 0.60}, 'G': {'H': 0.57, 'B': 0.75, 'L': 1.56},
        'H': {'H': 1.00, 'B': 0.87, 'L': 0.95}, 'I': {'H': 1.08, 'B': 1.60, 'L': 0.47},
        'K': {'H': 1.16, 'B': 0.74, 'L': 1.01}, 'L': {'H': 1.21, 'B': 1.30, 'L': 0.59},
        'M': {'H': 1.45, 'B': 1.05, 'L': 0.60}, 'N': {'H': 0.67, 'B': 0.89, 'L': 1.56},
        'P': {'H': 0.57, 'B': 0.55, 'L': 1.55}, 'Q': {'H': 1.11, 'B': 0.98, 'L': 1.10},
        'R': {'H': 0.98, 'B': 0.93, 'L': 1.06}, 'S': {'H': 0.77, 'B': 0.75, 'L': 1.43},
        'T': {'H': 0.83, 'B': 1.19, 'L': 0.96}, 'V': {'H': 1.06, 'B': 1.70, 'L': 0.50},
        'W': {'H': 1.08, 'B': 1.37, 'L': 0.96}, 'Y': {'H': 0.69, 'B': 1.47, 'L': 1.14}
    }
    
    result = []
    for aa in sequence.upper():
          scores = propensities[aa]
          structure = max(scores, key=scores.get)
          result.append(structure)
    return ''.join(result)
