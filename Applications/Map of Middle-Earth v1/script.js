const map = L.map('map', {
    crs: L.CRS.Simple,
    minZoom: -1,
    maxZoom: +4,
});

const bounds = [[0, 0], [768, 1024]];
const imageUrl = 'middle-earth-map.jpeg';
L.imageOverlay(imageUrl, bounds).addTo(map);
map.fitBounds(bounds);

const mapData = {
    paths: [
        { category: "Thorin and Company", file: "thorin-path.svg" },
        { category: "Frodo & Sam", file: "frodo-path.svg" },
        { category: "Merry & Pippin", file: "merry-path.svg" },
        { category: "Gimli & Legolas", file: "gimli-path.svg" },
        { category: "Boromir", file: "boromir-path.svg" },
        { category: "Aragorn", file: "aragorn-path.svg" },
        { category: "Gandalf the Grey", file: "gandalf-grey-path.svg" },
        { category: "Gandalf the White", file: "gandalf-white-path.svg" }
    ],
    quests: [
        {
            name: "Quest for Erebor",
            category: "Quest for Erebor",
            pins: [
                { coords: [555, 262], popup: {title: "Hobbiton", date: "", description: "Hobbiton was a hobbit village in the central regions of the Shire, within the borders of the Westfarthing."}, iconType: "hobbits" },
                { coords: [551, 333], popup: {title: "Bree", date: "", description: "Bree was the chief village of Bree-land, a small wooded region near the intersection of the main north-south and east-west routes through Eriador. Bree-land was the only part of Middle-earth where Men and hobbits dwelt side by side and Bree had a large population of Hobbits."}, iconType: "humans" },
                { coords: [570, 455], popup: {title: "Stone Trolls", date: "[May 28, T.A. 2941]", description: "Three Stone Trolls (William, Tom and Bert) captured Bilbo and the Company of Thorin. Thanks to Gandalf who tricked them, they kept fighting over how to cook the dwarves until the sun set up, frozing them into stone statues."}, iconType: "encounter" },
                { coords: [563, 495], popup: {title: "Rivendell (Imladris)", date: "", description: "Rivendell was established by Elrond in S.A. 1697 as a refuge from Sauron after the Fall of Eregion. It remained Elrond's seat throughout the remainder of the Second Age and until the end of the Third Age, when he took the White Ship for Valinor."}, iconType: "elves" },
                { coords: [585, 525], popup: {title: "Goblin-town", date: "", description: "Goblin-town was a Goblin dwelling under the Misty Mountains, which was ruled by the Great Goblin. Goblin-town was a series of tunnels and caverns, which went all the way through the mountains, with a 'back door' (the Goblin-gate) near the Eagle's Eyrie in Wilderland, which served as a means of escape, and an access to the Wilderland. A cave with a lake was deep beneath Goblin-town yet was connected to the Goblins' tunnels, with one passage leading to the 'back door'."}, iconType: "evil" },
                { coords: [588, 530], popup: {title: "Bilbo steals the Ring from Gollum", date: "[July 12, T.A. 2941]", description: "Bilbo picked up a strange golden ring in the dark passages under Goblin-town. He then met Gollum whom defied him to a riddle contest for his life. Bilbo won, but then Gollum went to get his magic ring to kill him anyway. He then discovered that his ring was missing, and understood that Bilbo took it. He chased Bilbo, but Bilbo unwittingly used the ring and escaped his notice."}, iconType: "encounter" },
                { coords: [645, 455], popup: {title: "Mount Gram", date: "", description: "Mount Gram was inhabited by Orcs led by their King Golfimbul. In T.A. 2747 they attacked much of northern Eriador, but were defeated in the Battle of Greenfields."}, iconType: "evil" },
                { coords: [588, 565], popup: {title: "Beorn's Hall", date: "", description: "Beorn's Hall was the home of Beorn, a powerful Skin-changer. Beorn hosted and aided Thorin and Company during their Quest for Erebor."}, iconType: "humans" },
                { coords: [605, 650], popup: {title: "Giant Spiders", date: "[August, T.A. 2941]", description: "Giant spiders (Ungolianth's spawns) managed to capture and entangle in webs each of the thirteen Dwarves. Only Bilbo's magic Ring and his Elven blade Sting allowed them to escape from being eaten, before being captured by Thranduil's elves."}, iconType: "encounter" },
                { coords: [623, 663], popup: {title: "Elvenking's Hall", date: "", description: "Elvenking's Hall were a cave system in northern Mirkwood, in which King Thranduil and many of the Elves of Mirkwood lived during most of the Third Age and into the Fourth Age."}, iconType: "elves" },
                { coords: [617, 680], popup: {title: "Esgaroth (Lake Town)", date: "", description: "Lake-Town was the township of the Lake-men in Wilderland. The town was constructed entirely of wood and stood upon wooden pillars sunk into the bed of the Long Lake, as a protection against the dragon Smaug, who dwelt nearby in the Lonely Mountain."}, iconType: "humans" },
                { coords: [618, 683], popup: {title: "Smaug", date: "[November 1, T.A. 2941]", description: "Bard fired a Black Arrow into the vulnerable spot on the dragon's belly. Roaring in fury and pain, Smaug fell from the sky and plummeted into the flaming ruins of Lake-town, his death marked the end of the great dragons in Middle-earth."}, iconType: "death" },
                { coords: [625, 683], popup: {title: "Dale", date: "", description: "Dale was a great city of the Northmen which was destroyed by Smaug and rebuilt as the capital of a great kingdom after his demise."}, iconType: "humans" },
                { coords: [635, 680], popup: {title: "Erebor", date: "", description: "The Longbeards had control of Erebor since at least the early Second Age. With the awakening of Durin's Bane in the capital of Khazad-dûm, Thráin I led a group of Dwarves to Erebor. Once there, the dwarves dug caves and halls to form an underground city, thus establishing the Kingdom under the Mountain in T.A. 1999."}, iconType: "dwarves" },
                { coords: [632, 685], popup: {title: "Thorin, Fíli and Kíli", date: "[November 23, T.A. 2941]", description: "When Bilbo regained consciousness, the battle was already over. Thorin II Oakenshield had been mortally wounded on the field, and his nephews Fíli and Kíli died defending him as he lay on the ground."}, iconType: "death" },
                { coords: [630, 678], popup: {title: "Battle of Five Armies", date: "[November 23, T.A. 2941]", description: "The five warring parties were the Goblins and the Wargs against Men, Elves and Dwarves on and near the Lonely Mountain."}, iconType: "battle" },
                { coords: [450, 600], popup: {title: "Dol Guldur", date: "", description: "Dol Guldur ('Hill of Sorcery' in Sindarin), also called 'the dungeons of the Necromancer', was a stronghold of Sauron located in the south of Mirkwood."}, iconType: "evil" }
            ]
        },
        {
            name: "Quest of the Ring",
            category: "Quest of the Ring",
            pins: [
                { coords: [563, 495], popup: {title: "Rivendell (Imladris)", date: "", description: "Rivendell was established by Elrond in S.A. 1697 as a refuge from Sauron after the Fall of Eregion. It remained Elrond's seat throughout the remainder of the Second Age and until the end of the Third Age, when he took the White Ship for Valinor."}, iconType: "elves" },
                { coords: [472, 475], popup: {title: "Moria (Khazad-dûm)", date: "", description: "Khazad-dûm was the grandest and most famous of the mansions of the Dwarves. There, for many thousands of years, a thriving Dwarvish community created the greatest city ever known."}, iconType: "dwarves" },
                { coords: [474, 497], popup: {title: "Gandalf the Grey", date: "[January 25, T.A. 3019]", description: "Gandalf pursued the Balrog from the deepests dungeons of Moria to Durin's Tower, climbing through the whole Endless Stair, where they fought for three days and two nights. In the end, the Balrog was cast down and it broke the mountain-side as it fell. Gandalf himself died following this ordeal, but was later sent back to Middle-earth with even greater powers as Gandalf the White."}, iconType: "death" },
                { coords: [555, 262], popup: {title: "Hobbiton", date: "", description: "Hobbiton was a hobbit village in the central regions of the Shire, within the borders of the Westfarthing."}, iconType: "hobbits" },
                { coords: [555, 275], popup: {title: "Battle of Bywater", date: "[November 3, T.A. 3019]", description: "The Battle of Bywater was a battle for control of the Shire and the final battle of the War of the Ring. After he fleed from the Battle of Isengard, Saruman took control over the Shire with a band of ruffians. When Frodo and his companions returned from the Coronation of Elessar, they rallied the hobbits wanting to resist and defeated the ruffians, then confronted Saruman. Wormtongue killed Saruman and was shot dead by the hobbits."}, iconType: "battle" },
                { coords: [540, 305], popup: {title: "Old Man Willow", date: "[September 26, T.A. 3018]", description: "Old Man Willow was a willow tree in the Old Forest, who might have been an Ent who had become tree-like, or possibly a Huorn. Old Man Willow cast a spell on the Hobbits, Frodo, Sam, Merry and Pippin, causing them to fall asleep and trying to kill them. They were saved by the timely arrival of Tom Bombadil who knew 'the tune for him'."}, iconType: "encounter" },
                { coords: [544, 309], popup: {title: "Tom Bombadil", date: "[September 26, T.A. 3018]", description: "Tom Bombadil, a mysterious creature living in the Dark Forst with his wife Goldberry, saved Frodo, Sam, Merry and Pippin from the Old Man Willow, an evil willow who cast a spell on them and trapped Merry and Pippin. He then hosted the hobbits for two nights, during which he told them many tales and songs."}, iconType: "encounter" },
                { coords: [540, 325], popup: {title: "Barrow-wights", date: "[September 28, T.A. 3018]", description: "The Barrow-wights were a kind of undead-like creatures, dead bones animated by evil spirits. Frodo, Sam, Merry an Pippin were trapped in the Barrow-downs by the spells of the Barrow-wights, and were nearly slain by the creatures. They were saved in the last minute by Tom, who seemed to have had complete authority over them."}, iconType: "encounter" },
                { coords: [551, 333], popup: {title: "Bree", date: "", description: "Bree was the chief village of Bree-land, a small wooded region near the intersection of the main north-south and east-west routes through Eriador. Bree-land was the only part of Middle-earth where Men and hobbits dwelt side by side and Bree had a large population of Hobbits."}, iconType: "humans" },
                { coords: [558, 385], popup: {title: "Weathertop (Amun Sûl)", date: "", description: "In T.A. 3018, Amun Sûl was the scene of two fights involving the Nazgûl: one with Gandalf on October 3 and one with the Ring-bearer three days later."}, iconType: "humans" },
                { coords: [450, 532], popup: {title: "Lothlórien", date: "", description: "Lothlórien (or Lórien) was a kingdom of Silvan Elves on the eastern side of the Hithaeglir. It was considered one of the most beautiful places in Middle-earth during the Third Age, and had the only mallorn-trees east of the sea."}, iconType: "elves" },
                { coords: [450, 600], popup: {title: "Dol Guldur", date: "", description: "Dol Guldur ('Hill of Sorcery' in Sindarin), also called 'the dungeons of the Necromancer', was a stronghold of Sauron located in the south of Mirkwood."}, iconType: "evil" },
                { coords: [353, 450], popup: {title: "Isengard (Angrenost)", date: "", description: "Isengard was one of the three major fortresses of Gondor, and held within it one of the realm's palantíri. In the latter half of the Third Age, the stronghold came into the possession of Saruman, becoming his home and personal domain until his defeat in the War of the Ring."}, iconType: "evil" },
                { coords: [345, 450], popup: {title: "Battle of Isengard", date: "[3 March, T.A. 3019]", description: "Spurred on by Meriadoc Brandybuck and Peregrin Took, the Ents, followed by Huorns, invaded the Ring of Isengard from Fangorn Forest. It led the the drowning of Isengard and the defeat of Saruman."}, iconType: "battle" },
                { coords: [300, 480], popup: {title: "Helm's Deep", date: "", description: "Helm's Deep was a large valley gorge in the north-western Ered Nimrais (White Mountains) below the Thrihyrne. It was actually the name of the whole defensive system including its major defensive structure, the Hornburg."}, iconType: "humans" },
                { coords: [305, 485], popup: {title: "Battle of the Hornburg", date: "[3-4 March, T.A. 3019]", description: "The Battle of the Hornburg took place at the mountain fortress of the Hornburg in the valley of Helm's Deep in Rohan. Taking place over the night of the 3-4 March T.A. 3019, it saw the attacking Uruk-hai of Saruman defeated by the Rohirrim led by Théoden and Erkenbrand."}, iconType: "battle" },
                { coords: [288, 505], popup: {title: "Edoras", date: "", description: "Edoras was the capital of Rohan that held the Golden Hall of Meduseld. Rohan's first capital was at Aldburg in the Folde, until King Eorl the Young or his son Brego built Edoras in T.A. 2569."}, iconType: "humans" },
                { coords: [263, 510], popup: {title: "Paths of the dead", date: "", description: "The Paths of the Dead was a haunted underground passage through the White Mountains that led from Harrowdale in Rohan to Blackroot Vale in Gondor."}, iconType: "humans" },
                { coords: [300, 605], popup: {title: "Boromir", date: "[February 26, T.A. 3019]", description: "Boromir died at Amon Hen, the westernmost of the three peaks at the southern end of Nen Hithoel. He perished trying to defend Merry and Pippin from Saruman's Orcs, slaying at least 20 of them before perishing after being hit by many arrows."}, iconType: "death" },
                { coords: [226, 654], popup: {title: "Minas Tirith", date: "", description: "Minas Tirith was originally a fortress, Minas Anor, built in S.A. 3320 by the Faithful Númenóreans. From T.A. 1640 onwards it was the capital of the South-kingdom and the seat of its Kings and ruling Stewards."}, iconType: "humans" },
                { coords: [230, 656], popup: {title: "Battle of Pelennor Fields", date: "[15 March, T.A. 3019]", description: "The Battle of the Pelennor Fields was the greatest battle of the War of the Ring. This battle saw the siege of Minas Tirith by Mordor's troops widely outnumbering the defenders, but resulted in the loss of Sauron's armies after the Witch King was killed in combat."}, iconType: "battle" },
                { coords: [230, 662], popup: {title: "Osgiliath", date: "", description: "Founded by Isildur and Anárion near the end of the Second Age, Osgiliath was designated the capital of the southern Númenórean kingdom in exile, Gondor. It stays so until the King's House was moved to the more secure Minas Anor in T.A. 1640."}, iconType: "humans" },
                { coords: [230, 680], popup: {title: "Minas Morgul", date: "", description: "Minas Morgul (originally called Minas Ithil) was the twin city of Minas Tirith before its fall to the forces of Sauron in the Third Age. It then became the stronghold of the Witch-king of Angmar until Sauron's defeat."}, iconType: "evil" },
                { coords: [240, 690], popup: {title: "Shelob", date: "[March 12, T.A. 3019]", description: "Shelob was born as the last child of the spider-like demon Ungoliant. On March 12 T.A. 3019, Gollum led Sam and Frodo into the tunnels of Shelob's Lair and abandoned them in the dark. He planned that Shelob would eat Sam and Frodo so that he could find the One Ring among the bones and clothes."}, iconType: "encounter" },
                { coords: [295, 690], popup: {title: "Black Gate (Morannon)", date: "", description: "The Black Gate was the main entrance into the land of Mordor. It was built by Sauron after he chose Mordor as a land to make into a stronghold in S.A. 1000."}, iconType: "evil" },
                { coords: [300, 690], popup: {title: "Battle of the Morannon", date: "[25 March, T.A. 3019]", description: "The Battle of the Morannon was the last major battle against Sauron in the War of the Ring, fought at the Black Gate of Mordor on 25 March T.A. 3019. The army of the West, 6,000 strong by now, led by Aragorn marched on the gate as a diversionary feint to distract Sauron's attention from Frodo and Sam, who were carrying the One Ring through Mordor. It was hoped that Sauron would think Aragorn had the Ring and was now trying to use it to overthrow Mordor."}, iconType: "battle" },
                { coords: [250, 725], popup: {title: "Mount Doom (Orodruin, Amon Amarth)", date: "", description: "Melkor created Mount Doom in the First Age. When Sauron chose the land of Mordor as his dwelling-place in the Second Age, Orodruin was the reason for his choice. The mountain erupted in S.A. 3429, signalling Sauron's attack on Gondor and it took the name Amon Amarth, 'Mount Doom'. This is where the One Ring was forged by Sauron, and where it was destroyed by Gollum."}, iconType: "evil" },
                { coords: [259, 751], popup: {title: "Barad-dûr", date: "", description: "Barad-dûr, also known as the Dark Tower, was the chief fortress of Sauron, on the Plateau of Gorgoroth in Mordor. Sauron began to build Barad-dûr in around S.A. 1000, and completed his fortress after 600 years of the construction with the power of the Ring. It was partially destroyed after Sauron's defeat against Isildur, and began to be rebuilt in T.A. 2951."}, iconType: "evil" },
                { coords: [555, 178], popup: {title: "Grey Havens (Mithlond)", date: "", description: "Founded by the Elves of Lindon in S.A. 1, the Grey Havens were known for their good harbourage and many ships; these were used by any of the Eldar to leave Middle-earth for Eressëa or Valinor."}, iconType: "elves" },
                { coords: [370, 490], popup: {title: "Merry and Pippin meet Treebeard", date: "[February 29, T.A. 3019]", description: "Treebeard discovered Merry and Pippin in Fangorn Forest after they escaped from Saruman's Orcs, and welcomed them to the WellingHall."}, iconType: "encounter" }
            ]
        }
    ],
    places: [
        {
            name: "Humans",
            category: "Humans",
            pins: [
                { coords: [551, 333], popup: {title: "Bree", description: "Bree was the chief village of Bree-land, a small wooded region near the intersection of the main north-south and east-west routes through Eriador. Bree-land was the only part of Middle-earth where Men and hobbits dwelt side by side and Bree had a large population of Hobbits."} },
                { coords: [558, 385], popup: {title: "Weathertop (Amun Sûl)", description: "In T.A. 3018, Amun Sûl was the scene of two fights involving the Nazgûl: one with Gandalf on October 3 and one with the Ring-bearer three days later."} },
                { coords: [588, 565], popup: {title: "Beorn's Hall", description: "Beorn's Hall was the home of Beorn, a powerful Skin-changer. Beorn hosted and aided Thorin and Company during their Quest for Erebor."} },
                { coords: [617, 680], popup: {title: "Esgaroth (Lake Town)", description: "Lake-Town was the township of the Lake-men in Wilderland. The town was constructed entirely of wood and stood upon wooden pillars sunk into the bed of the Long Lake, as a protection against the dragon Smaug, who dwelt nearby in the Lonely Mountain."} },
                { coords: [625, 683], popup: {title: "Dale", description: "Dale was a great city of the Northmen which was destroyed by Smaug and rebuilt as the capital of a great kingdom after his demise."} },
                { coords: [300, 480], popup: {title: "Helm's Deep", description: "Helm's Deep was a large valley gorge in the north-western Ered Nimrais (White Mountains) below the Thrihyrne. It was actually the name of the whole defensive system including its major defensive structure, the Hornburg."} },
                { coords: [288, 505], popup: {title: "Edoras", description: "Edoras was the capital of Rohan that held the Golden Hall of Meduseld. Rohan's first capital was at Aldburg in the Folde, until King Eorl the Young or his son Brego built Edoras in T.A. 2569."} },
                { coords: [263, 510], popup: {title: "Paths of the dead", description: "The Paths of the Dead was a haunted underground passage through the White Mountains that led from Harrowdale in Rohan to Blackroot Vale in Gondor."} },
                { coords: [226, 654], popup: {title: "Minas Tirith", description: "Minas Tirith was originally a fortress, Minas Anor, built in S.A. 3320 by the Faithful Númenóreans. From T.A. 1640 onwards it was the capital of the South-kingdom and the seat of its Kings and ruling Stewards."} },
                { coords: [230, 662], popup: {title: "Osgiliath", description: "Founded by Isildur and Anárion near the end of the Second Age, Osgiliath was designated the capital of the southern Númenórean kingdom in exile, Gondor. It stays so until the King's House was moved to the more secure Minas Anor in T.A. 1640."} },
            ]
        },
        {
            name: "Elves",
            category: "Elves",
            pins: [
                { coords: [555, 178], popup: {title: "Grey Havens (Mithlond)", description: "Founded by the Elves of Lindon in S.A. 1, the Grey Havens were known for their good harbourage and many ships; these were used by any of the Eldar to leave Middle-earth for Eressëa or Valinor."} },
                { coords: [563, 495], popup: {title: "Rivendell (Imladris)", description: "Rivendell was established by Elrond in S.A. 1697 as a refuge from Sauron after the Fall of Eregion. It remained Elrond's seat throughout the remainder of the Second Age and until the end of the Third Age, when he took the White Ship for Valinor."} },
                { coords: [623, 663], popup: {title: "Elvenking's Hall", description: "Elvenking's Hall were a cave system in northern Mirkwood, in which King Thranduil and many of the Elves of Mirkwood lived during most of the Third Age and into the Fourth Age."} },
                { coords: [450, 532], popup: {title: "Lothlórien", description: "Lothlórien (or Lórien) was a kingdom of Silvan Elves on the eastern side of the Hithaeglir. It was considered one of the most beautiful places in Middle-earth during the Third Age, and had the only mallorn-trees east of the sea."} },
            ]
        },
        {
            name: "Dwarves",
            category: "Dwarves",
            pins: [
                { coords: [472, 475], popup: {title: "Moria (Khazad-dûm)", description: "Khazad-dûm was the grandest and most famous of the mansions of the Dwarves. There, for many thousands of years, a thriving Dwarvish community created the greatest city ever known."} },
                { coords: [635, 680], popup: {title: "Erebor", description: "The Longbeards had control of Erebor since at least the early Second Age. With the awakening of Durin's Bane in the capital of Khazad-dûm, Thráin I led a group of Dwarves to Erebor. Once there, the dwarves dug caves and halls to form an underground city, thus establishing the Kingdom under the Mountain in T.A. 1999."} },
            ]
        },
        {
            name: "Hobbits",
            category: "Hobbits",
            pins: [
                { coords: [555, 262], popup: {title: "Hobbiton", description: "Hobbiton was a hobbit village in the central regions of the Shire, within the borders of the Westfarthing."} },
                { coords: [551, 333], popup: {title: "Bree", description: "Bree was the chief village of Bree-land, a small wooded region near the intersection of the main north-south and east-west routes through Eriador. Bree-land was the only part of Middle-earth where Men and hobbits dwelt side by side and Bree had a large population of Hobbits."} },
            ]
        },
        {
            name: "Evil",
            category: "Evil",
            pins: [
                { coords: [700, 420], popup: {title: "Carn Dûm", description: "Carn Dûm was the chief fortress of the realm of Angmar and the seat of its king until its defeat against the combined armies of Gondor, Lindon and Arnor in T.A. 1974."} },
                { coords: [645, 455], popup: {title: "Mount Gram", description: "Mount Gram was inhabited by Orcs led by their King Golfimbul. In T.A. 2747 they attacked much of northern Eriador, but were defeated in the Battle of Greenfields."} },
                { coords: [585, 525], popup: {title: "Goblin-town", description: "Goblin-town was a Goblin dwelling under the Misty Mountains, which was ruled by the Great Goblin. Goblin-town was a series of tunnels and caverns, which went all the way through the mountains, with a 'back door' (the Goblin-gate) near the Eagle's Eyrie in Wilderland, which served as a means of escape, and an access to the Wilderland. A cave with a lake was deep beneath Goblin-town yet was connected to the Goblins' tunnels, with one passage leading to the 'back door'."} },
                { coords: [450, 600], popup: {title: "Dol Guldur", description: "Dol Guldur ('Hill of Sorcery' in Sindarin), also called 'the dungeons of the Necromancer', was a stronghold of Sauron located in the south of Mirkwood."} },
                { coords: [353, 450], popup: {title: "Isengard (Angrenost)", description: "Isengard was one of the three major fortresses of Gondor, and held within it one of the realm's palantíri. In the latter half of the Third Age, the stronghold came into the possession of Saruman, becoming his home and personal domain until his defeat in the War of the Ring."} },
                { coords: [295, 690], popup: {title: "Black Gate (Morannon)", description: "The Black Gate was the main entrance into the land of Mordor. It was built by Sauron after he chose Mordor as a land to make into a stronghold in S.A. 1000."} },
                { coords: [230, 680], popup: {title: "Minas Morgul", description: "Minas Morgul (originally called Minas Ithil) was the twin city of Minas Tirith before its fall to the forces of Sauron in the Third Age. It then became the stronghold of the Witch-king of Angmar until Sauron's defeat."} },
                { coords: [250, 725], popup: {title: "Mount Doom (Orodruin, Amon Amarth)", description: "Melkor created Mount Doom in the First Age. When Sauron chose the land of Mordor as his dwelling-place in the Second Age, Orodruin was the reason for his choice. The mountain erupted in S.A. 3429, signalling Sauron's attack on Gondor and it took the name Amon Amarth, 'Mount Doom'. This is where the One Ring was forged by Sauron, and where it was destroyed by Gollum."} },
                { coords: [259, 751], popup: {title: "Barad-dûr", description: "Barad-dûr, also known as the Dark Tower, was the chief fortress of Sauron, on the Plateau of Gorgoroth in Mordor. Sauron began to build Barad-dûr in around S.A. 1000, and completed his fortress after 600 years of the construction with the power of the Ring. It was partially destroyed after Sauron's defeat against Isildur, and began to be rebuilt in T.A. 2951."} },
            ]
        }
    ],
    events: [
        {
            name: "Battles",
            category: "Battles",
            pins: [
                { coords: [555, 275], popup: {title: "Battle of Bywater", date: "[November 3, T.A. 3019]", description: "The Battle of Bywater was a battle for control of the Shire and the final battle of the War of the Ring. After he fleed from the Battle of Isengard, Saruman took control over the Shire with a band of ruffians. When Frodo and his companions returned from the Coronation of Elessar, they rallied the hobbits wanting to resist and defeated the ruffians, then confronted Saruman. Wormtongue killed Saruman and was shot dead by the hobbits."} },
                { coords: [630, 678], popup: {title: "Battle of Five Armies", date: "[November 23, T.A. 2941]", description: "The five warring parties were the Goblins and the Wargs against Men, Elves and Dwarves on and near the Lonely Mountain."} },
                { coords: [345, 450], popup: {title: "Battle of Isengard", date: "[3 March, T.A. 3019]", description: "Spurred on by Meriadoc Brandybuck and Peregrin Took, the Ents, followed by Huorns, invaded the Ring of Isengard from Fangorn Forest. It led the the drowning of Isengard and the defeat of Saruman."} },
                { coords: [305, 485], popup: {title: "Battle of the Hornburg", date: "[3-4 March, T.A. 3019]", description: "The Battle of the Hornburg took place at the mountain fortress of the Hornburg in the valley of Helm's Deep in Rohan. Taking place over the night of the 3-4 March T.A. 3019, it saw the attacking Uruk-hai of Saruman defeated by the Rohirrim led by Théoden and Erkenbrand."} },
                { coords: [230, 656], popup: {title: "Battle of Pelennor Fields", date: "[15 March, T.A. 3019]", description: "The Battle of the Pelennor Fields was the greatest battle of the War of the Ring. This battle saw the siege of Minas Tirith by Mordor's troops widely outnumbering the defenders, but resulted in the loss of Sauron's armies after the Witch King was killed in combat."} },
                { coords: [310, 680], popup: {title: "Battle of Dagorlad", date: "[3434 of the Second Age]", description: "The Battle of Dagorlad was fought between the army of the Last Alliance under Gil-galad and Elendil and an army of Orcs and other creatures loyal to Sauron."} },
                { coords: [300, 690], popup: {title: "Battle of the Morannon", date: "[25 March, T.A. 3019]", description: "The Battle of the Morannon was the last major battle against Sauron in the War of the Ring, fought at the Black Gate of Mordor on 25 March T.A. 3019. The army of the West, 6,000 strong by now, led by Aragorn marched on the gate as a diversionary feint to distract Sauron's attention from Frodo and Sam, who were carrying the One Ring through Mordor. It was hoped that Sauron would think Aragorn had the Ring and was now trying to use it to overthrow Mordor."} },

            ]
        },
        {
            name: "Deaths",
            category: "Deaths",
            pins: [
                { coords: [618, 683], popup:  {title: "Thorin, Fíli and Kíli", date: "[November 23, T.A. 2941]", description: "When Bilbo regained consciousness, the battle was already over. Thorin II Oakenshield had been mortally wounded on the field, and his nephews Fíli and Kíli died defending him as he lay on the ground."} },
                { coords: [632, 685], popup: {title: "Smaug", date: "[November 1, T.A. 2941]", description: "Bard fired a Black Arrow into the vulnerable spot on the dragon's belly. Roaring in fury and pain, Smaug fell from the sky and plummeted into the flaming ruins of Lake-town, his death marked the end of the great dragons in Middle-earth."} },
                { coords: [474, 497], popup: {title: "Gandalf the Grey", date: "[January 25, T.A. 3019]", description: "Gandalf pursued the Balrog from the deepests dungeons of Moria to Durin's Tower, climbing through the whole Endless Stair, where they fought for three days and two nights. In the end, the Balrog was cast down and it broke the mountain-side as it fell. Gandalf himself died following this ordeal, but was later sent back to Middle-earth with even greater powers as Gandalf the White."} },
                { coords: [300, 605], popup: {title: "Boromir", date: "[February 26, T.A. 3019]", description: "Boromir died at Amon Hen, the westernmost of the three peaks at the southern end of Nen Hithoel. He perished trying to defend Merry and Pippin from Saruman's Orcs, slaying at least 20 of them before perishing after being hit by many arrows."} },
            ]
        },
        {
            name: "Encounters",
            category: "Encounters",
            pins: [
                { coords: [540, 305], popup: {title: "Old Man Willow", date: "[September 26, T.A. 3018]", description: "Old Man Willow was a willow tree in the Old Forest, who might have been an Ent who had become tree-like, or possibly a Huorn. Old Man Willow cast a spell on the Hobbits, Frodo, Sam, Merry and Pippin, causing them to fall asleep and trying to kill them. They were saved by the timely arrival of Tom Bombadil who knew 'the tune for him'."} },
                { coords: [544, 309], popup: {title: "Tom Bombadil", date: "[September 26, T.A. 3018]", description: "Tom Bombadil, a mysterious creature living in the Dark Forst with his wife Goldberry, saved Frodo, Sam, Merry and Pippin from the Old Man Willow, an evil willow who cast a spell on them and trapped Merry and Pippin. He then hosted the hobbits for two nights, during which he told them many tales and songs."} },
                { coords: [540, 325], popup: {title: "Barrow-wights", date: "[September 28, T.A. 3018]", description: "The Barrow-wights were a kind of undead-like creatures, dead bones animated by evil spirits. Frodo, Sam, Merry an Pippin were trapped in the Barrow-downs by the spells of the Barrow-wights, and were nearly slain by the creatures. They were saved in the last minute by Tom, who seemed to have had complete authority over them."} },
                { coords: [570, 455], popup: {title: "Stone Trolls", date: "[May 28, T.A. 2941]", description: "Three Stone Trolls (William, Tom and Bert) captured Bilbo and the Company of Thorin. Thanks to Gandalf who tricked them, they kept fighting over how to cook the dwarves until the sun set up, frozing them into stone statues."} },
                { coords: [588, 530], popup: {title: "Bilbo steals the Ring from Gollum", date: "[July 12, T.A. 2941]", description: "Bilbo picked up a strange golden ring in the dark passages under Goblin-town. He then met Gollum whom defied him to a riddle contest for his life. Bilbo won, but then Gollum went to get his magic ring to kill him anyway. He then discovered that his ring was missing, and understood that Bilbo took it. He chased Bilbo, but Bilbo unwittingly used the ring and escaped his notice."} },
                { coords: [605, 650], popup: {title: "Giant Spiders", date: "[August, T.A. 2941]", description: "Giant spiders (Ungolianth's spawns) managed to capture and entangle in webs each of the thirteen Dwarves. Only Bilbo's magic Ring and his Elven blade Sting allowed them to escape from being eaten, before being captured by Thranduil's elves."} },
                { coords: [370, 490], popup: {title: "Merry and Pippin meet Treebeard", date: "[February 29, T.A. 3019]", description: "Treebeard discovered Merry and Pippin in Fangorn Forest after they escaped from Saruman's Orcs, and welcomed them to the WellingHall."} },
                { coords: [240, 690], popup: {title: "Shelob", date: "[March 12, T.A. 3019]", description: "Shelob was born as the last child of the spider-like demon Ungoliant. On March 12 T.A. 3019, Gollum led Sam and Frodo into the tunnels of Shelob's Lair and abandoned them in the dark. He planned that Shelob would eat Sam and Frodo so that he could find the One Ring among the bones and clothes."} },
                { coords: [563, 495], popup: {title: "Council of Elrond", date: "", description: ""} },
                { coords: [440, 532], popup: {title: "Galadriel and Celeborn", date: "", description: ""} },

            ]
        }
    ]
};

