"""
encrypt(00000000000000000000000000000000)
> ciphertext = ‘511d0780e5e4c8332f0b1821f52ac1f0’

receive(00000000000000000000000000000000511d0780e5e4c8332f0b1821f52ac1f0)
> plaintext = ‘df308cb2380bf3ccb62dfec068e7c5cce539824dea235980ba1ef09b8b96dc98’

getflag(e539824dea235980ba1ef09b8b96dc98)
> plaintext = enc_flag = '63727970746f7b35306d335f703330706c335f64306e375f3768316e6b5f49565f31355f316d70307237346e375f3f7d'
"""
enc_flag = '63727970746f7b35306d335f703330706c335f64306e375f3768316e6b5f49565f31355f316d70307237346e375f3f7d'
print(bytes.fromhex(enc_flag))
