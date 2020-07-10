#Untested And Currently Gives Error When It Cant Find A Payment ID

import requests, json

token = input(" > Token: ")

headers={
  'authorization': token
}

a = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers=headers)
print(a.text)
if a.status_code == 200:
  payment_source_id = a.json()[0]['id']
elif "" or None in a.json:
  print("no payment sources")

data={
  'expected_amount': 499,
  'gift': True,
  'payment_source_id': payment_source_id,
  'sku_subscription_plan_id': "511651871736201216"
}

r = requests.post('https://discord.com/api/v6/store/skus/521846918637420545/purchase', headers=headers, data=data)
if r.status_code == 200:
  print('Success')
  print(r.text)
else:
  print('ooof')