const layers = { quests: {}, places: {}, events: {}, paths: {} };

function addQuestMarkers() {
    const icons = {
        hobbits: L.icon({
            iconUrl: 'hobbits.svg',
            iconSize: [32, 32],
            iconAnchor: [16, 32],
            popupAnchor: [0, -32]
        }),
        elves: L.icon({
            iconUrl: 'elves.svg',
            iconSize: [32, 32],
            iconAnchor: [16, 32],
            popupAnchor: [0, -32]
        }),
        dwarves: L.icon({
            iconUrl: 'dwarves.svg',
            iconSize: [32, 32],
            iconAnchor: [16, 32],
            popupAnchor: [0, -32]
        }),
        humans: L.icon({
            iconUrl: 'humans.svg',
            iconSize: [32, 32],
            iconAnchor: [16, 32],
            popupAnchor: [0, -32]
        }),
        evil: L.icon({
            iconUrl: 'evil.svg',
            iconSize: [32, 32],
            iconAnchor: [16, 32],
            popupAnchor: [0, -32]
        }),
        death: L.icon({
            iconUrl: 'death.svg',
            iconSize: [32, 32],
            iconAnchor: [16, 32],
            popupAnchor: [0, -32]
        }),
        battle: L.icon({
            iconUrl: 'battle.svg',
            iconSize: [32, 32],
            iconAnchor: [16, 32],
            popupAnchor: [0, -32]
        }),
        encounter: L.icon({
            iconUrl: 'encounter.svg',
            iconSize: [32, 32],
            iconAnchor: [16, 32],
            popupAnchor: [0, -32]
        })
    };
    
    mapData.quests.forEach(quest => {
        const questGroup = [];

        quest.pins.forEach(pin => {
            const icon = icons[pin.iconType] || icons.humans;
            const popupContent = `
                <div class="popup-content">
                    <h3>${pin.popup.title}</h3>
                    <div class="popup-divider"></div>
                    <h4>${pin.popup.date}</h4>
                    <p>${pin.popup.description}</p>
                </div>
            `;
            const marker = L.marker(pin.coords, { icon }).bindPopup(popupContent);
            questGroup.push(marker);
        });
        layers.quests[quest.category] = questGroup;
    });
    layers.quests["All"] = Object.values(layers.quests).flat();
};


