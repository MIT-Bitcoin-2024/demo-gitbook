# Glosario (Trabajo en progreso)

## Términos comunes

***

<details>

<summary>Satoshi's (Sats)</summary>

Un satoshi es la centésima millonésima parte de un Bitcoin. En la Red de Lightning, un satoshi puede subdividirse aún más en 1000 piezas ([millisatoshi](https://docs.lightning.engineering/community-resources/glossary#millisatoshi)). Está nombrado así en honor al creador del Bitcoin, [Satoshi Nakamoto](https://docs.lightning.engineering/community-resources/glossary#satoshi-nakamoto).

</details>

<details>

<summary>mSats</summary>

Los mSats son cada una de las milésimas de un satoshi. Un satoshi es la unidad más pequeña para bitcoin, pero lightning puede transitar con unidades aún más pequeñas mientras los canales están abiertos. La cantidad se redondea a la baja al satoshi más cercano cuando se cierra el canal y se transmite a la cadena de bloques para adherirse al límite del bitcoin.

</details>

<details>

<summary>Pago</summary>

Un pago es una transacción que ocurre en la red de lightning. Los pagos se envían a través de los canales de pago de lightning y no se registran en la cadena de bloques de bitcoin.

_Créditos: bitcoin.design_

</details>

<details>

<summary>Firma digital</summary>

Dado que a una [clave privada](https://bitcoin.design/guide/glossary/#private-key) se le puede usar para demostrar que el titular controla una dirección específica, por lo tanto, puede autorizar transacciones desde la dirección. Esto se llama una firma digital.



Una de las actividades más importantes de la red Bitcoin es verificar que las firmas sean válidas.

_Créditos: bitcoin.design_

</details>

<details>

<summary>Clave Pública</summary>

La clave pública de una dirección de Bitcoin se puede derivar de la clave privada. La dirección en sí es un hash de la clave pública.

</details>

<details>

<summary>Clave Privada</summary>

Cada dirección de Bitcoin tiene una clave pública y una clave privada correspondiente, juntas se llaman un par de claves. Si tienes acceso a ambas, la clave pública y privada, efectivamente controlas los fondos en la dirección. Al igual que con las carteras HD, también hay pares de claves que controlan _ramas_ en el árbol jerárquico de la cartera, y en lo más alto está el par de claves extendidas (x-pub y x-prv para abreviar) que controlan todas las direcciones en la cartera.

La clave privada es una cadena de caracteres hexadecimales de 64 (o 256 si se describe en bits 1's y 0's) generada por el algoritmo de cifrado. Se ven algo así en forma hexadecimal:

`5KYZdUEo39z3FPrtuX2QbbwGnNP5zTd7yyr2SC1j299sBCnWjss`

O para la clave privada extendida:

`xprv9zrji5mK3nb4RbuR2ZYFtyzK3gn78KnEzkNP4ZxwwPPwcgQQVZqnjTMAGxmmM3jpmfsthQUtfD9iYPvnaqwejCjcyEswLqEhX4LPKNFUXT5`

_Créditos: bitcoin.design_

</details>

<details>

<summary>La Red Lightning</summary>

La [red lightning](https://lightning.network/) amplía bitcoin con canales de pago para aumentar la velocidad de las transacciones y reducir costos. Está siendo adoptada y aceptada ampliamente como la forma preferida de escalar bitcoin.

_Crédito: bitcoin.design_

</details>

<details>

<summary>Facturas Lightning</summary>

Los usuarios de la red lightning utilizan una factura lightning para solicitar un pago. Está definida por [BOLT 11](https://github.com/lightningnetwork/lightning-rfc/blob/master/11-payment-encoding.md) e incluye una cantidad a pagar, el destino del pago y un mensaje opcional. A diferencia de las direcciones de bitcoin, las facturas lightning caducan después de un periodo determinado. Por defecto, este es de 60 minutos.

_Crédito: bitcoin.design_

</details>

<details>

<summary>Passphrase</summary>

Se puede agregar una passphrase a la [frase de recuperación](https://bitcoin.design/guide/glossary/#recovery-phrase) para una seguridad adicional. Técnicamente, todas las frases de recuperación tienen una passphrase. Si no es establecida por el usuario, una cadena vacía ("") será utilizada por defecto. Usar la frase de recuperación con o sin la passphrase definida por el usuario recuperará dos monederos DIFERENTES. Las passphrases a veces se llaman la contraseña, la palabra extra o la 13ª/25ª palabra.

_Crédito: bitcoin.design_

</details>

<details>

<summary>Cartera Custodia</summary>

Una cartera custodia es una cartera en la que las claves privadas del usuario son mantenidas por un tercero, como un exchange. El tercero tiene control total sobre los fondos del usuario, mientras que el usuario solo tiene permiso para enviar y recibir bitcoins.

El tercero es responsable de proporcionar una copia de seguridad a la cartera en caso de que el usuario olvide su información de inicio de sesión. Una cartera custodia está sujeta a las prácticas de seguridad del tercero, lo que reduce la responsabilidad del usuario pero crea un riesgo incrementado en la frase de recuperación y las claves almacenadas por la cartera si el tercero es hackeado.

</details>

<details>

<summary>Cartera No Custodia</summary>

Las carteras no custodia brindan al usuario control total sobre sus fondos y las claves privadas asociadas. Al usar una cartera no custodia, un usuario es su propio banco; puede iniciar transacciones y es responsable de la seguridad de su cartera, incluyendo la protección de su frase de recuperación, la cual puede ser usada para restaurar su cartera si se pierde o se compromete.

</details>

<details>

<summary>Faraday</summary>

Faraday es un software de análisis desarrollado por Lightning Labs que puede ayudar a identificar las [necesidades de liquidez](https://docs.lightning.engineering/community-resources/glossary#liquidity-management) y los canales rentables en un [Nodo de Lightning](https://docs.lightning.engineering/community-resources/glossary#lightning-network-node).

</details>

<details>

<summary>Red de Cotilleo</summary>

La red de cotilleo de Lightning se usa para transmitir información sobre canales y compañeros de red.

</details>

<details>

<summary>Factura</summary>

Para recibir pagos de Lightning, el destinatario generalmente emite una factura que contiene información como una [clave pública](https://docs.lightning.engineering/community-resources/glossary#public-key), un [hash de pago](https://docs.lightning.engineering/community-resources/glossary#payment-hash), o una cantidad y etiqueta de factura. Las facturas están definidas en [BOLT 11](https://www.bolt11.org/).

</details>

<details>

<summary>Keysend</summary>

Keysend permite a los usuarios de la red Lightning enviar fondos a la clave pública de un nodo.

</details>

<details>

<summary>Watchtower</summary>

Un watchtower consta de un cliente y un servidor. El cliente compartirá información relevante para las [violaciones de canal](https://docs.lightning.engineering/community-resources/glossary#channel-breach) con el servidor, que intervendrá en caso de que observen una infracción en la cadena. Los watchtowers son necesarios en caso de que el cliente esté desconectado y no pueda observar la infracción por sí mismo.

</details>

<details>

<summary>ID de transacción</summary>

El ID de transacción (txid) es el hash de una transacción de Bitcoin. Los canales se identifican por el ID de transacción de su transacción de financiamiento.

</details>

<details>

<summary>Activo Taproot</summary>

Un protocolo impulsado por Taproot para emitir activos en Bitcoin que se pueden transferir a través de la Red Lightning para realizar transacciones instantáneas, de alto volumen y con comisiones bajas.

Los activos Taproot (anteriormente Taro) son un nuevo protocolo impulsado por Taproot para emitir activos en la cadena de bloques de Bitcoin que se puede transferir a través de la Red Lightning para realizar transacciones instantáneas, de alto volumen y con comisiones bajas. En su núcleo, los activos Taproot aprovechan la seguridad y estabilidad de la red Bitcoin y la velocidad, escalabilidad y comisiones bajas de Lightning.

Resumen de los activos Taproot:

1. Permite que los activos se emitan en la cadena de bloques de Bitcoin.
2. Se basa en taproot para la privacidad y la escalabilidad.
3. Los activos pueden ser depositados en los canales Lightning.
4. Los activos pueden ser transferidos a través de la Red Lightning existente.

</details>

<details>

<summary>Red de Pares</summary>

Una red de pares es cualquier sistema que no depende de un líder, en el que las conexiones se realizan directamente entre pares sin intermediarios.

</details>

<details>

<summary></summary>



</details>

## FAQ’s - Red Lightning

***

<details>

<summary>¿Cuántos Satoshi's (Sats) hay en un Bitcoin?</summary>

Cada una de las 21 millones de unidades de Bitcoin que existirán puede dividirse aún más en 100,000,000 satoshis.

</details>

<details>

<summary>¿Por qué vencen las facturas de Lightning?</summary>

¿Por qué vencen las facturas? Si las facturas no tuvieran vencimiento, es probable que los destinatarios se encontrarían con problemas de memoria/almacenamiento a medida que aumenta el número de preimágenes almacenadas localmente con cada intento de pago.

_Créditos: bitcoin.design_

</details>

<details>

<summary>¿Qué es un canal de la Red Lightning?</summary>

Un canal de la Red Lightning es un canal de pago entre pares que permite transacciones instantáneas y de bajo costo entre dos partes.

</details>

<details>

<summary>¿Cómo abro un canal de la Red Lightning?</summary>

Abre un canal enviando una pequeña cantidad de Bitcoin a otro nodo o cartera, que sirve como depósito para el canal.

</details>

<details>

<summary>¿Necesito ejecutar un nodo de la Red Lightning para usar la red?</summary>

No, no necesitas ejecutar un nodo para usar la Red Lightning. Puedes simplemente usar una aplicación de cartera de lightning para enviar y recibir pagos.

</details>

<details>

<summary>¿Qué es una "reserva de canal" y cómo afecta mi experiencia de incorporación?</summary>

La reserva de canal es la cantidad de Bitcoin requerida para abrir un canal de pago. Las reservas más altas pueden dificultar la búsqueda de nodos y la apertura de canales.

</details>

<details>

<summary>¿Qué debo hacer si mi transacción de Lightning falla mientras intento pagar a alguien?</summary>

Las transacciones de la Red Lightning pueden fallar por algunas razones comunes. La más frecuente suele ser simplemente no tener suficientes fondos en tu canal para cubrir el pago. Asegúrate de tener suficiente dinero en la cuenta desde la que estás enviando y no olvides tener en cuenta las comisiones de la red (\~2% del monto total que estás intentando enviar).

Otro problema común es que la transacción no pueda encontrar una ruta hacia el nodo Lightning del destinatario. Si eso sucede, simplemente inténtalo de nuevo unos minutos más tarde.

La Red Lightning todavía está evolucionando, por lo que algunas transacciones fallidas son normales. Pero esas dos cosas, fondos insuficientes y problemas de enrutamiento, tienden a ser los principales culpables cuando un pago de Lightning no se realiza.

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

## FAQ's Carteras de la Red Lightning

***

<details>

<summary>¿Cuáles son algunas carteras populares de la Red Lightning?</summary>

Algunas carteras populares de la Red Lightning incluyen:

* [Blue Wallet](https://bluewallet.io/)
* [Blink](https://www.blink.sv/)
* &#x20;[Muun](https://muun.com/)&#x20;
* [Wallet of Satoshi](https://www.walletofsatoshi.com/)
* [Billetera Zeus](https://zeusln.com/)
* [Breez](https://breez.technology/)

</details>

<details>

<summary>¿Las carteras de Lightning son las mismas que las de Bitcoin?</summary>

No, no son exactamente lo mismo.

Una cartera de Bitcoin almacena tus Bitcoins y realiza transacciones directamente en la red principal de Bitcoin. Sin embargo, con una cartera de Lightning, las transacciones se realizan en la red de Bitcoin utilizando canales especializados entre dos partes. Estos canales permiten transacciones fuera de la cadena que el propio Bitcoin no rastrea. Solo la apertura y cierre de estos canales se registran en la red Bitcoin.

En resumen, mientras que ambas carteras involucran a Bitcoin, una cartera de Lightning emplea canales adicionales para facilitar transacciones más rápidas y escalables.

</details>

<details>

<summary>¿Cuál es la diferencia entre una Cartera No custodia &#x26; Custodia?</summary>

<mark style="background-color:red;">**Cartera No custodia:**</mark>\
Una cartera No custodia te da control total sobre tu clave privada y frase de recuperación. Esto significa que solo tú puedes iniciar transacciones, asegurando que tus fondos solo pueden ser accedidos con tu acción directa. Sin embargo, es importante recordar que si olvidas o pierdes tu frase de recuperación, los fabricantes de la cartera no pueden ayudarte a recuperar el acceso a tus fondos.

<mark style="background-color:orange;">**Cartera Custodia:**</mark>\
Por otro lado, una cartera Custodia adopta un enfoque ligeramente diferente. En este tipo de cartera, no tienes control directo sobre la frase de recuperación. En cambio, normalmente inicias sesión con tu correo electrónico y contraseña. En una cartera Custodia, tienes que confiar en los fabricantes de la cartera para que protejan tu frase de recuperación y tu Bitcoin. Básicamente, los fabricantes de la cartera técnicamente tienen el control sobre tus fondos. Muchos exchanges proporcionan carteras Custodia como parte de sus servicios.

Para resumir, las carteras No custodia te dan control completo, mientras que las carteras Custodia requieren que confíes en los fabricantes de la cartera para proteger tus fondos. Es importante entender la diferencia y elegir la opción que se alinee con tus preferencias y nivel de confianza.

</details>

<details>

<summary>¿Cuál es la diferencia entre una Cartera en <mark style="color:yellow;">Caliente</mark> vs <mark style="color:blue;">Fría</mark></summary>

_<mark style="color:yellow;">Caliente</mark>_ y _<mark style="color:blue;">Fría</mark>_ describe una cartera en términos de estar conectada a Internet. Donde una <mark style="color:yellow;">cartera caliente</mark> está conectada a Internet, una <mark style="color:blue;">cartera fría</mark> no lo está.

La idea es que una <mark style="color:blue;">cartera fría</mark> es menos susceptible al robo de terceros a través de Internet. La mayoría de las aplicaciones de carteras de software se verían como <mark style="color:yellow;">calientes</mark> (aunque algunas se pueden usar solo para firmar en un dispositivo no conectado a Internet), y la mayoría de las aplicaciones de carteras de hardware se verían como <mark style="color:blue;">frías</mark> (aunque a veces se conectan para propósitos de firma).

</details>

<details>

<summary></summary>



</details>

<details>

<summary></summary>



</details>

## Lightning Bounties FAQ's

***

<details>

<summary>¿Qué son los Lightning Bounties?</summary>

Lightning Bounties es una Plataforma de Recompensas de Errores Web3 diseñada para desarrolladores de código abierto y la Red Lightning. Proporcionamos una plataforma para desarrolladores, cazadores de recompensas de errores y hackers éticos para descubrir e informar errores, vulnerabilidades y problemas de seguridad dentro de las aplicaciones y protocolos de la Red Lightning.

Lightning Bounties ofrece una oportunidad para que la comunidad de Lightning aborde proactivamente las posibles amenazas a la seguridad y asegure la seguridad e integridad general de la red.

La plataforma facilita la divulgación responsable de vulnerabilidades y recompensa a las personas por sus esfuerzos en identificar e informar problemas de seguridad, contribuyendo en última instancia a la mejora y estabilidad continua de la red Lightning.

A través de Lightning Bounties, los participantes pueden participar en un esfuerzo colaborativo para reforzar la seguridad del ecosistema de Lightning, y contribuir a una red más segura y confiable para todos los usuarios.

</details>

<details>

<summary>¿Quiénes son los usuarios típicos de Lightning Bounties?</summary>

Lightning Bounties está diseñado para dos grupos principales: **desarrolladores** y **organizaciones**.

Los **desarrolladores** pueden mostrar sus habilidades, ganar Bitcoin, y contribuir al crecimiento de la tecnología web3.

Las **organizaciones** pueden aprovechar un talentoso grupo de desarrolladores para mejorar la calidad y seguridad de sus proyectos de software.

</details>

<details>

<summary>¿Por qué tengo que vincular mi cuenta de GitHub para usar Lightning Bounties?</summary>

**Es necesario vincular tu cuenta de GitHub a Lightning Bounties por varias razones:**



**TLDR**: _Vincular tu cuenta de GitHub simplifica la búsqueda de errores, promueve la colaboración y garantiza la distribución adecuada de recompensas._

</details>

<details>

<summary></summary>



</details>

<details>

<summary></summary>



</details>
