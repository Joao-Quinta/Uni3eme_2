---
title: "TP7: generics en Java avec covariance et contravariance"
documentclass: article
papersize: a4
fontsize: 12pt
header-includes:
  - \usepackage{listings}
  - \usepackage{xcolor}
  - \usepackage{hyperref}
  - \usepackage{url}
  - \usepackage{subcaption}
output:
  html_document:
    number_sections: true
  pdf_document:
    number_sections: true
---


\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

\lstdefinestyle{mystyle}{
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=b,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2
}

\lstset{style=mystyle}



\section{Introduction}
Le but de ce TP va être de se familiariser avec les notions de *co-variance* et *contra-variance* en Java. Si vous avez un doute par rapport à ces notions, qui sont loin d'être triviales, nous vous recommendons de relire/revisionner le cours 7, deuxième partie. En particulier la mnémonique *PECS: Producer Extends Consumer Super* pourra nous être utile pour ce TP.

Pour ce TP7, vous êtes invités à reprendre votre TP6 (ou utiliser la solution TP6 fournie sur Moodle), car elle contient un générateur pseudo-aléatoire de potions magiques qui nous sera utile ici.

Toujours dans le cadre de notre RPG, nous allons cette fois-ci implémenter un marchant (*trader*) de potion magiques (healing ou mana). Par la suite, on pourra imaginer créer un vendeur plus général (aussi: armes, armures, sacs, etc.). Cependant pour ce TP, vous pouvez vous limiter à un vendeur de potions, car cela sera suffiant pour mettre en pratique les notions de co-variance et contra-variance.





\section{Exercice 1}

Pour mettre en place un système de vente, les potions magique vont désormais avoir un attribut *price* (``int``) en plus de leur précédents attributs, i.e.:

- name
- weight
- HP ou mana (selon le type de potion)

Il faudra aussi créer (ou reprendre des TP précédents) une classe ``Player`` ou ``GameCharacter`` par exemple, peu importe comment vous la nommez, mais qui permettra de créer des joueurs avec au minimum un nom, des points de vie et possiblement de mana ainsi qu'une quantité d'or qui leur permettra d'acheter des potions chez le marchand.

Dans cet exercice, il s'agit d'implémenter les composants mentionnés ci-dessus.


\section{Exercice 2}
Dans cet exercice, nous allons créer le marchand de potions. Celui-ci est un "peronnage non joueur" (PNJ) ou en anglais "non player character" (NPC) dans le jargon des RPG. Ceci veut dire que c'est un "joueur" qui est contrôlé par l'ordinateur et non par un joueur humain. Néanmoins on pourra utiliser la même super classe (``Player``) par exemple pour spécialiser ces NPCs.

Le trader (marchand) aura un stock de potions (que vous pouvez par exemple générer pseudo-aléatoirement) sous la formue d'une liste et le client aura un sac qu'on va aussi implémenter ici par une liste. En nous aidant de la mnémonique PECS essayez d'implémenter et utiliser les méthodes suivantes:

\begin{lstlisting}[language=Java]
public void buyPotion(List<? super Item> bag, Item potion, ...){...}
public Item sellPotion(List<? extends Item> stock, ... ){...}
\end{lstlisting}

Les "..." représentent pour vous la possibilité de rajouter d'autre arguments, si besoin. 

Ensuite créez un personnage trader et des acheteurs qui cont implémenter ces méthodes et faites faire des achats et vente de potions dans votre classe main. Vous pouvez aussi réfléchir à implémenter une méthode pour le payment: si la somme est suffisante, le vendeur acceptera de vous vendre l'objet demandé.


\section {Rendu}

Ce TP n'est pas noté. Néanmoins, nous vous demandons de le déposer sur Moodle via le widget prévu à cet effet. Archivez votre projet tout entier dans **un seul** fichier .zip avec la convention de nommage suivante: **prenomNomTP7.zip**.