function addPlaceMarkers() {
    const icons = {
        Humans: L.icon({
            iconUrl: 'humans.svg',
            iconSize: [32, 32],
            iconAnchor: [16, 32],
            popupAnchor: [0, -32]
        }),
        Elves: L.icon({
            iconUrl: 'elves.svg',
            iconSize: [32, 32],
            iconAnchor: [16, 32],
            popupAnchor: [0, -32]
        }),
        Dwarves: L.icon({
            iconUrl: 'dwarves.svg',
            iconSize: [32, 32],
            iconAnchor: [16, 32],
            popupAnchor: [0, -32]
        }),
        Hobbits: L.icon({
            iconUrl: 'hobbits.svg',
            iconSize: [32, 32],
            iconAnchor: [16, 32],
            popupAnchor: [0, -32]
        }),
        Evil: L.icon({
            iconUrl: 'evil.svg',
            iconSize: [32, 32],
            iconAnchor: [16, 32],
            popupAnchor: [0, -32]
        })
    };
    
    mapData.places.forEach(place => {
        const placeGroup = [];

        place.pins.forEach(pin => {
            const icon = icons[place.category] || icons.Other;
            const popupContent = `
                <div class="popup-content">
                    <h3>${pin.popup.title}</h3>
                    <div class="popup-divider"></div>
                    <p>${pin.popup.description}</p>
                </div>
            `;
            const marker = L.marker(pin.coords, { icon }).bindPopup(popupContent);
            placeGroup.push(marker);
        });
        layers.places[place.category] = placeGroup;
    });
    layers.places["All"] = Object.values(layers.places).flat();
};

