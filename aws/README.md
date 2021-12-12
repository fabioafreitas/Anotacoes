# AWS

-=-=-=-=-= módulo 2 =-=-=-=-=-=-
↓→↑←

Arquitetura em nuvem: Prática de aplicar características de nuvem numa solução que utilize serviços e recursos de nuvem.

AWS well-architect framework
-x Segurança
-x Excelência operacional
-> Confiabilidade
-> Eficiência de performance
-> Otimização de custo

Boa práticas AWS
1 - implementar escalabilidade em todos os níveis
2 - automatizar o ambiente
3 - tratar recursos como descartáveis (deletar o que não se utiliza)
4 - utilizar componentes com baixo acoplamento
5 - projetar serviços, não servidores
6 - escolher a solução de BD ideal
7 - elimitar pontos de falhar única
8 - aumentar eficiência de custos 
9 - usar armazenamento em cache (border computing)
10 - protegar toda a infraestrutura

Infraestrutura da AWS:
- regiões (22 no mundo), contêm zonas de disponibilidades
- replicações automática não ocorrem entre regiões
- zonas locais permitem trazer a infraestrutura para próximos dos usuários finais
- Escolher região: menor latência para usuários e conformidade legal
- Escolher zona de disponibilidade: pontos de presença de cache

-=-=-=-=-= módulo 3 =-=-=-=-=-=-

Dê apenas os provilégios mínimos para realizar o trabalho

Amazon S3:
- armazenam buckets
- buckets guardam arquivos
- buckets devem ter nomes únicos entre regiões
- objetos armazenados são imutáveis (para mudar deve-se upar uma nova versão modificada do objeto)
- Benefícios (durabilidade, disponibilidade, escalabilidade, segurança e performance)
- 5tb é o máximo de um único objeto
- pode armazenar sites estáticos
- usado como serviço de backup de dados

Classes do Amazon S3:
- Standard: dados acessados com frequência
- standard IA: dados duradouros acessados com pouca frequencia
- one zone ia: dados duradouros, não críticos e acessados com pouca frequencia
- glacier ou deep archive: para dados acessados raramente (1 ou 2 vezes por ano)

Data Lifecycle: Funcionalidade que altera o tier dos dados no bucket S3, reduizindo o tier do bucket para reduzir custos com o passar do tempo.


Transferência de Dados para o S3:
*Multipart Upload
	- Para arquivos 5MB ou aior
	- Upload por partes
* Transfer Accelatation:
	- Utilizar edge locations, para reduzir latência no upload
* Snowball -> transf de dados Petabytes
* Snowmobile -> transf de dados Exabytes

Escolhendo regiões para armazenamento:
- conformidades regulamentais
- proximidade dos usuários (latência)
- disponibilidade
- custo entre regiões
- replicar o ambiente