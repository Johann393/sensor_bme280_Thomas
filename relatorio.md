# Relatório Técnico da Dupla

## 1. Escopo e Objetivos
O objetivo deste projeto é implementar, com o uso da placa BitDogLab, a leitura do sensor BMP280 por meio da interface I2C e exibir em tempo real, no terminal do editor Thonny, os valores de temperatura e pressão atmosférica. Além de apresentar as leituras brutas obtidas diretamente do sensor, o sistema realiza também o cálculo de uma média móvel, permitindo comparar os dados filtrados com os valores originais.

Para o desenvolvimento, são utilizadas a biblioteca padrão do MicroPython, responsável pela configuração da interface I2C e controle do sistema, e a biblioteca bmp280.py, que estabelece a comunicação com o sensor e converte os dados digitais em valores físicos de temperatura e pressão.


## 2. Metodologia e Implementação
Para a realização deste experimento, foi utilizada a placa BitDogLab e o sensor de pressão e temperatura BMP280, com comunicação via protocolo I2C. O objetivo do projeto é realizar a leitura dos dados do sensor e aplicar um filtro de média móvel para suavizar as variações das medições.

Primeiramente, o sensor BMP280 foi conectado à BitDogLab utilizando um conector JST-PH de 4 pinos. As conexões elétricas foram feitas da seguinte forma: o pino GND do sensor foi ligado ao GND da placa, o pino VCC foi ligado ao VCC (3,3 V), o pino SDA do sensor foi conectado ao pino GP2 da BitDogLab e o pino SCL ao pino GP3. Em seguida, a BitDogLab foi conectada ao computador via cabo USB, permitindo a comunicação e execução do código no editor Thonny, utilizando o firmware MicroPython.

A arquitetura do sistema consiste em um microcontrolador central (BitDogLab) que realiza a comunicação com o sensor BMP280 por meio do barramento I2C. O microcontrolador envia comandos de leitura e recebe os dados brutos de temperatura e pressão, que são posteriormente processados no próprio código. As bibliotecas usadas foram: machine, time e bmp280.

A estratégia de programação adotada baseia-se em um laço principal (loop infinito) que realiza a leitura periódica das variáveis físicas, armazena os valores recentes e calcula uma média móvel de N amostras para reduzir o ruído nas medições. Essa abordagem foi escolhida por sua simplicidade e eficiência para aplicações embarcadas, oferecendo uma filtragem eficaz sem exigir grande capacidade de processamento.

O fluxo lógico do programa é o seguinte:
1 Inicialização do barramento I2C com os pinos GP2 (SDA) e GP3 (SCL).
2 Criação de um objeto BMP280 associado à interface I2C.
3 Definição de parâmetros do filtro, incluindo o tamanho da janela da média móvel (N).
4 Início do loop principal, no qual: são realizadas leituras de temperatura e pressão; os valores são armazenados em listas que representam a janela móvel;
calcula-se a média dos valores armazenados; os dados brutos e filtrados são exibidos no console; o programa aguarda um pequeno intervalo antes da próxima leitura.


## 3. Resultados e Análise
<img width="418" height="247" alt="image" src="https://github.com/user-attachments/assets/e88b5a19-5845-4d18-b6d8-4ab366f973e7" />

No mesmo local e instante da medição: 26°C e 1015 hPa (Barão geraldo Campinas dia 05/11/25 15:55) Vale notar que os meios consultados para saber a temperatura e pressão do local podem não ser tão exatos.

Os valores obtidos pelo sensor BMP280 apresentaram diferenças em relação aos dados ditos acima. Essa diferença ocorre principalmente porque o sensor mede a pressão absoluta no local onde está instalado, enquanto os valores divulgados em serviços meteorológicos correspondem à pressão reduzida ao nível do mar. Como Barão Geraldo está a cerca de 600 metros de altitude, é esperado que a pressão medida localmente seja menor — por volta de 940 hPa — o que coincide com o valor obtido pelo sensor.

Em relação à temperatura, a pequena diferença entre o valor medido (cerca de 26,5 °C) e o informado por fontes externas (26 °C) pode ser explicada por fatores como o calor gerado pelos componentes eletrônicos próximos, a falta de ventilação adequada ou a precisão limitada do sensor.

O uso da média móvel também influencia os resultados, pois o filtro suaviza variações rápidas, mas pode deslocar levemente o valor médio, resultando em uma leitura um pouco diferente da instantânea. Assim, as diferenças observadas são normais e coerentes com as condições de medição e as características do sensor.

Vale observar que as condições ambientais de medição podem influenciar nos resultados, uma vez que a temperatura e a pressão consultadas referem-se a um ambiente ao ar livre, enquanto as medições com o sensor foram realizadas em um ambiente fechado.




## 4. Dificuldades e Soluções
Durante o desenvolvimento do projeto, um dos principais desafios foi a instabilidade nas leituras de pressão e temperatura, causada por pequenas variações e ruídos naturais nas medições do sensor. Para mitigar esse problema, foi implementado um filtro de média móvel, que suavizou os dados e permitiu uma visualização mais estável e coerente com os valores esperados.

também foi observado que as condições do ambiente influenciaram as medições, especialmente quando o sensor estava em local fechado e sujeito ao aquecimento de componentes eletrônicos. Esse fator foi levado em consideração na análise dos resultados, destacando a importância de posicionar o sensor em locais adequados para medições mais precisas.

## 5. Conclusões e Trabalhos Futuros
O projeto permitiu compreender na prática o funcionamento da comunicação I2C e a integração entre a BitDogLab e o sensor BMP280, demonstrando a viabilidade de realizar leituras ambientais em tempo real com boa precisão. Os valores obtidos mostraram-se coerentes com os dados reais, considerando as diferenças esperadas devido à altitude local e às condições de medição.

O uso da filtragem por média móvel provou ser uma solução eficiente para reduzir ruídos e estabilizar as leituras, embora introduza um pequeno atraso nos resultados. Essa técnica mostrou-se simples e eficaz para aplicações embarcadas de baixo custo.

Como trabalhos futuros, pode-se aprimorar o sistema implementando outros métodos de filtragem digital, como filtros exponenciais ou medianos, que reagem mais rapidamente às variações. Além disso, seria possível adaptar o código para o ambiente C/C++ utilizando o Pico SDK, integrar o sensor com outros módulos (como displays ou sensores de umidade) e enviar os dados para um servidor remoto, ampliando as possibilidades de monitoramento ambiental e automação.
## 6. Referências
https://github.com/dafvid/micropython-bmp280
https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp280-ds001.pdf


