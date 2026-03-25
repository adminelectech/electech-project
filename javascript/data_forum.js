const forumQuestions = [
    {
        id: 1,
        category: "Maintenance",
        tags: ["#Maintenance", "#Moteur"],
        title: "Problème de couple sur un moteur asynchrone triphasé au démarrage étoile-triangle ?",
        description: "J'ai un moteur de 45kW qui peine à s'élancer en couplage étoile, ce qui provoque un appel de courant trop important au passage en triangle. Des conseils sur le réglage de la temporisation ou une autre solution ?",
        author: "Jean-Marc. D",
        date: "Il y a 2 heures",
        responses: [
            {
                author: "ExpertElec",
                date: "Il y a 1 heure",
                content: "Vérifiez si le couple résistant de la charge n'est pas trop élevé au démarrage. Un démarrage étoile-triangle ne fournit que 1/3 du couple nominal."
            },
            {
                author: "TechIndustrie",
                date: "Il y a 30 min",
                content: "Peut-être envisager un démarreur progressif (soft-starter) si le réseau le permet."
            }
        ]
    },
    {
        id: 2,
        category: "Électricité BTP",
        tags: ["#ÉlectricitéBTP", "#Solaire"],
        title: "Quelle section de câble DC conseilleriez-vous pour une installation de 6kW sur 25m ?",
        description: "Je prévois d'installer 16 panneaux de 375W. La distance entre le champ PV et l'onduleur est de 25 mètres. Quelle section pour limiter les pertes à moins de 1% ?",
        author: "Inès Tech",
        date: "Hier à 18:30",
        responses: [
            {
                author: "SolaireMaster",
                date: "Hier à 19:15",
                content: "Pour 6kW (environ 15A sous 400V DC), du 6mm² devrait suffire, mais du 10mm² sécurisera les pertes sur 25m."
            }
        ]
    },
    {
        id: 3,
        category: "Électricité BTP",
        tags: ["#ÉlectricitéBTP", "#Normes"],
        title: "Interprétation de la norme sur le type de DDR pour une borne de recharge VE ?",
        description: "Est-on obligé de poser un DDR de type B ou un type A '7mA' est-il suffisant si la borne intègre déjà une protection contre les courants de fuite DC ?",
        author: "Expert83",
        date: "23 Mars 2026",
        responses: []
    },
    {
        id: 4,
        category: "Autre",
        tags: ["#Électronique", "#Composants"],
        title: "Remplacement d'un condensateur de filtrage sur une alimentation à découpage.",
        description: "J'ai un condensateur gonflé de 470µF 35V. Puis-je le remplacer par un 680µF 50V ?",
        author: "BricoloElec",
        date: "22 Mars 2026",
        responses: [
            {
                author: "CompoFix",
                date: "22 Mars 2026",
                content: "Oui, la tension plus élevée est une sécurité, et la capacité légèrement supérieure aidera au filtrage sans risque majeur ici."
            }
        ]
    },
    {
        id: 5,
        category: "Automatisme",
        tags: ["#Automatisme", "#KNX"],
        title: "Problème d'adressage de participants sur un bus KNX.",
        author: "Domotechs",
        date: "21 Mars 2026",
        description: "Impossible d'adresser le 4ème module de sortie. Le voyant de programmation reste éteint.",
        responses: []
    },
    {
        id: 6,
        category: "Maintenance",
        tags: ["#Maintenance", "#Moteur"],
        title: "Comment tester l'isolement d'un moteur sans mégohmmètre ?",
        author: "Apprenti75",
        date: "20 Mars 2026",
        description: "Je suis en dépannage et j'ai oublié mon testeur d'isolement. Y a-t-il une astuce fiable ?",
        responses: [
            {
                author: "VieuxDeLaVieille",
                date: "20 Mars 2026",
                content: "Difficile d'avoir une mesure fiable sans appareil dédié. Un multimètre en position Ohms ne verra que les courts-circuits francs."
            }
        ]
    },
    {
        id: 7,
        category: "Autre",
        tags: ["#Énergie", "#Éolien"],
        title: "Rendement d'une micro-éolienne en milieu urbain.",
        author: "EcoVille",
        date: "19 Mars 2026",
        description: "Est-ce rentable d'installer une éolienne de pignon en centre-ville ?",
        responses: []
    },
    {
        id: 8,
        category: "Maintenance",
        tags: ["#Maintenance", "#Sécurité"],
        title: "Validité des gants isolants classe 00.",
        author: "SafetyFirst",
        date: "18 Mars 2026",
        description: "Quelle est la durée de vie réelle après la première utilisation ?",
        responses: []
    },
    {
        id: 9,
        category: "Maintenance",
        tags: ["#Maintenance", "#Outillage"],
        title: "Quel VAT choisir pour le milieu industriel ?",
        author: "IndusElec",
        date: "17 Mars 2026",
        description: "Je cherche un VAT robuste avec test de continuité et rotation de phase.",
        responses: []
    },
    {
        id: 10,
        category: "CAO / DAO",
        tags: ["#CAO/DAO", "#Logiciel"],
        title: "Alternative gratuite à AutoCAD Electrical ?",
        author: "JuniorDesigner",
        date: "16 Mars 2026",
        description: "Je cherche un logiciel open source pour réaliser des schémas de puissance.",
        responses: [
             {
                author: "FreeEngineer",
                date: "16 Mars 2026",
                content: "QElectroTech est excellent pour ça !"
            }
        ]
    },
    {
        id: 11,
        category: "Autre",
        tags: ["#Éclairage", "#LED"],
        title: "Pourquoi mes spots LED clignotent-ils légèrement lorsqu'ils sont éteints ?",
        author: "Lumens",
        date: "15 Mars 2026",
        description: "J'ai remplacé mes halogènes par des LED et j'observe un léger scintillement résiduel la nuit.",
        responses: []
    }
];
