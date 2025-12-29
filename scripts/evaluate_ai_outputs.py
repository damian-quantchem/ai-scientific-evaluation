import pandas as pd
import numpy as np

# Example: compare AI-predicted energies to DFT reference
df = pd.DataFrame({
    'species': ['A', 'B', 'C'],
    'ai_energy': [-0.80, 0.70, -1.05],
    'dft_energy': [-0.85, 0.65, -1.10]
})

df['error'] = df['ai_energy'] - df['dft_energy']

mae = np.mean(np.abs(df['error']))

print(f"Mean Absolute Error: {mae:.2f} eV")
