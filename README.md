# <NOME DO SENSOR> — Sensores na BitDogLab

Thomas Johann Hillermann Gomes (206624 / @Johann393) 
**Turma:** EA701 — 2025S2  
**Repositório:** (URL deste repo)

## 1. Descrição do sensor
- Fabricante / modelo: Fabricado pela Bosch Sensortec e o modelo é o BME280
- Princípio de funcionamento: É um sensor ambiental digital que mede temperatura, umidade relativa e pressão barométrica.
A parte da umidade utilza um sensor capacitivo/resistivo e as partes de pressão e temperatura usam a tecnologia MEMs da Bosch.
Isso viabiliza medições dessas 3 grandezas via protocolo I2C ou SPI. 
- Tensão/consumo típicos:
  Tensão/alimentação (VDD): 1.71 V a 3.6 V
  Tensão de interace (VDDIO): 1.2 V a 3.6 V
  Consumo tipico com atualização de 1 Hz: Umidade + temperatura (1.8 µA); pressão + temperatura (2.8 µA); Os 3 (3.6 µA); Modo sono (0.1 µA)
- Faixa de medição / resolução: 
  Faixa operacional de temperatura: -40°C à +85°C
  Faixa operacional de umidade: 0 a 100% de umidade relativa
  Faixa operacional de pressão: 300 hPa - 1100 hPa
  *para o medidor de umidade prcisão tipica de +- 3% e ruído RMS da pressão ~0,2 Pa (~ 1,7 cm em altitude)
  Resolução interna: pressão ate 0.16 Pa; temperatura até 0.1°C; umidade até 0.008% (umidade relativa)
  
- Datasheet (URL): https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf?utm_source=chatgpt.com

## 2. Conexões de hardware
- Tabela indicando as conexões entre BitDogLab e sensor:

BME 280  |  Bitdoglab(RP2040) | Descrição

VCC      |  3.3 V             | Alimentação
GND      |  GND               | Terra
SDA      |  SDA               | Serial data (GPIO 0)
SCL      |  SCL               | Serial clock (GPIO 1)

Foi usado um conector JST-PH de 4 pinos
![IMG_8234-min](https://github.com/user-attachments/assets/41aaee4c-3e40-4321-977a-55639e567145)

Na imagem temos 3 endereços. O endreço do OLED é o 0x3c e o do sensor é o 0x76
![IMG_8235-min](https://github.com/user-attachments/assets/b5bde196-2f79-4ac2-a398-b7e57ea66abc)



## 3. Dependências
- MicroPython/C versão: MicroPython para RP2040 e a versão usada/recomendada é a v1.22.1 ou superior
- Bibliotecas utilizadas: machine(nativa), time(nativa), ssd1306.py, bme280.py
- Como instalar (passo a passo): Baixe o seu editor de texto de preferência compatível com
  MicroPython (para este teste foi usado o Thonny).
## 4. Como executar
```bash
# MicroPython (Thonny): Instale primeiro o firmware MicroPython na RP2040. Depois abra o seu editor de texto de preferência compatível com
  MicroPython (para este teste foi usado o Thonny) e em seguida conecte a bitdoglab via USB no computador e o conector JST-PH de 4 pinos na bitdog com
  a pinagem da tabela já listada acima. Salve os arquivos na placa(File → Save to device: main.py, ssd1306.py e bme280.py), reinicie ela e depois o script main rodará automaticamente.
```

## 5. Exemplos de uso
- `src/exemplo_basico.py` — leitura bruta  
- `src/exemplo_filtrado.py` — leitura com média móvel  
- `test/` — códigos de teste com instruções  

## 6. Resultados e validação
- Prints/plots, fotos do setup, limitações, ruídos, dicas.

## 7. Licença
- Ver arquivo `LICENSE`.

---

> **Checklist de entrega**
> - [ ] README preenchido  
> - [ ] Foto/diagrama em `docs/`  
> - [ ] Código comentado em `src/`  
> - [ ] Testes em `test/` com instruções  
> - [ ] `relatorio.md` com lições aprendidas

## 📁 7. Estrutura do Repositório

O projeto segue o padrão definido pela disciplina EA801 — Sistemas Embarcados, 
visando padronizar as entregas e facilitar o reuso dos códigos e documentação.

Todos os arquivos de código devem estar em src/.
Diagramas, fotos, gráficos e documentos vão em docs/.
Scripts ou logs de teste ficam em test/.
O relatório técnico (relatorio.md) documenta todo o processo de engenharia.

Mantenha os nomes dos arquivos em minúsculas, sem acentos ou espaços, usando _ ou -.

```text
template_sensor/
├── README.md          → Descrição completa do projeto (sensor, ligações, execução e checklist)
├── relatorio.md       → Relatório técnico da dupla (resultados, análise e conclusões)
├── LICENSE            → Licença MIT de uso e distribuição
├── .gitignore         → Regras para ignorar arquivos temporários e binários
│
├── docs/              → Documentação e mídias
│   ├── ligacao.jpg    → Diagrama ou foto da ligação na BitDogLab
│   ├── esquema.pdf    → Esquemático opcional
│   └── outros arquivos de apoio
│
├── src/               → Códigos-fonte principais
│   ├── main.py        → Código principal (MicroPython)
│   ├── main.c         → Versão alternativa (C / Pico SDK)
│   ├── exemplos/      → Códigos ilustrativos adicionais
│   └── bibliotecas/   → Drivers, módulos auxiliares
│
└── test/              → Testes e validações
    ├── test_basico.py → Teste de leitura e resposta do sensor
    ├── test_ruido.py  → Avaliação de ruído ou estabilidade
    └── logs/          → Registros experimentais, dados e gráficos

```
