import type { Name } from "types";
import lauraTan from "./photos/laura-tan.jpg";
import kylaChristenson from "./photos/CCL_christenson.jpg";
import jeremySeidner from "./photos/CH_seidner.jpg";
import katjaKlosterman from "./photos/CCL_klosterman.jpg";
import danikaFlemming from "./photos/CH_fleming.jpg";
import karunaPyle from "./photos/CH_pyle.jpg";
import safaAwadalla from "./photos/no_img.gif";
import susiePuga from "./photos/CCL_puga.jpg";
import kelseyAtcheson from "./photos/CH_atcheson.jpg";
import juliaGarcia from "./photos/CH_garcia.jpg";
import lorenaAustin from "./photos/CH_austin.jpg";
import danielHoop from "./photos/CCL_hoop.jpg";
import drewHackmann from "./photos/CH_hackmann.jpg";
import elizabethMichael from "./photos/CH_michael.jpg";
import adamThompson from "./photos/LI_thompson.jpg";
import mckennaByrne from "./photos/LI_byrne.jpg";
import lurissaCarbajal from "./photos/LI_carbajal.jpg";
import madelineJones from "./photos/no_img.gif";
import cameronJanda from "./photos/MT_janda.jpg";
import morgenJohnson from "./photos/MT_johnsonM.jpg";
import davidAxton from "./photos/MT_axton.jpg";
import trucDoan from "./photos/SL_doan.jpg";
import toriVandekop from "./photos/MT_vandekop.jpg";
import stephanieRodriguez from "./photos/MT_rodriguez.jpg";
import elenaAlsen from "./photos/MT_alsen.jpg";
import kennySilverstro from "./photos/SL_silvestro.jpg";
import ibukunOluyi from "./photos/MT_oluyi.jpg";
import devanPratt from "./photos/MT_pratt.jpg";
import christopherJoseph from "./photos/MT_joseph.jpg";
import bryanBernal from "./photos/SL_bernal.jpg";
import edenochoaRamos from "./photos/MT_ochoa.jpg";
import charlotteSandy from "./photos/MT_sandy.jpg";
import elliotWasbotten from "./photos/MT_wasbotten.jpg";
import amandaAriola from "./photos/SL_ariola.jpg";
import ciaraHarding from "./photos/MT_harding.jpg";
import annaSchmidt from "./photos/MT_schmidt.jpg";
import cassidySlusser from "./photos/MT_slusser.jpg";
import malloryJudd from "./photos/SL_judd.jpg";
import jazmyneLandes from "./photos/MT_landes.jpg";
import josieBrzenk from "./photos/MT_brzenk.jpg";
import julieKaplan from "./photos/MT_kaplan.jpg";
import rosalindNguyen from "./photos/SL_nguyen.jpg";
import lucyPrimiano from "./photos/MT_primiano.jpg";
import akhilJohnson from "./photos/MT_johnsonA.jpg";
import anaAvila from "./photos/MT_avila.jpg";
import haileyCampbell from "./photos/SL_campbell.jpg";
import consueloArroyo from "./photos/MT_arroyo.jpg";
import nickLoquercio from "./photos/MT_loquercio.jpg";
import rachelSpencer from "./photos/MT_spencer.jpg";
import williamAtkin from "./photos/SL_atkin.jpg";
import taylorWarwick from "./photos/MT_warwick.jpg";
import johnJanezic from "./photos/MT_janezic.jpg";
import carlosZamora from "./photos/MT_zamora.jpg";
import cyrusCommissariat from "./photos/SL_commissariat.jpg";
import kahriHarrion from "./photos/MT_harrion.jpg";
import ruthOliver from "./photos/MT_oliver.jpg";
import alexandraMooney from "./photos/MT_mooney.jpg";



export type BioType = {
  name: Name,
  position: string,
  email: string,
  pictureURL: string
};

export type BioGroupType = {
  group: string,
  bios: Array<BioType>
};

