# Contagem de pessoas

O código disponibilizado aqui faz a contagem de pessoas usando YOLO. As detecções são enviadas para um servidor Thingsboard.

A solução é ideal para captura em uma sala. O código supõe o uso de uma câmera anexada ao equipamento de captura, bem como um servidor Thingsboard em funcionamento.

O código é baseado no trabalho desenvolvido por [Nimbus](https://github.com/ASTRAson/Nimbus)

## Requisitos

- Web Cam ou Raspberry Pi Cam
- Caso executando em uma Raspberry Pi, utilizar o modelo versão 4 ou superior

## Instalação

Instale as dependências usando ``` pip install -r requirements.txt ```

## Configuração

Renomeie o arquivo ```config-exemplo.yaml``` para ```config.yaml```.

Adicione ao arquivo o ```host``` do Thingsboard que será usado para envio das informações e o Token de Acesso do dispositivo criado no respectivo servidor do Thingsboard. Por favor, verifique a [documentação do Thingsboard](https://thingsboard.io/docs/) para detalhes sobre a criação de serviços e configuração de dispositivos.

No ```config.yaml``` escolha o modo de operação dentre as opções disponíveis:

- ```dev``` neste modo não ocorre o envio de dados ao Thinsgboard e a frequência de captura é bastante intensa (ideal para ambientes de desenvolvimento) 
- ```cv2``` é o modo que assume o uso de uma câmera USB
- ```pi``` é o modo para uso com uma câmera Raspberry Pi Cam em uma Raspberry Pi

Por padrão a captura no modo ```cv2``` é feita a cada **4 segundos** e o número de pessoas detectadas pelo modelo YOLO é armazenada. Uma média do número de pessoas detectadas é enviada a cada **60 segundos**. Desta forma, suaviza-se os efeitos da variação de detecção causados pela movimentação no ambiente.

No modo ```pi``` a captura é feita, por padrão, a cada **30 segundos** e os envios a cada **60 segundos**. Os tempos de captura e envio, exceto no modo ```dev```, podem ser modificados. Para isso, modifique o arquivo ```config.yaml```.

## Instruções de uso

``` python3 main.py ```