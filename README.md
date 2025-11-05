# BMP280 — Sensores na BitDogLab

Thomas Johann Hillermann Gomes (206624 / @Johann393) 
**Turma:** EA701 — 2025S2  
**Repositório:** https://github.com/Johann393/sensor_bme280_Thomas

## 1. Descrição do sensor
- Fabricante / modelo: Fabricado pela Bosch Sensortec e o modelo é o BMP280
- Princípio de funcionamento: É um sensor ambiental digital que mede temperatura e pressão barométrica.
  As partes de pressão e temperatura usam a tecnologia MEMs da Bosch.
Isso viabiliza medições dessas 2 grandezas via protocolo I2C ou SPI. 
- Tensão/consumo típicos:
  Tensão/alimentação (VDD): 1.71 V a 3.6 V
  Tensão de interace (VDDIO): 1.2 V a 3.6 V
  Consumo típico: Modo normal(1 Hz) 2.74 µA; Modo forçado(medição única) 2.0 µA; Modo sono 0.1 µA
- Faixa de medição / resolução:
  Temperatura: faixa operacional -40°C até 85°C; resolução típica 0.01°C; precisão típica +-1°C
  Pressão: faixa operacional 300 hPa a 1100 hPa; resolução interna até 0.16 hPA; precisão típica +- 0.12 hPa
  Comunicação: I2C(até 3.4MHz) ou SPI(até 10MHz)
   

  
- Datasheet (URL): (https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp280-ds001.pdf)

## 2. Conexões de hardware
- Tabela indicando as conexões entre BitDogLab e sensor:

<img width="757" height="206" alt="image" src="https://github.com/user-attachments/assets/e347c730-1fc1-43e9-9e4d-393f0c2b5772" />

Foi usado um conector JST-PH de 4 pinos
![IMG_8234-min](https://github.com/user-attachments/assets/41aaee4c-3e40-4321-977a-55639e567145)

Na imagem temos 3 endereços. O endreço do OLED é o 0x3c e o do sensor é o 0x76. Para verificar os endereços, o código que foi usado está dispoível 
na pasta test
![IMG_8235-min](https://github.com/user-attachments/assets/b5bde196-2f79-4ac2-a398-b7e57ea66abc)


## 3. Dependências
- MicroPython/C versão: MicroPython para RP2040 e a versão usada/recomendada é a v1.22.1 ou superior
- Bibliotecas utilizadas: machine(nativa), time(nativa), ssd1306.py, bmp280.py
- Como instalar (passo a passo): Baixe o seu editor de texto de preferência compatível com
  MicroPython (para este teste foi usado o Thonny).
  
## 4. Como executar
```bash
# MicroPython (Thonny): Instale primeiro o firmware MicroPython na RP2040. Depois abra o seu editor de texto de preferência compatível com
  MicroPython (para este teste foi usado o Thonny) e em seguida conecte a bitdoglab via USB no computador e o conector JST-PH de 4 pinos na bitdog com
  a pinagem da tabela já listada acima. Copie o arquivo bmp280.py deste repositório https://github.com/dafvid/micropython-bmp280 e abra com o Thonny, depois clique em "salvar como" e salve na RP2040 com o nome bmp280.py. Agora basta apenas executar o código desejado das pastas test/ ou src/.
```

## 5. Exemplos de uso
- `src/leitura_bruta_e_filtrado.py` — leitura bruta do sensor e leitura com média móvel para suavizar o ruído.  
- `test/adress` — código para encontrar o endereço(adress) do sensor  

## 6. Resultados e validação
- Prints/plots, fotos do setup, limitações, ruídos, dicas.

-Resultados do leitura_bruta_e_filtrado.py
<img width="425" height="207" alt="image" src="https://github.com/user-attachments/assets/a8f861c7-1fc0-464d-b3dc-a2d41cad857f" />



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
