Este pequeño script permite consultar la API de binance los precios de algunos pares de cryptos:

'BTCUSD_220325'
'ETHUSD_220325'
'XRPUSD_220325'
'BNBUSD_220325'
'ADAUSD_220325'
'LINKUSD_220325'
'BCHUSD_220325'
'DOTUSD_220325'
'LTCUSD_220325'
'BTCUSD_220624'
'ETHUSD_220624'
'XRPUSD_220624'
'BNBUSD_220624'
'ADAUSD_220624'
'LINKUSD_220624'
'BCHUSD_220624' 
'DOTUSD_220624'
'LTCUSD_220624'

y devuelve una tabla calculando el precio del futuro, del spot, los días a vencimiento, la tna, tea y la tasa directa en una tabla, separado por los vencimientos.

Los vencimientos están fijos.

TODO:

- pedir un input de los vtos a traer y devolver esos. Esto permite que el script no deba ser tocado sino modificado a partir del input.
