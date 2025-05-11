#!/usr/bin/env python3

import random
import secrets


def passwd_gen():
    initial_generation_hex = secrets.token_hex(32768)
    initial_generation_url_safe = secrets.token_hex(32768)
    initial_bucket = initial_generation_hex + initial_generation_url_safe
    shuffled_bucket = random.sample(initial_bucket, k=65536)
    l_bucket = list(shuffled_bucket)
    shaken_bucket = random.sample(l_bucket, k=65536)
    n_char = int((input
                  ("How many characters do you want in the generated hash?: ")))
    passwd_pick = random.sample(shaken_bucket, k=n_char)
    passwd = "".join(passwd_pick)
    print(passwd)


passwd_gen()
