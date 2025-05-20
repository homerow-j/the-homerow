#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import secrets


def hhg():
    random_bucket_01 = secrets.token_urlsafe(4096)
    random_bucket_02 = secrets.token_urlsafe(4096)
    cumulative_bucket = random_bucket_01 + random_bucket_02
    del random_bucket_01, random_bucket_02
    random_bucket_03 = secrets.token_urlsafe(4096)
    cumulative_bucket = cumulative_bucket + random_bucket_03
    del random_bucket_03
    random_bucket_04 = secrets.token_urlsafe(4096)
    cumulative_bucket = cumulative_bucket + random_bucket_04
    del random_bucket_04
    random_bucket_05 = secrets.token_urlsafe(4096)
    cumulative_bucket = cumulative_bucket + random_bucket_05
    del random_bucket_05
    random_bucket_06 = secrets.token_urlsafe(4096)
    cumulative_bucket = cumulative_bucket + random_bucket_06
    del random_bucket_06
    random_bucket_07 = secrets.token_urlsafe(4096)
    cumulative_bucket = cumulative_bucket + random_bucket_07
    del random_bucket_07
    random_bucket_08 = secrets.token_urlsafe(4096)
    cumulative_bucket = cumulative_bucket + random_bucket_08
    del random_bucket_08
    random_bucket_09 = secrets.token_urlsafe(4096)
    cumulative_bucket = cumulative_bucket + random_bucket_09
    del random_bucket_09
    random_bucket_10 = secrets.token_urlsafe(4096)
    filled_bucket = cumulative_bucket + random_bucket_10
    del cumulative_bucket, random_bucket_10
    n_char = int((input("# of characters (40960 max.): ")))
    hash_pick = random.sample(filled_bucket, k=n_char)
    hhg_result = "".join(hash_pick)
    print(hhg_result)
    return hhg_result


hhg()
