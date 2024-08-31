# lightning network faqs\_fr

## FAQ sur le Réseau Lightning

###

<details>

<summary>Combien y a-t-il de Satoshi (Sats) dans un Bitcoin?</summary>

Chacune des 21 millions d'unités de Bitcoin qui existeront jamais peut être divisée davantage en 100 000 000 de satoshis.

</details>

<details>

<summary>Pourquoi les factures Lightning expirent-elles?</summary>

Pourquoi les factures expirent-elles? Si les factures n'expiraient pas, les destinataires rencontreraient probablement des problèmes de mémoire/espace de stockage à mesure que le nombre d'images pré-calculées localement augmenterait avec chaque tentative de paiement.

_Credit: bitcoin.design_

</details>

<details>

<summary>Qu'est-ce qu'un canal du Réseau Lightning?</summary>

Un canal du Réseau Lightning est un canal de paiement peer-to-peer qui permet des transactions instantanées et à faible coût entre deux parties.

</details>

<details>

<summary>Comment j'ouvre un canal du Réseau Lightning?</summary>

On ouvre un canal en envoyant une petite quantité de Bitcoin à un autre nœud ou portefeuille, ce qui sert de dépôt pour le canal.

</details>

<details>

<summary>Dois-je gérer un nœud du Réseau Lightning pour utiliser le réseau?</summary>

Non, tu n'as pas besoin de gérer un nœud pour utiliser le Réseau Lightning. Tu peux simplement utiliser une application de portefeuille lightning pour envoyer et recevoir des paiements.

</details>

<details>

<summary>Qu'est-ce qu'une "réserve de canal" et comment cela affecte-t-il mon expérience d'intégration?</summary>

La réserve de canal est la quantité de Bitcoin requise pour ouvrir un canal de paiement. Des réserves plus élevées peuvent rendre plus difficile la recherche de nœuds et l'ouverture de canaux.

</details>

<details>

<summary>Que dois-je faire si ma transaction Lightning échoue alors que j'essaie de payer quelqu'un?</summary>

Les transactions du Réseau Lightning peuvent échouer pour quelques raisons courantes. La plus fréquente est généralement de ne pas avoir suffisamment de fonds dans ton canal pour couvrir le paiement. Assure-toi d'avoir assez d'argent dans le compte à partir duquel tu envoies et n'oublie pas de prendre en compte les frais de réseau (\~2% du montant total que tu essaies d'envoyer).

Un autre problème courant est que la transaction ne parvient pas à trouver une route vers le nœud Lightning du destinataire. Si cela se produit, essaie à nouveau quelques minutes plus tard.

Le Réseau Lightning est encore en évolution, donc certaines transactions échouées sont normales. **Mais ces deux choses - des fonds insuffisants et des problèmes de routage - ont tendance à être les principaux coupables lorsqu'un paiement Lightning ne passe pas.**

</details>

<details>

<summary>Quels sont certains cas d'utilisation réels du Réseau Lightning?</summary>

Le Réseau Lightning permet toutes sortes de cas d'utilisation passionnants, comme les micropaiements instantanés, les services pay-per-use, le pourboire numérique, et plus encore. Il a également le potentiel d'apporter des services financiers aux non-bancarisés et sous-bancarisés partout dans le monde.

</details>

<details>

<summary>Le Réseau Lightning est-il sécurisé?</summary>

Comme Batman protégeant Gotham, le Réseau Lightning a plusieurs couches de sécurité pour garder vos fonds en sécurité. Avec des fonctionnalités comme les portefeuilles multi-signatures et le routage en oignon, tes sats sont entre de bonnes mains.

</details>

<details>

<summary>Puis-je utiliser le Réseau Lightning pour envoyer de grandes transactions?</summary>

Bien que le Réseau Lightning soit idéal pour les petites transactions fréquentes, il peut ne pas être idéal pour les grandes transactions en raison de contraintes de liquidité. Pour des sommes plus importantes, il vaut mieux s'en tenir aux transactions Bitcoin sur chaîne.

</details>

<details>

<summary>Quels sont les avantages d'utiliser le Réseau Lightning pour le développement Web3?</summary>

Les transactions instantanées et à faible coût du Réseau Lightning en font la solution de paiement idéale pour le monde trépidant du développement web3. Les développeurs peuvent recevoir leurs récompenses en Bitcoin presque immédiatement, sans les tracas des frais élevés ou des temps de confirmation longs.

</details>

<details>

<summary>Qu'est-ce que les Zaps? ⚡️</summary>

⚡️Les Zaps sont un moyen d'envoyer une petite quantité de Bitcoin (sats) au portefeuille Lightning de quelqu'un, accompagnée d'un message ou d'une information, comme un mémo ou un lien. C'est comme envoyer un message texte, mais avec une petite quantité de Bitcoin attachée.

</details>

<details>

<summary>Qu'est-ce que les mSats (millisats)?</summary>

Les mSats sont chacun 1/1000 (un millième) d'un satoshi. Un satoshi est l'unité la plus petite pour le bitcoin, mais lightning peut effectuer des transactions avec des unités encore plus petites tant que les canaux sont ouverts. Le montant est [arrondi](https://github.com/lightningnetwork/lnd/blob/master/lnwire/msat.go#L22-L24) au satoshi le plus proche lorsque le canal est fermé et diffusé sur la blockchain pour respecter la limite de Bitcoin.

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
