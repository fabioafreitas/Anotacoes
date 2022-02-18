# Solar Energy

Artigo mostrando pesquisas sobre energia solar em sistemas embarcados

## TP4056 - Carregador de Bateria Li-íon

Funcionalidades:
- Gerencie o carregamento de corrente constante para tensão constante de uma bateria de lítio conectada
- Proteção de Sobre-Descarregamento: Evita a descarga abaixo de 2.4V, o mínimo antes de afetar a saúde da bateria. Se abaixo de 2.4v, ele só deixar descarregá-la a cima de 3.0v (tensão de liberação de sobre-carga). 
- Proteção de Sobre-Carregamento: Para de carregar a bateria assim que ela chga a 4.2v.
- Proteção de curto circuito e sobre-corrente: corta a saída da bateria se a descarga exceder uma cara de 3 Amperes ou ocorrer curto circuito.
- A proteção de partida suave limita a corrente de partida
- Carga lenta (recondicionamento da bateria): se o nível de tensão da bateria conectada for inferior a 2,9V, o módulo usará uma corrente de carga lenta de 130mA até que a tensão da bateria atinja 2,9V, ponto em que a corrente de carga será aumentada linearmente para a corrente de carga configurada.
