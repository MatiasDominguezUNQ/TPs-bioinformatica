import logomaker
import pandas as pd
import matplotlib.pyplot as plt

sequences = [
    "MLPGLALLLLAAWTMRALEVPTDGNAPLLVEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRAQCKTHPHFVIPYRCLVGEFVSDALLAPDKCKFLHQERMDVCETHLHWHTV",
    "MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTV",
    "MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTV"
]

aa_list = 'ACDEFGHIKLMNPQRSTVWY'
matrix = pd.DataFrame(0, index=range(len(sequences[0])), columns=list(aa_list))

for seq in sequences:
    for i, aa in enumerate(seq):
        matrix.loc[i, aa] += 1

# Normalizar a probabilidades
matrix = matrix / len(sequences)

logo = logomaker.Logo(matrix, font_name='Arial', color_scheme='weblogo_protein')
logo.ax.set_xlabel('Posición en la secuencia')
logo.ax.set_ylabel('Frecuencia')
plt.title('Logotipo de secuencia para proteínas alineadas')
plt.savefig('sequence_logo.png')
plt.show()
