# Glossaire (Travail en cours)

## Termes communs

***

<details>

<summary>Satoshi's (Sats)</summary>

Un satoshi représente le cent millionième d'un Bitcoin. Dans le réseau Lightning, un satoshi est encore divisible en 1000 morceaux ([millisatoshi](https://docs.lightning.engineering/community-resources/glossary#millisatoshi)). Il est nommé d'après le créateur du Bitcoin, [Satoshi Nakamoto](https://docs.lightning.engineering/community-resources/glossary#satoshi-nakamoto).

</details>

<details>

<summary>mSats</summary>

Les mSats sont chacun le millième d'un satoshi. Un satoshi est l'unité la plus petite pour le bitcoin, mais le réseau Lightning peut effectuer des transactions avec des unités encore plus petites tant que des canaux sont ouverts. Le montant est [arrondi à la baisse](https://github.com/lightningnetwork/lnd/blob/master/lnwire/msat.go#L22-L24) au satoshi le plus proche lorsque le canal est fermé et diffusé à la blockchain pour respecter la limite du bitcoin.

</details>

<details>

<summary>Paiement</summary>

Un paiement est une transaction qui a lieu sur le réseau Lightning. Les paiements sont acheminés par des canaux de paiement Lightning et ne sont pas enregistrés dans la blockchain Bitcoin.

_Crédit: bitcoin.design_

</details>

<details>

<summary>Signature</summary>

Puisqu'une [clé privée](https://bitcoin.design/guide/glossary/#private-key) peut être utilisée pour prouver que le détenteur contrôle une adresse spécifique, elle peut donc autoriser des transactions à partir de cette adresse. On appelle cela une signature numérique.



L'une des activités les plus importantes du réseau Bitcoin est de vérifier que les signatures sont valides.

_Crédit: bitcoin.design_

</details>

<details>

<summary>Clé publique</summary>

La clé publique d'une adresse Bitcoin peut être dérivée de la clé privée. L'adresse elle-même est un hash de la clé publique.

</details>

<details>

<summary>Clé privée</summary>

Chaque adresse Bitcoin a une clé publique et une clé privée correspondante, ensemble elles sont appelées une paire de clés. Si vous avez accès à la clé publique et à la clé privée, vous contrôlez effectivement les fonds de l'adresse. Comme avec les portefeuilles HD, il existe également des paires de clés qui contrôlent des _branches_ dans l'arbre hiérarchique du portefeuille, et tout en haut se trouve la paire de clés étendue (x-pub et x-prv pour faire court) qui contrôle toutes les adresses du portefeuille.

La clé privée est une chaîne de caractères hexadécimaux de 64 (ou 256 si décrite en binaires 1 et 0) générée par l'algorithme de cryptage. Elles ressemblent à quelque chose comme ça en forme hexadécimale :

`5KYZdUEo39z3FPrtuX2QbbwGnNP5zTd7yyr2SC1j299sBCnWjss`

Ou pour la clé privée étendue :

`xprv9zrji5mK3nb4RbuR2ZYFtyzK3gn78KnEzkNP4ZxwwPPwcgQQVZqnjTMAGxmmM3jpmfsthQUtfD9iYPvnaqwejCjcyEswLqEhX4LPKNFUXT5`

_Crédit: bitcoin.design_

</details>

<details>

<summary>The Lightning Network</summary>

Le [réseau Lightning](https://lightning.network/) étend le bitcoin avec des canaux de paiement pour augmenter la vitesse des transactions et réduire les coûts. Il est de plus en plus adopté et accepté comme le moyen préféré d'améliorer l'évolutivité du bitcoin.

_Crédit: bitcoin.design_

</details>

<details>

<summary>Factures Lightning</summary>

Les utilisateurs du réseau Lightning utilisent une facture Lightning pour demander un paiement. Elle est définie par [BOLT 11](https://github.com/lightningnetwork/lightning-rfc/blob/master/11-payment-encoding.md) et comprend un montant à payer, une destination de paiement, et un message facultatif. Contrairement aux adresses Bitcoin, les factures Lightning expirent après un certain temps. Par défaut, cela est réglé à 60 minutes.

_Crédit: bitcoin.design_

</details>

<details>

<summary>Phrase de passe</summary>

Une phrase de passe peut être ajoutée à la [phrase de récupération](https://bitcoin.design/guide/glossary/#recovery-phrase) pour une sécurité supplémentaire. Techniquement, toutes les phrases de récupération ont une phrase de passe. Si elle n'est pas définie par l'utilisateur, une chaîne vide (“”) sera utilisée par défaut. L'utilisation de la phrase de récupération avec ou sans la phrase de passe définie par l'utilisateur permet de récupérer deux portefeuilles DIFFÉRENTS. Les phrases de passe sont parfois appelées le mot de passe, le mot supplémentaire, ou le 13ème/25ème mot.

_Crédit: bitcoin.design_

</details>

<details>

<summary>Portefeuille en dépôt</summary>

Un portefeuille en dépôt est un portefeuille dans lequel les clés privées de l'utilisateur sont détenues par un tiers, tel qu'une plateforme d'échange. Ce tiers a un contrôle total sur les fonds de l'utilisateur, tandis que l'utilisateur n'a que la permission d'envoyer et de recevoir des bitcoins.

Le tiers est responsable de fournir une sauvegarde du portefeuille en cas d'oubli des informations de connexion par l'utilisateur. Un portefeuille en dépôt est soumis aux pratiques de sécurité du tiers, ce qui réduit la responsabilité de l'utilisateur, mais crée un risque accru pour la phrase de récupération et les clés stockées par le portefeuille si le tiers est piraté.

</details>

<details>

<summary>Portefeuille non dépositaire</summary>

Les portefeuilles non dépositaires donnent à l'utilisateur un contrôle total sur ses fonds et les clés privées associées. En utilisant un portefeuille non dépositaire, un utilisateur est sa propre banque ; il peut initier des transactions et est responsable de la sécurité de son portefeuille, y compris de la protection de sa phrase de récupération, qui peut être utilisée pour restaurer son portefeuille s'il est perdu ou compromis.

</details>

<details>

<summary>Faraday</summary>

Faraday est un logiciel d'analyse développé par Lightning Labs qui peut aider à identifier les [besoins en liquidités](https://docs.lightning.engineering/community-resources/glossary#liquidity-management) et les canaux rentables dans un [nœud Lightning](https://docs.lightning.engineering/community-resources/glossary#lightning-network-node).

</details>

<details>

<summary>Réseau de potins</summary>

Le réseau de potins de Lightning est utilisé pour diffuser des informations sur les canaux et les pairs.

</details>

<details>

<summary>Facture</summary>

Pour recevoir des paiements Lightning, le destinataire émet généralement une facture contenant des informations telles qu'une [clé publique](https://docs.lightning.engineering/community-resources/glossary#public-key), un [hash de paiement](https://docs.lightning.engineering/community-resources/glossary#payment-hash), ou un montant de facture et une étiquette. Les factures sont définies dans[ BOLT 11](https://www.bolt11.org/).

</details>

<details>

<summary>Keysend</summary>

Keysend permet aux utilisateurs du réseau Lightning d'envoyer des fonds à la clé publique d'un nœud.

</details>

<details>

<summary>Tour de guet</summary>

Une tour de guet se compose d'un client et d'un serveur. Le client partagera des informations pertinentes à propos des [violations de canal](https://docs.lightning.engineering/community-resources/glossary#channel-breach) avec le serveur, qui interviendra en cas d'observation d'une violation sur la chaîne. Les tours de guet sont nécessaires dans le cas où le client est hors ligne et incapable d'observer lui-même la violation.

</details>

<details>

<summary>ID de transaction</summary>

L'ID de transaction (txid) est le hash d'une transaction Bitcoin. Les canaux sont identifiés par l'ID de transaction de leur transaction de financement.

</details>

<details>

<summary>Actifs Taproot</summary>

Un protocole alimenté par Taproot pour l'émission d'actifs sur Bitcoin qui peuvent être transférés sur le réseau Lightning pour des transactions instantanées, de gros volumes et à faible frais.

Les actifs Taproot (anciennement Taro) est un nouveau protocole alimenté par Taproot pour l'émission d'actifs sur la blockchain Bitcoin qui peuvent être transférés sur le réseau Lightning pour des transactions instantanées, de gros volumes et à faibles frais. Au cœur, Taproot Assets exploite la sécurité et la stabilité du réseau Bitcoin et la vitesse, l'évolutivité et les faibles frais de Lightning.

Aperçu des actifs Taproot :

1. Permet l'émission d'actifs sur la blockchain Bitcoin
2. Exploite Taproot pour la confidentialité et l'évolutivité
3. Les actifs peuvent être déposés dans des canaux Lightning
4. Les actifs peuvent être transférés sur le réseau Lightning existant

</details>

<details>

<summary>Réseau Peer-to-Peer</summary>

Un réseau peer-to-peer est tout système qui ne repose pas sur un leader, dans lequel des connexions sont établies directement entre pairs sans intermédiaires.

</details>

<details>

<summary></summary>



</details>

## FAQ’s - Réseau Lightning

***

<details>

<summary>Combien de Satoshi (Sats) y a-t-il dans un Bitcoin?</summary>

Chacune des 21 millions d'unités de Bitcoin qui existeront peut être encore divisée en 100 000 000 de satoshis.

</details>

<details>

<summary>Pourquoi les factures Lightning expirent-elles?</summary>

Pourquoi les factures expirent-elles? Si les factures n'avaient pas de date d'expiration, les destinataires auraient probablement des problèmes de mémoire/stockage à mesure que le nombre de pré-images stockées localement augmenterait avec chaque tentative de paiement.

_Crédit: bitcoin.design_

</details>

<details>

<summary>Qu'est-ce qu'un canal du réseau Lightning?</summary>

Un canal du réseau Lightning est un canal de paiement peer-to-peer qui permet des transactions instantanées et à faible coût entre deux parties.

</details>

<details>

<summary>Comment ouvrir un canal du réseau Lightning?</summary>

Ouvrez un canal en envoyant une petite quantité de Bitcoin à un autre nœud ou portefeuille, qui sert de dépôt pour le canal.

</details>

<details>

<summary>Dois-je exploiter un nœud du réseau Lightning pour utiliser le réseau?</summary>

Non, vous n'avez pas besoin d'exploiter un nœud pour utiliser le réseau Lightning. Vous pouvez simplement utiliser une application de portefeuille Lightning pour envoyer et recevoir des paiements.

</details>

<details>

<summary>Qu'est-ce qu'une "réserve de canal" et comment cela affecte-t-il mon expérience à bord?</summary>

La réserve de canal est le montant de Bitcoin nécessaire pour ouvrir un canal de paiement. Des réserves plus importantes peuvent rendre plus difficile la recherche de nœuds et l'ouverture de canaux.

</details>

<details>

<summary>Que dois-je faire si ma transaction Lightning échoue en essayant de payer quelqu'un?</summary>

Les transactions du réseau Lightning peuvent échouer pour quelques raisons courantes. La plus fréquente est généralement de ne pas avoir suffisamment de fonds dans votre canal pour couvrir le paiement. Assurez-vous d'avoir suffisamment d'argent sur le compte à partir duquel vous envoyez et n'oubliez pas de tenir compte des frais de réseau (\~2% du montant total que vous essayez d'envoyer).

Un autre problème courant est l'incapacité de la transaction à trouver une route vers le nœud Lightning du destinataire. Si cela se produit, essayez à nouveau quelques minutes plus tard.

Le réseau Lightning est encore en évolution, donc certaines transactions échouées sont normales. Mais ces deux choses - des fonds insuffisants et des problèmes de routage - sont souvent les principales raisons pour lesquelles un paiement Lightning ne passe pas.

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

## FAQ's portefeuilles du Lightning Network

***

<details>

<summary>Quels sont quelques portefeuilles populaires du réseau Lightning?</summary>

Quelques portefeuilles du réseau Lightning populaires incluent :

* [Blue Wallet](https://bluewallet.io/)
* [Blink](https://www.blink.sv/)
* [Muun](https://muun.com/)
* [Wallet of Satoshi](https://www.walletofsatoshi.com/)
* [Zeus Wallet](https://zeusln.com/)
* [Breez](https://breez.technology/)

</details>

<details>

<summary>Les portefeuilles Lightning sont-ils les mêmes que les portefeuilles Bitcoin?</summary>

Non, ils ne sont pas tout à fait les mêmes.

Un portefeuille Bitcoin stocke vos Bitcoin et effectue des transactions directement sur le réseau Bitcoin principal. Cependant, avec un portefeuille Lightning, les transactions sont effectuées au-dessus du réseau Bitcoin en utilisant des canaux spécialisés entre deux parties. Ces canaux permettent des transactions hors chaîne que Bitcoin lui-même ne suit pas. Seul l'ouverture et la fermeture de ces canaux sont enregistrées sur le réseau Bitcoin.

En résumé, bien que les deux portefeuilles impliquent le Bitcoin, un portefeuille Lightning utilise des canaux supplémentaires pour faciliter des transactions plus rapides et plus évolutives.

</details>

<details>

<summary>Quelle est la différence entre un portefeuille non dépositaire et dépositaire?</summary>

<mark style="background-color:red;">**Portefeuille non dépositaire:**</mark>\
Un portefeuille non dépositaire vous donne un contrôle total sur votre clé privée et votre phrase de récupération. Cela signifie que vous êtes le seul à pouvoir initier des transactions, garantissant que vos fonds ne peuvent être accessibles qu'avec votre action directe. Cependant, il est important de se rappeler que si vous oubliez ou perdez votre phrase de récupération, les fabricants du portefeuille ne pourront pas vous aider à retrouver l'accès à vos fonds.

<mark style="background-color:orange;">**Portefeuille dépositaire:**</mark>\
D'un autre côté, un portefeuille dépositaire adopte une approche légèrement différente. Dans ce type de portefeuille, vous n'avez pas le contrôle direct de la phrase de récupération. Au lieu de cela, vous vous connectez généralement avec votre email et votre mot de passe. Dans un portefeuille dépositaire, vous devez faire confiance aux fabricants du portefeuille pour sécuriser votre phrase de récupération et votre Bitcoin. Essentiellement, les fabricants du portefeuille ont techniquement le contrôle de vos fonds. De nombreuses plateformes d'échange fournissent des portefeuilles dépositaires dans le cadre de leurs services.

En somme, les portefeuilles non dépositaires vous donnent un contrôle total, tandis que les portefeuilles dépositaires exigent que vous fassiez confiance aux fabricants du portefeuille pour sécuriser vos fonds. Il est important de comprendre la différence et de choisir l'option qui correspond à vos préférences et à votre niveau de confiance.

</details>

<details>

<summary>Quelle est la différence entre un <mark style="color:yellow;">portefeuille en ligne</mark> vs <mark style="color:blue;">portefeuille hors ligne</mark></summary>

Un marqueur\_<mark style="color:yellow;">en ligne</mark>\_ et un marqueur _<mark style="color:blue;">hors ligne</mark>_ décrivent un portefeuille en termes de connexion à l'internet. Là où un <mark style="color:yellow;">portefeuille en ligne</mark> est connecté à l'internet, un <mark style="color:blue;">portefeuille hors ligne</mark> ne l'est pas.

L'idée est qu'un <mark style="color:blue;">portefeuille hors ligne</mark> est moins susceptible d'être volé par un tiers sur l'internet. La plupart des applications de portefeuille logiciel seraient considérées comme <mark style="color:yellow;">en ligne</mark> (bien que certaines puissent être utilisées uniquement pour signer sur un appareil non connecté à l'internet), et la plupart des applications de portefeuille matériel seraient considérées comme <mark style="color:blue;">hors ligne</mark> (bien qu'elles soient parfois connectées pour des raisons de signature).

</details>

<details>

<summary></summary>



</details>

<details>

<summary></summary>



</details>

## FAQ's - Lightning Bounties

***

<details>

<summary>Qu'est-ce que Lightning Bounties?</summary>

Lightning Bounties est une plateforme de récompense pour la détection de bogues Web3 adaptée aux développeurs open-source et au réseau Lightning. Nous offrons une plateforme pour les développeurs, les chasseurs de bogues et les hackers éthiques pour découvrir et signaler les bogues, vulnérabilités et problèmes de sécurité dans les applications et protocoles du réseau Lightning.

Lightning Bounties offre une opportunité à la communauté Lightning de traiter proactivement les éventuelles menaces de sécurité et d'assurer la sécurité et l'intégrité globales du réseau.

La plateforme facilite la divulgation responsable des vulnérabilités et récompense les individus pour leurs efforts dans l'identification et la déclaration des problèmes de sécurité, contribuant finalement à l'amélioration continue et à la stabilité du réseau Lightning.

Grâce à Lightning Bounties, les participants peuvent s'engager dans un effort collaboratif pour renforcer la sécurité de l'écosystème Lightning et contribuer à un réseau plus sûr et plus fiable pour tous les utilisateurs.

</details>

<details>

<summary>Qui utilise généralement Lightning Bounties?</summary>

Lightning Bounties s'adresse à deux groupes principaux : les **développeurs** et les **organisations**.

Les **développeurs** peuvent mettre en valeur leurs compétences, gagner des Bitcoin et contribuer à la croissance de la technologie web3.

Les **organisations** peuvent puiser dans un pool talentueux de développeurs pour améliorer la qualité et la sécurité de leurs projets logiciels.

</details>

<details>

<summary>Pourquoi dois-je lier mon compte GitHub à Lightning Bounties?</summary>

**Lier votre compte GitHub à Lightning Bounties est nécessaire pour plusieurs raisons:**



**TLDR**: \_Lier votre compte GitHub simplifie la chasse aux bugs, favorise la collaboration

</details>