export const bioGroupsData: Array<BioGroupType> = [
  {
    group: "Professional Staff",
    bios: [
      {
        name: {
          first: "Brett",
          last: "Hunt"
        },
        position: "Executive Director",
        email: "brett.hunt@asu.edu",
        pictureURL: "http://mtaguild.org/wp-content/uploads/2017/03/Hunt.jpg"
      },
      {
        name: {
          first: "Laura",
          last: "Tan"
        },
        position: "Community Engagement Manager",
        email: "laura.tan@asu.edu",
        pictureURL: lauraTan
      },
      {
        name: {
          first: "Veronica",
          last: "Gutierrez"
        },
        position: "Curriculum and Course Manager",
        email: "veronica.gutierrez@asu.edu",
        pictureURL:
          "https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/31172232_10109489507961871_8004704684709249024_n.jpg?_nc_cat=0&oh=3ae84ab9f331bffdfeab4201fcf3cbd4&oe=5C377024"
      },
      {
        name: {
          first: "Kim",
          last: "Baldwin"
        },
        position: "Program Coordinator",
        email: "Kim.Baldwin@asu.edu",
        pictureURL:
          "https://scontent-lax3-2.xx.fbcdn.net/v/t1.0-9/29683676_10155792499042599_30777052938256661_n.jpg?_nc_cat=0&oh=f5aa35d2b7fb1fb6a023d90c486ee72c&oe=5BB44D14"
      },
      {
        name: {
          first: "Martin",
          last: "Cordova-Paredes"
        },
        position: "Project Coordinator",
        email: "Martin.Cordovaparedes@asu.edu",
        pictureURL:
          "https://webapp4.asu.edu/photo-ws/directory_photo/1823164?size=large"
      }
    ]
  },
  {
    group: "Chief of Staff and Committee Leads",
    bios: [
      {
        name: {
          first: "Kyla",
          last: "Christenson"
        },
        position: "Chief of Staff",
        email: "Kyla.Christenson@asu.edu",
        pictureURL: kylaChristenson
      },
      {
        name: {
          first: "Katja",
          last: "Klosterman"
        },
        position: "Culture Lead",
        email: "katja.Klosterman@asu.edu",
        pictureURL: katjaKlosterman
      },
      {
        name: {
          first: "Daniel",
          last: "Hoop"
        },
        position: "Education Lead",
        email: "dhoop@asu.edu",
        pictureURL: danielHoop
      },
      {
        name: {
          first: "Susie",
          last: "Puga"
        },
        position: "Engagement Lead",
        email: "Susana.Puga@asu.edu",
        pictureURL: susiePuga
      }
    ]
  },
  {
    group: "Section Leads",
    bios: [
      {
        name: {
          first: "Madeline",
          last: "Jones"
        },
        position: "Section 1",
        email: "mfjones5@asu.edu",
        pictureURL: madelineJones
      },
      {
        name: {
          first: "Truc",
          last: "Doan"
        },
        position: "Section 2",
        email: "tldoan@asu.edu",
        pictureURL: trucDoan
      },
      {
        name: {
          first: "Kenny",
          last: "Silvestro"
        },
        position: "Section 3",
        email: "kenny.silvestro@asu.edu",
        pictureURL: kennySilverstro
      },
      {
        name: {
          first: "Bryan",
          last: "Bernal"
        },
        position: "Section 4",
        email: "Bryan.Bernal@asu.edu",
        pictureURL: bryanBernal
      },
      {
        name: {
          first: "Amanda",
          last: "Ariola"
        },
        position: "Section 5",
        email: "Amanda.Ariola@asu.edu",
        pictureURL: amandaAriola
      },
      {
        name: {
          first: "Mallory",
          last: "Judd"
        },
        position: "Section 6",
        email: "Mallory.Tibbitts@asu.edu",
        pictureURL: malloryJudd
      },
      {
        name: {
          first: "Rosalind",
          last: "Nguyen"
        },
        position: "Section 7",
        email: "Rosalind.Nguyen@asu.edu",
        pictureURL: rosalindNguyen
      },
      {
        name: {
          first: "Hailey",
          last: "Campbell"
        },
        position: "Section 8",
        email: "Hailey.Campbell@asu.edu",
        pictureURL: haileyCampbell
      },
      {
        name: {
          first: "William",
          last: "Atkin"
        },
        position: "Section 9",
        email: "William.Atkin@asu.edu",
        pictureURL: williamAtkin
      },
      {
        name: {
          first: "Cyrus",
          last: "Commissariat"
        },
        position: "Section 10",
        email: "ccommiss@asu.edu",
        pictureURL: cyrusCommissariat
      }
    ]
  },
  {
    group: "Committee Chairs",
    bios: [
      {
        name: {
          first: "Jeremy",
          last: "Seidner"
        },
        position: "Admin Chair",
        email: "jseidne@asu.edu",
        pictureURL: jeremySeidner
      },
      {
        name: {
          first: "Drew",
          last: "Hackmann"
        },
        position: "Ambassadors Chair",
        email: "ehackma1@asu.edu",
        pictureURL: drewHackmann
      },
      {
        name: {
          first: "Kelsey",
          last: "Atcheson"
        },
        position: "Civil-Mil Chair",
        email: "katcheso@asu.edu",
        pictureURL: kelseyAtcheson
      },
      {
        name: {
          first: "Danika",
          last: "Flemming"
        },
        position: "Communications Chair",
        email: "drflemmi@asu.edu",
        pictureURL: danikaFlemming
      },
      {
        name: {
          first: "Karuna",
          last: "Pyle"
        },
        position: "Events Chair",
        email: "kbpyle@asu.edu",
        pictureURL: karunaPyle
      },
      {
        name: {
          first: "Julia",
          last: "Garcia"
        },
        position: "Service Chair",
        email: "jgarc143@asu.edu",
        pictureURL: juliaGarcia
      },
      {
        name: {
          first: "Safa",
          last: "Awadalla"
        },
        position: "Social Chair",
        email: "sawadall@asu.edu",
        pictureURL: safaAwadalla
      },
      {
        name: {
          first: "Elizabeth",
          last: "Michael"
        },
        position: "Training Chair",
        email: "Elizabeth.Michael@asu.edu",
        pictureURL: elizabethMichael
      },
      {
        name: {
          first: "Lorena",
          last: "Austin"
        },
        position: "Transfer Chair",
        email: "lmausti3@asu.edu",
        pictureURL: lorenaAustin
      }
    ]
  },
  {
    group: "Mission Teams",
    bios: [
      {
        name: {
          first: "Cameron",
          last: "Janda"
        },
        position: "MT 1 - Sexual & Domestic Violence",
        email: "cjanda@asu.edu",
        pictureURL: cameronJanda
      },
      {
        name: {
          first: "Morgen",
          last: "Johnson"
        },
        position: "MT 2 - Human Trafficking",
        email: "mejohn48@asu.edu",
        pictureURL: morgenJohnson
      },
      {
        name: {
          first: "David",
          last: "Axton"
        },
        position: "MT 3 - Gender Equality",
        email: "dfaxton@asu.edu",
        pictureURL: davidAxton
      },
      {
        name: {
          first: "Tori",
          last: "Van de Kop"
        },
        position: "MT 4 - Racial & LGBTQ Equality",
        email: "tvandekop@asu.edu",
        pictureURL: toriVandekop
      },
      {
        name: {
          first: "Stephanie",
          last: "Rodriguez"
        },
        position: "MT 5 - Immigration",
        email: "stephanie.a.rodriquez.1@asu.edu",
        pictureURL: stephanieRodriguez
      },
      {
        name: {
          first: "Elena",
          last: "Alsen"
        },
        position: "MT 6 - Cultural & Global Equality",
        email: "ealsen@asu.edu",
        pictureURL: elenaAlsen
      },
      {
        name: {
          first: "Ibukun",
          last: "Oluyi"
        },
        position: "MT 7 - Criminal Justice",
        email: "ioluyi@asu.edu",
        pictureURL: ibukunOluyi
      },
      {
        name: {
          first: "Devan",
          last: "Pratt"
        },
        position: "MT 8 - Security",
        email: "dcpratt1@asu.edu",
        pictureURL: devanPratt
      },
      {
        name: {
          first: "Christopher",
          last: "Joseph"
        },
        position: "MT 9 - Community Development",
        email: "cdjosep1@asu.edu",
        pictureURL: christopherJoseph
      },
      {
        name: {
          first: "Eden Ochoa",
          last: "Ramos"
        },
        position: "MT 10 - Youth Development",
        email: "eochoara@asu.edu",
        pictureURL: edenochoaRamos
      },
      {
        name: {
          first: "Charlotte ",
          last: "Sandy"
        },
        position: "MT 11 - Civic Engagement",
        email: "csandy@asu.edu",
        pictureURL: charlotteSandy
      },
      {
        name: {
          first: "Elliot",
          last: "Wasbotten"
        },
        position: "MT 12 - Disabilities & Empowerment",
        email: "ewasbott@asu.edu",
        pictureURL: elliotWasbotten
      },
      {
        name: {
          first: "Ciara",
          last: "Harding"
        },
        position: "MT 13 - Access to Healthcare",
        email: "chardin5@asu.edu",
        pictureURL: ciaraHarding
      },
      {
        name: {
          first: "Anna",
          last: "Schmidt"
        },
        position: "MT 14 - Access to Healthcare",
        email: "acschmid@asu.edu",
        pictureURL: annaSchmidt
      },
      {
        name: {
          first: "Cassidy",
          last: "Slusser"
        },
        position: "MT 15 - Veterans Healthcare & Services",
        email: "clusse1@asu.edu",
        pictureURL: cassidySlusser
      },
      {
        name: {
          first: "Jazmyne",
          last: "Landes"
        },
        position: "MT 16 - Public Health",
        email: "jslandes@asu.edu",
        pictureURL: jazmyneLandes
      },
      {
        name: {
          first: "Josie",
          last: "Brzenk"
        },
        position: "MT 17 - Mental Health",
        email: "jbrzenk@asu.edu",
        pictureURL: josieBrzenk
      },
      {
        name: {
          first: "Julie",
          last: "Kaplan"
        },
        position: "MT 18 - Mental Health",
        email: "jkaplan8@asu.edu",
        pictureURL: julieKaplan
      },
      {
        name: {
          first: "Lucy",
          last: "Primiano"
        },
        position: "MT 19 - Homelessness",
        email: "lprimia1@asu.edu",
        pictureURL: lucyPrimiano
      },
      {
        name: {
          first: "Akhil",
          last: "Johnson"
        },
        position: "MT 20 - Science, Technology, & Innovation",
        email: "agjohn13@asu.edu",
        pictureURL: akhilJohnson
      },
      {
        name: {
          first: "Ana",
          last: "Avila"
        },
        position: "MT 21 - Hunger & Nutrition",
        email: "agavila1@asu.edu",
        pictureURL: anaAvila
      },
      {
        name: {
          first: "Consuelo",
          last: "Arroyo"
        },
        position: "MT 22 - Environmental Sustainability",
        email: "carroyo3@asu.edu",
        pictureURL: consueloArroyo
      },
      {
        name: {
          first: "Nick",
          last: "Loquercio"
        },
        position: "MT 23 - Sustainability",
        email: "nioquerc@asu.edu",
        pictureURL: nickLoquercio
      },
      {
        name: {
          first: "Rachel",
          last: "Spencer"
        },
        position: "MT 24 - Animal Rights",
        email: "rmspenc2@asu.edu",
        pictureURL: rachelSpencer
      },
      {
        name: {
          first: "Taylor",
          last: "Warwick"
        },
        position: "MT 25 - Sustainability",
        email: "twarwic1@asu.edu",
        pictureURL: taylorWarwick
      },
      {
        name: {
          first: "John",
          last: "Janezic"
        },
        position: "MT 26 - Water Access & Sustainability",
        email: "jhjanezi@asu.edu",
        pictureURL: johnJanezic
      },
      {
        name: {
          first: "Carlos",
          last: "Zamora"
        },
        position: "MT 27 - Energy & Climate Sustainability",
        email: "cazamor1@asu.edu",
        pictureURL: carlosZamora
      },
      {
        name: {
          first: "Kahri",
          last: "Harrion"
        },
        position: "MT 28 - Education & Policy",
        email: "kharrion@asu.edu",
        pictureURL: kahriHarrion
      },
      {
        name: {
          first: "Ruth",
          last: "Oliver"
        },
        position: "MT 29 - Education",
        email: "rkoliver@asu.edu",
        pictureURL: ruthOliver
      },
      {
        name: {
          first: "Alexandra",
          last: "Mooney"
        },
        position: "MT 30 - Education",
        email: "amooney2@asu.edu",
        pictureURL: alexandraMooney
      }
    ]
  }
  {
    group: "Campus Liaisons",
    bios: [
      {
        name: {
          first: "Adam",
          last: "Thompson"
        },
        position: "Poly Campus Liaison",
        email: "Adam.Richard.Thompson@asu.edu",
        pictureURL: adamThompson
      },
      {
        name: {
          first: "McKenna",
          last: "Byrne"
        },
        position: "West Campus Liaison",
        email: "McKenna.Byrne@asu.edu",
        pictureURL: mckennaByrne
      },
      {
        name: {
          first: "Lurissa",
          last: "Carbajal"
        },
        position: "Downtown Campus Liaison",
        email: "lurissa.carbajal@asu.edu",
        pictureURL: lurissaCarbajal
      },
    ]
  }
];