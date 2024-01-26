# Contagem de pessoas

O código disponibilizado aqui faz a contagem de pessoas usando YOLO. As detecções são enviadas para um servidor Thingsboard.

A solução é ideal para captura em uma sala. O código supõe o uso de uma câmera anexada ao equipamento de captura, bem como um servidor Thingsboard em funcionamento.

O código é baseado no trabalho desenvolvido por [Nimbus](https://github.com/ASTRAson/Nimbus)

## Requisitos

- Raspberry Pi 3
- Web Cam

## Instalação

Instale as dependências usando ``` pip install -r requirements.txt ```

Renomeie o arquivo ```config-exemplo.yaml``` para ```config.yaml```.

Adicione ao arquivo o ```host``` do Thingsboard que será usado para envio das informações e o Token de Acesso do dispositivo criado no respectivo servidor do Thingsboard. Por favor, verifique a [documentação do Thingsboard](https://thingsboard.io/docs/) para detalhes sobre a criação de serviços e configuração de dispositivos.

## Instruções de uso

``` python3 main.py ```

Por padrão a captura é feita a cada **4 segundos** e o número de pessoas detectadas pelo modelo YOLO é armazenada. Uma média do número de pessoas detectadas é enviada a cada **60 segundos**. Desta forma, suaviza-se os efeitos da variação de detecção causados pela movimentação no ambiente.

Os tempos de captura e envio podem ser modificados. Para isso, modifique o arquivo ```config.yaml```.
