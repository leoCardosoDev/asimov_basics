import pandas as pd
import numpy as np
import timeit

# Gerar um grande conjunto de dados com IDs de usuários (com duplicatas)
num_records = 1_000_000
user_ids = np.random.randint(1, 100_000, size=num_records)  # 1 milhão de registros, 100 mil IDs únicos

# Criar um DataFrame
df = pd.DataFrame({'user_id': user_ids})

# Encontrar usuários únicos usando uma lista
def unique_users_list():
    return len(set(df['user_id'].tolist()))

# Encontrar usuários únicos usando um set
def unique_users_set():
    return len(set(df['user_id']))

# Medir o tempo de execução para cada método
tempo_lista = timeit.timeit(unique_users_list, number=10)
tempo_conjunto = timeit.timeit(unique_users_set, number=10)

print(f"Tempo usando lista: {tempo_lista:.6f} segundos")
print(f"Tempo usando set: {tempo_conjunto:.6f} segundos")
