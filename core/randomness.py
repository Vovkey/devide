import random
import hashlib

def get_rng(global_seed, algorithm_name):
    seed_string = f"{global_seed}:{algorithm_name}"

    seed = int(
        hashlib.sha256(seed_string.encode()).hexdigest(),
        16
    )

    return random.Random(seed)
