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
        pictureURL: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/15170783_1415096675175086_4730606509373821185_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeHJ3-1GLZArXq26gPpAuEPB0gyFjdwLbW3oDm0CAwm6PpDg-QpHSMyYh8jP044hXmGdICD0l4mcxNSMz2Pecj2P37mZ-eUc-ml2kYC4IdItsg&oh=f11e384a801000c6ac6700be0c2d2021&oe=5B7364AB'
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
          last: 'Pena'
        },
        position: 'Section 6',
        email: '',
        pictureURL: ''
      },
      {
        name: {
          first: 'Andrea',
          last: 'Arellano'
        },
        position: 'Section 7',
        email: '',
        pictureURL: ''
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
        pictureURL: ''
      },
      {
        name: {
          first: 'Maddy',
          last: 'Arnold'
        },
        position: 'Section 10',
        email: '',
        pictureURL: ''
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
        pictureURL: ''
      },
      {
        name: {
          first: 'Drew',
          last: 'Hackmann'
        },
        position: 'Ambassadors Chair',
        email: '',
        pictureURL: ''
      },
      {
        name: {
          first: 'Breanna',
          last: 'Wright'
        },
        position: 'Civil-Mil Chair',
        email: '',
        pictureURL: ''
      },
      {
        name: {
          first: 'Sara',
          last: 'Neves Perez'
        },
        position: 'Communications Chair',
        email: '',
        pictureURL: ''
      },
      {
        name: {
          first: 'Justin',
          last: 'Rainge'
        },
        position: 'Events Chair',
        email: '',
        pictureURL: ''
      },
      {
        name: {
          first: 'Caroline',
          last: 'Livingston'
        },
        position: 'Mentorship Chair',
        email: '',
        pictureURL: ''
      },
      {
        name: {
          first: 'Joey',
          last: 'Graham'
        },
        position: 'Service',
        email: '',
        pictureURL: ''
      },
      {
        name: {
          first: 'Tayelee',
          last: 'Holtrop'
        },
        position: 'Social',
        email: '',
        pictureURL: ''
      },
      {
        name: {
          first: 'Pooja',
          last: 'Addla Hari'
        },
        position: 'Training',
        email: '',
        pictureURL: ''
      },
      {
        name: {
          first: 'Kyla',
          last: 'Christenson'
        },
        position: 'Transfer',
        email: '',
        pictureURL: ''
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