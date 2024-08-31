# lightning network faqs\_fr\_fr

Voici la traduction en français montréalais en gardant "Lightning Bounties":

## FAQ sur le Lightning Network

###

<details>

<summary>Combien y a-t'il de Satoshi (Sats) dans un Bitcoin?</summary>

Chaque de la gang des 21 millions de p'tits Bitcoin qui existeront pogne peut être divisée encore plus dans 100 000 000 de satoshis.

</details>

<details>

<summary>Pourquoi les factures Lightning ont-elles une date limite?</summary>

Pourquoi les factures ont-elles une date limite? Si les factures n'avaient pas de date limite, le destinataire aurait sûrement des problèmes de stockage à mesure que le nombre d'images pré-calculées grimpe avec chaque essai de paiement.

_Credit: bitcoin.design_

</details>

<details>

<summary>C'est quoi un canal du Lightning Network?</summary>

Un canal du Lightning Network c'est un canal de paiement peer-to-peer qui permet des transactions instantanées et à faible coût entre deux parties.

</details>

<details>

<summary>Comment j'ouvre un canal du Lightning Network?</summary>

Pour ouvrir un canal, tu balances une petite quantité de Bitcoin à un autre noeud ou porte-feuille, c'est ça qui sert de dépôt.

</details>

<details>

<summary>Est-ce que j'ai besoin de gérer un noeud Lightning pour utiliser le réseau?</summary>

Non, t'as pas besoin de gérer un noeud pour utiliser le Lightning Network. T'as juste à utiliser une application de porte-feuille Lightning pour envoyer et recevoir des paiements.

</details>

<details>

<summary>Qu'est-ce qu'une "réserve de canal" et comment ça affecte mon expérience?</summary>

La réserve de canal, c'est la quantité de Bitcoin nécessaire pour ouvrir un canal de paiement. Si la réserve est trop élevée, ça peut rendre plus difficile de trouver des noeuds et d'ouvrir des canaux.

</details>

<details>

<summary>Que dois-je faire si ma transaction Lightning échoue alors que j'essaie de payer quelqu'un?</summary>

Les transactions du Lightning Network peuvent échouer pour plusieurs raisons. La plus commune c'est généralement de ne pas avoir assez d'fonds dans ton canal pour couvrir le paiement. Faut que t'aies assez d'argent dans ton compte pour pouvoir envoyer et n'oublie pas les frais du réseau (\~2% du montant total que tu veux envoyer).

Un autre problème commun c'est que la transaction ne trouve pas une route vers le noeud Lightning du destinataire. Si ça arrive, essaie encore quelques minutes plus tard.

Le Lightning Network est encore en train d'évoluer, donc il arrive que des transactions échouent. **Ces deux problèmes - manque de fonds et problèmes de routage - sont généralement les coupables quand un paiement Lightning ne passe pas.**

</details>

<details>

<summary>Quels sont quelques cas d'utilisation réels du Lightning Network?</summary>

Le Lightning Network permet toutes sortes de cas d'utilisation fun, comme les micropaiements instantanés, les services pay-per-use, les tips numériques, et plus encore. Ça a aussi le potentiel de rendre les services financiers accessibles aux gens sans banque partout dans le monde.

</details>

<details>

<summary>Est-ce que le Lightning Network est sécurisé?</summary>

Comme Batman qui protège Gotham, le Lightning Network a plusieurs niveaux de sécurité pour garder tes fonds en sécurité. Avec des features comme les portefeuilles multi-signatures et le routage en oignon, tes sats sont entre des bonnes mains.

</details>

<details>

<summary>Est-ce que je peux utiliser le Lightning Network pour envoyer de grosses transactions?</summary>

Bien que le Lightning Network soit génial pour les petites transactions fréquentes, c'est pas l'idéal pour des grosses transactions à cause de problèmes de liquidité. Pour des montants plus élevés, c'est mieux d'utiliser les transactions Bitcoin sur la chaîne.

</details>

<details>

<summary>Quels sont les avantages d'utiliser le Lightning Network pour le développement Web3?</summary>

Les transactions instantanées et peu chères du Lightning Network en font la solution de paiement idéale pour le développement web3. Les développeurs peuvent recevoir leurs primes en Bitcoin presque immédiatement, sans avoir à s'occuper des frais élevés ou des temps de confirmation longs.

</details>

<details>

<summary>Qu'est-ce que les Zaps? ⚡️</summary>

⚡️Les Zaps, c'est un moyen d'envoyer une petite quantité de Bitcoin (sats) au portefeuille Lightning de quelqu'un, avec un message ou une information, genre un mémo ou un lien. C'est comme envoyer un texto, mais avec une petite quantité de Bitcoin attachée.

</details>

<details>

<summary>Qu'est-ce que les mSats (millisats)?</summary>

Les mSats, c'est chacun 1/1000 (un millième) d'un satoshi. Un satoshi, c'est la plus petite unité de bitcoin, mais Lightning peut réaliser des transactions avec des unités encore plus petites tant que les canaux sont ouverts. Le montant est [arrondi](https://github.com/lightningnetwork/lnd/blob/master/lnwire/msat.go#L22-L24) au plus proche satoshi lorsque le canal est fermé et diffusé sur la blockchain pour respecter la limite de Bitcoin.

<img src="https://static.wixstatic.com/media/8b683e_5fadb3f8111444c8902ff8ddadd28c7d~mv2.jpeg/v1/fill/w_1344,h_449,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/8b683e_5fadb3f8111444c8902ff8ddadd28c7d~mv2.jpeg" alt="" data-size="original">

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
