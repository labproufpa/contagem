# Contagem de pessoas

O código disponibilizado aqui faz a contagem de pessoas usando YOLO. As detecções são enviadas para um servidor Thingsboard. 

A solução é ideal para captura em uma sala. O código supõe o uso de uma câmera anexada ao equipamento de captura.

O código é baseado no trabalho desenvolvido em [Nimbus](https://github.com/ASTRAson/Nimbus)

## Requisitos

- Raspberry Pi 3
- Web Cam

## Instalação

``` pip install -m requirements.txt ```

## Instruções de uso

``` python3 main.py ```

Por padrão a captura é feita a cada **4 segundos** e o número de pessoas detectadas pelo modelo YOLO é armazenada. Uma média do número de pessoas detectadas é enviada a cada **60 segundos**. Desta forma, suaviza-se os efeitos da variação de detecção causados pela movimentação no ambiente.

Os tempos de captura e envio podem ser modificados.