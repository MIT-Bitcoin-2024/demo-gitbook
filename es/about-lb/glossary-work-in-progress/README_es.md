Por favor ten en cuenta: No traduzcas el nombre de la marca 'Lightning Bounties'. El nombre de la marca debe permanecer exactamente como está.

# Glosario (En Progreso)

## Términos comunes

***

<details>

<summary> Satoshi's (Sats) </summary>

Un satoshi es 1/100 millonésima parte de un Bitcoin. En la Red Lightning, un satoshi se puede dividir aún más en 1000 partes (llamado [millisatoshi](https://docs.lightning.engineering/community-resources/glossary#millisatoshi)). Se le pone ese nombre en honor al creador de Bitcoin, [Satoshi Nakamoto](https://docs.lightning.engineering/community-resources/glossary#satoshi-nakamoto).

</details>

<details>

<summary> mSats </summary>

Los mSats son cada 1/1000 (una milésima) de un satoshi. Un satoshi es la unidad más pequeña para bitcoin, pero lightning puede manejar con unidades aún más pequeñas mientras los canales están abiertos. La cantidad es [redondeada hacia abajo](https://github.com/lightningnetwork/lnd/blob/master/lnwire/msat.go#L22-L24) al satoshi más cercano cuando se cierra el canal y se difunde en la cadena de bloques para cumplir con el límite de bitcoin.

</details>

<details>

<summary> Pago </summary>

Un pago es una transacción que ocurre en la red lightning. Los pagos se enrutan a través de canales de pago lightning y no se registran en la cadena de bloques de bitcoin.

_Crédito: bitcoin.design_

</details>

<details>

<summary> Firma </summary>

Dado que una [clave privada](https://bitcoin.design/guide/glossary/#private-key) puede usarse para demostrar que el titular controla una dirección específica, por lo tanto, puede autorizar transacciones desde la dirección. Esto se llama una firma digital.

<img src="../../.gitbook/assets/image (4).png" alt="https://bitcoin.design/assets/images/guide/glossary/signature.jpg" data-size="original">

Una de las actividades más importantes de la red Bitcoin es verificar que las firmas sean válidas.

_Crédito: bitcoin.design_

</details>

<details>

<summary> Clave Pública </summary>

La clave pública de una dirección de bitcoin se puede derivar de la clave privada. La propia dirección es un hash de la clave pública.

</details>

<details>

<summary> Clave Privada </summary>

Cada dirección de Bitcoin tiene una clave pública y una clave privada correspondiente, juntas se llaman un par de claves. Si tienes acceso a ambas, la clave pública y privada, efectivamente controlas los fondos de la dirección. Al igual que con las billeteras HD, también hay pares de claves que controlan _ramas_ en el árbol jerárquico de la billetera y en la parte superior está el par de claves extendido (x-pub y x-prv para abreviar) que controla todas las direcciones en la billetera.

La clave privada es una cadena de caracteres hexadecimal de 64 dígitos (o 256 si se describe en binario con 1's y 0's) generada por el algoritmo de cifrado. Se ven algo así en forma hexadecimal:

`5KYZdUEo39z3FPrtuX2QbbwGnNP5zTd7yyr2SC1j299sBCnWjss`

O para la clave privada extendida:

`xprv9zrji5mK3nb4RbuR2ZYFtyzK3gn78KnEzkNP4ZxwwPPwcgQQVZqnjTMAGxmmM3jpmfsthQUtfD9iYPvnaqwejCjcyEswLqEhX4LPKNFUXT5`

_Crédito: bitcoin.design_

</details>

<details>

<summary> La Red Lightning </summary>

La [red lightning](https://lightning.network/) extiende bitcoin con canales de pago para aumentar la velocidad de las transacciones y reducir los costos. Está siendo ampliamente adoptada y aceptada como la forma preferida de escalar bitcoin.

_Crédito: bitcoin.design_

</details>

<details>

<summary>Facturas Lightning </summary>

Los usuarios de la red lightning utilizan una factura lightning para solicitar un pago. Está definido por [BOLT 11](https://github.com/lightningnetwork/lightning-rfc/blob/master/11-payment-encoding.md) e incluye una cantidad a pagar, destino del pago y un mensaje opcional. A diferencia de las direcciones de bitcoin, las facturas lightning caducan después de un tiempo determinado. Por defecto, este está configurado para 60 minutos.

_Crédito: bitcoin.design_

</details>

<details>

<summary> Frase de Acceso </summary>

Se puede agregar una frase de acceso a la [frase de recuperación](https://bitcoin.design/guide/glossary/#recovery-phrase) para mayor seguridad. Técnicamente, todas las frases de recuperación tienen una frase de acceso. Si el usuario no la establece, se usará una cadena vacía ("") por defecto. Usar la frase de recuperación con o sin la frase de acceso definida por el usuario recuperará dos billeteras DIFERENTES. Las frases de acceso a veces se llaman contraseña, la palabra extra o la palabra 13/25.

_Crédito: bitcoin.design_

</details>

<details>

<summary> Billetera Custodia </summary>

Una billetera custodia es una billetera en la que las claves privadas del usuario son mantenidas por un tercero, como un intercambio. El tercero tiene control total sobre los fondos del usuario, mientras que el usuario solo tiene permiso para enviar y recibir bitcoin.

El tercero es responsable de proporcionar una copia de seguridad de la billetera en caso de que el usuario olvide su información de inicio de sesión. Una billetera custodia está sujeta a las prácticas de seguridad del tercero, lo que reduce la responsabilidad del usuario, pero crea un riesgo mayor para la frase semilla y las claves almacenadas por la billetera si el tercero es hackeado.

</details>

<details>

<summary> Billetera No Custodia </summary>

Las billeteras no custodia le dan al usuario control total sobre sus fondos y las claves privadas asociadas. Al usar una billetera no custodia, un usuario es su propio banco; pueden iniciar transacciones y son responsables de la seguridad de su billetera, incluyendo la protección de su frase semilla, que se puede usar para restaurar su billetera si esta se pierde o se ve comprometida.

</details>

<details>

<summary> Faraday </summary>

Faraday es un software de análisis desarrollado por Lightning Labs que puede ayudar a identificar [necesidades de liquidez](https://docs.lightning.engineering/community-resources/glossary#liquidity-management) y canales rentables en un [Nodo Lightning](https://docs.lightning.engineering/community-resources/glossary#lightning-network-node).

</details>

<details>

<summary>Red de Chismes </summary>

La red de chismes de Lightning se utiliza para transmitir información sobre canales y pares.

</details>

<details>

<summary> Factura </summary>

Para recibir pagos de Lightning, el destinatario generalmente emite una factura que contiene información como una [clave pública](https://docs.lightning.engineering/community-resources/glossary#public-key), [hash de pago](https://docs.lightning.engineering/community-resources/glossary#payment-hash), o un monto y etiqueta de la factura. Las facturas están definidas en [BOLT 11](https://www.bolt11.org/).

</details>

<details>

<summary> Keysend </summary>

Keysend permite a los usuarios de la Red Lightning enviar fondos a una clave pública de un nodo.

</details>

<details>

<summary> Torre de Vigilancia </summary>

Una torre de Vigilancia consiste en un cliente y un servidor. El cliente compartirá información relevante para las [violaciones de canal](https://docs.lightning.engineering/community-resources/glossary#channel-breach) con el servidor, el cual intervendrá en el caso en que observe una violación en la cadena. Se necesitan las Torre de Vigilancia en caso de que el cliente esté desconectado e incapaz de observar la violación por sí mismo.

</details>

<details>

<summary> ID de Transacción </summary>

El ID de la transacción (txid) es el hash de una transacción de Bitcoin. Los canales son identificados por el ID de la transacción de su transacción de financiación.

</details>

<details>

<summary> Activos Taproot </summary>

Un protocolo respaldado por Taproot para emitir activos en Bitcoin que se pueden transferir a través de la Red Lightning para transacciones instantáneas, de alto volumen y con tarifas bajas.

Los Activos Taproot (anteriormente Taro) es un nuevo protocolo respaldado por Taproot diseñado para emitir activos en la blockchain de Bitcoin que se pueden transferir a través de la Red Lightning para transacciones instantáneas, de alto volumen y con tarifas bajas. En esencia, los Activos Taproot aprovechan la seguridad y estabilidad de la red Bitcoin y la velocidad, escalabilidad y bajas tarifas de Lightning.

Resumen de los Activos Taproot:

1. Permite emitir activos en la blockchain de Bitcoin
2. Aprovecha taproot para privacidad y escalabilidad
3. Los activos se pueden depositar en canales Lightning
4. Los activos se pueden transferir a través de la Red Lightning existente


</details>

<details>

<summary> Red Peer-to-Peer </summary>

Una red peer-to-peer es cualquier sistema que no depende de un líder, en el que las conexiones se realizan directamente entre pares sin intermediarios.

</details>

<details>

<summary></summary>

</details>

## Preguntas frecuentes - Red Lightning

***

<details>

<summary> ¿Cuántos Satoshi's (Sats) hay en un Bitcoin? </summary>

Cada una de las 21 millones de unidades de Bitcoin que existirán puede dividirse en 100,000,000 satoshis.

</details>

<details>

<summary> ¿Por qué las Facturas Lightning caducan? </summary>

¿Por qué caducan las facturas? Si las facturas no tuvieran fecha de vencimiento, es probable que los destinatarios se encontraran con problemas de memoria/almacenamiento a medida que el número de preimágenes almacenadas localmente crece con cada intento de pago.

_Crédito: bitcoin.design_

</details>

<details>

<summary> ¿Qué es un canal de la Red Lightning? </summary>

Un canal de la Red Lightning es un canal de pago entre pares que permite transacciones instantáneas y de bajo costo entre dos partes.

</details>

<details>

<summary> ¿Cómo abro un canal en la Red Lightning? </summary>

Abres un canal enviando una pequeña cantidad de Bitcoin a otro nodo o billetera, que sirve como depósito para el canal.

</details>

<details>

<summary> ¿Necesito administrar un nodo de la Red Lightning para usar la red? </summary>

No, no necesitas administrar un nodo para usar la Red Lightning. Puedes usar simplemente una aplicación de billetera Lightning para enviar y recibir pagos.

</details>

<details>

<summary> ¿Qué es una "reserva de canal" y cómo afecta mi experiencia de incorporación? </summary>

La reserva de canal es la cantidad de Bitcoin requerida para abrir un canal de pago. Reservas más altas pueden dificultar la búsqueda de nodos y la apertura de canales.

</details>

<details>

<summary> ¿Qué debo hacer si mi transacción Lightning falla mientras intento pagar a alguien? </summary>

Las transacciones de la Red Lightning pueden fallar por varias razones comunes. La más frecuente suele ser simplemente no tener fondos suficientes en el canal para cubrir el pago. Asegúrate de tener suficiente dinero en la cuenta desde la que estás enviando y no olvides incluir en el cálculo las tarifas de la red (~2% del monto total que estás intentando enviar).

Otro problema común es que la transacción no pueda encontrar una ruta al nodo Lightning del destinatario. Si esto sucede, simplemente prueba nuevamente unos minutos después.

La Red Lightning sigue evolucionando, por lo que algunas transacciones fallidas son normales. Pero esas dos cosas: fondos insuficientes y problemas de ruteo suelen ser los principales culpables cuando un pago Lightning no se realiza.

</details>

<details>

<summary></summary>

</details>

<details>

<summary></summary>

</details>

<details>

<summary></summary>

</details>

## Preguntas frecuentes de las billeteras de la Red Lightning 

***

<details>

<summary> ¿Cuáles son algunas billeteras populares de la Red Lightning? </summary>

Algunas billeteras de la Red Lightning populares incluyen:

* [Blue Wallet](https://bluewallet.io/)
* [Blink](https://www.blink.sv/)
* [Muun](https://muun.com/)
* [Wallet of Satoshi](https://www.walletofsatoshi.com/)
* [ Zeus Wallet](https://zeusln.com/)
* [Breez](https://breez.technology/)

</details>

<details>

<summary> ¿Las billeteras Lightning son lo mismo que las billeteras Bitcoin? </summary>

No, no son exactamente las mismas.

Una billetera Bitcoin almacena tu Bitcoin y realiza transacciones directamente en la red Bitcoin principal. Sin embargo, con una billetera Lightning, las transacciones se realizan encima de la red Bitcoin utilizando canales especializados entre dos partes. Estos canales permiten transacciones fuera de la cadena que el propio Bitcoin no rastrea. Solo la apertura y cierre de estos canales se registran en la red Bitcoin.

En resumen, aunque ambas billeteras involucran Bitcoin, una billetera lightning aprovecha canales adicionales para facilitar transacciones más rápidas y escalables.

</details>

<details>

<summary> ¿Cuál es la diferencia entre una billetera No custodia y una Custodia? </summary>

**Billetera No custodia:** Una billetera no custodia te proporciona un control total sobre tu clave privada y tu frase de recuperación. Esto significa que tú eres el único que puede iniciar transacciones, asegurando que tus fondos solo se pueden acceder con tu intervención directa. Sin embargo, recuerda que si olvidas o pierdes tu frase de recuperación, la empresa creadora de la billetera no podrá ayudarte a recuperar el acceso a tus fondos.

**Billetera Custodia:** Por otro lado, una billetera custodia toma un enfoque ligeramente diferente. En este tipo de billetera, no tienes control directo sobre la frase de recuperación. En su lugar, normalmente inicias sesión con tu correo electrónico y contraseña. En una billetera custodia, debes confiar en los creadores de la billetera para proteger tu frase de recuperación y tu Bitcoin. Esencialmente, los creadores de la billetera tienen técnicamente el control sobre tus fondos. Muchas bolsas proporcionan billeteras custodia como parte de sus servicios.

En resumen, las billeteras no custodia te brindan un control total, mientras que las billeteras custodia requieren que confíes en los creadores de la billetera para proteger tus fondos. Es importante entender la diferencia y elegir la opción que se alinea con tus preferencias y nivel de confianza.

</details>

<details>

<summary> ¿Cuál es la diferencia entre una billetera en caliente (Hot) y una billetera en frío (Cold)? </summary>

Los términos hot (en caliente) y cold (en frío) describen una billetera en términos de conexión con el internet. Si una billetera está en caliente, está conectada a internet, si está en frío, no lo está.

La idea es que una billetera en frío es menos propensa al robo por terceros a través de Internet. La mayoría de las aplicaciones de billeteras de software se considerarían en caliente (aunque algunas se pueden usar solo para firmar en un dispositivo no conectado a Internet), y la mayoría de las aplicaciones de billeteras de hardware se considerarían en frío (aunque a veces se conectan para fines de firma).

</details>

<details>

<summary></summary>

</details>

<details>

<summary></summary>

</details>



## Preguntas frecuentes de Lightning Bounties

***

<details>

<summary> ¿Qué es Lightning Bounties? </summary>

Lightning Bounties es una plataforma de recompensas por bugs de Web3 adaptada a desarrolladores de código abierto y la Red Lightning. Proporcionamos una plataforma para desarrolladores, cazadores de recompensas por bugs y hackers éticos para descubrir e informar bugs, vulnerabilidades y problemas de seguridad dentro de las aplicaciones y protocolos de la Red Lightning.

Lightning Bounties ofrece una oportunidad para que la comunidad de Lightning aborde proactivamente las posibles amenazas de seguridad y garantice la seguridad e integridad general de la red.

La plataforma facilita la divulgación responsable de vulnerabilidades y recompensa a las personas por sus esfuerzos en identificar e informar problemas de seguridad, contribuyendo en última instancia a la mejora y estabilidad continua de la red Lightning.

A través de Lightning Bounties, los participantes pueden participar en un esfuerzo colaborativo para fortalecer la seguridad del ecosistema Lightning, y contribuir a una red más segura y confiable para todos los usuarios.

</details>

<details>

<summary> ¿Quién suele utilizar Lightning Bounties? </summary>

Lightning Bounties atiende a dos grupos principales: **desarrolladores** y **organizaciones**.

Los **desarrolladores** pueden mostrar sus habilidades, ganar Bitcoin y contribuir al crecimiento de la tecnología web3.

Las **organizaciones** pueden aprovechar un grupo talentoso de desarrolladores para mejorar la calidad y seguridad de sus proyectos de software.

</details>

<details>

<summary> ¿Por qué debo vincular mi cuenta de GitHub para usar Lightning Bounties? </summary>

**Vincular tu cuenta de GitHub a Lightning Bounties es necesario por varias razones:**

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">

**EN RESUMEN**: _Vincular tu cuenta de GitHub simplifica la búsqueda de bugs, promueve la colaboración y asegura la distribución adecuada de las recompensas._

</details>

<details>

<summary></summary>

</details>

<details>

<summary></summary>

</details>