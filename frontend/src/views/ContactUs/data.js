// @flow

import type {Name} from 'types'

export type BioType = {
  name: Name,
  position: string,
  email: string,
  pictureURL: string,
}

export type BioGroupType = {
  group: string,
  bios: Array<BioType>,
}

export const bioGroupsData: Array<BioGroupType> = [
  {
    group: 'Professional Staff',
    bios: [
      {
        name: {
          first: 'Brett',
          last: 'Hunt'
        },
        position: 'Executive Director',
        email: 'brett.hunt@asu.edu',
        pictureURL: 'https://media.licdn.com/dms/image/C4E03AQEZhdBD_g71lw/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=PtxvyFt752cYRK8T5-_UBt0Zm0OmAwwuIqTmRszARpw'
      },
      {
        name: {
          first: 'Jessica',
          last: 'Eldridge'
        },
        position: 'Assistant Director',
        email: 'jessica.eldridge@asu.edu',
        pictureURL: 'https://media.licdn.com/dms/image/C5603AQFZodEmhbZklg/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=2RTWz6XPLTfkwe8JJboA8QhJkWUKZaAGzLXqgjfpqDY'
      },
      {
        name: {
          first: 'Laura',
          last: 'Tan'
        },
        position: 'Community Engagement Coordinatpr',
        email: 'laura.tan@asu.edu',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/295423_262292843879255_1708700154_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeFW7Njp6Oo410Y3OccOqDLNPjTK6XWuxt0xsVggoxoC1jEtRoEe8uHFowAMrhYlIRXuGFg14lu8gsjd094xw5hoATCtVvoJvgIbh6VprVr53g&oh=ecb8929f3e4202b2ad8dbef7017cb21b&oe=5B344FA3'
      },
      {
        name: {
          first: 'Veronica',
          last: 'Gutierrez'
        },
        position: 'Curriculum and Course Manager',
        email: 'veronica.gutierrez@asu.edu',
        pictureURL: 'https://scontent.fphx1-1.fna.fbcdn.net/v/t31.0-8/26678217_10109089048805231_1239174116842371196_o.jpg?oh=d353c7b96da89b13b54e5cf4791f8bc0&oe=5B09F765'
      }
    ]
  },
  {
    group: 'Chief of Staff and Committee Leads',
    bios: [
      {
        name: {
          first: 'Kara',
          last: 'Lehman'
        },
        position: 'Chief of Staff',
        email: '',
        pictureURL: 'https://media.licdn.com/dms/image/C5103AQEg_3HmNMpWaQ/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=N8xvwwupgSVbciIHWMoS_lpSeHaWmpNuU1kLnTycdO4'
      },
      {
        name: {
          first: 'David',
          last: 'Huff'
        },
        position: 'Culture',
        email: '',
        pictureURL: 'https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/24993450_1202445663222249_5173404211670915679_n.jpg?oh=c93352a8342a2ab947679bd03a6eb5b4&oe=5B16F9B5'
      },
      {
        name: {
          first: 'Adam',
          last: 'Thompson'
        },
        position: 'Education',
        email: '',
        pictureURL: 'https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/27750841_1452239774905278_109012201486380910_n.jpg?oh=3d4239d32c9776c1627cb9a634b996de&oe=5B2637CD'
      },
      {
        name: {
          first: 'Matthew',
          last: 'Moy'
        },
        position: 'Engagement',
        email: '',
        pictureURL: 'https://media.licdn.com/dms/image/C5603AQG9-vhumjBmdw/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=6pvItHDToctRCuVc5BTvfiUBQRCXrEZiAXAlv8ePk7Q'
      },
      ]
  },
  {
    group: 'Section Leads',
    bios: [
      {
        name: {
          first: 'Savanna',
          last: 'Soldevere'
        },
        position: 'Section 1',
        email: '',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/28795721_1675923255835460_7141392406632362971_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeEpjJ1OfO0bPf1i8mPyTzO0zrGLksLYVwrdmGfdfyt1XGUVmEULbXYNme-_m5hxwqfikPDV80s93qexPWBugBkYbAvT2LBKge6KzuwC3v6J-A&oh=aa50a19681781a152842821af20f0d37&oe=5B65CE2B'
      },
      {
        name: {
          first: 'Truc',
          last: 'Doan'
        },
        position: 'Section 2',
        email: '',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t31.0-8/25073085_10208142107589059_8061053466842241584_o.jpg?_nc_cat=0&_nc_eui2=v1%3AAeGbOe7zKtxBjpoocbyfKhSTZwOuzBcp0ptHVEeHm5_tLBCdwlaT3rAgFTIkFXPr27cnYGHzmL--VNrop-Z1qge3HWP3TAkCfbkOFXi5wheAGg&oh=15edd1bdc7cd4cf3d659526f1826e5d7&oe=5B6C30A2'
      },
      {
        name: {
          first: 'Jordan',
          last: 'Paul'
        },
        position: 'Section 3',
        email: '',
        pictureURL: 'https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/19657283_1413556345397037_2967285048553981257_n.jpg?oh=160501d7b1e20531f6f73f5b59ba5b66&oe=5B08FDD0'
      },
      {
        name: {
          first: 'Emma',
          last: 'Sounart'
        },
        position: 'Section 4',
        email: '',
        pictureURL: 'https://media.licdn.com/dms/image/C5603AQHdyVxgfrh7UA/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=EPwks-Vy0I2gKo5Oj7prZVA8hK-aTkU0tiB8zhpsm-k'
      },
      {
        name: {
          first: 'Katja',
          last: 'Klosterman'
        },
        position: 'Section 5',
        email: '',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t31.0-8/21640745_276439699512702_8691988110552036578_o.jpg?_nc_cat=0&_nc_eui2=v1%3AAeG2u-3dt7A_az0O4gzTci7_nv6XF4HLhKybkgSzNDStx_-ARdDo4zZ-0_AYukrfv63q-iED0htUUQ2wc-FoooBiIOfUN04EntwLXmvymJpe7A&oh=cab16e617938a50dc1d82bc7faf8376b&oe=5B304F30'
      },
      {
        name: {
          first: 'Marianna',
          last: 'Peña'
        },
        position: 'Section 6',
        email: '',
        pictureURL: 'https://media.licdn.com/dms/image/C4D03AQEgu8rLnSkEQg/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=LzzqiO7P_L30ZaCSzrUlWmetay7BaEN_cDmG6DXKGGk'
      },
      {
        name: {
          first: 'Andrea',
          last: 'Arellano'
        },
        position: 'Section 7',
        email: '',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/29792700_1086979038111957_2769352569781246734_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeHbCd1O3Zbon-S0SR5_k7ORTR8W38MMXhIPFhxqrYQgDFSZNP52sfLYBQizNW04w5EZuWpaaNbutGv1nZr51hCxoEO-1uRYbxQlZK61mDkQjA&oh=0c3b699e4e1a4955e7b1851d0544dd07&oe=5B664505'
      },
      {
        name: {
          first: 'Jacob',
          last: 'Ragsdale'
        },
        position: 'Section 8',
        email: '',
        pictureURL: ''
      },
      {
        name: {
          first: 'Samantha',
          last: 'Stone'
        },
        position: 'Section 9',
        email: '',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/15747557_1292463974147727_4193737941078067186_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeHuFCpm6PPhiFIHVACNZQOnskr0AqDu4aGdwZSgE-Gp9g8QGQYy87axZB9qRQiSgcBj53edQQDetGFYZsx8-Ov7xdKgo24Cx1vacnrYLZ7eYA&oh=96578ee475e8cce4f8053e6f2444cdc8&oe=5B35DDC2'
      },
      {
        name: {
          first: 'Maddie',
          last: 'Arnold'
        },
        position: 'Section 10',
        email: '',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/15107444_1612269835454493_2333612002911913476_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeGKfLEXIMpd0Bbu0C41rdDBCy4yp3SXdMX5cdwl5podXBNCXlm6F2rA1fpvaefiQm22R7CLJsFBBhal1WBbS8WSACWRtiXYjFNrppfxX9Mgiw&oh=25ee0fe9fc8d8d1a80cb573f962a5f86&oe=5B680FB9'
      },
    ]
  },
  {
    group: 'Committee Chairs',
    bios: [
      {
        name: {
          first: 'Jeremy',
          last: 'Seidner'
        },
        position: 'Admin Chair',
        email: '',
        pictureURL: 'https://media.licdn.com/dms/image/C5603AQGledn5coGyVw/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=xVjDZW-qa651bieLyMI5R5NYJWuJjlgExQA_yKcTSJQ'
      },
      {
        name: {
          first: 'Drew',
          last: 'Hackmann'
        },
        position: 'Ambassadors Chair',
        email: '',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/16831977_1867537380189704_7874044308575759814_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeH3NySFx2GnOeXTEmZHlTe9QWa7mgPvvKm_yTFH7A33rpuTIpOaADc5YeeTVzzjv009bQa6TCTWOB3LQVy-i90DhekS-OWBpOpjsh-Z40dCyQ&oh=d2d33a9df39049d2a545e5785a568149&oe=5B2A395A'
      },
      {
        name: {
          first: 'Breanna',
          last: 'Wright'
        },
        position: 'Civil-Mil Chair',
        email: '',
        pictureURL: 'https://media.licdn.com/dms/image/C5603AQG1Q0pMozaYcg/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=ntZBsTmCahfu_khTskVx_3AtXvgkmca_JpUj64z1lhE'
      },
      {
        name: {
          first: 'Sara',
          last: 'Neves Perez'
        },
        position: 'Communications Chair',
        email: '',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/19060026_10212235284504635_4234299516823943275_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeFZV6sCWBusApiI7pYoAyILFL9YB-k4lrnaaLjiBw4YaJ1twcrQI1_VgOaM3Jnnz780BFGnn30F3uFHQVjZ1aM48Z3UB-ST9raAWhDcEPEwcA&oh=aa57ec0ef4a06373ea8686aed3bcdfc1&oe=5B362EC1'
      },
      {
        name: {
          first: 'Justin',
          last: 'Rainge'
        },
        position: 'Events Chair',
        email: '',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t31.0-8/21768940_1929571243934485_8974410512505753576_o.jpg?_nc_cat=0&_nc_eui2=v1%3AAeGWc0OZESLyWlxwbSesk9kVFomqzfekfHxKpFOJkuvH0N9sI6uXaApNyLesXH4TEVhwrC_eGg77HTQvZ2g33OAEPoYU3BJN-qoHjPo21HGnZg&oh=dadc032135d729fd1475b04326a55af1&oe=5B299651'
      },
      {
        name: {
          first: 'Caroline',
          last: 'Livingston'
        },
        position: 'Mentorship Chair',
        email: '',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t31.0-8/17880148_780493898782379_5991580927269278218_o.jpg?_nc_cat=0&_nc_eui2=v1%3AAeGSx3jRrLqDOdtDw4vyyMxn_uadYF74I-iKRetqs2M-OYkod8Tv-eGPr2GGsMfZYNihqtbIEcmoEQkVLUaxaMJswAAcTWeskB-SsZMcK2cPqA&oh=a2cda67d900b5dab071ee1fddb4a2d22&oe=5B73DCB9'
      },
      {
        name: {
          first: 'Joey',
          last: 'Graham'
        },
        position: 'Service',
        email: '',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/10624643_732878030092678_8120086573989626366_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeGZr19m9hvv4TcXNg7R0WArFEthIKHfFwUqP9EFzle4trqvskGvrGn9JJKR5YJEP67zNu4W9eJZXzOXEaR9MMJKj1D7lpWW5XFCwmmFkJNo8A&oh=356b2aa4a51c06208dd3f38d5fd69f1f&oe=5B358479'
      },
      {
        name: {
          first: 'Tayelee',
          last: 'Holtrop'
        },
        position: 'Social',
        email: '',
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/23473282_153980968547040_560708824949638159_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeG3aCa3v_11Gemuk9Gy3MA7qQiJAZaXVsasP2fupR2wfvLv_RPKEiU-4yUVJJS8EkL29z3lW7bItTIz5ByORld-vDpfFDxEclQ_IJ3l1yo1jQ&oh=edbe3bfa83c1893c9b821c61f5604581&oe=5B75F4AB'
      },
      {
        name: {
          first: 'Pooja',
          last: 'Addla Hari'
        },
        position: 'Training',
        email: '',
        pictureURL: 'https://media.licdn.com/dms/image/C5603AQGC_HeC0N6ugQ/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=Q72A6KmeoG_R_W3tlI3wZf9kZFYI_voraTevDsHnGvg'
      },
      {
        name: {
          first: 'Kyla',
          last: 'Christenson'
        },
        position: 'Transfer',
        email: '',
        pictureURL: 'https://media.licdn.com/dms/image/C4D03AQGJivSPiznj2w/profile-displayphoto-shrink_800_800/0?e=1527994800&v=alpha&t=H_Ab3BCNHtLUsKyuWSboth4wlwK6P4wlWsCsDe01hMs'
      },

    ]
  },
  {
    group: 'Mission Team 1-15',
    bios: []
  },
  {
    group: 'Mission Team 16-30',
    bios: []
  },

]