function addEventMarkers() {
    const icons = {
        Deaths: L.icon({
            iconUrl: 'death.svg',
            iconSize: [32, 32],
            iconAnchor: [16, 32],
            popupAnchor: [0, -32]
        }),
        Battles: L.icon({
            iconUrl: 'battle.svg',
            iconSize: [32, 32],
            iconAnchor: [16, 32],
            popupAnchor: [0, -32]
        }),
        Encounters: L.icon({
            iconUrl: 'encounter.svg',
            iconSize: [32, 32],
            iconAnchor: [16, 32],
            popupAnchor: [0, -32]
        })
    };

    mapData.events.forEach(event => {
        const eventGroup = [];

        event.pins.forEach(pin => {
            const icon = icons[event.category] || icons.Other;
            const popupContent = `
                <div class="popup-content">
                    <h3>${pin.popup.title}</h3>
                    <div class="popup-divider"></div>
                    <h4>${pin.popup.date}</h4>
                    <p>${pin.popup.description}</p>
                </div>
            `;
            const marker = L.marker(pin.coords, { icon }).bindPopup(popupContent);
            eventGroup.push(marker);
        });
        layers.events[event.category] = eventGroup;
    });
    layers.events["All"] = Object.values(layers.events).flat();
};

function toggleLayer(groupKey, category, show) {
    const group = layers[groupKey][category];
    if (!group) return;
    group.forEach(marker => {
        if (show) {
            marker.addTo(map);
        } else {
            map.removeLayer(marker);
        }
    });
};

