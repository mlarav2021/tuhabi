/*
#----------------------------------------------------------------------------
# Created By  : Marco Antonio Lara Vargas
# Created Date: 2022-06-25
# version ='1.0'
# ---------------------------------------------------------------------------
"""Ejercicio 1 Consulta de clientes y protocolos de la  tabla traffic"""  
# ---------------------------------------------------------------------------
*/

with traffic as (
select
	client,
	protocol,
	sum(traffic_in + traffic_out) traffic_total
from
	traffic
group by
	client,
	protocol)
select
	client,
	array_to_string(array_agg(protocol order by traffic_total desc ), ',') protocol
from
	traffic
group by
	client
order by
	client asc