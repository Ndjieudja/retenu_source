$(() => {
    let doc = document.querySelector('body').parentNode;
    let body = document.querySelector('body');

    let title = document.createElement('title');
    const titleText = document.createTextNode('Documents Pointage');
    title.appendChild(titleText);
    doc.insertBefore(title, body);

    let header = document.createElement('header');
    let divHeader = document.createElement('div');
    let spanHeader = document.createElement('span');
    const headerText = document.createTextNode("Toujours lire les contraintes d'utilisation");
    spanHeader.appendChild(headerText);
    divHeader.appendChild(spanHeader);
    header.appendChild(divHeader);
    body.appendChild(header);

    // NOTES
    let notes = document.createElement('p');
    $(notes).attr('class', 'notes');
    const notesText = document.createTextNode("En cas de problème ou d'incompréhension, référez vous aux contraintes.");
    notes.appendChild(notesText);


    let container = document.createElement('div');
    $(container).attr('class', 'container');
    let titleContent = document.createElement('h1');
    const titleContentText = document.createTextNode('Gestion des documents de fiche de non pointage');
    titleContent.appendChild(titleContentText);
    container.appendChild(titleContent)

    let intro = document.createElement('div');
    $(intro).attr('class', 'intro');
    let introP = document.createElement('p');
    const introPText = document.createTextNode(
    "Ce document vous asiste sur les opérations de BTI vente et de BTI achat. De l'enregistrement du cahier de BTI jusqu'aux enregistrements des BTI vente et BTI achat sur chacune des feuilles de ce cahier, cette documentation répond successivement aux questions : Quel est l'ordre des opérations de BTI ? Comment enregistrer une opération de BTI ? Quelles sont les règles à respecter pour chaque opération de BTI ?"
    );
    introP.appendChild(introPText);
    intro.appendChild(introP);
    container.appendChild(intro);

    // BODY CONTENT
    let content = document.createElement('div');
    $(content).attr('class', 'content');
    let features = document.createElement('div');
    $(features).attr('class', 'features');


    let titleFeatures = document.createElement('h2');
    const titleFeaturesText = document.createTextNode('1. Fonctionnalités');
    titleFeatures.appendChild(titleFeaturesText);
    features.appendChild(titleFeatures);

    let featuresContent = document.createElement('div');
    $(featuresContent).attr('class', 'features-content');
    let featuresDiv = document.createElement('div');
    let featuresContentTitle = document.createElement('h2');
    const featuresContentTitleText = document.createTextNode('1.1 Enregistrement du cahier de BTI');
    featuresContentTitle.appendChild(featuresContentTitleText);
    featuresDiv.appendChild(featuresContentTitle);

    let pFeat1 = document.createElement('p');
    const pFeat1Text = document.createTextNode("La première opération à effectuer parmi les différentes opération de BTI est l'enregistrement du cahier de BTI. Une fois dans l'application de gestion des documents, après avoir ouvert le sous menu 'Gestion des document BTI', remplissez le formulaire avec les informations qui figurent sur le cahier physique de BTI.");
    pFeat1.appendChild(pFeat1Text);
    featuresDiv.appendChild(pFeat1);

    const featLiText = [
        "'Agence' est l'agence à laquelle le cahier est attribué. Vous la renseignerez dans la partie suivante;",
        "'Nombre de Début' est le numéro de la première feuille du cahier;",
        "'Nombre de Fin' est évidement le numéro de la dernière feuille du cahier;",
        "'Code' est le premier numéro manuscrit sur la première de couverture du cahier;",
        "'Date Emission' est la date d'enregistrement du cahier;",
        "'Date de Cloture' est logiquement la date de cloture du cahier, elle est renseignée automatiquement lorsque toutes les feuilles du cahier sont utilisées ou annulées."
    ];
    let ulFeat1 = document.createElement('ul');
    for (let i of featLiText) {
        let li = document.createElement('li');
        const liText = document.createTextNode(i);
        li.appendChild(liText);
        ulFeat1.appendChild(li);
    }
    pFeat1.appendChild(ulFeat1);
    featuresDiv.appendChild(pFeat1);

    let pFeat2 = document.createElement('p');
    const pFeat2Text = document.createTextNode("Après avoir sauvegardé les informations renseignées, un numéro est généré. Il permet d'identifier le cahier de façon unique. Ce numéro vous servira dans la partie suivante à attribuer un cahier à une agence. Bien que le cahier de BTI soit crée et enregistré, il n'est malheureusement pas encore utilisable car, il n'est encore attribué à aucune agence. Attribuons notre cahier de BTI précédement enregistré à une agence.");
    pFeat2.appendChild(pFeat2Text);
    featuresDiv.appendChild(pFeat2);
    featuresDiv.appendChild(notes.cloneNode(true));

    featuresContent.appendChild(featuresDiv);

    // SECOND SECTION FEATURES
    let featuresSecond = document.createElement('div');
    let featuresSecondTitle = document.createElement('h2');
    const featuresSecondTitleText = document.createTextNode("1.2 Attribution du cahier de BTI à une agence");
    featuresSecondTitle.appendChild(featuresSecondTitleText);
    featuresSecond.appendChild(featuresSecondTitle);

    let featuresSecondP = document.createElement('p');
    const featuresSecondPText = document.createTextNode("Sous le menu 'Gestion des documents BTI', ouvrer le sous menu 'Enregistrer l'agence sur le document'. Renseigner les informations requises.");
    featuresSecondP.appendChild(featuresSecondPText);

    const featuresSecondLiText = [
    "'Agence' est l'agence à laquelle vous voulez attribuer le cahier;",
    "'Numéro du cahier de BTI' est l'identifiant unique précédement généré lors de l'enregistrement du cahier."
    ];
    let featuresSecondUl = document.createElement('ul');
    for (let i of featuresSecondLiText) {
        let li = document.createElement('li');
        const liText = document.createTextNode(i);
        li.appendChild(liText);
        featuresSecondUl.appendChild(li);
    }
    featuresSecondP.appendChild(featuresSecondUl);
    featuresSecond.appendChild(featuresSecondP);

    let featuresSecondP2 = document.createElement('p');
    let featuresSecondPText2 = document.createTextNode("Après avoir sauvegardé les informations renseignées, valider le document en cliquant sur le bouton 'Valider le document'. Retour sur le formulaire d'enregistrement du cahier de BTI, l'ajout de l'agence à provoquer l'apparition du bouton 'Valider le document' qui permet de rendre le cahier prêt à l'utilisation.");
    featuresSecondP2.appendChild(featuresSecondPText2);
    featuresSecond.appendChild(featuresSecondP2);
    featuresSecond.appendChild(notes.cloneNode(true));

    featuresContent.appendChild(featuresSecond);

    // THIRD PART
    let featuresDiv2 = document.createElement('div');
    let featuresContentTitle2 = document.createElement('h2');
    const featuresContentTitleText2 = document.createTextNode('1.3 Opérations de BTI');
    featuresContentTitle2.appendChild(featuresContentTitleText2);
    featuresDiv2.appendChild(featuresContentTitle2);

    let pDiv2 = document.createElement('p');
    const pDiv2Text = document.createTextNode("Lors d'une opération de BTI vente, après avoir renseigner l'agence émettrice, les numéros des feuilles du cahier attribué à cet agence deviennent disponibles comme numéro de BTI. Si tel n'est pas le cas, veuillez attribuer au préalable un cahier de BTI à cet agence pour que ses feuilles deviennent disponibles.");
    pDiv2.appendChild(pDiv2Text);
    featuresDiv2.appendChild(pDiv2);

    let pDiv3 = document.createElement('p');
    const pDiv3Text = document.createTextNode("Par contre, lors d'une opération de BTI achat, les numeros des feuilles de tous les cahiers attribués et non utilisés sont disponibles indépendement de l'agence. Car, il ne vous est pas demandé de renseigner l'agence émettrice. Donc, la sélection du numéro de BTI à ce niveau demande plus d'attention vu le nombre important de numéros proposés.");
    pDiv3.appendChild(pDiv3Text);
    featuresDiv2.appendChild(pDiv3);

    let pDiv4 = document.createElement('p');
    const pDiv4Text = document.createTextNode("Lorsqu'une opération de BTI est finalisée, c'est-à-dire lorsque la vente et l'achat sont greffés. Le numéro de BTI utilisé n'est plus disponible et ne pourra plus jamais être utilisé.");
    pDiv4.appendChild(pDiv4Text);
    featuresDiv2.appendChild(pDiv4);
    featuresDiv2.appendChild(notes.cloneNode(true));

    featuresContent.appendChild(featuresDiv2);

    let featuresDiv3 = document.createElement('div');
    let featuresContentTitle3 = document.createElement('h2');
    const featuresContentTitleText3 = document.createTextNode('1.4 Opérations sur une feuille du cahier de BTI');
    featuresContentTitle3.appendChild(featuresContentTitleText3);
    featuresDiv3.appendChild(featuresContentTitle3);

    let pFeatDiv3 = document.createElement('p');
    const pFeatDiv3Text = document.createTextNode("Les opérations sur une feuille sont surtout consultatives.");
    pFeatDiv3.appendChild(pFeatDiv3Text);

    const featLiText2 = [
        "montant total de la vente.",
        "montant total d'achat.",
        "état de l'opération de BTI, validé, greffé, ...",
        "BTI vente et BTI achat enregistrés sur cette feuille."
    ];
    let ulFeatDiv3 = document.createElement('ul');
    for (let i of featLiText2) {
        let li = document.createElement('li');
        const liText = document.createTextNode(i);
        li.appendChild(liText);
        ulFeatDiv3.appendChild(li);
    }
    pFeatDiv3.appendChild(ulFeatDiv3);
    featuresDiv3.appendChild(pFeatDiv3);

    let pFeatDiv4 = document.createElement('p');
    const pFeatDiv4Text = document.createTextNode("Néanmoins, il existe une existe deux opérations de modification d'état pour une feuille. Une feuille peut être annulé en cliquant sur le bouton Annuler. Après avoir annulée une feuille, elle n'est plus disponible et ne pourra plus être utilisée. Elle peut également être activée en cliquant sur le bouton Activer si elle était à l'état annulé.");
    pFeatDiv4.appendChild(pFeatDiv4Text);
    featuresDiv3.appendChild(pFeatDiv4);
    featuresDiv3.appendChild(notes);

    featuresContent.appendChild(featuresDiv3);

    features.appendChild(featuresContent);

    content.appendChild(features);

    // CONSTRAINS
    let constrains = document.createElement('div');
    $(constrains).attr('class', 'constrains');
    let titleConstrains = document.createElement('h2');
    const titleConstrainsText = document.createTextNode('2. Contraintes');
    titleConstrains.appendChild(titleConstrainsText);
    constrains.appendChild(titleConstrains);

    let constrainsContent = document.createElement('div');
    $(constrainsContent).attr('class', 'constrains-content');

    // FIRST PART OF CONSTRAINS
    let firstConstrains = document.createElement('div');
    let firstConstrainsTitle = document.createElement('h2');
    const firstConstrainsTitleText = document.createTextNode("2.1 Contraintes sur l'enregistrement du cahier de BTI");
    firstConstrainsTitle.appendChild(firstConstrainsTitleText);
    firstConstrains.appendChild(firstConstrainsTitle);

    let firstConstrainsP = document.createElement('p');
    let firstConstrainsOl = document.createElement('ol');
    const firstConstrainsOlText = [
        "Le nombre de début doit être inférieur au nombre de fin.",
        "Un numéro de feuille ne peut appartenir à deux cahiers.",
        "Un cahier ne peut être validé s'il n'est attribué à aucune agence.",
        "Un cahier en cours d'utilisation ne peut être annulé."
    ];
    for(let i of firstConstrainsOlText) {
        let li = document.createElement('li');
        const liText = document.createTextNode(i);
        li.appendChild(liText);
        firstConstrainsOl.appendChild(li);
    }
    firstConstrainsP.appendChild(firstConstrainsOl);
    firstConstrains.appendChild(firstConstrainsP);

    constrainsContent.appendChild(firstConstrains);

    // SECOND PART OF CONSTRAINS
    let secondConstrains = document.createElement('div');
    let secondConstrainsTitle = document.createElement('h2');
    const secondConstrainsTitleText = document.createTextNode("2.2 Contraintes sur l'attribution du cahier de BTI à une agence");
    secondConstrainsTitle.appendChild(secondConstrainsTitleText);
    secondConstrains.appendChild(secondConstrainsTitle);

    let secondConstrainsP = document.createElement('p');
    let secondConstrainsOl = document.createElement('ol');
    const secondConstrainsOlText = [
        "Une agence ne peut recevoir un nouveau cahier sans avoir clôturé au moins un des deux précédents reçu.",
        "En cas de nécessité d'attribution de plus de deux cahiers à une agence, l'approbation de l'administrateur est nécessaire.",
        "Un document en cours d'utilisation ne peut être annulé."
    ];
    for(let i of secondConstrainsOlText) {
        let li = document.createElement('li');
        const liText = document.createTextNode(i);
        li.appendChild(liText);
        secondConstrainsOl.appendChild(li);
    }
    secondConstrainsP.appendChild(secondConstrainsOl);
    secondConstrains.appendChild(secondConstrainsP);

    constrainsContent.appendChild(secondConstrains);

    // THIRD PART OF CONSTRAINS
    let thirdConstrains = document.createElement('div');
    let thirdConstrainsTitle = document.createElement('h2');
    const thirdConstrainsTitleText = document.createTextNode("2.3 Contraintes sur les opérations sur une feuille du cahier de BTI");
    thirdConstrainsTitle.appendChild(thirdConstrainsTitleText);
    thirdConstrains.appendChild(thirdConstrainsTitle);

    let thirdConstrainsP = document.createElement('p');
    let thirdConstrainsOl = document.createElement('ol');
    const thirdConstrainsOlText = [
        "une feuille ne peut être annulée qu'à l'état brouillon.",
        "Une feuille ne peut être activée que si elle était préalablement annulée.",
        "Une feuille préalablement annulée ne peut être activée si deux cahiers de cette agence sont ouvert."
    ];
    for(let i of thirdConstrainsOlText) {
        let li = document.createElement('li');
        const liText = document.createTextNode(i);
        li.appendChild(liText);
        thirdConstrainsOl.appendChild(li);
    }
    thirdConstrainsP.appendChild(thirdConstrainsOl);
    thirdConstrains.appendChild(thirdConstrainsP);
    constrainsContent.appendChild(thirdConstrains);

    constrains.appendChild(constrainsContent);

    content.appendChild(constrains);

    container.appendChild(content);

    body.appendChild(container);


    let footer = document.createElement('footer');
    let divFooter = document.createElement('div');
    let spanCopyright = document.createElement('span');
    $(spanCopyright).attr('class', 'copyright');
    const spanCopyrightText = document.createTextNode('&#169;');
    spanCopyright.appendChild(spanCopyrightText);
    const divFooterText = document.createTextNode(' Copyright 2022 | Par ');
    let footerLink = document.createElement('a');
    $(footerLink).attr({class: 'social', href: 'https://app-avenue.herokuapp.com'})
    footerLinkText = document.createTextNode('Dongmo Geraud');
    footerLink.appendChild(footerLinkText);
    // divFooter.appendChild(spanCopyright);
    divFooter.appendChild(divFooterText);
    divFooter.appendChild(footerLink);
    footer.appendChild(divFooter);
    body.appendChild(footer);
    $('footer a').attr('target', function() {
        return '_blank';
    });
});