function addPathOverlays() {
    mapData.paths.forEach(path => {
        const svgOverlay = L.imageOverlay(path.file, bounds);
        layers.paths[path.category] = svgOverlay;
    });
    layers.paths["All"] = mapData.paths.map(path => layers.paths[path.category]);
};

function togglePath(category, show) {
    const layer = layers.paths[category];
    if (!layer) return;
    if (Array.isArray(layer)) {
        layer.forEach(subLayer => {
            if (show) {
                subLayer.addTo(map);
            } else {
                map.removeLayer(subLayer);
            }
        });
    } else {
        if (show) {
            layer.addTo(map);
        } else {
            map.removeLayer(layer);
        }
    }
};

document.querySelectorAll('#sidebar input[type="checkbox"]').forEach(input => {
    input.addEventListener('change', function () {
        const groupKey = this.closest('ul').previousElementSibling.textContent.toLowerCase();
        const category = this.value;
        const show = this.checked;
        if (groupKey === 'paths') {
            togglePath(category, show);
        } else {
            toggleLayer(groupKey, category, show);
        }
    });
});

const sidebar = document.getElementById('sidebar');
const toggleButton = document.getElementById('toggle-sidebar');

toggleButton.addEventListener('click', () => {
    sidebar.classList.toggle('collapsed');
    toggleButton.classList.toggle('collapsed');

    if (sidebar.classList.contains('collapsed')) {
        toggleButton.textContent = '>'; 
    } else {
        toggleButton.textContent = '<'; 
    }
});


addPathOverlays();
addQuestMarkers();
addPlaceMarkers();
addEventMarkers();

