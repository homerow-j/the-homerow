#!/usr/bin/env python3
import sys
import random
import secrets


def hhg(n_chars=10240):
    random_bucket_01 = secrets.token_urlsafe(1024)
    random_bucket_02 = secrets.token_urlsafe(1024)
    cumulative_bucket_01 = random_bucket_01 + random_bucket_02
    del random_bucket_01, random_bucket_02
    random_bucket_03 = secrets.token_urlsafe(1024)
    cumulative_bucket_02 = cumulative_bucket_01 + random_bucket_03
    del random_bucket_03, cumulative_bucket_01
    random_bucket_04 = secrets.token_urlsafe(1024)
    cumulative_bucket_03 = cumulative_bucket_02 + random_bucket_04
    del random_bucket_04, cumulative_bucket_02
    random_bucket_05 = secrets.token_urlsafe(1024)
    cumulative_bucket_04 = cumulative_bucket_03 + random_bucket_05
    del cumulative_bucket_03, random_bucket_05
    random_bucket_06 = secrets.token_urlsafe(1024)
    cumulative_bucket_05 = cumulative_bucket_04 + random_bucket_06
    del cumulative_bucket_04, random_bucket_06
    random_bucket_07 = secrets.token_urlsafe(1024)
    cumulative_bucket_06 = cumulative_bucket_05 + random_bucket_07
    del cumulative_bucket_05, random_bucket_07
    random_bucket_08 = secrets.token_urlsafe(1024)
    cumulative_bucket_07 = cumulative_bucket_06 + random_bucket_08
    del cumulative_bucket_06, random_bucket_08
    random_bucket_09 = secrets.token_urlsafe(1024)
    cumulative_bucket_08 = cumulative_bucket_07 + random_bucket_09
    del cumulative_bucket_07, random_bucket_09
    random_bucket_10 = secrets.token_urlsafe(1024)
    filled_bucket = cumulative_bucket_08 + random_bucket_10
    del cumulative_bucket_08, random_bucket_10
    if len(sys.argv) > 1:
        n_chars = int(sys.argv[1])
    else:
        n_chars = int((input("# of characters (10240 max.): ")))
    hash_pick = random.sample(filled_bucket, k=n_chars)
    hhg_result = "".join(hash_pick)
    print(hhg_result)


hhg()
